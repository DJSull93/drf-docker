import re
import platform
import matplotlib.pyplot as plt
from django.db import models
import pandas as pd
import numpy as np
import time
from project2.mywork.common.models import FileDTO, Printer, Reader, Scrapper


class Election_19th(Reader):

    def __init__(self):
        self.f = FileDTO()
        self.r = Reader()
        self.p = Printer()
        self.s = Scrapper()

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



if __name__ == '__main__':
    e = Election_19th()
    e.get_url()

