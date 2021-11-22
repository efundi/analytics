import caliper
import pytz
import uuid
import json
from datetime import *
from caliper.constants import *
from openlrw.client import OpenLRW
from openlrw.exceptions import *
import requests
import json, os, sys
from dotenv import load_dotenv

load_dotenv()

dt = datetime.now()


namespace = "za.az.nwu.aos.analytics"

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

#.env credentials
username = os.environ.get("open_lrw_username")
password = os.environ.get("open_lrw_password")

cprt("header", "Starting Application." )
cprt("okblue", "Setting up openLRW Integration." )
openlrw = OpenLRW( "http://143.160.210.115:9966", "3c3aec1c-1a5b-490c-b3c9-89004c19fc32" , "0757caf0-9b2e-4abc-a0e2-b8ea86f3e6c4" ) # Create an instance of the client
#openlrw.setup_email('http://143.160.210.115', 'francois@opencollab.co.za', 'francois@opencollab.co.za')  # Optional: Allows you to send emails
# print(openlrw)
cprt("okblue", "Generating JWT" )
try:
  jwt = openlrw.generate_jwt()
except  Exception as inst:
  cprt("fail", "Could not generate token. Check if server is running.")

#  -----------------------------------------
# creating an actor
# ------------------------------------------
def get_actor():
  # actor = { 
  #   '@context' : 'http://purl.imsglobal.org/ctx/caliper/v1p1',
  #   '@id': 'https://school.edu/user/554433',
  #   '@type':  'Person',
  #   'dateCreated': '2018-08-01T06:00:00.000Z',
  #   'dateModified': '2018-09-02T11:30:00.000Z',
  #   'name': 'Francois'
  # }

  actor = {}
  actor["@context"] = 'http://purl.imsglobal.org/ctx/caliper/v1p1'
  actor["@id"] = 'https://school.edu/user/554433'
  actor["type"] = ENTITY_TYPES['PERSON']
  actor["dateCreated"] = datetime.now(tz=pytz.UTC).isoformat()[:23] + 'Z'
  actor["dateModified"] = datetime.now(tz=pytz.UTC).isoformat()[:23] + 'Z'
  actor["name"] = 'Francois Campbell'
  print("---------------------")
  print("")
  print(json.dumps(actor, indent=4))
  print("")
  print("---------------------")
  return actor

def get_group():
  group = {}
  group["@context"] = 'http://purl.imsglobal.org/ctx/caliper/v1p1'
  group["@id"] = 'https://school.edu/group/554433'
  group["type"] = ENTITY_TYPES['GROUP']
  group["dateCreated"] = datetime.now(tz=pytz.UTC).isoformat()[:23] + 'Z'
  group["dateModified"] = datetime.now(tz=pytz.UTC).isoformat()[:23] + 'Z'
  group["name"] = 'Discussion Group'
  print("---------------------")
  print("")
  print(json.dumps(group, indent=4))
  print("")
  print("---------------------")
  return group

def get_ed_app():
  #  {
  #               "@context": "string",
  #               "@id": "string",
  #               "@type": "string",
  #               "dateCreated": "2021-10-12T14:46:32.897Z",
  #               "dateModified": "2021-10-12T14:46:32.897Z",
  #               "description": "string",
  #               "extensions": {
  #                   "additionalProp1": "string",
  #                   "additionalProp2": "string",
  #                   "additionalProp3": "string"
  #               },
  #               "name": "string"
  #           }
  ed_app = {}
  ed_app["@context"] = 'http://purl.imsglobal.org/ctx/caliper/v1p1'
  ed_app["@id"] = 'https://school.edu/ed_app/554433'
  ed_app["type"] = ENTITY_TYPES['GROUP']
  ed_app["dateCreated"] = datetime.now(tz=pytz.UTC).isoformat()[:23] + 'Z'
  ed_app["dateModified"] = datetime.now(tz=pytz.UTC).isoformat()[:23] + 'Z'
  ed_app["name"] = 'Discussion Group'
  print("---------------------")
  print("")
  print(json.dumps(ed_app, indent=4))
  print("")
  print("---------------------")
  return ed_app

