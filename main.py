import time
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Укажите путь к ChromeDriver
service = Service(r"C:\Tools\chromedriver-win64\chromedriver-win64\chromedriver.exe")

# Инициализация драйвера
driver = webdriver.Chrome(service=service)
# driver = webdriver.Chrome()

# Открытие страницы
driver.get("https://web.whatsapp.com/")


# Сделайте скриншот элемента
# WebDriverWait(driver, 3*60).until(
# 	EC.presence_of_element_located((By.CSS_SELECTOR, "#app > div > div.x1c4vz4f.xs83m0k.xdl72j9.x1g77sc7.x78zum5.xozqiw3.x1oa3qoh.x12fk4p8.x1nhvcw1.xdt5ytf.xe4h88v.x1dr59a3.xp22266.xw2csxc.x1odjw0f.xyinxu5.xbxaen2.x1g2khh7.x1u72gb5.xp9ttsr.x6s0dn4.x9f619.xcnrxux.xvmahel.xdounpk > div.x1c4vz4f.xs83m0k.xdl72j9.x1g77sc7.x78zum5.xozqiw3.x1oa3qoh.x12fk4p8.xeuugli.x2lwn1j.xl56j7k.xdt5ytf.x6s0dn4 > div.x1lliihq > div > div > div.x1c4vz4f.xs83m0k.xdl72j9.x1g77sc7.x78zum5.xozqiw3.x1oa3qoh.x12fk4p8.xeuugli.x2lwn1j.x1nhvcw1.x1q0g3np.x1cy8zhl.x1ism021.x1w450gt > div.x1c4vz4f.xs83m0k.xdl72j9.x1g77sc7.xeuugli.x2lwn1j.xozqiw3.xamitd3.x7v7x1q.x1n2onr6.x5zbcu4.x1dnwe82.x8vdgqj > div > canvas")))

# element = driver.find_element(By.CSS_SELECTOR, "#app > div > div.x1c4vz4f.xs83m0k.xdl72j9.x1g77sc7.x78zum5.xozqiw3.x1oa3qoh.x12fk4p8.x1nhvcw1.xdt5ytf.xe4h88v.x1dr59a3.xp22266.xw2csxc.x1odjw0f.xyinxu5.xbxaen2.x1g2khh7.x1u72gb5.xp9ttsr.x6s0dn4.x9f619.xcnrxux.xvmahel.xdounpk > div.x1c4vz4f.xs83m0k.xdl72j9.x1g77sc7.x78zum5.xozqiw3.x1oa3qoh.x12fk4p8.xeuugli.x2lwn1j.xl56j7k.xdt5ytf.x6s0dn4 > div.x1lliihq > div > div > div.x1c4vz4f.xs83m0k.xdl72j9.x1g77sc7.x78zum5.xozqiw3.x1oa3qoh.x12fk4p8.xeuugli.x2lwn1j.x1nhvcw1.x1q0g3np.x1cy8zhl.x1ism021.x1w450gt > div.x1c4vz4f.xs83m0k.xdl72j9.x1g77sc7.xeuugli.x2lwn1j.xozqiw3.xamitd3.x7v7x1q.x1n2onr6.x5zbcu4.x1dnwe82.x8vdgqj > div > canvas")
# element.screenshot("element_screenshot.png")

# time.sleep(3)

# Узнать открылос ли ватсап
WebDriverWait(driver, 3*60).until(
	EC.presence_of_element_located((By.CSS_SELECTOR,"#pane-side > div:nth-child(1)")))

time.sleep(5)


while True:
	try:
		# войти на нужную группу
		WebDriverWait(driver, 60).until(
			EC.presence_of_element_located((By.CLASS_NAME,"_ak8q")))
		group_elements = driver.find_elements(By.CLASS_NAME, "_ak8q")

		for el in group_elements:
			if (el.text == "Öskemen Debate"):
				driver.execute_script("arguments[0].scrollIntoView(true);", el)
				el.click()
		break
	except selenium.common.exceptions.StaleElementReferenceException as e:
		pass

print("as")


WebDriverWait(driver, 60).until(
	EC.presence_of_element_located((By.CSS_SELECTOR,"#main > div.x1n2onr6.x1vjfegm.x1cqoux5.x14yy4lh > div > div.x10l6tqk.x13vifvy.x17qophe.xyw6214.x9f619.x78zum5.xdt5ytf.xh8yej3.x5yr21d.x6ikm8r.x1rife3k.xjbqb8w.x1ewm37j > div.x3psx0u.xwib8y2.xkhd6sd.xrmvbpv > div:nth-child(2)")))

