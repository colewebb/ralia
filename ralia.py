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
# terminal_command = ""
import subprocess
# importing subprocess module so that this Python script can invoke outside programs and scripts.

status = "This program's status is stable. Don't touch it. Use the compiled version\ninstead."

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
executed = False

while count >= executed_count:
	query = username + "@" + host + ":" + location + prompt
	input = raw_input(query)
	if input == "exit":
		exit()
	elif input == "x":
		exit()
	elif input == "v":
		print(status)
	elif input == "c":
		subprocess.call("xfce4-terminal -x ralia.sh", shell = True)
		exit()
	else:
		input_line = input + " -> "
		for line in db:
			if line.startswith(input_line):
				execute_platform = line.split(input_line,1)
				execute = execute_platform[1]
				execute = execute.rstrip()
				execute = terminal_command + execute
				subprocess.call(execute, shell=True)
				executed_count = executed_count + 1
				executed_count = 0
				subprocess.call("ralia.sh", shell = True)
				exit()
			else:
				executed_count = executed_count + 1
				continue
