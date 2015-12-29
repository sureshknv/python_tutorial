#!/usr/bin/python
import sys
file_name=raw_input("Enter the file name:")
if len(file_name)==0:
    print "Next time please enter something"
    sys.exit()
try:
    file=open(file_name, "w")
except IOError:
    print "There is an error in opening a file and writing" ,file_name
    sys.exit()
print "Enter '",file_finish,
print "' When Finished"
while file_text != file_finish:
    file_text=raw_input("Enter the text: ")
    if file_text==file_finish:
        file.close
        break
    file.write(file_text)
    file.write("\n")
file.close()

try:
    file=open(file_name, "r")
except IOError:
    print "There was an error in reading"
    sys.exit()
file_text=file.read()
file.close()
print file_text




