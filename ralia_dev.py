db_location = "/home/rebooted/Scripts/ralia/db.txt"

# the user prompt is in the form <username>@<host>:<location><prompt>
import os
username = os.getenv("USER")
host = "ralia"
prompt = " >>> "
location = os.getenv("PWD")

# this command is put in front of the executed command when it is passed to the system
# for execution.
terminal_command = "xfce4-terminal -x "
import subprocess
# importing subprocess module so that this Python script can invoke outside programs and scripts.

try:
	db = open(db_location)
except:
	print("The standard database file appears not to exist.\nIf it does, please edit this file and\nchange the 'db' variable to the location of\nthe database file.")
	exit()

# looking for a database file, and giving an error if the file isn't found.

count = 0
executed_count = 0
for line in db:
	count = count + 1
db.close()
db = open(db_location)

ran_command = False
if count > executed_count:
	while True:
		executed_count = 0
		input = raw_input(username + "@" + host + ":" + location + prompt)
		if input == "exit":
			exit()
		elif input == "x":
			exit()
		else:
			input = input + " -> "
			for line in db:
				executed_count = executed_count + 1
				if line.startswith(input):
					execute_platform = line.split(input,1)
					execute = execute_platform[1]
					execute = execute.rstrip()
					execute = terminal_command + execute
					ran_command = True
					subprocess.call(execute, shell=True)
				else:
					print("key not found")
					continue
else:
	subprocess.call(input)

