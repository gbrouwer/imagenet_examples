import os
import sys
import pandas as pd
import numpy as np
import requests
import bs4

#-------------------------------------------------------
def getResultCount(q):

	print('----------------------------------------------------')
	q = '"Gijs Joost Brouwer"'
	r = requests.get('http://www.google.com/search',params={'q': q,"tbs": "li:1"})
	r.raise_for_status()
	soup = bs4.BeautifulSoup(r.text)
	print(soup)
    # s = soup.find('div', {'id': '/resultStats'}).text
    # if not s:
    #     return 0
    # m = re.search(r'([0-9,]+)', s)
    # return int(m.groups()[0].replace(',', ''))

#-------------------------------------------------------
if __name__ == '__main__':
	
	count = getResultCount('bezerker')
	print(count)

	# #Read File
	# data = []
	# with open('../data/meta/imagenet_codes_raw.txt','r') as f:
	# 	for line in f:
	# 		elements = line.rstrip().lower().split(' ')
	# 		desc = elements[-1]
	# 		desc = desc.replace('_',' ')
	# 		data.append((elements[0],desc))

	# #To DataFrame
	# df = pd.DataFrame(data)
	# df.columns = ['code','desc']
	
	# #Store
	# df.to_csv('../data/meta/imagenet_codes.csv',index=False)

