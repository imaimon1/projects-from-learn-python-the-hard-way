class Room(object):

	def __init__(self,name,description):
		self.name=name
		self.description=description
		self.paths={}
		
	def go(self,direction):
		return self.paths.get(direction,None)
		
	def add_paths(self,paths):
		self.paths.update(paths)
central_corridor = Room("Central Corridor", "")
laser_weapon_armory =Room("Laser Weapon Armory","")
the_bridge = Room("The Bridge", "")
escape_pod = Room("Escape Pod", "")
the_end_winner = Room("The End", "you win")
the_end_loser =Room("the End","you lose")
escape_pod.add_paths({'2':the_end_winner,'*':the_end_loser})
generic_death = Room('death','you died')
the_bridge.add_paths({'throw the bomb': the_bridge,'*':generic_death})
laser_weapon_armory.add_paths({'0123':the_bridge,'*':generic_death})
central_corridor.add_paths({'shoot':generic_death,'dodge':generic_death,'tell a joke':laser_weapon_armory})

START = central_corridor