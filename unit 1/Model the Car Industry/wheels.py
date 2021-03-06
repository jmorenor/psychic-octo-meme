from random import choice

class Wheels(object):
	"""docstring for Wheels"""
	# Procedure to ask the buyer which wheels he or she would like to choose
	def choose_wheel(self,wheels,user=""):
		options = wheels.keys()
		if not user:
			i = 1
			for option in options:
				print "{}. Model Name: {}".format(i,option)
				print "   Weight: {} g\n   Production Cost: EUR {}\n".format(wheels[option]["weight"], wheels[option]["cost"])
				i += 1
				
			user_input = raw_input("Which wheels do you want to choose? ")
			print("")
		else:
			user_input = choice(range(1,len(wheels)+1))
			i = len(wheels)
		
		if isinstance(int(user_input),int) and user_input > 0 and int(user_input) <= i:
			user_input = int(user_input)
			return options[user_input-1]
		else:
			print("Please choose a valid option!\n")
			return self.choose_wheel(wheels)

	def __init__(self,user=""):
		wheels = {'Torch': {'cost': 50, 'weight': 900}, 'Mavic': {'cost': 100, 'weight': 685},'Zipp': {'cost': 25, 'weight': 865}}
		self.wheel_model = self.choose_wheel(wheels,user)
		self.wheel_weight = wheels[self.wheel_model]["weight"]
		self.wheel_cost = wheels[self.wheel_model]["cost"]
		
	def __str__(self):
		return "Model: {0}\nWeight (g): {1}\n".format(self.wheel_model,self.wheel_weight)