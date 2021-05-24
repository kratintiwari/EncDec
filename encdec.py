#! usr/bin/python3

import sys,getopt
import urllib.parse
import re

def encdec(argv):
	toEncode=''
	toDecode=''

	try:
		opts,args = getopt.getopt(argv,"h:e:d:",["enc=","dec="])
	except getopt.GetoptError:
		print ('encdec.py -e <string/url to encode> -d <string/url to decode>')
		sys.exit(2)

	for opt,arg in opts:
		if opt == '-h':
			print ("""encdec.py -e '<string/url to encode>' -d '<string/url to decode>'""")
			sys.exit()

		elif opt == '-e':
			toEncode = str(arg)

			whitespace = re.search(' +', toEncode) #search if passed argument has whitespace or not
			if whitespace:
				
				encodedString = urllib.parse.quote_plus(toEncode,safe='')
				print('-------------------')
				print(encodedString)
				print('-------------------')
			else:
				
				encodedString = urllib.parse.quote(toEncode,safe='')
				print('-------------------')
				print(encodedString)
				print('-------------------')


		elif opt == '-d':
			toDecode = str(arg)

			decodedString = urllib.parse.unquote(toDecode)
			print('-------------------')
			print(decodedString)
			print('-------------------')


if __name__ == "__main__":
	encdec(sys.argv[1:]) 
