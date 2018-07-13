from .Address import Address
from datetime import date as dt_Date
from datetime import datetime as dt_DateTime
from datetime import time as dt_Time

class Event:
    event_count = 0
    def __init__(self, name, address=None, start_date=None, end_date=None, start_time=None, end_time=None,description=None):
        self.id = self.event_count
        self.event_count += 1
        self.__name = name
        self.__address = address
        self.__start_date = start_date
        self.__end_date = end_date
        self.__start_time = start_time
        self.__end_time = end_time
        self.__description = description

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_address(self, address):
        if isinstance(address, Address):
            self.__address = address
        else:
            self.__address = None
            raise TypeError('the address parameter must be of type Address')

    def get_address(self):
        return self.__address.address_formated()

    def get_address_type_address(self):
        return self.__address.copy()

    def set_start_date(self, start_date_event):
        if isinstance(start_date_event, dt_Date):
            self.__start_date = start_date_event
        else:
            self.__start_date = None
            raise TypeError('the date_event parameter must be of type date')

    def get_start_date(self):
        return self.__start_date

    def set_end_date(self, end_date_event):
        if isinstance(end_date_event, dt_Date):
            self.__start_date = end_date_event
        else:
            raise TypeError('the date_event parameter must be of type date')

    def get_end_date(self):
        return self.__end_date

    def set_start_time(self, start_time_event):
        if isinstance(start_time_event, dt_Time):
            self.__start_time = start_time_event
        else:
            self.__start_time = None

    def get_start_time(self):
        return self.__start_time

    def set_end_time(self, end_time_event):
        if isinstance(end_time_event, dt_Time):
            self.__start_time = end_time_event
        else:
            self.__end_time = None

    def get_end_time(self):
        return self.__end_time

    def set_description(self, description):
        if isinstance(description, str):
            self.__description = description
        else:
            self.__description = ''

    def get_description(self):
        return self.__description

    # def __repr__(self):
    # 	return self.__str__()

    def __str__(self):
        return self.event_formated()

    def event_formated(self):
        try:
            start_date = self.__start_date.strftime('%d/%m/%y %H:%M')
        except Exception:
            start_date = 'Null'

        try:
            end_date = self.__end_date.strftime('%d/%m/%y %H:%M')
        except Exception:
            end_date = 'Null'

        return '({} - {}) {}: {}'.format(start_date,
                                         end_date,
                                         self.get_name(),
                                         self.get_description())