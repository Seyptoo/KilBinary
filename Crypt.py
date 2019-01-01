def calc(octet):
	print("calcul de %s" % (octet))
	for n in range(0, 10000):
		for n2 in range(0, 10000):
			addition = n + n2
			#return("%s + %s = %s" % (str(n), str(n2), str(addition)))
			#input('')
			soustraction = n - n2
			soustraction2 = n2 - n
			multiplication  = n * n2
			try:
				division = int(n / n2)
				division2 = int(n2 / n)
				if division == int(octet):
					return("%s/%s=" % (str(n), str(n2)))
				if division2 == int(octet):
					return("%s/%s=" % (str(n2), str(n)))
			except:
				pass
			
			if addition == int(octet):
				return("%s+%s=" % (str(n), str(n2)))
			if soustraction == int(octet):
				return("%s-%s=" % (str(n), str(n2)))
			if soustraction2 == int(octet):
				return("%s-%s=" % (str(n2), str(n)))
			if multiplication == int(octet):
				return("%s*%s=" % (str(n), str(n2)))
				
def alphabet_convert(calcbin):
	alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	alphabet = list(alphabet)
	
	text_crypt = ""
	
	for caractere in calcbin:
		try:
			car = int(caractere)
			pos = alphabet[car]
			text_crypt += pos
			
		except:
			text_crypt += caractere
			
	return(text_crypt)
	
def text_to_bin(texte):
	list_octet = [ bin(ord(ch))[2:].zfill(8) for ch in texte ]
	liste = []
	
	for octet in list_octet:
		seg_1 = octet[:3]
		seg_2 = octet[3:]
		
		liste.append(seg_1)
		liste.append(seg_2)
		
	return(liste)

calc_text = ""

texte = input("crypt> ")

bin_list = text_to_bin(texte)

for octet in bin_list:
	calcul = calc(octet)
	calc_text += calcul

final_crypt = alphabet_convert(calc_text)
print("HASH: "+final_crypt)
	
