from script import *




def CheckIn(email,pas,event_link):
	obj = dsc_bot()
	obj.login(event_link,email,pas)
	obj.bot.get(event_link)
	time.sleep(5)
	obj.bot.get(event_link)
	time.sleep(15)
	sort_check = obj.bot.find_element_by_xpath('/html/body/div[1]/div/div/div/div[3]/div/div/div/div/div/div[2]/div/div/div[4]/div/table/thead/tr/th[3]')
	sort_check.click()
	count = 2
	after_count = 7
	for k in range(1900):
			

			

			try:
				checkin_btn = obj.bot.find_element_by_xpath(f'/html/body/div[1]/div/div/div/div[3]/div/div/div/div/div/div[2]/div/div/div[4]/div/table/tbody/tr[2]/td[3]/label/span')
				checkin_btn.click()
				#checkin_btnplus = obj.bot.find_element_by_class_name('contentScrollContainer')
				#checkin_btnplus.send_keys(Keys.DOWN)
				time.sleep(1)

				sort_check = obj.bot.find_element_by_xpath('/html/body/div[1]/div/div/div/div[3]/div/div/div/div/div/div[2]/div/div/div[4]/div/table/thead/tr/th[3]')
			
				sort_check.click()
				time.sleep(1)
				sort_check.click()
			except:
				pass


			


			#count+=1
			time.sleep(2)
			
	time.sleep(10)




info = (open("secret_info.txt","r").read()).split(' ')
email =info[0]
pas = info[2]
event_link = 'https://dsc.community.dev/accounts/dashboard/#/chapter-194/event-7214/manage'
CheckIn(email,pas,event_link)

#obj.login(email,pas)
