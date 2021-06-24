import re
import platform
import matplotlib.pyplot as plt
from django.db import models
import pandas as pd
import numpy as np
import time
from bs4 import BeautifulSoup
from project2.mywork.common.models import FileDTO, Printer, Reader, Scrapper
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Election_19th(Reader):

    def __init__(self):
        self.f = FileDTO()
        self.r = Reader()
        self.p = Printer()
        self.s = Scrapper()
        self.sido_names_values = []
        self.df = []
        self.data = []
        self.sido_name = []

    @staticmethod
    def get_num(tmp):
        return float(re.split('\(', tmp)[0].replace(',',''))

    def get_url(self):
        f = self.f
        r = self.r
        p = self.p
        s = self.s
        driv = s.driver()
        driv.get("http://info.nec.go.kr/main/showDocument.xhtml?electionId=0000000000&topMenuId=VC&secondMenuId=VCCP09")
        driv.find_element_by_id("electionType1").click()
        driv.find_element_by_id("electionName").send_keys("제19대")
        driv.find_element_by_id("electionCode").send_keys("대통령선거")
        sido_list_raw = driv.find_element_by_xpath("""//*[@id="cityCode"]""")
        sido_list = sido_list_raw.find_elements_by_tag_name("option")
        sido_names_values = [option.text for option in sido_list]
        sido_names_values = sido_names_values[2:]
        print(sido_names_values)

    def move_sido(self, name):
        f = self.f
        r = self.r
        p = self.p
        s = self.s
        driv = s.driver()
        wait = WebDriverWait(driv, 10)
        element = driv.find_element_by_id("cityCode")
        element.send_keys(name)
        make_xpath = """//*[@id="searchBtn"]"""
        wait.until(EC.element_to_be_clickable((By.XPATH, make_xpath)))
        driv.find_element_by_xpath(make_xpath).click()

    def append_data(self):
        data = self.data
        sido_name = self.sido_name
        get_n = self.get_num()
        election_result_raw = {'광역시도': [], '시군': [], 'pop': [], 'moon': [], 'hong': [], 'ahn': []}
        for each in self.df[0].values[1:]:
            data['광역시도'].append(sido_name)
            data['시군'].append(each[0])
            data['pop'].append(get_n(each[2]))
            data['moon'].append(get_n(each[3]))
            data['hong'].append(get_n(each[4]))
            data['ahn'].append(get_n(each[5]))
        for each_sido in self.sido_names_values:
            self.move_sido(each_sido)
            html = self.driv.page_source
            soup = BeautifulSoup(html, 'html.parser')
            table = soup.find('table')
            df = pd.read_html(str(table))
            df.append(each_sido, election_result_raw)
        election_result = pd.DataFrame(election_result_raw,
                                       columns=['광역시도', '시군', 'pop', 'moon', 'hong', 'ahn'])
        election_result
        election_result.to_csv('../data/05. election_result.csv', encoding='utf-8', sep=',')


if __name__ == '__main__':
    e = Election_19th()
    # e.get_url()
    e.append_data()

