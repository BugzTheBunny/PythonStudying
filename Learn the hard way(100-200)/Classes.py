class Song(object):

	def __init__(self, lyrics):
		self.lyrics = lyrics

	def br():
		print('--------------------')

	def sing_me_a_song(self):
		for line in self.lyrics:
			print(line)
		Song.br()

happy_bday = Song(["Happy birth day to you", "I don't want to get sued", "So ill stop right here"])
bulls_on_prade = Song(["They rally around the family", "With pockets full of shells"])
new_song = ['aa','bb','cc','dd']

happy_bday.sing_me_a_song()
bulls_on_prade.sing_me_a_song()

Song(new_song).sing_me_a_song()

