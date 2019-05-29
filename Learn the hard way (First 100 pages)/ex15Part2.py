#Study drill, creating something simmlar to the next ex.
# open function parameters -

#	 'w' stands for write - 
#	 "r" stands for read - 
# 	 "a" stands for append - 
#  		*They stand for the mode you are using the file in

from sys import argv

script, filename = argv

print(f"Opening {filename}...")
txt_output = open(filename,'r')
print(txt_output.read())
txt_output.close()
txt_input = open(filename, 'a')
txt_input.write("\n")
txt_input.write("NewLine")
txt_input.write("\n")
txt_input.write("NewLine")
txt_input.write("\n")
txt_input.write("NewLine")
txt_input.write("\n")
txt_input.write("NewLine")
txt_input.write("\n")
txt_input.write("NewLine2")

print("Closing..")
txt_input.close()
