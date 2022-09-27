import random
from dice import Dice

number = 0
count = 0
race = 0
age = 0
apg = 0
disposition = 0
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
	return race
def getGender():
	gender = Dice.D100(0)
	if gender in range(1,50):
		gender = str("Gender: Male,")
	elif gender in range(51,100):
		gender = str("Gender: Female,")
	return gender

def getprofession():
	newapg = 0
	p = Dice.D100(0)
	if p in range(1,25) or age < 16:
		newapg = str(" Profession: Commoner(Unemployed),")
		
	elif p in range(26,90):
		r = Dice.D100(0)
		if r in range(1,2):
			newapg = str(" Profession: Farmer,")
			
		elif r in range(3,4):
			newapg = str(" Profession: Artist,")
			
		elif r in range(5,6):
			newapg = str(" Profession: Herbalist,")
			
		elif r in range(7,8):
			newapg = str(" Profession: Horse Trainer,")
			
		elif r in range(9,10):
			newapg = str(" Profession: Blacksmith,")
			
		elif r in range(11,12):
			newapg = str(" Profession: Finesmith,")
			
		elif r in range(13,14):
			newapg = str(" Profession: Locksmith,")
			
		elif r in range(15,16):
			newapg = str(" Profession: Jeweler,")
			
		elif r in range(17,18):
			newapg = str(" Profession: Entertainer,")
			
		elif r in range(19,20):
			newapg = str(" Profession: Teacher,")
			
		elif r in range(21,22):
			newapg = str(" Profession: Armourer,")
			
		elif r in range(23,24):
			newapg = str(" Profession: Cook,")
			
		elif r in range(25,26):
			newapg = str(" Profession: Tailor,")
			
		elif r in range(27,28):
			newapg = str(" Profession: Ropemaker,")
			
		elif r in range(29,30):
			newapg = str(" Profession: Fletcher,")
			
		elif r in range(31,32):
			newapg = str(" Profession: Cooper,")
			
		elif r in range(33,34):
			newapg = str(" Profession: Cartwright,")
			
		elif r in range(35,36):
			newapg = str(" Profession: Carpenter,")
			
		elif r in range(37,38):
			newapg = str(" Profession: Grave Digger / Undertaker,")
			
		elif r in range(39,40):
			newapg = str(" Profession: Winemaker,")
			
		elif r in range(41,42):
			newapg = str(" Profession: Ferryman,")
			
		elif r in range(43,44):
			newapg = str(" Profession: Shipwright,")
			
		elif r in range(45,46):
			newapg = str(" Profession: Ships Capitan,")
			
		elif r in range(47,48):
			newapg = str(" Profession: Fortune Teller,")
			
		elif r in range(49,50):
			newapg = str(" Profession: Handmaiden,")
			
		elif r in range(51,52):
			newapg = str(" Profession: Miller,")
			
		elif r in range(53,54):
			newapg = str(" Profession: Executioner,")
			
		elif r in range(55,56):
			newapg = str(" Profession: Restauranteur,")
			
		elif r in range(57,58):
			newapg = str(" Profession: Priest / Cultist,")
			
		elif r in range(59,60):
			newapg = str(" Profession: Engineer,")
			
		elif r in range(61,62):
			newapg = str(" Profession: Scribe,")
			
		elif r in range(63,64):
			newapg = str(" Profession: Soldier,")
			
		elif r in range(65,66):
			newapg = str(" Profession: Banker,")
			
		elif r in range(67,68):
			newapg = str(" Profession: Apothecary,")
			
		elif r in range(69,70):
			newapg = str(" Profession: Woodcutter,")
			
		elif r in range(71,72):
			newapg = str(" Profession: Tax Collector,")
			
		elif r in range(73,74):
			newapg = str(" Profession: Prostitute,")
			
		elif r in range(75,76):
			newapg = str(" Profession: Fishmonger,")
			
		elif r in range(77,78):
			newapg = str(" Profession: Butcher,")
			
		elif r in range(79,80):
			newapg = str(" Profession: Fruiterer,")
			
		elif r in range(81,82):
			newapg = str(" Profession: Conman,")
			
		elif r in range(83,84):
			newapg = str(" Profession: Petty Thief,")
			
		elif r in range(85,86):
			newapg = str(" Profession: Healer,")
			
		elif r in range(87,88):
			newapg = str(" Profession: Butler,")
			
		elif r in range(89,90):
			newapg = str(" Profession: Clerk,")
			
		elif r in range(91,92):
			newapg = str(" Profession: Baker,")
			
		elif r in range(93,94):
			newapg = str(" Profession: Cheesemaker,")
			
		elif r in range(95,96):
			newapg = str(" Profession: Innkeeper,")
			
		elif r in range(97,98):
			newapg = str(" Profession: Dung Shoveller,")
			
		elif r in range(99,100):
			newapg = str(" Profession: Courier,")
			

	elif p in range(91,100):
		newapg = str(" Profession: Adventurer,")
		
	
	return newapg
