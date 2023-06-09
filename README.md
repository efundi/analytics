# NWU-AOS-Analytics-Data-Processor
An OpenLRW Project to harvest data from Apereo Sakai and inject it into the OpenLRW using the caliper standard.


touch .env

nano .env
</code>

### Content of .env file, which is read when the test.py is run

<code>
DATABASE_URI=<DATABASE_SERVER_IP_ADDRESS_HERE>
DATABASE_NAME=<DATABASE_NAME_ADDRESS_HERE>
DATABASE_USERNAME=<DATABASE_USERNAME_HERE>
DATABASE_PASSWORD=<DATABASE_USERNAME_PASSWORD_HERE>
DATABASE_PORT=3306
PROXY_URL=<PROXY_URL_HERE>
TARGET_URI=xxx.xxx.xxx.xxx:9966
TARGET_NAME=OpenLRW
TARGET_USERNAME=
TARGET_PASSWORD=
LOG_LOCATION=.

</code> 