def get_users():
  # print(jwt)
  cprt("UNDERLINE", "\nGetting users from the DB" )
  try: 
    users = openlrw.get_users(jwt) # All the users
    for user in users:
      print("User ID: %s" % (user))
    cprt("okgreen", "Succeeded!")
  except ExpiredTokenException:
    cprt("FAIL", "Failed to Get the requested information from DB" )
    OpenLRW.pretty_error("Error", "JWT Expired")




print("")
cprt("okcyan", "creating Caliper Options and sensor")
the_config = caliper.HttpOptions(
    host='http://analytics.aos.nwu.ac.za/events/',
    auth_scheme='Bearer',
    api_key= jwt )


# Here you build your sensor; it will have one client in its registry,
# with the key 'default'.
the_sensor = caliper.build_simple_sensor(
    sensor_id = 'http://analytics.aos.nwu.ac.za/sensor',
    config_options = the_config )

# Create an event
def create_navigation_event():
  print("")
  print("")
  cprt("bold", "Getting other information from DB" )
  cprt("okcyan", "Navigation Envelope!!!")
  data = open( "profile_data/navigation_event_envelope.json", 'r')
  try: 
    openlrw.send_caliper(json.load(data))
    cprt("okgreen", "Great Success")
  except BadRequestException as e:
    # print(str(e.message))
    print("An Error")
    # openlrw.pretty_error("Bad Request", "An error happened.")
  except InternalServerErrorException as f:
    print(str(f.message))
    # openlrw.pretty_error("Internal Server Error", "An error happened.")

  # the_event = caliper.events.NavigationEvent(
  #   # id = uuid.uuid4(),
  #   id 				= str("urn:uuid:" + str(uuid.uuid4())),	 
  #   #profile="NavigationEvent",
  #   # event="submission",
  #   action 			= CALIPER_ACTIONS["NAVIGATED_TO"],
  #   actor  			= get_actor(),
  #   edApp  			= "https://analytics.opencollab.co.za/NWU_Analytics",
  #   object 			= "https://analytics.opencollab.co.za/NWU_Analytics",
  #   # type 			= "ToolUseEvent",
  #   eventTime 		= datetime.now(tz=pytz.UTC).isoformat()[:23] + 'Z',
  #   extensions		= None,
  #   federatedSession = "",
  #   # generated		= None,
  #   group 			= get_group(),
  #   membership 		= None,
  #   session 		= None,
  #   #event_object = "the_caliper_DigitalResource_the_actor_is_using",
  #   referrer 		= "https://caliper.opencollab.co.za",
  #   target 			= "https://caliper.opencollab.co.za/contact-us" )

  # events = []
  # events.append(the_event.as_json(thin_props=True, thin_context=True))
  # Once built, you can use your sensor to send one or more often used
  # entities; suppose for example, you'll be sending a number of events
  # that all have the same actor
  # try: 
  #   openlrw.send_caliper( the_event.as_json(thin_props=True, thin_context=True) )
  #   cprt("okgreen", "OK Success")
  # except Exception as inst:
  #   cprt("fail", "Failed to insert Caliper Entry into DB, why?" )
  #   print(inst)

# print( events)
# #json_serialised_event = the_event.as_json(thin_props=True, thin_context=True)

# cprt("okcyan", "Insert Caliper Entry into DB " )
# try: 
#   #openlrw.send_caliper(jwt, event)
# 	openlrw.send_caliper(jwt, events)
# except Exception as inst:
# 	cprt("fail", "Failed to insert Caliper Entry into DB, why?" )
# 	print(inst)
# 	# OpenLRW.pretty_error("Error", "Failed to insert Caliper Entry into DB ")

