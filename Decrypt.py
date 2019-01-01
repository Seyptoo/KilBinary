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
				instanceResult = int(BytesOp[0]) + int(BytesOp[1])
	
			elif("-" in BytesOp):
				# Test then for subtractions and development.
				BytesOp = BytesOp.split("-")
				instanceResult = int(BytesOp[0]) - int(BytesOp[1])

			elif("*" in BytesOp):
				# Multiplications and split the variable next.
				BytesOp = BytesOp.split("*")
				instanceResult = int(BytesOp[0]) * int(BytesOp[1])

			elif("/" in BytesOp):
				# Division for data recovery.
				BytesOp = BytesOp.split("/")
				instanceResult = int(BytesOp[0]) / int(BytesOp[1])
			
			if(NumberOne%2 != 0):
				if(len(str(instanceResult)) < 3):
					while len(str(instanceResult)) < 3:
						instanceResult = "0"+str(instanceResult)
			else:
				if(len(str(instanceResult)) < 5):
					while len(str(instanceResult)) < 5:
						instanceResult = "0"+str(instanceResult)
		
			DecryptAlgorithm += str(instanceResult)
			NumberOne += 1

	return(DecryptAlgorithm)
