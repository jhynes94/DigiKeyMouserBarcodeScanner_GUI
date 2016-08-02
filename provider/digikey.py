from bs4 import BeautifulSoup

#Run Command:      type input_file.txt | python digi-reader.py >> output.csv

import urllib2
import urllib
import sys

def digiKeyPageToData(digi_url):

	req2 = urllib2.Request(digi_url, headers={'User-Agent' : "electronic-parser"})
	page2 = urllib2.urlopen(req2)
	soup2 = BeautifulSoup(page2.read(), 'html.parser')
	u = soup2.find_all('table', id='product-details')

	DigiPN = u[0].find("td", id="reportPartNumber").get_text().encode('ascii', 'ignore').strip().replace("\n", "")

	data = {
		"provider": 'digikey',
		"provider_pn": DigiPN,
		"manufacturer_pn": u[0].find_all('h1', itemprop="model")[0].contents[0].replace(" ", "").replace("\n", "").encode('ascii', 'ignore'),
		"description": u[0].find_all('td', itemprop="description")[0].contents[0].replace("\n", "").encode('ascii', 'ignore').strip()
	}
	return data


def partNumber2Data(digi_pn):
	data = None

	try:
		if digi_pn is not None:
			digi_url = "http://search.digikey.com/scripts/DkSearch/dksus.dll?Detail&name={}".format(digi_pn)
			

			return digiKeyPageToData(digi_url)

	except Exception as e:
		sys.stderr.write('error: reading digikey page for {} reason: {}\n'.format(digi_pn, e))
		return None




def barcode2data(barcode):

	data = None

	try:
		if barcode is not None:
			digi_url = digi_url = "http://www.digikey.com/product-detail/en/x/x/{}".format(barcode)

			return digiKeyPageToData(digi_url)

	except Exception as e:
			data = None

			barcode = barcode + "0"

			try:
				if barcode is not None:
					digi_url = digi_url = "http://www.digikey.com/product-detail/en/x/x/{}".format(barcode)

					return digiKeyPageToData(digi_url)

			except Exception as e:
				sys.stderr.write('error: reading digikey page for {} reason: {}\n'.format(barcode, e))
				return None
