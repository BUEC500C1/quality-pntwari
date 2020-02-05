#!/home/ece-student/anaconda3/bin/python
#chmod 755 splitargs
# -*- coding: utf-8 -*-


# Created by: Pat Rick Ntwari
# Homework 1, EC500


# Converting numbers from arabic to roman numerals

import pytest
import arabic

def test_answer():
    assert arabic.arab_to_roman(1994) == "MCMXCIV"
    assert arabic.arab_to_roman(30) == "XXX"
    assert arabic.arab_to_roman(221) == "CCXXI"
    assert arabic.arab_to_roman(7) == "VII"
    #assert arabic.arab_to_roman(15) == "XVI"      ## WRONG

