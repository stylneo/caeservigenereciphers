#!/usr/bin/env python3

'''
Enconder/Decoder for Caeser and Vigenere ciphers
Usage:
	ceaser_vigenere_cipher.py <MODE> <MESSAGE> <KEY/KEYWORD>
	<MODE>:
		cE for encoding with Caeser Cipher
		cD for decoding with Caeser Cipher
		vE for encoding with Vigenere Cipher
		vD for encoding with Vigenere Cipher
	<MESSAGE>:
		String you want to encode (characters not in the defined alphabet will be skipped)
	<KEY/KEYWORD>
		Integer in the case of Caeser cipher
		String in the case of Vigenere cipher
	Ex:
		python ceaser_vigenere_cipher.py cE "hello world" 3
		Output: khoor zruog
		
		python ceaser_vigenere_cipher.py vD "tlthijicupxl" letmeread
		Output: ihavesecrets
'''

__author__	= 'Stylianos Neocleous'
__email__	= 's.neocleous@campus.fct.unl.pt'
__date__	= '2018/03/18'

import sys

alphabet = 'abcdefghijklmnopqrstuvwxyz'

def encode(letter, shift):
	return alphabet[(alphabet.find(letter)+shift)%len(alphabet)]
	
def decode(letter, shift):
	return alphabet[(alphabet.find(letter)-shift)%len(alphabet)]

def encodeMsg(message, shift):
	out=''
	for letter in message:
		if letter in alphabet:
			out+=encode(letter, shift)
		else:
			out+=letter
	return out

def decodeMsg(message, shift):
	out = ''
	for letter in message:
		if letter in alphabet:
			out+=decode(letter, shift)
		else:
			out+=letter
	return out
	
def vigenereEncode(message, keyword):
	index = 0
	out = ''
	for letter in message:
		if letter in alphabet:
			out+=encode(letter, alphabet.find(keyword[index]))
			index=(index+1)%len(keyword)
		else:
			out+=letter
	return out

def vigenereDecode(message, keyword):
	index = 0
	out = ''
	for letter in message:
		if letter in alphabet:
			out+=decode(letter, alphabet.find(keyword[index]))
			index=(index+1)%len(keyword)
		else:
			out+=letter
	return out

def printUsage():
	print('Usage: {} <MODE> <MESSAGE> <KEY/KEYWORD>'.format(sys.argv[0]))
	print('''Modes:
	cE for encoding with Caeser Cipher
	cD for decoding with Caeser Cipher
	vE for encoding with Vigenere Cipher
	vD for encoding with Vigenere Cipher''')
	
def main():
	
	if len(sys.argv) != 4:
		printUsage()
	elif sys.argv[1] == 'cE':
		message = sys.argv[2].lower()
		try:
			shift = int(sys.argv[3])
		except ValueError:
			print('Error parsing key. Use an integer for the key.')
			return
		print(encodeMsg(message, shift))
	elif sys.argv[1] == 'cD':
		message = sys.argv[2].lower()
		try:
			shift = int(sys.argv[3])
		except ValueError:
			print('Error parsing key. Use an integer for the key.')
			return
		print(decodeMsg(message, shift))
	elif sys.argv[1] == 'vE':
		message = sys.argv[2].lower()
		keyword = sys.argv[3].lower()
		for k in keyword:
			if not k.isalpha():
				raise ValueError('Invalid keyword, use characters in the a-z range')
		print(vigenereEncode(message, keyword))
	elif sys.argv[1] == 'vD':
		message = sys.argv[2].lower()
		keyword = sys.argv[3].lower()
		for k in keyword:
			if not k.isalpha():
				raise ValueError('Invalid keyword, use characters in the a-z range')
		print(vigenereDecode(message, keyword))
	else:
		printUsage()
	
	
if __name__ == '__main__':
	main()