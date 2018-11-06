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
	for name in names:
		i= 0
		output.write( """BEGIN:VCARD
VERSION:3.0
N:"""+ name +""";Test
FN:hELL"""+ name  +"""
TEL;TYPE=CELL:122"""+ str( i ) + """
EMAIL;TYPE=INTERNET:rgm-ietf@htt-consult.com
END:VCARD\n""" )
		i += 1