# a = 0
# while True:
# 	parent_element = driver.find_element(By.CSS_SELECTOR, "#main > div.x1n2onr6.x1vjfegm.x1cqoux5.x14yy4lh > div > div.x10l6tqk.x13vifvy.x17qophe.xyw6214.x9f619.x78zum5.xdt5ytf.xh8yej3.x5yr21d.x6ikm8r.x1rife3k.xjbqb8w.x1ewm37j > div.x3psx0u.xwib8y2.xkhd6sd.xrmvbpv")
# 	try:
# 		scroll_focus_element = parent_element.find_element(By.CSS_SELECTOR, ":scope > *")
# 		driver.execute_script("arguments[0].scrollIntoView(true);", scroll_focus_element)
# 		a += 1
# 		print(a)
# 	except selenium.common.exceptions.StaleElementReferenceException:
# 		print("Element became stale. Trying again...")
# 		continue

# 	try:
# 		if driver.find_element(By.CSS_SELECTOR, "._amk4._aqjf._amkb"):
# 			break
# 	except Exception as e:
# 		pass
# 	time.sleep(1)

mes_conteiner = driver.find_element(By.CSS_SELECTOR, '#main > div.x1n2onr6.x1vjfegm.x1cqoux5.x14yy4lh > div > div.x10l6tqk.x13vifvy.x17qophe.xyw6214.x9f619.x78zum5.xdt5ytf.xh8yej3.x5yr21d.x6ikm8r.x1rife3k.xjbqb8w.x1ewm37j > div.x3psx0u.xwib8y2.xkhd6sd.xrmvbpv')
messages = mes_conteiner.find_elements(By.CSS_SELECTOR, '[role="row"]')
for message in messages:
	print(message.text)


driver.quit()

# сообщение отм что группа создана
# #main > div._amm9 > div > div._ajyl > div.x3psx0u.xwib8y2.xkhd6sd.xrmvbpv > div:nth-child(2) > div > div > div

# ожидания синхронизаций
# <button class="x14m1o6m x150wa6m x1b9z3ur x9f619 x1rg5ohu x1okw0bk x193iq5w x123j3cw xn6708d x10b6aqq x1ye3gou x13a8xbf xdod15v x2b8uid x1lq5wgf xgqcy7u x30kzoy x9jhf4c"><div class="x78zum5 x6s0dn4 x1r0jzty x17zd0t2"><span aria-hidden="true" data-icon="sync-in-progress" class=""><svg viewBox="0 0 16 21" height="14" width="11" preserveAspectRatio="xMidYMid meet" class="" fill="none"><title>sync-in-progress</title><path fill-rule="evenodd" clip-rule="evenodd" d="M8 0.71003V2.50003C12.42 2.50003 16 6.08003 16 10.5C16 11.54 15.8 12.54 15.43 13.45C15.16 14.12 14.3 14.3 13.79 13.79C13.52 13.52 13.41 13.11 13.56 12.75C13.85 12.06 14 11.29 14 10.5C14 7.19003 11.31 4.50003 8 4.50003V6.29003C8 6.74003 7.46 6.96003 7.14 6.65003L4.35 3.86003C4.15 3.66003 4.15 3.35003 4.35 3.15003L7.15 0.360031C7.46 0.0400305 8 0.260031 8 0.71003ZM2 10.5C2 13.81 4.69 16.5 8 16.5V14.71C8 14.26 8.54 14.04 8.85 14.35L11.64 17.14C11.84 17.34 11.84 17.65 11.64 17.85L8.85 20.64C8.54 20.96 8 20.74 8 20.29V18.5C3.58 18.5 0 14.92 0 10.5C0 9.46003 0.2 8.46003 0.57 7.55003C0.84 6.88003 1.7 6.70003 2.21 7.21003C2.48 7.48003 2.59 7.89003 2.44 8.25003C2.15 8.94003 2 9.71003 2 10.5Z" fill="#8696A0"></path></svg></span><div>Синхронизация более старых сообщений. Нажмите, чтобы посмотреть прогресс.</div></div></button>
# #main > div._amm9 > div > div._ajyl > div.x78zum5.x1okw0bk.xl56j7k.xqy66fx.x4uap5.x1hhzuzn.xkhd6sd > button


# Для скроллинга сообщений
# #main > div._amm9 > div > div._ajyl > div.x3psx0u.xwib8y2.xkhd6sd.xrmvbpv > div:nth-child(2)


# названия группый
# #pane-side > div:nth-child(1) > div > div > div:nth-child(1) > div > div > div > div._ak8l > div._ak8o > div._ak8q > span

# class="_amk4 _aqjf _amkb"


# <div class="_amjw _amk1 _aotl  focusable-list-item" tabindex="-1">

# <div class="" role="row">

# class="_amk4 _aqjf _amkb"