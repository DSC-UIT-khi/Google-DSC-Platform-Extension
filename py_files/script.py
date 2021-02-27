from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import datetime
import time
import os
import keyboard
import pandas as pd
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
class dsc_bot:
	def __init__(self):
		self.bot = webdriver.Chrome(executable_path=r'chromedriver.exe')

	def message(self,message):

		a1= QMessageBox()
		a1.setWindowTitle("Error!")
		a1.setText(message)
		a1.setIcon(QMessageBox.Information)
		a1.setStandardButtons(QMessageBox.Ok)
		x = a1.exec_()
	def login(self,uni_link,email,pas):
		bot = self.bot

		bot.get('https://dsc.community.dev/accounts/dashboard/')
		time.sleep(2)
		'''try:
			login_btn = bot.find_element_by_xpath("/html/body/header/div[1]/div/div[2]/ul/li[5]/a")
			login_btn.click()
		except:
			pass
		time.sleep(2)'''

		email_in = bot.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input")
		email_in.send_keys(email)
		nxt_btn = bot.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/div[2]")
		nxt_btn.click()
		#keyboard.send('enter', do_press=True, do_release=True)
		time.sleep(4)
		pas_in = bot.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input")
		pas_in.send_keys(pas)
		nxt1_btn = bot.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/div[2]")
		nxt1_btn.click()
		#keyboard.send('enter', do_press=True, do_release=True)
		time.sleep(4)
	def start(self,f_name,l_name,eemail,event_sel):
		bot = self.bot
		#bot.get('https://dsc.community.dev/accounts/dashboard/#/chapter-194/event-8554/manage')
		bot.get(event_sel)
		#dash_btn = bot.find_element_by_xpath("/html/body/nav/div/div[2]/ul /li[6]/a")
		#dash_btn.click()
		#time.sleep(7)
		#bot.get('https://dsc.community.dev/accounts/dashboard/#/chapter-194/event-8554/manage')
		bot.get('https://dsc.community.dev/accounts/dashboard/')
		time.sleep(1)
		print('running')
		bot.get(event_sel)
		#bot.get(event_sel)
		#time.sleep(7)
		try:
			
			count = 1


			
			for f_name,l_name,eemail in zip(f_name,l_name,eemail):
				#print(name)
				print(f_name,"fname")

				
				add_btn = bot.find_element_by_xpath("/html/body/div[1]/div/div/div/div[3]/div/div/div/div/div/div[2]/div/div/div[2]/div/div[1]/div/div/a")
				add_btn.click()
				time.sleep(2)
				try:
					add_new = bot.find_element_by_xpath("/html/body/div[1]/div/div/div/div[3]/div/div/div/div/div/div[2]/div/div/div[2]/div/div[1]/div[2]/div/div/div[2]/div/a")
					add_new.click()
					time.sleep(2)
				except:
					add_in = bot.find_element_by_xpath("/html/body/div[1]/div/div/div/div[3]/div/div/div/div/div/div[2]/div/div/div[2]/div/div[1]/div[2]/div/div/input")
					add_in.click()
					time.sleep(2)
					add_new = bot.find_element_by_xpath("/html/body/div[1]/div/div/div/div[3]/div/div/div/div/div/div[2]/div/div/div[2]/div/div[1]/div[2]/div/div/div[2]/div/a")
					add_new.click()
					time.sleep(2)


				if count == 1 :



					add_first = bot.find_element_by_xpath("/html/body/div[1]/div/div/div/div[3]/div/div/div/div/div/div[2]/div/div/div[2]/div/div[1]/div/div/div/div[2]/div/input")
					add_first.send_keys(f_name)
					add_last = bot.find_element_by_xpath("/html/body/div[1]/div/div/div/div[3]/div/div/div/div/div/div[2]/div/div/div[2]/div/div[1]/div/div/div/div[3]/div/input")
					add_last.send_keys(l_name)
					add_email = bot.find_element_by_xpath("/html/body/div[1]/div/div/div/div[3]/div/div/div/div/div/div[2]/div/div/div[2]/div/div[1]/div/div/div/div[4]/div/input")
					add_email.send_keys(eemail)
				else:
					add_first = bot.find_element_by_xpath("/html/body/div[1]/div/div/div/div[3]/div/div/div/div/div/div[2]/div/div/div[2]/div/div[1]/div/div/div["+str(count)+"]/div[2]/div/input")
					add_first.send_keys(f_name)
														 
					add_last = bot.find_element_by_xpath("/html/body/div[1]/div/div/div/div[3]/div/div/div/div/div/div[2]/div/div/div[2]/div/div[1]/div/div/div["+str(count)+"]/div[3]/div/input")
					add_last.send_keys(l_name)
					add_email = bot.find_element_by_xpath("/html/body/div[1]/div/div/div/div[3]/div/div/div/div/div/div[2]/div/div/div[2]/div/div[1]/div/div/div["+str(count)+"]/div[4]/div/input")
					add_email.send_keys(eemail)
				#add_att  =bot.find_element_by_xpath("/html/body/div[1]/div/div/div/div[3]/div/div/div/div/div/div[2]/div/div/div[2]/div/div[1]/div/div/a")
				#add_att.click()
				time.sleep(2)
				count +=1

				
			save_btn =bot.find_element_by_xpath("/html/body/div[1]/div/div/div/div[3]/div/div/div/div/div/div[2]/div/div/div[2]/div/div[1]/button")
			save_btn.click()
			time.sleep(2)

		except:
			
			self.message(f'Check Internet Connection or if there is event created at {event_sel}')

	def draft(self):
		drft_btn = bot.find_element_by_xpath("/html/body/div[1]/div/div/div/div[3]/div/div/div/div/div/div[1]/div[1]/div/div/div[2]/div/div[2]")
		drft_btn.click()
		time.sleep(2)
