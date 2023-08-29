from collections import defaultdict
import pymysql
pymysql.install_as_MySQLdb()
import MySQLdb
import sys, os, datetime, json, copy, requests, pytz
from datetime import timedelta
import smtplib
from email.mime.text import MIMEText
# from sshtunnel import SSHTunnelForwarder
import unicodedata
import os 
# from caliper.constants import *
from cal_constants import *
from mysql_db_connector import *
from second import display_session_packet, create_session_events
from rich import print, inspect
from rich.console import Console
from rich.table import Table
from rich.progress import track
from dotenv import load_dotenv
import logging, pickle

logging.basicConfig(filename='app.log', filemode='a', format='%(name)s - %(asctime)s - %(levelname)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S', level=logging.INFO)
logger = logging.getLogger(__name__)
logger.info('')
logger.info('====================================')
logger.info('= Start of App                      =')
logger.info('====================================')
logger.info('Retrieving environment parameters')

load_dotenv()

console = Console()
username = os.environ.get("open_lrw_username")
password = os.environ.get("open_lrw_password")
target_sakai_url = os.environ.get("target_sakai_url")
target_sakai_version = os.environ.get("target_sakai_version")
batch_size = os.environ.get("BATCH_SIZE", 1000)
hour_block = os.environ.get("HOUR_BLOCK", 12)
"""
Retrieve information from Sakai
"""
logger.info('Configurating parameters for the scale and scope of data collection')
yesterday = datetime.datetime.now() - timedelta(days=1)
# yesterday = datetime.datetime.today()
start_time = " 00:00:00"
end_time = " 23:59:59"
# hour_block = 12
logger.info('Hour Block Size : %s' % ( hour_block ))
if yesterday.hour < int(hour_block):
    start_time = " 00:00:00"
    end_time = " 00:59:59"
else:
    start_time = " 00:00:00"
    end_time = " 00:59:59"
	
yesterday_start_date = yesterday.strftime('%Y-%m-%d') + start_time
yesterday_end_date = yesterday.strftime('%Y-%m-%d') + end_time

logger.info('Preparing Caliper configurations')
context_1 = "http://purl.imsglobal.org/ctx/caliper/v1p1"
context_2 = "http://purl.imsglobal.org/ctx/caliper/v1p2"
target_system = "https://%s" % ( target_sakai_url )
target_type = "LearnManagementSystem"
target_version = "v%s" % (target_sakai_version)
edApp = { 
	"id": target_system,
    "type": "LearnManagementSystem",
    "version": target_version}
# Move to a central class
actor = {"id" : "", "type": ENTITY_TYPES["PERSON"] }	

def process_sessions(db):
	logger.info('Beggining to process the session related data and profiles.')
	"""
	Get all events between a specific range with a specific type.
	In this instance it will be Session LoggedIn, LoggedOut, TimeOut
	"""

	sakai_session_events_query = """
		SELECT se.*, ss.session_user, ss.SESSION_START, suim.eid 
		FROM sakai_event se 
 		LEFT JOIN sakai_session ss ON se.session_id = ss.session_id
		LEFT JOIN sakai_user_id_map suim ON suim.USER_ID = ss.SESSION_USER
 		WHERE se.event_date between '{0}' AND '{1}' AND event IN ('user.login', 'user.login.container', 'user.login.ws', 'user.logout');
	"""
	cur = db.cursor(MySQLdb.cursors.DictCursor)
	print(sakai_session_events_query.format(yesterday_start_date, yesterday_end_date  ))
	cur.execute(sakai_session_events_query.format(yesterday_start_date, yesterday_end_date  ))

	# print all the first cell of all the rows
	session_events = cur.fetchall()
	print("Total Events: %s" % (len(session_events)))
	logger.info("Total Events to be processed: %s" % (len(session_events)))
	if len(session_events) > 0:
		rowcnt = 0
		for row in session_events:
			rowcnt = rowcnt + 1
			# print(row)
			logger.info("Processing row: %s / %s" % (rowcnt, len(session_events)))
			packet = {}
			packet["data"] = []
			packet["data"].append(format_session_events(row))
			packet["sensor"] = "string"
			packet["sendTime"] = datetime.datetime.now(tz=pytz.UTC).isoformat()[:23] + 'Z'
			print(json.dumps(packet, indent=4))
			create_session_events(packet)
			# logger.info("Size of packet: %s " % ( len(packet["data"]) ))
		print("Total Session events: %s" % (rowcnt))
		logger.info("Completed processing sessions: %s / %s" % (rowcnt, len(session_events)))
		# print(json.dumps(packet, indent=4))
	else:
		print("No Events: no further action required")
	cur.close()


def format_session_events(event):
	session_obj = {}
	session_obj["@context"] = context_1
	session_obj["id"] = "urn:uuid:%s" % (event["SESSION_ID"])
	session_obj["type"] = EVENT_TYPES["SESSION_EVENT"]
	actor_obj  = actor
	actor_obj["id"] = event["eid"]
	session_obj["actor"] = actor
	if event["EVENT"] == "user.logout":
		session_obj["action"] = CALIPER_ACTIONS["LOGGED_OUT"]
	elif event["EVENT"] == "user.login" or event["EVENT"] == "user.login.container" or  event["EVENT"] == "user.login.ws":
		session_obj["action"] = CALIPER_ACTIONS["LOGGED_IN"]
	obj = {}
	obj["id"] = target_system
	obj["type"] = target_type 
	obj["version"] = target_version
	session_obj["object"] = obj
	session_obj["eventTime"] = event["EVENT_DATE"].isoformat()[:23] + 'Z'
	session_obj["edApp"] = edApp
	sess = {}
	sess["id"] = event["SESSION_ID"]
	sess["type"] = ENTITY_TYPES["SESSION"]
	sess["user"] = event["session_user"]
	sess["dateCreated"] = event["SESSION_START"].isoformat()[:23] + 'Z'
	sess["startedAtTime"] = event["EVENT_DATE"].isoformat()[:23] + 'Z'
	session_obj["session"] = sess

	# print("")
	# print("-------------------------------------------------------------------------------")
	# print("")
	# print(session_obj)
	return session_obj

