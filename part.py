class Part:

    def __init__(self, barcode):
        self.barcode = barcode
        self.digiPN = ''
        self.manfPN = ''
        self.Description = ''

	def addDigiPN(self, digiPN):
		self.digiPN = digiPN

	def addManfPN(self, manfPN):
		self.manfPN = manfPN

	def addDescription(self, Description):
		self.Description = Description

	def add_trick(self):
		pass

    def getPart(self):
    	try:
    		print self.barcode
    	except Exception as e:
    		print "No barcode"
        try:
        	print self.digiPN
        except Exception as e:
    		print "No DigiKey PN"
        try:
        	print self.manfPN
        except Exception as e:
    		print "No Manufacturer Part Number"
        try:
        	print self.Description
        except Exception as e:
    		print "No Description"

aPart = Part('2345739000000025774934')
aPart.getPart()



#aPart.addManfPN('Dizzle-Corp')
aPart.getPart()
