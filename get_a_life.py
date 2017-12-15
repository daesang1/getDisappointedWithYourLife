

fo = open("disappoint.txt", 'r')
print "Name of the file: ", fo.name

count = []
rline = ""
while rline != "EOF":
	rline = fo.readline()
	if " hrs on record\n" in rline:
		print ("This is test: " + rline)
		count += [float(rline.replace(" hrs on record",""))]
	

print sum(count) 
