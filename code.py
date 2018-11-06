import sys

if len( sys.argv ) > 3  :
	print "Sorry currently this script supports a single input file"
else:
	csv = open(sys.argv[1], "r")
	if not ".vcf" in sys.argv[2]:
		output = open(sys.argv[2]+".vcf", "w")
	else:
		output = open(sys.argv[2], "w")

	names = ["samfan","nrhhsiae","random"]
	numbers = []
	for line in csv:
		numbers.append( line )
	i = 0
	for number in numbers:
		i = i + 1
		output.write( """BEGIN:VCARD
VERSION:3.0
N:"""+ str(i) +""";FRomPC
FN:hELL"""+ str(i)  +"""
TEL;TYPE=CELL:+91"""+ number[:10] +"""
END:VCARD\n""" )
		print(i)
		i += 1
