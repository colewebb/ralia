import subprocess
input = raw_input("What do you want to search for? ")
execute = "firefox https://en.wikipedia.org/wiki/Special:Search?search='" + input + "'"
subprocess.call(execute, shell=True)
