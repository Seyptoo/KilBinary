#coding:utf-8

from optparse import *

parser = OptionParser(add_help_option=False)
parser.add_option("-e", "--encrypt", dest="encrypt", help="encrypt")
parser.add_option("-d", "--decrypt", dest="decrypt", help="decrypt")
parser.add_option("-v", "--validys", dest="validys", help="validys")
(options, args) = parser.parse_args()

encrypt = options.encrypt
decrypt = options.decrypt
validys = options.validys
