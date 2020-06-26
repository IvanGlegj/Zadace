#Papir, Škare, Kamen, Gušter, Spock The Big Bang Theory

Prvi_Igrac = input("Unesite ime prvog igrača: ")
Drugi_Igrac = input("Unesite ime drugog igrača: ")

ponovo = "Yes" 
kriva_vrijednost = False 

Bodovi_1 = int(0)
Bodovi_2 = int(0)

while ponovo == "Yes":
	print("=" * 20)
	print("Odaberite jedno od navedenog: Papir, Škare, Kamen, Gušter, Spock")
	print("=" * 20)

	odabir_1 = str(input("{}: ".format(Prvi_Igrac)))
	odabir_2 = str(input("{}: ".format(Drugi_Igrac)))

	if(odabir_1 == odabir_2):
		print("Izjednačeno!")
		kriva_vrijednost = True

	elif(odabir_1 == "Papir"):
		if(odabir_2 == "Kamen"):
			print("{} je pobijedio!".format(Prvi_Igrac))
			Bodovi_1 += 1 
		elif(odabir_2 == "Škare"):
			print("{} je pobijedio!".format(Drugi_Igrac))
			Bodovi_2 += 1
		elif(odabir_2 == "Gušter"):
			print("{} je pobjedio!".format(Drugi_Igrac))
			Bodovi_2 += 1
		elif(odabir_2 == "Spock"):
			print("{} je pobjedio!".format(Prvi_Igrac))
			Bodovi_1 += 1
		else:
			print("{} je unio/jela krivu vrijednost.".format(Drugi_Igrac))
			kriva_vrijednost = True

	elif(odabir_1 == "Kamen"):
		if(odabir_2 == "Škare"):
			print("{} je pobijedio!".format(Prvi_Igrac))
			Bodovi_1 += 1	
		elif(odabir_2 == "Papir"):
			print("{} je pobijedio!".format(Drugi_Igrac))
			Bodovi_2 += 1
		elif(odabir_2 == "Gušter"):
			print("{} je pobjedio!".format(Drugi_Igrac))
			Bodovi_2 += 1
		elif(odabir_2 == "Spock"):
			print("{} je pobjedio!".format(Prvi_Igrac))
			Bodovi_1 += 1
		else:
			print("{} je unio/jela krivu vrijednost.".format(Drugi_Igrac))
			kriva_vrijednost = True

	elif(odabir_1 == "Škare"):
		if(odabir_2 == "Papir"):
			print("{} je pobijedio!".format(Prvi_Igrac))
			Bodovi_1 += 1	
		elif(odabir_2 == "Kamen"):
			print("{} je pobijedio!".format(Drugi_Igrac))
			Bodovi_2 += 1
		elif(odabir_2 == "Gušter"):
			print("{} je pobjedio!".format(Prvi_Igrac))
			Bodovi_1 += 1
		elif(odabir_2 == "Spock"):
			print("{} je pobjedio!".format(Drugi_Igrac))
			Bodovi_2 += 1	
		else:
			print("{} je unio/jela krivu vrijednost.".format(Drugi_Igrac))
			kriva_vrijednost = True

	elif(odabir_1 == "Gušter"):
		if(odabir_2 == "Papir"):
			print("{} je pobijedio!".format(Prvi_Igrac))
			Bodovi_1 += 1	
		elif(odabir_2 == "Kamen"):
			print("{} je pobijedio!".format(Drugi_Igrac))
			Bodovi_2 += 1
		elif(odabir_2 == "Škare"):
			print("{} je pobjedio!".format(Drugi_Igrac))
			Bodovi_2 += 1
		elif(odabir_2 == "Spock"):
			print("{} je pobjedio!".format(Prvi_Igrac))
			Bodovi_1 += 1	
		else:
			print("{} je unio/jela krivu vrijednost.".format(Drugi_Igrac))
			kriva_vrijednost = True
	
	elif(odabir_1 == "Spock"):
		if(odabir_2 == "Papir"):
			print("{} je pobijedio!".format(Drugi_Igrac))
			Bodovi_2 += 1	
		elif(odabir_2 == "Kamen"):
			print("{} je pobijedio!".format(Prvi_Igrac))
			Bodovi_1 += 1
		elif(odabir_2 == "Škare"):
			print("{} je pobjedio!".format(Prvi_Igrac))
			Bodovi_1 += 1
		elif(odabir_2 == "Gušter"):
			print("{} je pobjedio!".format(Drugi_Igrac))
			Bodovi_2 += 1
		else:
			print("{} je unio/jela krivu vrijednost.".format(Drugi_Igrac))
			kriva_vrijednost = True

	else:
		print("{} je unio/jela krivu vrijednost.".format(Prvi_Igrac))
		kriva_vrijednost = True

	if(kriva_vrijednost == False):
		print("=" * 20)
		print("{} ima {} bodova.".format(Prvi_Igrac, Bodovi_1))
		print("{} ima {} bodova.".format(Drugi_Igrac, Bodovi_2))
		print("=" * 20)

	ponovo = input("Započeti novu Igru? (Da/Ne)")