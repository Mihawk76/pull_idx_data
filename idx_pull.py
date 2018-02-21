from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import urllib
 
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument("--test-type")
options.binary_location = "/usr/bin/chromium"
driver = webdriver.Chrome("/home/daniel/tools_embedded/program_python/chromedriver")
#driver = webdriver.Chrome(chrome_options=options)
driver.get('http://www.idx.co.id/id-id/beranda/perusahaantercatat/laporankeuangandantahunan.aspx')
years = ['2014','2015','2016']
for year in years:
	
 
	# click radio button
	python_button = driver.find_elements_by_xpath("//input[@name='dnn$ctr518$MainView$FR' and @value='rbFinancialReport']")[0]
	python_button.click()
 
	# type text
	text_area = driver.find_element_by_id('dnn_ctr518_MainView_cbCODE_Input')
	#text_area.send_keys("print('AALI')")
	text_area.send_keys("AALI")

	# Drop down menu
	select = Select(driver.find_element_by_id('dnn_ctr518_MainView_ddlYearCalendar'))

	# select by visible text
	#select.select_by_visible_text('2017')
	select.select_by_visible_text(year)

	# Drop down menu
	select = Select(driver.find_element_by_id('dnn_ctr518_MainView_ddlPeriod'))

	# select by visible text
	select.select_by_visible_text('Triwulan III')

 
	# click submit button
	#submit_button = driver.find_elements_by_xpath('//*[@id="editor"]/table/tbody/tr[3]/td/table/tbody/tr/td/div/table/tbody/tr/td[3]/input')[0]
	submit_button = driver.find_elements_by_id('dnn_ctr518_MainView_lbSearch')[0]
	submit_button.click()
	time.sleep(10)

	# click link
	#link = driver.find_element_by_link_text('http://www.idx.co.id/Portals/0/StaticData/ListedCompanies/Corporate_Actions/New_Info_JSX/Jenis_Informasi/01_Laporan_Keuangan/02_Soft_Copy_Laporan_Keuangan\Laporan%20Keuangan%20Tahun%202017\TW1\AALI\FinancialStatement-2017-I-AALI.xlsx')
	link = driver.find_element_by_id('dnn_ctr518_MainView_lvSearchingResult_ctrl0_rptMain_ctl00_hl')
	print(link.get_attribute('href'))
	urllib.urlretrieve(link.get_attribute('href'), year + "laporan1.pdf")
	#html = response.read()
	#link.click()


