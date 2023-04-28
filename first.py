import caliper
import pytz
import uuid
import json
from datetime import *
# from caliper.constants import *
from cal_constants import *

dt = datetime.now()
the_config = caliper.HttpOptions(
    host='http://analytics.aos.nwu.ac.za/events/',
    auth_scheme='Bearer',
    api_key='' )

# Here you build your sensor; it will have one client in its registry,
# with the key 'default'.
the_sensor = caliper.build_simple_sensor(
    sensor_id = 'http://analytics.aos.nwu.ac.za/sensor',
    config_options = the_config )

namespace = "za.az.nwu.aos.analytics"
#print( uuid.uuid4())
# myuuid = uuid.uuid4()
# # myuuidStr = str("c740e305-da8d-4649-8934-242b1ccc51fe")
# myuuidStr = str(myuuid)
# #uuid.uuid5("za.az.nwu.aos.analytics", "Analytics")
# sameMyUuid = uuid.UUID(myuuidStr)
# print( sameMyUuid )  
# print(uuid.uuid4().hex )
# print(the_sensor.get_config() )
# print(the_sensor )
# Here, you will have caliper entity representations of the various
# learning objects and entities in your wider system, and you provide
# them into the constructor for the event that has just happened.
#
# Note that you don't have to pass an action into the constructor because
# the NavigationEvent only supports one action, part of the
# Caliper base profile: caliper.constants.BASE_PROFILE_ACTIONS['NAVIGATED_TO']
#
# print(EVENT_TYPES)
# print(CALIPER_PROFILES)
# print(CALIPER_ACTIONS)
the_event = caliper.events.NavigationEvent(
	# id = uuid.uuid4(),
	id 				= str("urn:uuid:" + str(uuid.uuid4())),	 
	#profile="NavigationEvent",
	# event="submission",
	action 			= CALIPER_ACTIONS["NAVIGATED_TO"],
    actor  			= {
    	"id": "https://example.edu/users/554433",
      	"type": "Person"
    },
    edApp  			= "https://analytics.opencollab.co.za/NWU_Analytics",
    object 			= "https://analytics.opencollab.co.za/NWU_Analytics",
    # type 			= "ToolUseEvent",
    eventTime 		= datetime.now(tz=pytz.UTC).isoformat()[:23] + 'Z',
    extensions		= None,
    federatedSession=None,
    generated		=None,
    group 			= "https://analytics.opencollab.co.za/the_course_offering_in_play_as_caliper_Organization_entity",
    membership 		= None,
    session 		= None,
    #event_object = "the_caliper_DigitalResource_the_actor_is_using",
    referrer 		= "https://caliper.opencollab.co.za",
    target 			= "https://caliper.opencollab.co.za/contact-us" )

# Once built, you can use your sensor to send one or more often used
# entities; suppose for example, you'll be sending a number of events
# that all have the same actor

print( the_event.as_json(thin_props=True, thin_context=True))

##sent_identities = the_sensor.send(the_event.actor)

# The return structure from the sensor will be a dictionary of lists: each
# item in the dictionary has a key corresponding to a client key,
# so ret['default'] fetches back the list of URIs of all the @ids of
# the fully described Caliper objects you have sent with that describe call.
#
# Now you can use this list with event sendings to send only the identifiers
# of already-described entities, and not their full forms:

##the_sensor.send(the_event, described_objects=sent_identities)

# You can also just send the event in its full form, with all fleshed out
# entities:

##the_sensor.send(the_event)

# You can check the status code sent back by the endpoint for the last
# invocation of send():

##assert the_sensor.status_code in [200, 201, 202]

# If you create your configuration with debug=true, then your sensor will
# keep a list of the full responses (it uses the "requests" library under the
# covers, so these will be response objects from that library:

# the_sensor.config.DEBUG = true
# sent_identifies = the_sensor.send(the_event.actor)
# the_sensor.send(the_event, described_objects=sent_identities)
# responses = the_sensor.debug