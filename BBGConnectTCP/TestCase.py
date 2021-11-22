# -*- coding: utf-8 -*-
"""
Created on Fri Nov 19 09:47:14 2021

@author: Kelian
"""

if __name__ == "__main__":
    
    import Client
    
    Node = Client.BBGRequest()
    df = Node.blp(Tickers=["ESA Index"], Start_Date="20150901")
