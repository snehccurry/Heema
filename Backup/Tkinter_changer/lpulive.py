from selenium import webdriver
from selenium import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as ExpectedConditions
from selenium.webdriver.support.ui import Select
import time
import os
import subprocess
import threading
import random



def wait_css_selector(code):
        wait.until(
            ExpectedConditions.presence_of_element_located((By.CSS_SELECTOR, code))
        )
def wait_xpath(code):
        wait.until(
            ExpectedConditions.presence_of_element_located((By.XPATH, code))
        )





main_directory="C:\\Users\\Administrator\\Documents\\TEST\\working scripts\\Opensea nft uploader"
project_path=main_directory

#os.system('cmd /k " cd C:\\Program Files\\Google\\Chrome Beta\\Application && chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\\Users\\Administrator\\Documents\\TEST\\localhost"')

subprocess.Popen(
        [
            "start",
            "chrome",
            "--remote-debugging-port=8989",
            "--user-data-dir=" + main_directory + "/chrome_profile",
        ],
        shell=True,
)


"""
opt = Options()
opt.add_experimental_option("debuggerAddress", "localhost:8989")
driver = webdriver.Chrome(
executable_path=project_path + "/chromedriver.exe",
options=opt,
						)
"""

"""#os.startfile("launcher.py")
#print( row[0],row[1],row[2],row[3],row[4],row[5])#row[0]name;row[1]age;row[2]religion;row[3]gender;row[4]occupation;row[5]value
option = webdriver.ChromeOptions()
#option.add_experimental_option('excludeSwitches', ['enable-logging'])
option.add_experimental_option("debuggerAddress","localhost:8989")
#option.add_argument("--headless")
#option.add_argument("disable-gpu")"""
"""
browser = webdriver.Chrome(executable_path=main_directory+"/chrom`edriver.exe", options=option)

browser.get('https://youtube.com')





browser.close()
"""






opt = Options()
opt.add_experimental_option("debuggerAddress", "localhost:8989")
driver = webdriver.Chrome(
	        executable_path=project_path + "/chromedriver.exe",
	        chrome_options=opt,)
wait = WebDriverWait(driver,random.randint(4,10))
#driver.get('https://instagram.com')

#driver.get("https://www.instagram.com/cristiano")
#browser = webdriver.Chrome(executable_path=main_directory+"/chromedriver.exe", options=option)
	
"""
try:


	wait_css_selector("#loginForm > div > div:nth-child(1) > div > label > input")
	email_box=driver.find_element_by_css_selector("#loginForm > div > div:nth-child(1) > div > label > input")

	username="realabhaygaur"
	email_box.send_keys(username)








	#enters the password
	#loginForm > div > div:nth-child(2) > div > label > input
	wait_css_selector("#loginForm > div > div:nth-child(2) > div > label > input")
	password_box=driver.find_element_by_css_selector("#loginForm > div > div:nth-child(2) > div > label > input")

	password="abhaygaur44456"
	password_box.send_keys(password)


	login_button=driver.find_element_by_css_selector("#loginForm > div > div:nth-child(3) > button > div")
	login_button.click()

	not_now=driver.find_element_by_css_selector("#mount_0_0_rG > div > div:nth-child(1) > div > div:nth-child(4) > div > div > div.rq0escxv.l9j0dhe7.du4w35lb > div > div.iqfcb0g7.tojvnm2t.a6sixzi8.k5wvi7nf.q3lfd5jv.pk4s997a.bipmatt0.cebpdrjk.qowsmv63.owwhemhu.dp1hu0rb.dhp61c6y.l9j0dhe7.iyyx5f41.a8s20v7p > div > div > div > div > div > div > div > div._a9-z > button._a9--._a9_1")
	not_now.click()
	cancel_save_info=driver.find_element_by_css_selector("#react-root > section > main > div > div > div > div > button")
	cancel_save_info.click()
except:
	pass

"""

#time.sleep(5)

#mount_0_0_BY > div > div:nth-child(1) > div > div.rq0escxv.l9j0dhe7.du4w35lb > div > div > div.j83agx80.cbu4d94t.d6urw2fd.dp1hu0rb.l9j0dhe7.du4w35lb > div._a3gq._ab-1 > section > main > div > header > section > div._ab8w._ab94._ab99._ab9f._ab9m._ab9p > div > div > div > span > span._abgm._abn8 > button
#wait_css_selector("#mount_0_0_tv > div > div:nth-child(1) > div > div.rq0escxv.l9j0dhe7.du4w35lb > div > div > div.j83agx80.cbu4d94t.d6urw2fd.dp1hu0rb.l9j0dhe7.du4w35lb > div._a3gq._ab-1 > section > main > div > header > section > div._aa_m > div._ab8w._ab94._ab99._ab9f._ab9k._ab9p._abb3 > div > div > div > span > span._abgm._abn8 > button")


"""
wait_xpath("//*[text()='Follow']")
follow_button=driver.find_element_by_xpath("//*[text()='Follow']")

follow_button.click()
"""


made_list=["https://lpulive.lpu.in/"]
driver.get("https://lpulive.lpu.in/")

driver.find_element_by_xpath()

"""
for i in range(10000):
	try:
		for j in range(4):
			chosen_celeb=random.choice(made_list)
			print(f"chosen_celeb is: {chosen_celeb}")
			driver.get(chosen_celeb)

			try:
				time.sleep(3)
				wait_xpath("//header/section[1]/div[1]/div[2]/div[1]/div[2]/div[1]/span[1]/span[1]/button[1]")

				already_follow_button=driver.find_element_by_xpath("//header/section[1]/div[1]/div[2]/div[1]/div[2]/div[1]/span[1]/span[1]/button[1]")
				already_follow_button.click()
				unfollow=driver.find_element_by_xpath("//button[contains(text(),'Unfollow')]")
				unfollow.click()
				time.sleep(3)

			except:
				time.sleep(3)
				print("passed and following")
				wait_xpath("//*[text()='Follow']")
				follow_button=driver.find_element_by_xpath("//*[text()='Follow']")

				follow_button.click()
				sleeping_for=random.randint(25,30)
				print("sleeping for : ", sleeping_for)
				time.sleep(sleeping_for)
			try:
				time.sleep(3)
				wait_xpath("//header/section[1]/div[1]/div[2]/div[1]/div[2]/div[1]/span[1]/span[1]/button[1]")

				already_follow_button=driver.find_element_by_xpath("//header/section[1]/div[1]/div[2]/div[1]/div[2]/div[1]/span[1]/span[1]/button[1]")
				already_follow_button.click()
				unfollow=driver.find_element_by_xpath("//button[contains(text(),'Unfollow')]")
				unfollow.click()
				time.sleep(5)
			except:
				pass
		time.sleep(random.randint(20,50))
		#sleeping_for=random.randint(60,200)
		#print("sleeping for : ", sleeping_for)
		#time.sleep(sleeping_for)
		#wait_time=random.randint(400,900)
		#print("waiting for ",wait_time)
		#time.sleep(wait_time)
	except:
		print("starting all over again")
"""