def process_views(db):
	print("[bold blue]Processing Read[/bold blue]")
	events = """'annc.read',
	'asn.read.assignment' 
	'asn.read.submission', 
	'calendar.read', 
	'chat.read', 
	'content.read', 
	'forums.read',
	'forums.topic.read',
	'lessonbuilder.item.read',
	'lessonbuilder.page.read', 
	'lessonbuilder.read', 
	'messages.read', 
	'podcast.read',
	'podcast.read.public', 
	'syllabus.read', 
	'webcontent.myworkspace.read', 
	'webcontent.read', 
	'webcontent.service.read', 'webcontent.site.read', 'wiki.read', 'gradebook.studentView', 'poll.viewResult', 'profile.friends.view.other',
	'profile.friends.view.own', 'roster.view', 'roster.view.photos'"""

	"""
	Get all events between a specific range that have been read.
	We will pay special attention to the all tools which have a read or viewed event
	Exclude where no session user id as that would be gateway and public.
	"""
	sakai_read_events_query = """
		SELECT se.*, ss.session_user, ss.SESSION_START, suim.eid 
		FROM sakai_event se 
		LEFT JOIN sakai_session ss ON se.session_id = ss.session_id
		LEFT JOIN sakai_user_id_map suim ON suim.USER_ID = ss.SESSION_USER
		WHERE 
			se.event_date between '{0}' AND '{1}' 
			AND event IN ({2})
			AND ss.session_user IS NOT NULL;
			;
	"""
	cur = db.cursor(MySQLdb.cursors.DictCursor)
	print(sakai_read_events_query.format(yesterday_start_date, yesterday_end_date, events ))
	cur.execute(sakai_read_events_query.format(yesterday_start_date, yesterday_end_date, events  ))

	# print all the first cell of all the rows
	session_events = cur.fetchall()
	print("Total Events: %s" % (len(session_events)))
	packet = {}
	packet["data"] = []
	if len(session_events) > 0:
		for row in session_events:
			# print(row)	 
			packet["data"].append(format_viewed_events(row))
		packet["sensor"] = "string"
		packet["sendTime"] = datetime.datetime.now(tz=pytz.UTC).isoformat()[:23] + 'Z'

		print("Total Session events: %s" % (len(packet["data"])))

		# print(json.dumps(packet, indent=4))
		create_session_events(packet)
	else:
		print("No Events: no further action required")
	cur.close()


def format_viewed_events(event):
	session_obj = {}
	session_obj["@context"] = context_1
	session_obj["id"] = "urn:uuid:%s" % (event["SESSION_ID"])
	session_obj["type"] = EVENT_TYPES["VIEW_EVENT"]
	actor_obj  = actor
	actor_obj["id"] = event["eid"]
	session_obj["actor"] = actor
	obj = {}
	if "view" in event["EVENT"] or "read" in event["EVENT"]:
		session_obj["action"] = CALIPER_ACTIONS["VIEWED"]
		if event["EVENT"] == "webcontent.myworkspace.read":
			obj["type"] = CALIPER_TYPES["LINK"]
			obj["id"] = event["REF"]
			obj["name"] = event["CONTEXT"]
		elif event["EVENT"] == "content.read":
			obj["type"] = CALIPER_TYPES["TOOL_USE_EVENT"]
			obj["id"] = event["REF"]
			obj["name"] = event["CONTEXT"]
		elif event["EVENT"] == "calendar.read":
			obj["type"] = CALIPER_TYPES["TOOL_USE_EVENT"]
			obj["id"] = event["REF"]
			obj["name"] = event["CONTEXT"]
		elif event["EVENT"] == "syllabus.read":
			obj["type"] = CALIPER_TYPES["TOOL_USE_EVENT"]
			obj["id"] = event["REF"]
			obj["name"] = event["CONTEXT"]
		elif event["EVENT"] == "lessonbuilder.page.read":
			obj["type"] = CALIPER_TYPES["PAGE"]
			obj["id"] = event["REF"]
			obj["name"] = event["CONTEXT"]
	# elif event["EVENT"] == "user.logout":
	# 	# session_obj["action"] = CALIPER_ACTIONS["REVIEWED"]
	# 	print(session_obj)
	obj["version"] = target_version
	session_obj["object"] = obj
	session_obj["eventTime"] = event["EVENT_DATE"].isoformat()[:23] + 'Z'
	session_obj["edApp"] = edApp
	sess = {}
	sess["id"] = event["SESSION_ID"]
	sess["type"] = ENTITY_TYPES["SESSION"]
	sess["user"] = event["session_user"]
	sess["dateCreated"] = event["SESSION_START"].isoformat()[:23] + 'Z'
	sess["startedAtTime"] = event["EVENT_DATE"].isoformat()[:23] + 'Z'
	session_obj["session"] = sess
	return session_obj

def process_tool_use(db):
    print("[bold blue]Processing Tool Use[/bold blue]")

if __name__ == "__main__":
	logger.info('Beginning data retrieval and transformation.')
	print("[bold blue]Displaying Session Packet[/bold blue]")
	print(display_session_packet())
	process_sakai_queries()

