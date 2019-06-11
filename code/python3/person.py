#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 12:42:22 2019

@author: sbulut
"""
import datetime as dt

class Person:
    def __init__(self,fullname,birthdate):
        self.fullname = fullname
        self.birthdate = birthdate #expect format year/month/day
    
    def getage(self):
        now = dt.datetime.now()
        
        year = now.year
        month = now.month
        day = now.day
        
        lbirth = self.birthdate.split('/')
        byear = int(lbirth[0])
        bmonth = int(lbirth[1])
        bday = int(lbirth[2])
        
        age_year = year - byear
        age_month = month - bmonth
        age_day = day - bday
        age=str(age_year)+' years '+str(age_month)+' months '+str(age_day)+'days'
        
        return age