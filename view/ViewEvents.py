from view import View
from viewModel.ViewModelEvents import ViewModelEvents

class ViewEvents(View.View):
	def __init__(self, root):
		self.events = None
		self.root = root
		self.viewModelList = []
		self.viewModel = None # para evitar inconsistência ao atribuir (pois ViewModelEvents chama update)
		self.viewModel = ViewModelEvents(self)
		self.viewModel.attach(self)

	def show(self):
		self.update()
		print('*********************************************')
		print('*                  Eventos                  *')
		print('*********************************************')
		if self.events is not None:
			for e in self.events:
				print(e)
		else:
			print('Nenhum eventos disponível!')
		print('*********************************************')


	def update(self):
		if self.viewModel is not None:
			self.state = self.viewModel.get_state()
			self.events = self.viewModel.get_events()


	def find_Open_events (self):
		self.viewModel.find_Open_events()
		pass

	def find_period_events(self,dt_start,dt_end):
		pass

	def __del__(self):
		del self.viewModel
