
"""This file contains all locators related to Flipkart page"""

#login page
login_main_button = "//*[text()='Login']"
email_xpath = "//*[text()='Enter Email/Mobile number']//ancestor::form//*[@type='text']"
password_xpath = "//*[@type='password']"
# login_submit_xpath = "//*[@type='submit']"
login_submit_xpath ="(//button[@type='submit'])[2]"
#main page
search_textbox_xpath = "//*[@type='text' and @name='q']"
search_dynamic_pop_up ="//li"
page_num_xpath = "//nav//a[{}]"
#product page
product = "//div[starts-with(@style,'flex-grow')]//div[@class='_1AtVbE col-12-12'][{}]"
last_element= "//*[text()='Help Center']"
first_element = "//*[text()='Offer Zone']"
backtotop = "//*[text()='Back to top']"
buy_now = "//*[@type='button']"
#checkout page
continue_xpath = "//*[text()='CONTINUE']"

