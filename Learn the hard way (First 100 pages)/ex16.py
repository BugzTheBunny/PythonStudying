#Copieng information from one file to another, and appending it in the end.
#Normally the first argument is sample.txt, and the second is sample2.txt
from sys import argv
#this import gives you the function tha tests if a file exists or no.
from os.path import exists

script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}")

#normal:

#in_file = open(from_file)
#indata = in_file.read()

#one line:
#reads from a file it opens
indata = open(from_file).read()
outdata = open(to_file).read()
#Cheking the length of the file by bytes
print(f"The file exists? {exists(to_file)} and the input file is {len(indata)} bytes long , output data is {len(outdata)}")
input() 

#While you are in 'a' appending mode, you still have to use .write()
out_file = open(to_file, 'a').write(indata)

