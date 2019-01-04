#coding:utf-8

import sys
import subprocess


CHECK_VERSION = sys.version_info <= (3,0)
if(CHECK_VERSION):
	# Let's test if the program is in Python 2 or 3.
	sys.exit("[!] Version of Python is incorrect.")

def BertModel(hashing_octet):
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
	for BytesRow in range(0, 10000):
		# Create loop for hashsing.
		for OctetRow in range(0, 10000):
			# Create loop for octets.
			AOperation = BytesRow + OctetRow
			SOperation = BytesRow - OctetRow
			ZOperation = OctetRow - BytesRow
			MOperation = BytesRow * OctetRow

			try:
				# When the function is of good cause..
				# If there is a problem with the division, go straight into the exception.

				DOperation = int(BytesRow / OctetRow)
				OOperation = int(OctetRow / BytesRow)

				if DOperation == int(hashing_octet):
					return("%s/%s=" % (str(BytesRow), str(OctetRow)))
				if OOperation == int(hashing_octet):
					return("%s/%s=" % (str(OctetRow), str(BytesRow)))
				
				# A division error can happen so I made an exception.
				# The truth that it's cool to make an exception but I put a pass to do nothing.
			except ZeroDivisionError as e:
				pass

			if AOperation == int(hashing_octet):
				return("%s+%s=" % (str(BytesRow), str(OctetRow)))
			if SOperation == int(hashing_octet):
				return("%s-%s=" % (str(BytesRow), str(OctetRow)))
			if ZOperation == int(hashing_octet):
				return("%s-%s=" % (str(OctetRow), str(BytesRow)))
			if MOperation == int(hashing_octet):
				return("%s*%s=" % (str(BytesRow), str(OctetRow)))
				
def BertPanel(BinaryCalc):
	"""
	This function will test the algorithm.
	Opp check the algorithm.

	Parameters
	----
	BinaryCalc : It's the bytes in the hash

	Return
	----
	He will return the hash with success.	
	"""
	Alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	Alphabet = list(Alphabet)
	
	AlgorithmCrypt = ""
	
	for Character in BinaryCalc:
		try:
			# Create exception for testing.
			Nulling = int(Character)
			Appends = Alphabet[Nulling]
			AlgorithmCrypt += Appends
			# Success for loop hashing.
		except:
			AlgorithmCrypt += Character
			
	return(AlgorithmCrypt)
	
def BertVic(Texting):
	"""
	This function will test the algorithm.
	Opp check the algorithm.

	Parameters
	----
	Texting : It's the bytes in the hash

	Return
	----
	He will return the hash with success.	
	"""
	ListBytes = [ bin(ord(ch))[2:].zfill(8) for ch in Texting ]
	ArguLists = []
	
	for Bytes in ListBytes:
		SegmentOne = Bytes[:3]
		SegmentTwo = Bytes[3:]
		
		ArguLists.append(SegmentOne)
		ArguLists.append(SegmentTwo)
		
	return(ArguLists)


if __name__ == "__main__":
	if(argument.encrypt):
		ArgumentText = ""
		BinaryList = BertVic(argument.encrypt)

		for Bytes in BinaryList:
			ArgumentCalc = BertModel(Bytes)
			ArgumentText += ArgumentCalc
		# Calling the function 'BertPanel(ArgumentText)'
		ArgumentFunc = BertPanel(ArgumentText)
		print("HASH : "+ ArgumentFunc)
	else:
		print("[!] Please enter options -e.")


