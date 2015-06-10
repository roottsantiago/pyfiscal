from base import BaseGenerator


class CalculeRFC(BaseGenerator):

	def __init__(self):
		super(CalculeRFC, self).__init__()

	@property
	def rfc(self):
		pass

class CalculeCURP(BaseGenerator):

	def __init__(self):
		super(CalculeCURP, self).__init__()

	@property
	def curp(self):
		pass

class CalculeGeneric(BaseGenerator): 

	def __init__(self):

		super(CalculeGeneric, self).__init__()

		self.genera_curp()
		self.genera_rfc()

	@property
	def data(self):
		value = super(CalculeGeneric, self).data
	
		return value