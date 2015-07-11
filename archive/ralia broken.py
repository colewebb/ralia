db_location = "home/rebooted/Scripts/ralia/db.txt"
username = "user"
host = "ralia"
prompt = " >>> "

import subprocess

# importing subprocess module so that this Python script can invoke outside programs and scripts.

try:
	db = open("/home/rebooted/Scripts/ralia/db.txt")
except:
	print("The standard database file appears not to exist.\nIf it does, please edit this file and\nchange the 'db' variable to the location of\nthe database file.")
	exit()

# looking for a database file, and giving an error if the file isn't found.

count = 0
searched_count = 0
for line in db:
	count = count + 1

while True:
	input = raw_input(username + "@" + host + prompt)
	if input == "exit":
		exit()
	else:
		while searched_count >= count:
			for line in db:
				searched_count = searched_count + 1
				if line.startswith(input):
					input = input + " -> "
					execute_platform = line.split(input,1)
					execute = execute_platform[1]
					execute = execute.rstrip()
					subprocess.call(execute, shell=True)
				else:
					continue
		

