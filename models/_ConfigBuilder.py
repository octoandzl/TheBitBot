"""config.json Configuration Builder"""

from os.path import isfile
from json import dump
from re import compile as re_compile
from sys import exit as sys_exit


class ConfigBuilder():

    def __init__(self) -> None:
        self._b = 0
        self._c = 0
        self._k = 0
        self._t = 0

    def init(self) -> None:
        print("*** config.json Configuration Builder ***")

        if isfile('config.json'):
            print("config.json already exists.")
            sys_exit()
        config = {}

        choice = input("Do you want to use the Coinbase Pro exchange (1=yes, 2=no:default)? ")
        if choice == '1':
            self._c = 1
            config['coinbasepro'] = {}
            config['coinbasepro']['api_url'] = 'https://api.pro.coinbase.com'

        try:
            with open('./config.json', 'w') as fout :
                dump(config, fout, indent=4)
            print("config.json saved!")
        except Exception as err:
                print(err)
                

if __name__=="__main__":
    confbuilder = ConfigBuilder()
    confbuilder.init()
