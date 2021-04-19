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


	checkin_btnplus = obj.bot.find_element_by_class_name('contentScrollContainer')

	count = 2
	while True:

			for x in range(10):
				try:
					checkin_btn = obj.bot.find_element_by_xpath(f'/html/body/div[1]/div/div/div/div[3]/div/div/div/div/div/div[2]/div/div/div[4]/div/table/tbody/tr[{count}]/td[3]/label/span')
					checkin_btn.click()
				except:
					checkin_btnplus.send_keys(Keys.DOWN)
					checkin_btn = obj.bot.find_element_by_xpath(f'/html/body/div[1]/div/div/div/div[3]/div/div/div/div/div/div[2]/div/div/div[4]/div/table/tbody/tr[{count}]/td[3]/label/span')
					checkin_btn.click()

				time.sleep(0.2)
				count+=1
			checkin_btnplus = obj.bot.find_element_by_class_name('contentScrollContainer')
			for x in range(14):
				checkin_btnplus.send_keys(Keys.DOWN)



			count=3
			time.sleep(2)

	time.sleep(10)




info= (open("secret_info.txt","r").read()).split(' ')
email =info[0]
pas = info[2]
event_link = 'https://dsc.community.dev/accounts/dashboard/#/chapter-194/event-6611/manage'
CheckIn(email,pas,event_link)

#obj.login(email,pas)
