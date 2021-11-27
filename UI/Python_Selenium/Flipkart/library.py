'''
ui common methods implemented here
'''
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from constants import *
from properties import last_element,first_element,backtotop
import time,random

class Common:

    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)

    def goto_url(self,url):
        self.driver.get(url)

    def waitfortheelement_to_load(self,locator,timeout=30,elementname=''):
        try:
            ele = WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.XPATH, locator)))
            while(timeout):
                try:
                    if ele.is_displayed() and ele.is_enabled():
                        break
                    timeout=timeout-1
                    time.sleep(1)
                except:
                    ele = WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.XPATH, locator)))
                    timeout = timeout - 1
                    time.sleep(1)
        except TimeoutException:
            error_message = "Unable to load - " + elementname

            raise Exception(error_message)

    def get_element_handle(self,locator,timeout=30,elementname=''):
        try:
            ele = WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.XPATH, locator)))
            return ele
        except TimeoutException:
            error_message = "Unable to get element " + elementname
            raise Exception(error_message)

    def click(self,locator,timeout=30,name=''):
        time.sleep(2)
        ele = self.get_element_handle(locator)
        if ele.is_displayed() and ele.is_enabled():
            ele.click()
        else:
            print("element- is not displayed/enabled".format(name))

    def settext(self,locator,textbox_value,name=''):
        timeout = 5
        while timeout:
            try:
                ele = self.get_element_handle(locator, elementname=name)
                ele.click()
                break
            except WebDriverException:
                print("Got timeout Exception")
                timeout = timeout - 1
                time.sleep(0.5)

        #above code to handle stale element exception

        ele = self.get_element_handle(locator,elementname=name)
        try:
            ele.click()
            ele.clear()
            ele.send_keys(textbox_value)
        except:
            error_message = "Unable to enter value-"+textbox_value
            raise Exception(error_message)

    def get_search_list(self,locator,name=''):
        self.waitfortheelement_to_load(locator)
        ele_list = self.driver.find_elements_by_xpath(locator)
        return ele_list

    def select_any_product_from_searchlist(self,locator,name=''):
        '''
        This library call selects product randomly which populates from search text box
        '''

        ele_list = self.get_search_list(locator,name)
        for product in ele_list:
            if "televisions" in product.text:
                time.sleep(0.5)
                product.click()
                break
        # product = random.choice(ele_list)
        # product.click()

    def goto_page_number(self,locator,page_no=3,name=''):
        loc = locator.format(page_no)
        #scroll to element
        # self.driver.execute_script("arguments[0].scrollIntoView();",loc)
        # doc = 'document.getElementByXPATH("' + loc + '").scrollIntoView(true)'
        # self.driver.execute_script(doc)
        self.waitfortheelement_to_load(loc,elementname=name)
        self.click(loc,name=name)

    def switch_to_window(self,tab_index):
        if len(self.driver.window_handles) > 1:
            self.driver.switch_to.window(self.driver.window_handles[int(tab_index)])
        else:
            raise("unable to switch window")

    def select_product(self,locator,product,name=''):
        # self.switch_to_window(1)
        product_num = locator.format(product)
        self.waitfortheelement_to_load(product_num,elementname=name)
        self.click(product_num,name)

    def scroll_down(self):
        # self.driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
        # timer = 60
        # while (timer):
        #     try:
        #         ele = self.driver.find_element_by_xpath(last_element)
        #         if ele:
        #             break
        #     except:
        #         pass
        #     self.driver.execute_script("scrollBy(0,500);")
        #     time.sleep(1)
        #     timer = timer - 1
        SCROLL_PAUSE_TIME = 0.5

        # Get scroll height
        last_height = self.driver.execute_script("return document.body.scrollHeight")

        while True:
            # Scroll down to bottom
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            # Wait to load page
            time.sleep(SCROLL_PAUSE_TIME)

            # Calculate new scroll height and compare with last scroll height
            new_height = self.driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height

    def take_screenshot(self):
        self.driver.save_screenshot(PATH)

    def scroll_up(self):
        timer=60
        self.waitfortheelement_to_load(backtotop)
        while(timer):
            try:
                ele= self.driver.find_element_by_xpath(backtotop)
                if not (ele.is_displayed() and ele.is_enabled()):
                    break
                self.driver.execute_script("scrollBy(0,-1000);")
                time.sleep(1)
                timer = timer - 1
            except:
                break









