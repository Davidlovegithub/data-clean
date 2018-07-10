# -*- coding: utf-8 -*-
"""
Created on Fri Jul  6 11:15:50 2018

@author: User
"""

import xlrd
from sklearn import linear_model
import numpy as np
import pandas as pd
import csv

df1=pd.read_csv('保险行业清洗数据.csv',header=None,sep=' ',encoding = ‘GB2312’)
