import sys

action = sys.argv[1]
string = sys.argv[2]

encrypt_dict = {
    'z': '0\\',
    'q': '1\\',
    'a': '2\\',
    'b': '2|',
    'c': '2/',
    'd': '3\\',
    'e': '3|',
    'f': '3/',
    'g': '4\\',
    'h': '4|',
    'i': '4/',
    'j': '5\\',
    'k': '5|',
    'l': '5/',
    'm': '6\\',
    'n': '6|',
    'o': '6/',
    'p': '7\\',
    'r': '7|',
    's': '7/',
    't': '8\\',
    'u': '8|',
    'v': '8/',
    'w': '9\\',
    'x': '9|',
    'y': '9/'

}

decrypt_dict = {
     '0\\': 'z',
     '1\\': 'q',
     '2\\': 'a',
     '2|': 'b',
     '2/': 'c',
     '3\\': 'd',
     '3|': 'e',
     '3/': 'f',
     '4\\': 'g',
     '4|': 'h',
     '4/': 'i',
     '5\\': 'j',
     '5|': 'k',
     '5/': 'l',
     '6\\': 'm',
     '6|': 'n',
     '6/': 'o',
     '7\\': 'p',
     '7|': 'r',
     '7/': 's',
     '8\\': 't',
     '8|': 'u',
     '8/': 'v',
     '9\\': 'w',
     '9|': 'x',
     '9/': 'y',
}
 
def rotary_decrypt(string):
	output = ""
	for x in string_list:
		output+=decrypt_dict[x] 
	return output

def rotary_encrypt(string):
	output = ""
	for x in string_list:
		output+=encrypt_dict[x] 
	return output


if action == "-d":
	#print "decrypt"
	input_string = string.lower()
	n = 2
	# "explode" string into pairs of characters
	string_list = [input_string[i:i+n] for i in range(0, len(input_string), n)]
	decrypted_string = rotary_decrypt(string_list)
	print decrypted_string.upper()

elif action == "-e":
	#print "encrypt"
	input_string = string.lower()
	string_list = list(input_string)
	encrypted_string = rotary_encrypt(string_list)
	print encrypted_string.upper()
else:
	print "wat"
	






