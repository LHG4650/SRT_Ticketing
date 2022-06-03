import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
srt_hompage_path = "https://etk.srail.kr/main.do"

driver = webdriver.Chrome('chromedriver.exe')

#driver.implicitly_wait(5)

driver.get('https://etk.srail.kr/main.do')


login_btn = driver.find_element_by_css_selector('#wrap > div.header.header-e > div.global.clear > div > a:nth-child(2)')
login_btn.click()           #로그인 버튼 클릭


driver.find_element_by_css_selector('#login-form > fieldset > div.input-area.loginpage.clear > div.fl_l > div.top.val_m.inputgroup > label:nth-child(6)').click() #번호로 로그인 클릭
driver.find_element_by_css_selector('#srchDvNm03').click() #아이디창 클링
driver.find_element_by_css_selector('#srchDvNm03').send_keys('01050264650') #폰번입력

pw = "비밀번호"
driver.find_element_by_css_selector('#hmpgPwdCphd03').click() #비번 클링
driver.find_element_by_css_selector('#hmpgPwdCphd03').send_keys(pw)
#driver.find_element_by_css_selector('#hmpgPwdCphd03').send_keys(keys.RETURN)

#driver.execute_script(f"document.getElementsByName('hmpgPwdCphd')[0][0][0].value='{pw}'")

#driver.find_element_by_css_selector('#hmpgPwdCphd03').
#driver.find_element_by_css_selector('#hmpgPwdCphd03').send_keys(pw) #폰번입력
#hmpgPwdCphd03



#login-form > fieldset > div.input-area.loginpage.clear > div.fl_l > div.con.srchDvCd3.dis_none > div > div.fl_r > input
#driver.find_element_by_css_selector('#login-form > fieldset > div.input-area.loginpage.clear > div.fl_l > div.con.srchDvCd1 > div > div.fl_r > input').send_keys(Keys.ENTER) #로그인 버튼 클릭
a = driver.find_element_by_css_selector('#login-form > fieldset > div.input-area.loginpage.clear > div.fl_l > div.con.srchDvCd1 > div > div.fl_r > input') #로그인 버튼 클릭
print(time.time())
time.sleep(3)
print(time.time())


driver.execute_script("arguments[0].click();",a)


a  = input("일시정지")
