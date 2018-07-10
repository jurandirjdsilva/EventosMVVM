from .Location import Address
from datetime import date as dt_Date
from datetime import datetime as dt_DateTime
from datetime import time as dt_Time

class Event:
	def __init__(self, name, address, start_date, end_date, start_time, description):
		self.__name = name
		self.__address = address
		self.__start_date = start_date
		self.__end_date = end_date
		self.__start_time = start_time
		self.__description = description

	def set_name(self, name):
		self.__name = name

	def set_address(self, address):
		if isinstance(address, Address):
			self.__address = address
		else:
			raise TypeError('the address parameter must be of type Address')

	def set_start_date(self, start_date_event):
		if isinstance(start_date_event, dt_Date):
			self.__start_date = start_date_event
		else:
			raise TypeError('the date_event parameter must be of type date')

	def set_end_date(self, end_date_event):
		if isinstance(end_date_event, dt_Date):
			self.__start_date = end_date_event
		else:
			raise TypeError('the date_event parameter must be of type date')

	def set_time(self, time_event):
		if isinstance(time_event, dt_Time):
			self.__start_time = time_event
			askajskajskajsoasjaokj