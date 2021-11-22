from collections import defaultdict
import MySQLdb, sys, os, datetime, json, copy, requests
from datetime import timedelta
import smtplib
from email.mime.text import MIMEText
from sshtunnel import SSHTunnelForwarder
import unicodedata
import os 
from sakai import *

"""
Ubuntu install
apt-get install python-dev libmysqlclient-dev
pip install -r requirements.txt
"""

db_server = {
		"db_server_name": "Sakai Production DB Server",
		"db_name": "sakai_10_1", 
		"db_user": "sakaiuser", 
		"db_password": "S@kaiP@ssw0rd", 
		"db_host": "127.0.0.1",
		"db_port": 3306,
		"ssh_tunnel": True,
		"ssh_details":{ 
			"ssh_host": "195.201.139.96",
			"ssh_port": 22,
			"ssh_user": "dev",
			"ssh_password": "q76Ren3Gvmmx9uKu",
		}
	}


def process_sakai_queries():
	tunnel = db_server["ssh_details"]
	db  = None
	# print(tunnel)
	with SSHTunnelForwarder(
		(tunnel["ssh_host"], tunnel["ssh_port"]),
		ssh_password=tunnel["ssh_password"],
		ssh_username=tunnel["ssh_user"],
		remote_bind_address=(db_server["db_host"], db_server["db_port"])) as server:
			print("Trying to make a connection")
			print(server.local_bind_port)
			db = MySQLdb.connect(host=db_server["db_host"],
				user=db_server["db_user"],
				passwd=db_server["db_password"],
				db=db_server["db_name"],
				port=server.local_bind_port)

			process_sessions(db)
			process_views(db)
			# process_tool_use(db)
			db.close()
			
			

def execute_queries(db):
	return db

def testDBConnection(db):
	cur = db.cursor()
	cur.execute("show tables")

	# print all the first cell of all the rows
	table_list = cur.fetchall()
	print("Total Tables: %s" % (len(table_list)))
	for row in table_list:
		print(row[0])

	cur.close()
	db.close()

