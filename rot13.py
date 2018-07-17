#!/usr/bin/env python

__author__ = "TuesdayIVU (Kyle)"
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "TuesdayIVU (Kyle)"
__email__ = "tuesdayivu@gmail.com"
__status__ = "Meh"

#encrypt: e = (x+k)(mod 26)
#decrypt: e = (x-k)(mod 26)

import argparse


parser = argparse.ArgumentParser(
	formatter_class=argparse.RawDescriptionHelpFormatter,
	description=('''
Basic Encryption and Decryption using a rotation on a 26 character alphabet.
'''))

parser.add_argument('-e', metavar='Number to encrypt on', help='encrypt by n numbers', type=int, choices=range(1, 25))
parser.add_argument('-d', metavar='Number to decrypt on', help='decrypt by n numbers', type=int, choices=range(1, 25))
parser.add_argument('-s', metavar='string', help='String to rotate k times', required=True)
args = parser.parse_args()

if (args.s):
	input_string = args.s.upper()
	input_list = list(input_string)
	output = ""
	for x in input_list:
		if (65 <= ord(x) <= 90):
			if (args.e):
				k = int(args.e) #convert string to int
				e = ((ord(x)-65)+k) % 26
			elif (args.d):
				k = int(args.d) #convert string to int
				e = ((ord(x)-65)+k) % 26
			output+=chr(e+65)
		elif (ord(x) == 32):
			output+=" "
		else:
			error=""

print output





