# update: we can cd out of directories and up the tree, but we can't
# cd back down into other directories. Also, cding into a directory 
# appears to break the prompt. It refuses to take more commands.

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

status = "devel"

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

query = username + "@" + host + ":" + location + prompt

while count >= executed_count:
	input = raw_input(query)
	if input == "exit":
		exit()
	elif input == "x":
		exit()
	elif input == "v":
		print(status)
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
				executed = True
				print(executed_count)
				executed_count = 0
			else:
				executed_count = executed_count + 1
				continue
	if executed == False:
		if input.startswith("cd "):
			input = input + " && ralia.sh"
			subprocess.call(input, shell=True)
			exit()
		else:
			subprocess.call(input, shell=True)
