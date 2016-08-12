import csv
import sys

class Catalog:
   'Catalog of items'

   catalogList = []

   #Load CSV from Stored file
   def __init__(self):
      try:
         with open('catalog.csv', 'rb') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
            for row in spamreader:
               print ', '.join(row)

      except Exception as e:
         sys.stderr.write('error: Loading File\nreason: {}\n'.format(e))

   def loadCSV(self, CSV):
      try:
         with open( CSV, 'rb') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
            for row in spamreader:
               print ', '.join(row)

      except Exception as e:
         sys.stderr.write('error: Loading File\nreason: {}\n'.format(e))

   def add(self):
      pass

   def delete():
      pass

   def update():
      pass