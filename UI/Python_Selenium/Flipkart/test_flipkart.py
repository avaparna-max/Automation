from properties import *
from constants import *
from library import *

control_obj = Common()
class TestFlipkart:
    def test1(self):
        control_obj.goto_url(URL)
        # control_obj.waitfortheelement_to_load(login_main_button,elementname="login main btn")
        # control_obj.click(login_main_button,name="main login btn")
        control_obj.waitfortheelement_to_load(email_xpath, elementname="mail_textbox")
        control_obj.settext(email_xpath,EMAIL_ID,name='mail_textbox')
        control_obj.settext(password_xpath,PASSWORD,name="password_textbox")
        control_obj.click(login_submit_xpath, name='login_submit')
        time.sleep(1)
        control_obj.waitfortheelement_to_load(search_textbox_xpath,elementname="search_textbox")
        control_obj.settext(search_textbox_xpath,"televi",name="search_textbox")
        control_obj.select_any_product_from_searchlist(search_dynamic_pop_up,name="product_popup")
        control_obj.goto_page_number(page_num_xpath,name="page_no")
        control_obj.select_product(product,2,name="2nd_product")
        control_obj.switch_to_window(1)
        control_obj.scroll_down()
        control_obj.scroll_up()
        control_obj.waitfortheelement_to_load(buy_now,elementname="buy_now")
        control_obj.click(buy_now,name="buy_now")
        control_obj.waitfortheelement_to_load(continue_xpath,elementname="Continue_button")
        control_obj.take_screenshot()
        time.sleep(2)
        control_obj.driver.quit()

if __name__ == '__main__':
    t = TestFlipkart()
    t.test1()
