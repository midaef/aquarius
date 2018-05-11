
from ezprint import *
import random

glasses = []

class glass:

	dg = []

	def __init__(self, v = 1000, vl = 1000):
		self.v = v
		self.vl = vl
	
	def draw(self):
		n = 5
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
			dg.append('║≈≈≈≈≈≈║')
		else:
			dg.append('║      ║')
		dg.reverse()
		for i in dg:
			p(i)


def main():
	kol = int(input('Amount of glasses: '))
	for i in range(kol):
		glasses.append(glass())
		glasses[i].draw()
		p('')
	for i in range(1, kol + 1):
		v = int(input('Volume of ' + str(i) + ' glass: '))
		vl = int(input('Fill of ' + str(i) + ' glass: '))
		glasses[i - 1].v = v
		glasses[i - 1].vl = vl
		glasses[i - 1].draw()
	





if __name__ == '__main__':
	main()