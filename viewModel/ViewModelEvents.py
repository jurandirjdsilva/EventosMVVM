from viewModel import ViewModel
from model.DAO import EventDAO
from hashlib import md5

class ViewModelEvents(ViewModel.ViewModel):
	def __init__(self, view_events):
		# self.viewList = []
		self.view_events = view_events
		self.state = None

	def get_events(self):
		self.events = EventDAO.select_all_events()

	def update(self):
		self.get_events()
		self.get_state()
	# 	os demias aqui
		self.view_events.update()

	def find_Open_events(self):
		#TODO  busca no modelo

		self.notify()

	def find_period_events(self, dt_start, dt_end):
		# TODO  busca no modelo
		self.notify()

	def update_state(self):
		"""
		Atualiza o estado da instância corrente
		"""
		values = ''.join(str(x) for x in self.__dict__.values() if x != self.state)
		self.state = md5(values).hexdigest()

	def __del__(self):
		del self.state