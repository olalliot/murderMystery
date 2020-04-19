import random
import pprint

class Game:
	"""docstring for Game"""
	def __init__(self):
		#super(Game, self).__init__()
		self.cast = [
			'David',
			'Rosa',
			'Charles',
			'Jacob',
			'Eileen',
			'Amber',
			'Arno',
			'Octave',
			'Alisha',
			'Grace',
			'Simon',
			'Mia',
			'Lucas',
			'Eleonore',
			'Pascal',
			'Justine',
		]
		self.num_characters_total = len(self.cast)

	def gameStartup(self):
		"""function to setup a new game"""

		#Pick 8 characters at random from all available
		shuffled = self.cast
		random.shuffle(shuffled)
		picked_cast = []
		for i in range(0, 8):
			picked_cast.append(shuffled[i])



gameInstance = Game()
gameInstance.gameStartup()
		