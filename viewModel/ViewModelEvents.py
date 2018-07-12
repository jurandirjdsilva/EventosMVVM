from viewModel import ViewModel
from model.DAO import EventDAO
from hashlib import md5
from threading import Thread
from time import sleep

class ViewModelEvents(ViewModel.ViewModel):
	def __init__(self, view_events):
		self.viewList = []
		self.view_events = view_events
		self.state = None
		self.events = None
		self.__T = Thread(target=self.observer)
		self.__T.start()


	def get_events(self):
		self.events = EventDAO.select_all_events()
		return self.events

	def update(self):
		self.get_events()
		self.get_state()
	# 	os demias aqui
		self.view_events.update()

	def find_Open_events(self):
		#TODO  busca no modelo

		self.notify()

	def find_period_events(self, dt_start, dt_end):
		self.events = EventDAO.select_by_period(dt_start,dt_end)

		self.notify()

	def update_state(self):
		"""
		Atualiza o estado da instância corrente
		"""
		values = ''.join(str(x) for x in self.__dict__.values() if x != self.state)
		self.state = md5(values.encode()).hexdigest()

	def observer(self):
		while True:
			old_state = self.state
			self.update_state()
			if old_state != self.state:
				self.view_events.update()
			sleep(1)

	def __del__(self):
		del self.state