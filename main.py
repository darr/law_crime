#!/usr/bin/python
# -*- coding: utf-8 -*-
#####################################
# File name : main.py
# Create date : 2019-08-21 19:39
# Modified date : 2019-08-21 20:45
# Author : DARREN
# Describe : not set
# Email : lzygzh@126.com
#####################################
from __future__ import division
from __future__ import print_function

from anliwang_spider import AnLiCrimeSpider
from courtlaw_spider import CourtLawSpider

from lawlib_spider import LawLibSpider
from sifawang_spider import SifaCrimeSpider

from export_data import LawSpider
from crime_law import LawGraph

def run_anliwang_spider():
    handler = AnLiCrimeSpider()
    handler.crime_spider()

def run_court_law_spider():
    handler = CourtLawSpider()
    handler.court_spider()


def run_law_lib_spider():
    handler = LawLibSpider()
    handler.court_spider()

def run_sifawang_spider():
    handler = SifaCrimeSpider()
    handler.crime_spider()

def run_export_data():
    handler = LawSpider()
    handler.export_data_crime()

def run_crime_law():
    handler = LawGraph()
    tuples = handler.build_lawdict()
    for tuple in tuples:
        print(tuple)

def run():
    #run_anliwang_spider()
    #run_court_law_spider()
    #run_law_lib_spider()
    #run_sifawang_spider()
    #run_export_data()
    run_crime_law()

run()

