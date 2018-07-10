class Address:
	def __init__(self, number, street, neighborhood, city, state):
		self.__number = number
		self.__street = street
		self.__neighborhood = neighborhood
		self.__city = city
		self.__state = state

	def set_number(self, number):
		self.__number = number

	def set_street(self, street):
		self.__street = street

	def set_neighborhood(self, neighborhood):
		self.__neighborhood = neighborhood

	def set_city(self, city):
		self.__city = city

	def set_state(self, state):
		self.__state = state

	def get_number(self):
		return self.__number

	def get_street(self):
		return self.__street

	def get_neighborhood(self):
		return self.__neighborhood

	def get_city(self):
		return self.__city

	def get_state(self):
		return self.__state

	def __repr__(self):
		return self.__str__()

	def __str__(self):
		return '{}, {}, {}, {} - {}'.format(self.get_street(), \
		                                    self.get_number(), \
		                                    self.get_neighborhood(), \
		                                    self.get_city(),
		                                    self.get_state())