# cprt("okcyan", "Trying another way!!!")
# event = '{ "@message": "blah", "sensor": "https://example.edu/sensor/001", "sendTime": "2015-09-15T11:05:01.000Z", "data": [ { "@context": "http://purl.imsglobal.org/ctx/caliper/v1/Context", "@type": "http://purl.imsglobal.org/caliper/v1/Event", "actor": { "@id": "https://example.edu/user/554433", "@type": "http://purl.imsglobal.org/caliper/v1/lis/Person" }, "action": "http://purl.imsglobal.org/vocab/caliper/v1/action#Viewed", "eventTime": "2015-09-15T10:15:00.000Z", "object": { "@id": "https://example.com/viewer/book/34843#epubcfi(/4/3)", "@type": "http://www.idpf.org/epub/vocab/structure/#volume" } } ] }'

# try: 
#   openlrw.send_caliper(event)
#   cprt("okgreen", "Great Success")
# except BadRequestException as e:
#   print(str(e.message))
#   openlrw.pretty_error("Bad Request", "An error happened.")
# except InternalServerErrorException as e:
#   print(str(e.message))
#   openlrw.pretty_error("Internal Server Error", "An error happened.")



def insert_event():
  cprt("okcyan", "Trying YET another way!!!")
  data = open( "profile_data/envelope.json", 'r')
  try: 
    openlrw.send_caliper(json.load(data))
    cprt("okgreen", "Great Success")
  except BadRequestException as e:
    print(str(e.message))
    openlrw.pretty_error("Bad Request", "An error happened.")
  except InternalServerErrorException as e:
    print(str(e.message))
    openlrw.pretty_error("Internal Server Error", "An error happened.")


# cprt("okblue", "Get data")
# results = openlrw.get_users(jwt)
# users = openlrw.get_users(jwt) # All the users
# for user in users:
#   print( user)

# cprt("okblue", "Get every users data")
# for user in users:
#   ress = openlrw.get_results_for_a_user(str(user), jwt)
#   print( ress )


def get_tennants():
  #@curl -X GET "http://143.160.210.115:9966/api/tenants" -H "accept: */*"
  #response = requests.get('http://143.160.210.115:9966/api/tenants', headers={'Authorization': 'token {}'.format(jwt)})
  response = requests.get('http://143.160.210.115:9966/api/tenants', headers={'Authorization': 'Bearer {}'.format(jwt)})
  # headers = {'X-Requested-With': 'XMLHttpRequest'}
  # data = {"username": username , "password": password}
  # print('{}'.format(jwt))
  # data = {"token": '{}'.format(jwt) }
  try:
  #   response = requests.get("http://143.160.210.115:9966/api/tenants", headers=headers, json=data)
    print(response.content)  
  except:
    response = ""
    print("Failed !")


# Create an event
def create_annotation_event():
  print("")
  print("")
  cprt("bold", "Getting other information from DB" )
  cprt("okcyan", "Annotation Envelope!!!")
  data = open( "profile_data/annotation_envelope.json", 'r')
  try: 
    openlrw.send_caliper(json.load(data))
    cprt("okgreen", "Great Success")
  except BadRequestException as e:
    # print(str(e.message))
    print("An Error")
    # openlrw.pretty_error("Bad Request", "An error happened.")
  except InternalServerErrorException as f:
    print(str(f.message))


def create_assessment_start_event():
  print("")
  print("")
  cprt("bold", "Getting other information from DB" )
  cprt("okcyan", "Assessment Start Envelope!!!")
  data = open( "profile_data/assessment_start_envelope.json", 'r')
  try: 
    openlrw.send_caliper(json.load(data))
    cprt("okgreen", "Great Success")
  except BadRequestException as e:
    # print(str(e.message))
    print("An Error")
    # openlrw.pretty_error("Bad Request", "An error happened.")
  except InternalServerErrorException as f:
    print(str(f.message))

def create_assessment_item_event():
  print("")
  cprt("okcyan", "Assessment item Envelope!!!")
  data = open( "profile_data/assessment_item_event_envelope.json", 'r')
  try: 
    openlrw.send_caliper(json.load(data))
    cprt("okgreen", "Great Success")
  except BadRequestException as e:
    # print(str(e.message))
    print("An Error")
    # openlrw.pretty_error("Bad Request", "An error happened.")
  except InternalServerErrorException as f:
    print(str(f.message))    


