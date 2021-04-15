import unittest
import os
from selenium import webdriver
from time import sleep
import requests
import json
import jsonpath
from selenium.webdriver.chrome.options import Options

Options.headless = True
class Test(unittest.TestCase):
    def test_write_csv_file(self):
        api_req_url = 'http://sevensigmahealthcaresolutions.com/listendata.php'
        response = requests.get(api_req_url)
        print(response.content)

        json_response = json.loads(response.text)

        options = Options()
        options.headless = True
        driver = webdriver.Chrome(executable_path="C:\chromedriver\chromedriver.exe", options=options)

        print(type(json_response))
        a = jsonpath.jsonpath(json_response[0], 'user')
        b = jsonpath.jsonpath(json_response[0], 'url')
        c = jsonpath.jsonpath(json_response[0], 'websiteuser')
        d = jsonpath.jsonpath(json_response[0], 'websitepwd')

        print(c[0])
        print(d[0])
        sleep(2)
        user = json_response[0]['user']
        url = json_response[0]['url']
        websiteuser = json_response[0]['websiteuser']
        websitepwd = json_response[0]['websitepwd']
        driver.get(url)

        driver.maximize_window()
        sleep(2)
        driver.find_element_by_xpath(
            '//*[@id="messagetable"]/tbody/tr[4]/td/input').click()

        user = driver.find_element_by_xpath('//*[@id="username"]')
        user.send_keys(c)
        pasword = driver.find_element_by_xpath('//*[@id="password"]')
        pasword.send_keys(d)
        signin_btn = driver.find_element_by_xpath(
            '/html/body/table/tbody/tr[2]/td[2]/form/table/tbody/tr[1]/td[3]/table/tbody/tr[9]/td/input')
        signin_btn.click()
        sleep(3)

        # driver.find_element_by_xpath('//*[@id="ihaveseennmi"]').click()
        # driver.find_element_by_xpath('//*[@id="li_4"]').click()
        # driver.find_element_by_xpath('//*[@id="4"]/li[2]/a').click()
        # submit_btn = driver.find_element_by_xpath(
        #     '//*[@id="mainheader"]/table/tbody/tr[2]/td[2]/form/table/tbody/tr[4]/td/input')
        # submit_btn.click()




if __name__ == "__main__":
    unittest.main()





