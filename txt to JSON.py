#! /usr/bin/env python3

import os
import requests

dir="/data/feedback/"
url= "<Running web-service URL>"


for file in os.listdir(dir):
    tipos = ["title","name","date","feedback"]
    datos = {}
    lineas = []
    print(file)
    with open(dir+"/"+file,"r") as txtfile:
        x = 0
        for line in txtfile:
            datos[tipos[x]]  = line.rstrip('\n')
            x += 1
    print(datos)
    response = requests.post(url,json=datos)
