from selenium import webdriver
import time 

try:
    global browser
    browser = webdriver.Firefox()
    print(browser)
    browser.get('https://shimo.im')
    time.sleep(1)
    # 获取登录按钮并点击
    btm1 = browser.find_element_by_xpath('//button[contains(@class,"login-button")]')
    btm1.click()

    # 输入注册的账户和密码
    browser.find_element_by_xpath('//input[contains(@name,"mobileOrEmail")]').send_keys('895220007@qq.com')
    browser.find_element_by_xpath('//input[contains(@name,"password")]').send_keys('wwqwwq')
    time.sleep(1)
    browser.find_element_by_xpath('//button[contains(@class,"sm-button submit")]').click()

    # 获取 cookies信息
    cookies = browser.get_cookies()
    print(cookies)
    time.sleep(3)

except Exception as e:
    print(e)
finally:
    browser.close()