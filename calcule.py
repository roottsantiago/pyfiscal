from base import BaseGenerator


class Calcule(BaseGenerator): 

	def __init__(self):

		super(Calcule, self).__init__()

		self.genera_curp()
		self.genera_rfc()

	@property
	def data(self):
		value = super(Calcule, self).data
		return value