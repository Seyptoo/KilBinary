#coding:utf-8

import binascii
import sys
import subprocess

CHECK_VERSION = sys.version_info <= (3,0)
if(CHECK_VERSION):
	# Let's test if the program is in Python 2 or 3.
	sys.exit("[!] Version of Python is incorrect.")

def BertModel(AlgorithmBytes):
	"""
	This function will test the algorithm.
	Opp check the algorithm.

	Parameters
	----
	AlgorithmBytes : It's the bytes in the hash

	Return
	----
	He will return the hash with success.	
	"""
	DecryptAlgorithm = ("")
	NumberOne = 1
	# We create the basic variables.
	AlgorithmBytes = AlgorithmBytes.split("=")
	
	for BytesOp in AlgorithmBytes:
		# Create loop for hashsing.
		if(BytesOp != ''):
			# Test is variable is empty.
			if("+" in BytesOp):
				# Test for additions of hash and development.
				BytesOp = BytesOp.split("+")
				resultat = int(BytesOp[0]) + int(BytesOp[1])
	
			elif("-" in BytesOp):
				# Test then for subtractions and development.
				BytesOp = BytesOp.split("-")
				resultat = int(BytesOp[0]) - int(BytesOp[1])

			elif("*" in BytesOp):
				# Multiplications and split the variable next.
				BytesOp = BytesOp.split("*")
				resultat = int(BytesOp[0]) * int(BytesOp[1])

			elif("/" in BytesOp):
				# Division for data recovery.
				BytesOp = BytesOp.split("/")
				resultat = int(BytesOp[0]) / int(BytesOp[1])
			
			if(NumberOne%2 != 0):
				if(len(str(resultat)) < 3):
					while len(str(resultat)) < 3:
						resultat = "0"+str(resultat)
			else:
				if(len(str(resultat)) < 5):
					while len(str(resultat)) < 5:
						resultat = "0"+str(resultat)
		
			DecryptAlgorithm += str(resultat)
			NumberOne += 1

	return(DecryptAlgorithm)
	
	
def BertPanel(calcbin):
	alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	alphabet = list(alphabet)
	
	text_decrypt = ""
	
	for caractere in calcbin:
		if caractere in alphabet:
			pos = alphabet.index(caractere)
			text_decrypt += str(pos)
			
		else:
			text_decrypt += caractere
	
	return(text_decrypt)
	
def text_to_bin(texte):
	list_octet = [ bin(ord(ch))[2:].zfill(8) for ch in texte ]
	liste = []
	
	for octet in list_octet:
		seg_1 = octet[:3]
		seg_2 = octet[3:]
		
		liste.append(seg_1)
		liste.append(seg_2)
		
	return(liste)

text_crypt = input("decrypt> ")
binaire_list = BertPanel(text_crypt)
binaire = BertModel(binaire_list)
decypt_text = binascii.unhexlify('%x' % int('0b' + binaire, 2)).decode("ascii")
print("\n TEXTE : "+decypt_text)



	
