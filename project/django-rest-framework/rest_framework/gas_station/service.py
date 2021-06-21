from rest_framework.common.entity import FileDTO
from rest_framework.common.services import Printer, Reader, Scrapper
import pandas as pd
import numpy as np
import folium
from selenium import webdriver
from glob import glob
'''
문제 정의
셀프 주유소는 정말 저렴한가

'''

class GasStation(Reader):

    def __init__(self):
        self.f = FileDTO()
        self.r = Reader()
        self.p = Printer()
        self.s = Scrapper()

    def get_url(self):
        f = self.f
        r = self.r
        p = self.p
        s = self.s
        f.url = 'https://www.opinet.co.kr/searRgSelect.do'
        driver = s.driver()

        gu_list_raw = driver.find_element_by_xpath("""//*[@id="SIGUNGU_NMG""")
        gu_list = gu_list_raw.find_element_by_xpath
        gu_names = [option.gas_attribute("value") for option in gu_list]
        gu_names.remove("")

    def gas_station_price_info(self):
        f = self.f
        r = self.r
        # print(glob('./data/지역_위치별*xls'))
        station_files = glob('./data/지역_위치별*.xls')
        tmp_raw = []
        for i in station_files:
            t = pd.read_excel(i, header=2)
            tmp_raw.append(t)
        station_raw = pd.concat(tmp_raw)
        station_raw.info()
        print("*"*100)
        print(station_raw.head(2))
        print(station_raw.tail(2))
        stations = pd.DataFrame({'Oil_store': station_raw['상호'],
                                 '주소': station_raw['상호'],
                                 '가격': station_raw['상호'],
                                 '셀프': station_raw['상호'],
                                 '상표': station_raw['상호']})
        print(stations.head())
        stations['구'] = [i.split()[1] for i in stations['주소']]
        stations['구'].unique()
        # print(stations[station_raw['구']=='서울특별시'])
        stations[stations['구'] == '서울특별시'] = '성동구'
        stations['구'].unique()
        stations[stations['구'] == '특별시'] = '도봉구'
        stations['구'].unique()
        stations = stations[stations['가격'] != '-']
        stations = stations[stations['가격'] != '성동구']
        stations['가격'] = [float(i) for i in stations['가격']]
        stations.reset_index(inplace=True)
        del stations['index']
        print(stations.columns)
        print(stations.head(2))
        print(stations.tail(2))


if __name__ == '__main__':
    g = GasStation()
    # g.get_url()
    g.gas_station_price_info()