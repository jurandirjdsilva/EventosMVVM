class Event:
	def __init__(self, name, address, start_date, final_date, description):
		self.name = name
		self.address = address
		self.start_date = start_date
		self.final_date = final_date
		self.description = description

	def set_name(self, name):
		self.name = name

	def set_address(self, address):
		self.address = address