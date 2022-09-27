import random
from dice import Dice

number = 0
count = 0
race = 0
age = 0

charnum = input("How many NPC's do you need?: ")
def getrace():
	number = Dice.D100(0)
	if number in range(1,80):
		race = str("Human")
	elif number in range(81,87):
		race = str("Elf")
	elif number in range(88,92):
		race = str("Dwarf")
	elif number in range(93,100):
		r = Dice.D20(0)
		if r in range(1,3):
			race = str("Halfling")
		elif r in range(4,6):
			race = str("Half Elf")
		elif r in range(7,8):
			race = str("Gnome")
		elif r in range(9,10):
			race = str("Orc")
		elif r == 11:
			race = str("Half Orc")
		elif r == 12:
			race = str("Goblin")
		elif r == 13:
			race = str("Drow")
		elif r == 14:
			race = str("Tabaxi")
		elif r == 15:
			race = str("Kenku")
		elif r == 16:
			race = str("Tiefling")
		elif r == 17:
			race = str("Aasimar")
		elif r == 18:
			race = str("Dragonborn")
		elif r == 19:
			race = str("Goliath")
		elif r == 20:
			race = str("Arakocra")
			
		
	return race
def getapg():
	roll_list = []
	for i in range(3):
		roll_list.append(Dice.D100(0))
	print(roll_list)

	g = int(roll_list[0])
	if g in range(1,50):
		apg = str("Gender: Male,")
	elif g in range(51,100):
		apg = str("Gender: Female,")
	p = int(roll_list[1])
	if p in range(1,25):
		newapg = str(" Profession: Commoner(Unemployed),")
		apg = apg + newapg
	elif p in range(26,90):
		r = Dice.D100(0)
		if r in range(1,2):
			newapg = str(" Profession: Farmer,")
			apg = apg + newapg
		elif r in range(3,4):
			newapg = str(" Profession: Artist,")
			apg = apg + newapg
		elif r in range(5,6):
			newapg = str(" Profession: Herbalist,")
			apg = apg + newapg
		elif r in range(7,8):
			newapg = str(" Profession: Horse Trainer,")
			apg = apg + newapg
		elif r in range(9,10):
			newapg = str(" Profession: Blacksmith,")
			apg = apg + newapg
		elif r in range(11,12):
			newapg = str(" Profession: Finesmith,")
			apg = apg + newapg
		elif r in range(13,14):
			newapg = str(" Profession: Locksmith,")
			apg = apg + newapg
		elif r in range(15,16):
			newapg = str(" Profession: Jeweler,")
			apg = apg + newapg
		elif r in range(17,18):
			newapg = str(" Profession: Entertainer,")
			apg = apg + newapg
		elif r in range(19,20):
			newapg = str(" Profession: Teacher,")
			apg = apg + newapg
		elif r in range(21,22):
			newapg = str(" Profession: Armourer,")
			apg = apg + newapg
		elif r in range(23,24):
			newapg = str(" Profession: Cook,")
			apg = apg + newapg
		elif r in range(25,26):
			newapg = str(" Profession: Tailor,")
			apg = apg + newapg
		elif r in range(27,28):
			newapg = str(" Profession: Ropemaker,")
			apg = apg + newapg
		elif r in range(29,30):
			newapg = str(" Profession: Fletcher,")
			apg = apg + newapg
		elif r in range(31,32):
			newapg = str(" Profession: Cooper,")
			apg = apg + newapg
		elif r in range(33,34):
			newapg = str(" Profession: Cartwright,")
			apg = apg + newapg
		elif r in range(35,36):
			newapg = str(" Profession: Carpenter,")
			apg = apg + newapg
		elif r in range(37,38):
			newapg = str(" Profession: Grave Digger / Undertaker,")
			apg = apg + newapg
		elif r in range(39,40):
			newapg = str(" Profession: Winemaker,")
			apg = apg + newapg
		elif r in range(41,42):
			newapg = str(" Profession: Ferryman,")
			apg = apg + newapg
		elif r in range(43,44):
			newapg = str(" Profession: Shipwright,")
			apg = apg + newapg
		elif r in range(45,46):
			newapg = str(" Profession: Ships Capitan,")
			apg = apg + newapg
		elif r in range(47,48):
			newapg = str(" Profession: Fortune Teller,")
			apg = apg + newapg
		elif r in range(49,50):
			newapg = str(" Profession: Handmaiden,")
			apg = apg + newapg
		elif r in range(51,52):
			newapg = str(" Profession: Miller,")
			apg = apg + newapg
		elif r in range(53,54):
			newapg = str(" Profession: Executioner,")
			apg = apg + newapg
		elif r in range(55,56):
			newapg = str(" Profession: Restauranteur,")
			apg = apg + newapg
		elif r in range(57,58):
			newapg = str(" Profession: Priest / Cultist,")
			apg = apg + newapg
		elif r in range(59,60):
			newapg = str(" Profession: Engineer,")
			apg = apg + newapg
		elif r in range(61,62):
			newapg = str(" Profession: Scribe,")
			apg = apg + newapg
		elif r in range(63,64):
			newapg = str(" Profession: Soldier,")
			apg = apg + newapg
		elif r in range(65,66):
			newapg = str(" Profession: Banker,")
			apg = apg + newapg
		elif r in range(67,68):
			newapg = str(" Profession: Apothecary,")
			apg = apg + newapg
		elif r in range(69,70):
			newapg = str(" Profession: Woodcutter,")
			apg = apg + newapg
		elif r in range(71,72):
			newapg = str(" Profession: Tax Collector,")
			apg = apg + newapg
		elif r in range(73,74):
			newapg = str(" Profession: Prostitute,")
			apg = apg + newapg
		elif r in range(75,76):
			newapg = str(" Profession: Fishmonger,")
			apg = apg + newapg
		elif r in range(77,78):
			newapg = str(" Profession: Butcher,")
			apg = apg + newapg
		elif r in range(79,80):
			newapg = str(" Profession: Fruiterer,")
			apg = apg + newapg
		elif r in range(81,82):
			newapg = str(" Profession: Conman,")
			apg = apg + newapg
		elif r in range(83,84):
			newapg = str(" Profession: Petty Thief,")
			apg = apg + newapg
		elif r in range(85,86):
			newapg = str(" Profession: Healer,")
			apg = apg + newapg
		elif r in range(87,88):
			newapg = str(" Profession: Butler,")
			apg = apg + newapg
		elif r in range(89,90):
			newapg = str(" Profession: Clerk,")
			apg = apg + newapg
		elif r in range(91,92):
			newapg = str(" Profession: Baker,")
			apg = apg + newapg
		elif r in range(93,94):
			newapg = str(" Profession: Cheesemaker,")
			apg = apg + newapg
		elif r in range(95,96):
			newapg = str(" Profession: Innkeeper,")
			apg = apg + newapg
		elif r in range(97,98):
			newapg = str(" Profession: Dung Shoveller,")
			apg = apg + newapg
		elif r in range(99,100):
			newapg = str(" Profession: Courier,")
			apg = apg + newapg

	elif p in range(91,100):
		newapg = str(" Profession: Adventurer,")
		apg = apg + newapg
	
	a = int(roll_list[2])
	
	if a in range(1,15):
		newapg = str(" Alignment: Lawful Good")
		apg = apg + newapg
	elif a in range(16,20):
		newapg = str(" Alignment: Neutral Good")
		apg = apg + newapg
	elif a in range(21,25):
		newapg = str(" Alignment: Chaotic Good")
		apg = apg + newapg
	elif a in range(26,30):
		newapg = str(" Alignment: Lawful Neutral")
		apg = apg + newapg
	elif a in range(31,50):
		newapg = str(" Alignment: True Neutral")
		apg = apg + newapg
	elif a in range(51,53):
		newapg = str(" Alignment: Chaotic Neutral")
		apg = apg + newapg
	elif a in range(54,70):
		newapg = str(" Alignment: Lawful Evil")
		apg = apg + newapg
	elif a in range(71,90):
		newapg = str(" Alignment: Neutral Evil")
		apg = apg + newapg
	elif a in range(91,100):
		newapg = str(" Alignment: Chaotic Evil")
		apg = apg + newapg

	return apg

def getage():
	r = Dice.D100(0)
	if race == "Dwarf":
		age = r * 4
	elif race == "Elf":
		age = r * 6
		
	else:
		age = r
	return age
	print(" ")

while True:
	race = getrace()
	apg = getapg()
	age = getage()
	print("Race: " + str(race))
	print(apg)
	print("Age: " + str(age) ) 
	count +=1
	if int(count) >= int(charnum):
		break

print("Done!")

