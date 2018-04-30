from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import urllib
import sys
import MySQLdb
import sys
from selenium.common.exceptions import TimeoutException
 
# open a database connection
# be sure to change the host IP address, username, password and database name to match your own
connection = MySQLdb.connect (host = "localhost", user = "root", passwd = "satunol10", db = "Stock")
# prepare a cursor object using cursor() method
cursor = connection.cursor ()
# execute the SQL query using execute() method.
cursor.execute ("select * from Daftar_Perusahaan")
listCompany=[]
# fetch all of the rows from the query
data = cursor.fetchall ()
# print the rows
for row in data :
	#print row[0], row[1]
	listCompany.append(row[1])
# close the cursor object
cursor.close ()
# close the connection
connection.close ()
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument("--test-type")
options.binary_location = "/usr/bin/chromium"
driver = webdriver.Chrome("/home/daniel/tools_embedded/program_python/chromedriver")
#driver = webdriver.Chrome(chrome_options=options)
#years = ['2009','2010','2011','2012','2013','2014','2015','2016']
years = ['2017','2018']
triwulans = ['Triwulan I','Triwulan II','Triwulan III']
#triwulans = ['Triwulan 1','Triwulan 2','Triwulan 3']
for listComp in listCompany[544:]:
	for year in years:
	
		for triwulan in triwulans:
			#wait load
			driver.get('http://web.idx.id/id-id/beranda/perusahaantercatat/laporankeuangandantahunan.aspx')
			delay = 3 #seconds
			try:
				myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, 'IdOfMyElement')))
				print "Page is ready!"
			except TimeoutException:
				print "Loading took too much time!"
			# click radio button
			python_button = driver.find_elements_by_xpath("//input[@name='dnn$ctr518$MainView$FR' and @value='rbFinancialReport']")[0]
			#python_button = driver.find_elements_by_xpath("//input[@name='financialReportType' and @value='rdf']")[0]
			#python_button = driver.find_elements_by_id('tofr1')[0]
			python_button.click()
 
			# Drop down menu
			select = Select(driver.find_element_by_id('dnn_ctr518_MainView_ddlYearCalendar'))
			#select = Select(driver.find_element_by_id('yearList'))

			# select by visible text
			#select.select_by_visible_text('2017')
			select.select_by_visible_text(year)

			# Drop down menu
			select = Select(driver.find_element_by_id('dnn_ctr518_MainView_ddlPeriod'))
			#select = Select(driver.find_element_by_id('periodList'))

			# select by visible text
			select.select_by_visible_text(triwulan)

			# type text
			text_area = driver.find_element_by_id('dnn_ctr518_MainView_cbCODE_Input')
			#text_area = driver.find_element_by_id('emitenList')
			#text_area.send_keys("print('AALI')")
			text_area.clear()
			text_area.send_keys(listComp)
 
			# click submit button
			#submit_button = driver.find_elements_by_xpath('//*[@id="editor"]/table/tbody/tr[3]/td/table/tbody/tr/td/div/table/tbody/tr/td[3]/input')[0]
			submit_button = driver.find_elements_by_id('dnn_ctr518_MainView_lbSearch')[0]
			#submit_button = find_elements_by_xpath("//button[@id='searchButton' and @class='btn btn-primary']")[0]
			submit_button.click()
			time.sleep(3)

			# click link
			#link = driver.find_element_by_link_text('http://www.idx.co.id/Portals/0/StaticData/ListedCompanies/Corporate_Actions/New_Info_JSX/Jenis_Informasi/01_Laporan_Keuangan/02_Soft_Copy_Laporan_Keuangan\Laporan%20Keuangan%20Tahun%202017\TW1\AALI\FinancialStatement-2017-I-AALI.xlsx')
			try:
				link = driver.find_element_by_id('dnn_ctr518_MainView_lvSearchingResult_ctrl0_rptMain_ctl00_hl')
				#link = driver.find_element_by_class_name('financial-report-download ng-scope')
				print(link.get_attribute('href'))
				urllib.urlretrieve(link.get_attribute('href'), listComp + "_" + year + "_" + triwulan + "_laporan1.pdf")
			except Exception as ex:
				print "Unexpected error:", sys.exc_info()[0]
			#html = response.read()
			#link.click()