def getalignment():
	a = Dice.D100(0)
	
	if a in range(1,15):
		alignment = str(" Alignment: Lawful Good")
		
	elif a in range(16,20):
		alignment = str(" Alignment: Neutral Good")
		
	elif a in range(21,25):
		alignment = str(" Alignment: Chaotic Good")
		
	elif a in range(26,30):
		alignment = str(" Alignment: Lawful Neutral")
		
	elif a in range(31,50):
		alignment = str(" Alignment: True Neutral")
		
	elif a in range(51,53):
		alignment = str(" Alignment: Chaotic Neutral")
		
	elif a in range(54,70):
		alignment = str(" Alignment: Lawful Evil")
		
	elif a in range(71,90):
		alignment = str(" Alignment: Neutral Evil")
		
	elif a in range(91,100):
		alignment = str(" Alignment: Chaotic Evil")
		

	return alignment

def getage():
	r = Dice.D100(0)
	if race == "Dwarf":
		age = r * 4
	elif race == "Elf":
		age = r * 6
		
	else:
		age = r
	return age


def getdisposition():
	disposition = 0
	r = Dice.D100(0)
	if r in range(1,2):
		disposition = str("Shy")
	elif r in range(3,4):
		disposition = str("Aloof / Superior")
	elif r in range(5,8):
		disposition = str("Fool / Idiotic")
	elif r in range(9,10):
		disposition = str("Cocky / Arrogant")
	elif r in range(11,12):
		disposition = str("Envious")
	elif r in range(13,14):
		disposition = str("Grumpy")
	elif r in range(15,16):
		disposition = str("Mischievous")
	elif r in range(17,20):
		disposition = str("Playful / Joking")
	elif r in range(21,22):
		disposition = str("Insane")
	elif r in range(23,24):
		disposition = str("Abrupt / Unpredictable")
	elif r in range(25,26):
		disposition = str("Melancholic / Airy")
	elif r in range(27,30):
		disposition = str("Romantic")
	elif r in range(31,32):
		disposition = str("Frustrated")
	elif r in range(33,34):
		disposition = str("Stressed")
	elif r in range(35,36):
		disposition = str("Weird")
	elif r in range(37,40):
		disposition = str("Serene / Peaceful")
	elif r in range(41,42):
		disposition = str("Cagy / Mysterious")
	elif r in range(43,44):
		disposition = str("Distracted")
	elif r in range(45,46):
		disposition = str("Sad")
	elif r in range(47,50):
		disposition = str("Single-Minded")
	elif r in range(51,52):
		disposition = str("Angry")
	elif r in range(53,54):
		disposition = str("Blase")
	elif r in range(55,56):
		disposition = str("Joyous")
	elif r in range(57,60):
		disposition = str("Vengeful")
	elif r in range(61,62):
		disposition = str("Malicious")
	elif r in range(63,64):
		disposition = str("Afraid")
	elif r in range(65,66):
		disposition = str("Disgusted")
	elif r in range(67,70):
		disposition = str("Resignation")
	elif r in range(71,72):
		disposition = str("Nostalgic")
	elif r in range(73,74):
		disposition = str("Envious")
	elif r in range(75,76):
		disposition = str("Determined")
	elif r in range(77,80):
		disposition = str("Aloof / Superior")
	elif r in range(81,82):
		disposition = str("Distain")
	elif r in range(83,85):
		disposition = str("Hopelessness")
	elif r in range(86,88):
		disposition = str("Amused")
	elif r in range(89,92):
		disposition = str("Recless")
	elif r in range(93,95):
		disposition = str("Lonely")
	elif r in range(96,98):
		disposition = str("Frivolous")
	elif r in range(99,100):
		disposition = str("Disoriented")
	return disposition
while True:
	race = getrace()
	apg = getprofession()
	age = getage()
	gender =getGender()
	alignment= getalignment()
	disposition = getdisposition()
	print("Race: " + str(race))
	print("Age: " + str(age))
	print(gender) 
	print(apg)
	print(alignment)
	print("Disposition: " + str(disposition))
	print(" ")
	count +=1
	if int(count) >= int(charnum):
		break

print("Done!")

