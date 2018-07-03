from .Address import Address
from datetime import date as dt_date
from datetime import datetime as dt_datetime
from datetime import time as dt_time

class Event:
	def __init__(self, name, address, date, time, description):
		self.__name = name
		self.__address = address
		self.__date = date
		self.__time = time
		self.__description = description

	def set_name(self, name):
		self.__name = name

	def set_address(self, address):
		if isinstance(address, Address):
			self.__address = address
		else:
			raise TypeError('the address parameter must be of type Address')

	def set_date(self, date_event):
		if isinstance(date_event, dt_date):
			self.__date = date_event
		else:
			raise TypeError('the date_event parameter must be of type date')

	def set_time(self, time_event):
		if isinstance(time_event, dt_time):
			self.__time = time_event