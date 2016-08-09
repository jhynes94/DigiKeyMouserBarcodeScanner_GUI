class Part:
   'Part for catalog'

	def __init__(self, barcode):
		self.barcode = barcode

	def getPart(self):
		return self.barcode