def create_assessment_end_event():
  print("")
  cprt("okcyan", "Assessment item Envelope!!!")
  data = open( "profile_data/assessment_end_event_envelope.json", 'r')
  try: 
    openlrw.send_caliper(json.load(data))
    cprt("okgreen", "Great Success")
  except BadRequestException as e:
    # print(str(e.message))
    print("An Error")
    # openlrw.pretty_error("Bad Request", "An error happened.")
  except InternalServerErrorException as f:
    print(str(f.message))

def create_assignable_event():
  print("")
  cprt("okcyan", "Assignable Event Envelope!!!")
  data = open( "profile_data/assignable_event_envelope.json", 'r')
  try: 
    openlrw.send_caliper(json.load(data))
    cprt("okgreen", "Great Success")
  except BadRequestException as e:
    # print(str(e.message))
    print("An Error")
    # openlrw.pretty_error("Bad Request", "An error happened.")
  except InternalServerErrorException as f:
    print(str(f.message))    


def create_forum_event():
  print("")
  cprt("okcyan", "Forum Event Envelope!!!")
  data = open( "profile_data/forum_event_envelope.json", 'r')
  try: 
    openlrw.send_caliper(json.load(data))
    cprt("okgreen", "Great Success")
  except BadRequestException as e:
    # print(str(e.message))
    print("An Error")
    # openlrw.pretty_error("Bad Request", "An error happened.")
  except InternalServerErrorException as f:
    print(str(f.message))    

def create_media_event():
  print("")
  cprt("okcyan", "Media Event Envelope!!!")
  data = open( "profile_data/media_event_envelope.json", 'r')
  try: 
    openlrw.send_caliper(json.load(data))
    cprt("okgreen", "Great Success")
  except BadRequestException as e:
    # print(str(e.message))
    print("An Error")
    # openlrw.pretty_error("Bad Request", "An error happened.")
  except InternalServerErrorException as f:
    print(str(f.message))   

def create_grade_event():
  print("")
  cprt("okcyan", "Forum Event Envelope!!!")
  data = open( "profile_data/grade_event_envelope.json", 'r')
  try: 
    openlrw.send_caliper(json.load(data))
    cprt("okgreen", "Great Success")
  except BadRequestException as e:
    # print(str(e.message))
    print("An Error")
    # openlrw.pretty_error("Bad Request", "An error happened.")
  except InternalServerErrorException as f:
    print(str(f.message))    

def create_session_event():
  print("")
  cprt("okcyan", "Session Event Envelope!!!")
  data = open( "profile_data/session_event_envelope.json", 'r')
  try: 
    openlrw.send_caliper(json.load(data))
    cprt("okgreen", "Great Success")
  except BadRequestException as e:
    # print(str(e.message))
    print("An Error")
    # openlrw.pretty_error("Bad Request", "An error happened.")
  except InternalServerErrorException as f:
    print(str(f.message))    

# Capture session events given data
def create_session_events(data_packet):
  print("")
  cprt("okcyan", "Capture Session Events")
  try: 
    openlrw.send_caliper(data_packet)
    cprt("okgreen", "Great Success")
  except BadRequestException as e:
    # print(str(e.message))
    print("An Error")
    # openlrw.pretty_error("Bad Request", "An error happened.")
  except InternalServerErrorException as f:
    print(str(f.message)) 


def display_session_packet():
    data = open( "profile_data/session_event_envelope.json", 'r')
    return json.load(data)

#  -----------------------------------------
# Main
# ------------------------------------------

if __name__ == "__main__":
  # get_tennants()
  # get_users()
  # create_tennant()
  # create_user()
  # get_data()
#   create_navigation_event()
#   create_annotation_event()
#   create_assessment_start_event()
#   create_assessment_item_event()
#   create_assessment_end_event()
#   create_assignable_event()
#   create_forum_event()
#   # create_grade_event()
#   create_media_event()
  create_session_event()
  
