from selenium import webdriver
browser = webdriver.Firefox()
browser.get('https://automatetheboringstuff.com')

elem = browser.find_element_by_css_selector('.entry-content > ol:nth-child(15) > li:nth-child(1) > a:nth-child(1)')

elem

elem.click()

elems = browser.find_element_by_css_selector('p')
len(elems)

searchElem = browser.find_element_by_css_selector('.search-field')

searchElem.send_keys('zophie')

searchElem.submit()
browser.back()
browser.forward()
browser.refresh()
browser.quit()
browser = webdriver.Firefox()
browser.get('https://automatetheboringstuff.com')

elem = browser.find_element_by_css_selector('.entry-content > p:nth-child(4)')
elem.text

elem = browser.find_element_by_css_selector('html')
elem.text

 