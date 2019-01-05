#coding:utf-8

import binascii
import sys
import subprocess

from modules import options
from modules import Crypt
from modules import Decrypt

class Algorithm(object):
	def __init__(self, ArgumentText=None,
				BinaryList=None):
		# Calling options since directory modules.
		self.encrypt = options.encrypt
		self.decrypt = options.decrypt

		self.Argument = ArgumentText
		self.BinaryList = BinaryList

	def __str__(self):
		if(self.encrypt):
			self.Argument = ""
			self.BinaryList = Crypt.BertVic(self.encrypt)
			# Calling function available connection.
			for Bytes in self.BinaryList:
				ArgumentCalc = Crypt.BertModel(Bytes)
				self.Argument += ArgumentCalc

			ArgumentFunc = Crypt.BertPanel(self.Argument)
			# Algorithm is created.. binary
			print("[+] ENCRYPT : "+ ArgumentFunc)
			
		if(self.decrypt):
			self.BinaryList = Decrypt.BertPanel(self.decrypt)
			BinaryArguments = Decrypt.BertModel(self.BinaryList)
			DecryptArguments = binascii.unhexlify('%x' % int('0b' + BinaryArguments, 2)).decode("ascii")
			print("[+] DECRYPT : "+ DecryptArguments)

	def ArgumentOptions(self):
		if not(self.encrypt or self.decrypt):
			starting = subprocess.Popen(["python", sys.argv[0], "--help"])
		
if __name__ == "__main__":
	Calling = Algorithm()
	Calling.ArgumentOptions()
	Calling.__str__()	
			
