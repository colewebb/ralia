# This is only finding the first entry in the database.

import subprocess

db_s_location = "/home/rebooted/Scripts/ralia/apps/db-s.txt"
s_input = raw_input("file >>> ")
executed = False
terminal_command = "xdg-open "
try:
	s_db = open(db_s_location)
except:
	print("The database file for the s[tart] app appears not to exist.\nIf it does, please edit the ralia.py file and\nchange the 'db-s' variable to the location of\nthe database file.")
	exit()
for line in s_db:
	s_input = s_input + " -> "
	if line.startswith(s_input):
		execute_platform = line.split(s_input,1)
		execute = execute_platform[1]
		execute = execute.rstrip()
		print execute
		executed = True
		subprocess.call(terminal_command + execute,shell=True)
	elif executed == False:
		print("Searching")
	else:
		print("You had better not ever see this.")
