from collections import defaultdict
import pymysql
pymysql.install_as_MySQLdb()
import MySQLdb
import sys, os, datetime, json, copy, requests
from datetime import timedelta
import unicodedata
# from caliper.constants import *
from openlrw.client import OpenLRW
from openlrw.exceptions import *
# from caliper.constants import *
# from mysql_db_connector import *
from dotenv import load_dotenv

load_dotenv()

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def cprt(style, txt):
	"""
	HEADER
    OKBLUE
    OKCYAN
    OKGREEN
    WARNING
    FAIL
    ENDC
    BOLD
    UNDERLINE
	"""
	style = style.lower()
	if style == "header":
		print(bcolors.HEADER + txt+ bcolors.ENDC)
	if style == "okblue":
		print(bcolors.OKBLUE + txt+ bcolors.ENDC)
	if style == "okcyan":
		print(bcolors.OKCYAN + txt+ bcolors.ENDC)
	if style == "okgreen":
		print(bcolors.OKGREEN + txt+ bcolors.ENDC)
	if style == "warning":
		print(bcolors.WARNING + txt+ bcolors.ENDC)				
	if style == "fail":
		print(bcolors.FAIL + txt+ bcolors.ENDC)		
	if style == "bold":
		print(bcolors.BOLD + txt+ bcolors.ENDC)		
	if style == "underline":
		print(bcolors.UNDERLINE + txt+ bcolors.ENDC)	

# console = Console()
database_uri = os.environ.get("DATABASE_URI")
database_name = os.environ.get("DATABASE_NAME")
database_username = os.environ.get("DATABASE_USERNAME")
database_password = os.environ.get("DATABASE_PASSWORD")
database_port = int(os.environ.get("DATABASE_PORT"))
proxy_url = os.environ.get("PROXY_URL")
open_lrw_uri = os.environ.get("TARGET_URI")
open_lrw_name = os.environ.get("TARGET_NAME")
open_lrw_username = os.environ.get("TARGET_USERNAME")
open_lrw_password = os.environ.get("TARGET_PASSWORD")
logfile = os.environ.get("LOG_LOCATION")

yesterday = datetime.datetime.today() - timedelta(days=1000)
# yesterday = datetime.datetime.today()
yesterday_start_date = yesterday.strftime('%Y-%m-%d') + " 00:00:00"
yesterday_end_date = yesterday.strftime('%Y-%m-%d') + " 23:59:59"


proxy_servers = {
   'http': proxy_url,
   'https': proxy_url,
}

def get_tennants():
  response = requests.get('http://%s/api/tenants' % (open_lrw_uri), headers={'Authorization': 'Bearer {}'.format(jwt)}, proxies=proxy_servers )
  try:
    print(response.content)  
  except:
    response = ""
    print("Failed !")

if __name__ == "__main__":
	cprt("header", "Displaying TEST DATA")
	print("----------------------------")
	db = MySQLdb.connect(host=database_uri,
				user=database_username,
				passwd=database_password,
				db=database_name,
				port=database_port)
	sakai_session_events_query = """
		SELECT count(*)
		FROM sakai_event se 
		WHERE se.event_date between '{0}' AND '{1}' ;
	"""
	cur = db.cursor(MySQLdb.cursors.DictCursor)
	print(sakai_session_events_query.format(yesterday_start_date, yesterday_end_date  ))
	cur.execute(sakai_session_events_query.format(yesterday_start_date, yesterday_end_date  ))

	# print all the first cell of all the rows
	session_events = cur.fetchone()
	cprt("okgreen", "Sakai DB Connections Successful: Result Total Events: %s" % (session_events))

	cprt("header", "Starting Application." )
	cprt("okblue", "Setting up openLRW Integration." )
	openlrw = OpenLRW( "http://%s" % (open_lrw_uri),open_lrw_username , open_lrw_password ) # Create an instance of the client
	print(openlrw)
	cprt("okblue", "Generating JWT" )
	try:
		jwt = openlrw.generate_jwt()
	except  Exception as inst:
		cprt("fail", "Could not generate token. Check if server is running.")
		print(inst)
	get_tennants()
