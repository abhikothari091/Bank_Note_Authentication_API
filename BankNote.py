# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 10:14:57 2024

@author: DELL
"""
# pydantic can be used to capture the requests, it incorportaees user friendly errors

from pydantic import BaseModel

class BankNote(BaseModel):
    variance : float
    skewness : float
    curtosis : float
    entropy : float
    