#Paper, Scissors, Rock, Lizard, Spock The Big Bang Theory
#Ivan Glegj

Ime_Prvog_Igraca = input("Unesite ime igrača 1...")
Ime_Drugog_Igraca = input("Unesite ime igrača 2...")

ponovo = "Ponovi" #Ponavljanje igre
kriva_vrijednost = False #Neće prikazati bodove ako je netko unio krivu vrijednost

Bodovi_1 = int(0)
Bodovi_2 = int(0)

#Glavna petlja
while ponovo == "Ponovi":
	print("=" * 20)
	print("Odaberite jedno od navedenog: Papir, Škare, Kamen, Gušter, Spock")
	print("=" * 20)

	#Igračev odabir
	odabir_1 = str(input("{}: ".format(Ime_Prvog_Igraca)))
	odabir_2 = str(input("{}: ".format(Ime_Drugog_Igraca)))

	#Provjere
	if(odabir_1 == odabir_2):
		print("Izjednačeno!")
		kriva_vrijednost = True

	elif(odabir_1 == "Papir"):
		if(odabir_2 == "Kamen"):
			print("{} je pobijedio!".format(Ime_Prvog_Igraca))
			Bodovi_1 += 1 
		elif(odabir_2 == "Škare"):
			print("{} je pobijedio!".format(Ime_Drugog_Igraca))
			Bodovi_2 += 1
		elif(odabir_2 == "Gušter"):
			print("{} je pobjedio!".format(Ime_Drugog_Igraca))
			Bodovi_2 += 1
		elif(odabir_2 == "Spock"):
			print("{} je pobjedio!".format(Ime_Prvog_Igraca))
			Bodovi_1 += 1
		else:
			print("{} je unio/jela krivu vrijednost.".format(Ime_Drugog_Igraca))
			kriva_vrijednost = True

	elif(odabir_1 == "Kamen"):
		if(odabir_2 == "Škare"):
			print("{} je pobijedio!".format(Ime_Prvog_Igraca))
			Bodovi_1 += 1	
		elif(odabir_2 == "Papir"):
			print("{} je pobijedio!".format(Ime_Drugog_Igraca))
			Bodovi_2 += 1
		elif(odabir_2 == "Gušter"):
			print("{} je pobjedio!".format(Ime_Drugog_Igraca))
			Bodovi_2 += 1
		elif(odabir_2 == "Spock"):
			print("{} je pobjedio!".format(Ime_Prvog_Igraca))
			Bodovi_1 += 1
		else:
			print("{} je unio/jela krivu vrijednost.".format(Ime_Drugog_Igraca))
			kriva_vrijednost = True

	elif(odabir_1 == "Škare"):
		if(odabir_2 == "Papir"):
			print("{} je pobijedio!".format(Ime_Prvog_Igraca))
			Bodovi_1 += 1	
		elif(odabir_2 == "Kamen"):
			print("{} je pobijedio!".format(Ime_Drugog_Igraca))
			Bodovi_2 += 1
		elif(odabir_2 == "Gušter"):
			print("{} je pobjedio!".format(Ime_Prvog_Igraca))
			Bodovi_1 += 1
		elif(odabir_2 == "Spock"):
			print("{} je pobjedio!".format(Ime_Drugog_Igraca))
			Bodovi_2 += 1	
		else:
			print("{} je unio/jela krivu vrijednost.".format(Ime_Drugog_Igraca))
			kriva_vrijednost = True

	elif(odabir_1 == "Gušter"):
		if(odabir_2 == "Papir"):
			print("{} je pobijedio!".format(Ime_Prvog_Igraca))
			Bodovi_1 += 1	
		elif(odabir_2 == "Kamen"):
			print("{} je pobijedio!".format(Ime_Drugog_Igraca))
			Bodovi_2 += 1
		elif(odabir_2 == "Škare"):
			print("{} je pobjedio!".format(Ime_Drugog_Igraca))
			Bodovi_2 += 1
		elif(odabir_2 == "Spock"):
			print("{} je pobjedio!".format(Ime_Prvog_Igraca))
			Bodovi_1 += 1	
		else:
			print("{} je unio/jela krivu vrijednost.".format(Ime_Drugog_Igraca))
			kriva_vrijednost = True
	
	elif(odabir_1 == "Spock"):
		if(odabir_2 == "Papir"):
			print("{} je pobijedio!".format(Ime_Drugog_Igraca))
			Bodovi_2 += 1	
		elif(odabir_2 == "Kamen"):
			print("{} je pobijedio!".format(Ime_Prvog_Igraca))
			Bodovi_1 += 1
		elif(odabir_2 == "Škare"):
			print("{} je pobjedio!".format(Ime_Prvog_Igraca))
			Bodovi_1 += 1
		elif(odabir_2 == "Gušter"):
			print("{} je pobjedio!".format(Ime_Drugog_Igraca))
			Bodovi_2 += 1
		else:
			print("{} je unio/jela krivu vrijednost.".format(Ime_Drugog_Igraca))
			kriva_vrijednost = True

	else:
		print("{} je unio/jela krivu vrijednost.".format(Ime_Prvog_Igraca))
		kriva_vrijednost = True

	#Ako je netko unio krivu vrijednost ili ako je izjednačeno, neće prikazati bodove.
	if(kriva_vrijednost == False):
		print("=" * 20)
		print("{} ima {} bodova.".format(Ime_Prvog_Igraca, Bodovi_1))
		print("{} ima {} bodova.".format(Ime_Drugog_Igraca, Bodovi_2))
		print("=" * 20)

	ponovo = input("Ponovite igru? (Da/Ne)")