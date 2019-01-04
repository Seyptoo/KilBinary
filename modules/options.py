#coding:utf-8

from optparse import *

parser = OptionParser()
parser.add_option("-e", "--encrypt", dest="encrypt", help="encrypt")
parser.add_option("-d", "--decrypt", dest="decrypt", help="decrypt")
(options, args) = parser.parse_args()

encrypt = options.encrypt
decrypt = options.decrypt
