from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.keys import Keys
import time 
import unittest

class NewVisitor(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def wait_for_row_in_list_table(self,row_text):
        start_time = time.time()
        while True:
            try:
                table = self.browser.find_element_by_id('user_list_table')
                rows = table.find_elements_by_tag_name('td')
                self.assertIn(row_text, [row.text for row in rows])
                return
            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(0.5)

    #He want to calculate the number

    def test_user_can_calculate_post(self):
        
        #He want to plus the nummber
        #He go to calculator website
        self.browser.get('http://127.0.0.1:8000/')

        link_calpost = self.browser.find_element_by_name('calpost')
        link_calpost.send_keys(Keys.ENTER)
        time.sleep(1)

        #He notice this webapp is calculator from title and head of this page
        self.assertIn('Calculator',self.browser.title)
        self.assertIn('Calculator',self.browser.find_element_by_tag_name('h1').text)

        #----------------plus-------------------------
        #He see both of input box and type the number
        input1_box = self.browser.find_element_by_name('input1')
        input1_box.send_keys(40)
        input2_box = self.browser.find_element_by_name('input2')
        input2_box.send_keys(20)
        time.sleep(1)
        
        #When he entered the number ,he clicked plus equation for summation two number
        plus_btn = self.browser.find_element_by_name('plus')
        plus_btn.send_keys(Keys.ENTER)
        time.sleep(2)

        #He notice the result appear under buttons 
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertIn('60.0',page_text)

        

        #-------------subtract--------------
        #He see both of input box and type the number
        input1_box = self.browser.find_element_by_name('input1')
        input1_box.send_keys(40)
        input2_box = self.browser.find_element_by_name('input2')
        input2_box.send_keys(20)
        time.sleep(1)

        #When he entered the number ,he clicked plus equation for summation two number
        plus_btn = self.browser.find_element_by_name('subtract')
        plus_btn.send_keys(Keys.ENTER)
        time.sleep(2)

        #He notice the result appear under buttons 
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertIn('20.0',page_text)

        

        #-------------multiple---------
        #He see both of input box and type the number
        input1_box = self.browser.find_element_by_name('input1')
        input1_box.send_keys(40)
        input2_box = self.browser.find_element_by_name('input2')
        input2_box.send_keys(20)
        time.sleep(1)

        #When he entered the number ,he clicked plus equation for summation two number
        plus_btn = self.browser.find_element_by_name('multiple')
        plus_btn.send_keys(Keys.ENTER)
        time.sleep(2)

        #He notice the result appear under buttons 
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertIn('800.0',page_text)

        

        #--------------divide--------------
        #He see both of input box and type the number
        input1_box = self.browser.find_element_by_name('input1')
        input1_box.send_keys(40)
        input2_box = self.browser.find_element_by_name('input2')
        input2_box.send_keys(20)
        time.sleep(1)

        #When he entered the number ,he clicked plus equation for summation two number
        plus_btn = self.browser.find_element_by_name('divide')
        plus_btn.send_keys(Keys.ENTER)
        time.sleep(2)

        #He notice the result appear under buttons 
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertIn('2.0',page_text)


        #He notice that when he pressed theoperator btn , there have equation appear to history
        self.assertIn('40.0 + 20.0 = 60.0',page_text)

        #He notice that when he pressed theoperator btn , there have equation appear to history
        self.assertIn('40.0 - 20.0 = 20.0',page_text)

        #He notice that when he pressed theoperator btn , there have equation appear to history
        self.assertIn('40.0 * 20.0 = 800.0',page_text)

        #He notice that when he pressed theoperator btn , there have equation appear to history
        self.assertIn('40.0 / 20.0 = 2.0',page_text)



        remove_all_btn = self.browser.find_element_by_name('remove_all')
        remove_all_btn.send_keys(Keys.ENTER)
        
        
        time.sleep(1)
        self.fail('finish the test !!')

    def test_user_can_calculate_get(self):
        
        #He want to plus the nummber
        #He go to calculator website
        self.browser.get('http://127.0.0.1:8000/')

        link_calpost = self.browser.find_element_by_name('calget')
        link_calpost.send_keys(Keys.ENTER)
        time.sleep(1)

        #He notice this webapp is calculator from title and head of this page
        self.assertIn('Calculator',self.browser.title)
        self.assertIn('Calculator',self.browser.find_element_by_tag_name('h1').text)

        #----------------plus-------------------------
        #He see both of input box and type the number
        input1_box = self.browser.find_element_by_name('input1')
        input1_box.send_keys(40)
        input2_box = self.browser.find_element_by_name('input2')
        input2_box.send_keys(20)
        time.sleep(1)
        
        #When he entered the number ,he clicked plus equation for summation two number
        plus_btn = self.browser.find_element_by_name('plus')
        plus_btn.send_keys(Keys.ENTER)
        time.sleep(2)

        #He notice the result appear under buttons 
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertIn('60.0',page_text)

        

        #-------------subtract--------------
        #He see both of input box and type the number
        input1_box = self.browser.find_element_by_name('input1')
        input1_box.send_keys(40)
        input2_box = self.browser.find_element_by_name('input2')
        input2_box.send_keys(20)
        time.sleep(1)

        #When he entered the number ,he clicked plus equation for summation two number
        plus_btn = self.browser.find_element_by_name('subtract')
        plus_btn.send_keys(Keys.ENTER)
        time.sleep(2)

        #He notice the result appear under buttons 
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertIn('20.0',page_text)

        

        #-------------multiple---------
        #He see both of input box and type the number
        input1_box = self.browser.find_element_by_name('input1')
        input1_box.send_keys(40)
        input2_box = self.browser.find_element_by_name('input2')
        input2_box.send_keys(20)
        time.sleep(1)

        #When he entered the number ,he clicked plus equation for summation two number
        plus_btn = self.browser.find_element_by_name('multiple')
        plus_btn.send_keys(Keys.ENTER)
        time.sleep(2)

        #He notice the result appear under buttons 
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertIn('800.0',page_text)

        

        #--------------divide--------------
        #He see both of input box and type the number
        input1_box = self.browser.find_element_by_name('input1')
        input1_box.send_keys(40)
        input2_box = self.browser.find_element_by_name('input2')
        input2_box.send_keys(20)
        time.sleep(1)

        #When he entered the number ,he clicked plus equation for summation two number
        plus_btn = self.browser.find_element_by_name('divide')
        plus_btn.send_keys(Keys.ENTER)
        time.sleep(2)

        #He notice the result appear under buttons 
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertIn('2.0',page_text)


        #He notice that when he pressed theoperator btn , there have equation appear to history
        self.assertIn('40.0 + 20.0 = 60.0',page_text)

        #He notice that when he pressed theoperator btn , there have equation appear to history
        self.assertIn('40.0 - 20.0 = 20.0',page_text)

        #He notice that when he pressed theoperator btn , there have equation appear to history
        self.assertIn('40.0 * 20.0 = 800.0',page_text)

        #He notice that when he pressed theoperator btn , there have equation appear to history
        self.assertIn('40.0 / 20.0 = 2.0',page_text)



        remove_all_btn = self.browser.find_element_by_name('remove_all')
        remove_all_btn.send_keys(Keys.ENTER)
        
        
        time.sleep(1)
        self.fail('finish the test !!')


