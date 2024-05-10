print("Whatsapp Export processor loaded...") #Built for Whatsappp message exports 
import time
import string
import sys
t = time.strftime("%H:%M:%S", time.localtime())
def clean(msg):
	out = msg.lower().translate(str.maketrans('', '', string.punctuation))
	try:
		out = out.replace('media omitted' , '')
	except:
		pass
	return(out)
inputFile = input("[?]Enter the name of your .txt data file: ") #input raw data file
outputFile = input("[?]Give your output .txt file a name: ") #write data in output file
print("(if file already exists, the output will be appended, not overwritten)")
output = open(outputFile , 'a') # will append to file or make few file
time.sleep(0.001)
try:
	textfile = open(inputFile ,"r") # Input File 
except:
	print(f"Your input file {inputFile} does not exist!")
	sys.exit()
print("File loaded successfully...")
time.sleep(0.001)
print("File processing has begun...")
strlines = textfile.readlines()
cleanlines = []
n = 0
start_time = time.time()
for _ in range(len(strlines)):
	rawmsg = strlines[n].replace("\n","").split(":") #remove line breaks
	try:
		msg = rawmsg[2] #second split element
		cleanlines.append(clean(msg))
		output.write(clean(msg)) #write element in output file
	except:
		cleanlines.append(clean(rawmsg[0]))
		output.write(clean(rawmsg[0]))
	if n%5000 == 0:
		print("[!]Reached message number: " , n) #pogress record
	n = n + 1
N = n - 1
end_time = time.time()
print(f"Finished running loop in {end_time - start_time:.2f} seconds.")
print("Ended process. Total messages processed: ", N)
