# -*- coding: utf-8 -*-
"""
Created on Thu Nov 18 13:43:54 2021

@author: Kelian
"""

import socket
import json
import pandas as pd
import os

class BBGRequest:
    
    def __init__(self):
        self.s = ""
               
    def Tcp_connect(self, HostIp, Port):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect((HostIp, Port))
        return
       
    def Tcp_Write(self, D):
       self.s.send(str.encode(D))
       return 
       
    def Tcp_Read(self):
    	a = ' '
    	while a == ' ':
    		a = self.s.recv(4096).decode()
    	return a
    
    def Tcp_Close(self):
       self.s.close()
       return 
    
    def GetServerAddress(self):
        if "ServerAddress.txt" in os.listdir(r"Address/"):
            AddressFile = open(r"Address/ServerAddress.txt", "r")
            Address = AddressFile.read()
            return Address
        else:
            Address = input("What is the Server Local IP Address ?\n")
            AddressFile = open(r"Address/ServerAddress.txt", "w")
            AddressFile.write(Address)
            AddressFile.close()
            return Address
        
    def blp(self, Tickers = [], flds=["PX_LAST"], 
            Start_Date="20150101", End_Date="20230101"):
        Address = self.GetServerAddress()
        self.Tcp_connect(Address, 5023)
        dico = {}
        dico["Ticker"] = Tickers  # Check all different
        dico["flds"] = flds
        dico["Start_Date"] = Start_Date
        dico["End_Date"] = End_Date
        if Tickers == []:
            dico = "Close"
        rq = json.dumps(dico)
        self.Tcp_Write(rq)
        response = self.Tcp_Read()
        if rq != '"Close"':
            response = pd.read_json(response)
        self.Tcp_Close()
        return response
