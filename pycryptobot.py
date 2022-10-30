#!/usr/bin/env python3
# encoding: utf-8

"""Python Crypto Bot consuming Coinbase Pro or Binance APIs"""

import functools
import json
import os
import sched
import signal
import sys
import time
from datetime import datetime, timedelta

import pandas as pd

# minimal traceback
sys.tracebacklimit = 1
s = sched.scheduler(time.time, time.sleep)
pd.set_option('display.float_format', '{:.8f}'.format)



if __name__=='__main__':
    #print('Hello World')

    result = 3/0