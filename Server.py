# -*- coding: utf-8 -*-
"""
Created on Thu Nov 18 12:29:56 2021

@author: Kelian
"""

import socket
from xbbg import blp
import json

# things to begin with
def Tcp_connect( HostIp, Port ):
    global s
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HostIp, Port))
    return

def Tcp_server_wait ( numofclientwait, port ):
    global s2
    s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s2.bind(('',port))
    s2.listen(numofclientwait)

def Tcp_server_next ( ):
    global s
    s = s2.accept()[0]

def Tcp_Write(D):
    s.send(str.encode(D))
    return

def Tcp_Read( ):
    a = ' '
    while a == ' ':
        a = s.recv(4096).decode()
    return a

def Tcp_Close( ):
    s.close()
    return

def BBGRequest(rq):
    df = blp.bdh(tickers=rq["Ticker"], flds=rq["flds"],
                 start_date=rq["Start_Date"], end_date=rq["End_Date"])
    return df.to_json()

def CheckBBG(rq):
    try:
        rq = json.loads(rq)
        rq = BBGRequest(rq)
        return rq
    except:
        Tcp_Close()
        print("Error")

def main():
    Tcp_server_wait(1, 5023)
    print("TCP Connection established..")
    while True:
        Tcp_server_next()
        response = Tcp_Read()
        print(response)
        if response == '"Close"':
            break
        Tcp_Write(CheckBBG(response))

    Tcp_Close()
    print("TCP Closed!")

main()

