import binascii

def calc(octet):
	decrypt = ""
	n = 1

	octet = octet.split("=")
	
	for calc in octet:
		if calc != '':
			print("[*] calcul de %s" % (calc))
			if "+" in calc:
				calc = calc.split("+")
				resultat = int(calc[0]) + int(calc[1])
				print("[-] "+str(resultat))
			elif "-" in calc:
				calc = calc.split("-")
				resultat = int(calc[0]) - int(calc[1])
				print("[-] "+str(resultat))
			elif "*" in calc:
				calc = calc.split("*")
				resultat = int(calc[0]) * int(calc[1])
				print("[-] "+str(resultat))
			elif "/" in calc:
				calc = calc.split("/")
				resultat = int(calc[0]) / int(calc[1])
				print("[-] "+str(resultat))
			
			if n%2 != 0:
				if len(str(resultat)) < 3:
					while len(str(resultat)) < 3:
						resultat = "0"+str(resultat)
			else:
				if len(str(resultat)) < 5:
					while len(str(resultat)) < 5:
						resultat = "0"+str(resultat)
						
			print("RES: "+str(resultat))
		
			decrypt += str(resultat)
			n += 1

	return(decrypt)
	
	
def alphabet_convert(calcbin):
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
binaire_list = alphabet_convert(text_crypt)
binaire = calc(binaire_list)
decypt_text = binascii.unhexlify('%x' % int('0b' + binaire, 2)).decode("ascii")
print("\n---------------\n[+] Decrypt SUCCESS ! ")
print("\nTEXTE: "+decypt_text)



	
