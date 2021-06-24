from django.db import models
from dataclasses import dataclass
from abc import *
import pandas as pd
import json
import googlemaps
from selenium import webdriver
from icecream import ic
pd.set_option('display.width', 1000)
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)


class PrinterBase(metaclass=ABCMeta):
    @abstractmethod
    def dframe(self):
        pass


class ReaderBase(metaclass=ABCMeta):

    @abstractmethod
    def new_file(self):
        pass

    @abstractmethod
    def csv(self):
        pass

    @abstractmethod
    def xls(self):
        pass

    @abstractmethod
    def json(self):
        pass


class ScrapperBase(metaclass=ABCMeta):

    @abstractmethod
    def driver(self):
        pass

@dataclass
class FileDTO(object):

    context: str
    fname: str
    url : str
    dframe: object

    @property # getter임
    def context(self) -> str: return self._context

    @context.setter # setter이며 따로 설정 이런 형식으로 함
    def context(self, context): self._context = context

    @property
    def fname(self) -> str: return self._fname

    @fname.setter
    def fname(self, fname): self._fname = fname

    @property
    def dframe(self) -> str: return self._dframe

    @dframe.setter
    def dframe(self, dframe): self._dframe = dframe

    @property
    def url(self) -> str: return self._url

    @url.setter
    def url(self, url): self._url = url


class Printer(PrinterBase):

    def dframe(self, this):
        print('*' * 100)
        print(f'1. target type is {type(this)}')
        print(f'2. target colums is \n{this.columns}')
        print(f'3. target TOP is \n{this.head()}')
        print(f'4. target number of null is \n{this.isnull().sum()}')
        print('*' * 100)


class Reader(ReaderBase):

    def new_file(self, file) -> str:
        return file.context + file.fname

    def csv(self, file) -> object:
        return pd.read_csv(f'{self.new_file(file)}.csv', encoding='UTF-8', thousands=',')

    def xls(self, file, header, usecols) -> object:
        return pd.read_excel(f'{self.new_file(file)}.xls', header=header, usecols=usecols)

    def json(self, file) -> object:
        return json.load(open(f'{self.new_file(file)}.json', encoding='UTF-8'))

    def gmaps(self) -> object:
        return googlemaps.Client(key='')

class Scrapper(ScrapperBase):

    def driver(self) -> object:
        return webdriver.Chrome(executable_path='/usr/local/bin/chromedriver')

    def aouto_login(self) -> object:
        pass