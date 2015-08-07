input = some-key
terminal-command = "xfce4-terminal --tab -x "
if input == ".":
	call terminal-command xdg-open $PWD
elif input == "..":
	call terminal-command xdg-open $PWD #without the last directory on the end
else:
	find some-key in db
	return key-value
	call terminal-command xdg-open key-value
