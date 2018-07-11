from view import View
from viewModel.ViewModelEvents import ViewModelEvents

class ViewEvents (View.View):
	def __init__(self, root):
		self.events = None
		self.root = root
		self.viewModelList = []
		self.viewModel = ViewModelEvents(self)
		self.viewModel.attach(self)
		pass

	def show(self):
		self.update()
		print('*********************************************')
		print('*                  Eventos                  *')
		print('*********************************************')
		for e in self.events:
			print(e)
		print('*********************************************')

	def update(self):
		self.state = self.viewModel.get_state()
		self.events = self.viewModel.get_events()


	def find_Open_events (self):
		self.viewModel.find_Open_events()
		pass

	def find_period_events(self,dt_start,dt_end):
		pass
