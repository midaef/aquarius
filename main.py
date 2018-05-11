
from ezprint import *
import random

glasses = []

def enter(max = 0, text = '>>>'):
	inp = input(text)
	try:
		inp = int(inp)
	except:
		return enter(max = max, text = text)

	if max != 0:
		if inp <= max and inp >= 0:
			return inp
		else:
			return enter(max = max, text = text)
	else:
		if inp >= 0:
			return inp
		else:
			return enter(max = max, text = text)


class glass:

	dg = []

	def __init__(self, v = 1000, vl = 1000):
		self.v = v
		self.vl = vl
	

	def draw(self):
		n = 6
		d = self.v / n

		dg = []
		dg.append('╚══════╝')

		if self.vl >= d:
			dg.append('║░░░░░░║')
		else:
			dg.append('║      ║')

		if self.vl >= 2 * d:
			dg.append('║░░░░░░║')
		else:
			dg.append('║      ║')

		if self.vl >= 3 * d:
			dg.append('║░░░░░░║')
		else:
			dg.append('║      ║')

		if self.vl >= 4 * d:
			dg.append('║░░░░░░║')
		else:
			dg.append('║      ║')

		if self.vl >= 5 * d:
			dg.append('║░░░░░░║')
		else:
			dg.append('║      ║')

		if self.vl >= 6 * d:
			dg.append('║≈≈≈≈≈≈║')
		else:
			dg.append('║      ║')

		dg.reverse()
		for i in dg:
			p(i)

	def getVolume(self):
		return self.v

	def setVolume(self, v):
		self.v = v

	def getFill(self):
		return self.vl

	def setFill(self, vl):
		self.vl = vl

def main():
	cls()
	kol = enter(text = 'Amount of glasses: ')
	# kol = int(input('Amount of glasses: '))
	for i in range(kol):
		glasses.append(glass())
		# glasses[i].draw()
		# p('')
	for i in range(1, kol + 1):
		v = enter(text = 'Volume of ' + str(i) + ' glass: ')
		glasses[i - 1].setVolume(v)
		# v = int(input('Volume of ' + str(i) + ' glass: '))
		vl = enter(glasses[i - 1].getVolume(), text = 'Fill of ' + str(i) + ' glass: ')
		# vl = int(input('Fill of ' + str(i) + ' glass: '))
		
		glasses[i - 1].setFill(vl)
	
	for g in glasses:
		g.draw()
		p()

	





if __name__ == '__main__':
	main()