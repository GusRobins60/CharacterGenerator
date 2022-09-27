import random

itr = 0
count = 0
roll = 0

class Dice:
	def __init__(self,roll):
		self.roll = roll

	def D100(itr):
		x = 0
		newroll = 0
		if itr == 0:
			roll = random.randint(1,100)
			newroll = roll
		else:
			while int(x) < int(itr):
				roll= random.randint(1,100)
				newroll = newroll + roll
				x += 1
		return int(newroll)

	def D20(itr):
		x = 0
		newroll = 0
		if itr == 0:
			roll = random.randint(1,20)
			newroll = roll
		else:
			while int(x) < int(itr):
				roll= random.randint(1,20)
				newroll = newroll + roll
				x += 1
		return int(newroll)

	def D12(itr):
		x = 0
		newroll = 0
		if itr == 0:
			roll = random.randint(1,12)
			newroll = roll
		else:
			while int(x) < int(itr):
				roll= random.randint(1,12)
				newroll = newroll + roll
				x += 1
		return int(newroll)

	def D10(itr):
		x = 0
		newroll = 0
		if itr == 0:
			roll = random.randint(1,10)
			newroll = roll
		else:
			while int(x) < int(itr):
				roll= random.randint(1,10)
				newroll = newroll + roll
				x += 1
		return int(newroll)

	def D6(itr):
		x = 0
		newroll = 0
		if itr == 0:
			roll = random.randint(1,6)
			newroll = roll
		else:
			while int(x) < int(itr):
				roll= random.randint(1,6)
				newroll = newroll + roll
				x += 1
		return int(newroll)
		
	def D8(itr):
		x = 0
		newroll = 0
		if itr == 0:
			roll = random.randint(1,8)
			newroll = roll
		else:
			while int(x) < int(itr):
				roll= random.randint(1,8)
				newroll = newroll + roll
				x += 1
		return int(newroll)
	def D4(itr):
		x = 0
		newroll = 0
		if itr == 0:
			roll = random.randint(1,4)
			newroll = roll
		else:
			while int(x) < int(itr):
				roll= random.randint(1,4)
				newroll = newroll + roll
				x += 1
		return int(newroll)