from selenium import webdriver
driver = webdriver.Chrome("/usr/local/bin/chromedriver") #본인의 chrome driver 주소
import json
from collections import OrderedDict
import threading

file_data = OrderedDict()

def notice():
	driver.get('https://it.jbnu.ac.kr/it/index.do')

	data = {}
	for i in range(5):
		# xpath '//*[@id="recentBbsArtclObj_681_1050"]/li[%d]/a'안의 %d값을 1씩 올려 순차적으로 공지를 가져온다.
		text = driver.find_element_by_xpath('//*[@id="recentBbsArtclObj_681_1050"]/li[%d]/a'%(i+1)).text
		title = text[:-6]
		date = text[-5:]
		url = driver.find_element_by_xpath('//*[@id="recentBbsArtclObj_681_1050"]/li[%d]/a'%(i+1)).get_attribute("href")
		file_data["title"] = title
		file_data["date"] = date
		file_data["url"] = url
		data[i]=file_data
	with open('ithome.json', 'w', encoding = "utf-8") as make_file:
		json.dump(data, make_file, ensure_ascii=False, indent="\t")

class Repeat:

	def __init__(self):
		pass

	def Reithome(self):
		print("im d w")
		notice()
		threading.Timer(3600,self.Reithome).start()

re = Repeat()
re.Reithome()