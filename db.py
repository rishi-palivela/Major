# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="hitesh",
  database="majorProject"
)

mycursor = mydb.cursor()

query = "Select * from TV where `Speaker`=%s AND `Size`=%s AND `HD`=%s AND `HDMI`=%s AND `USB`=%s ORDER BY `Cost`, `Ratings` LIMIT 3"
  
def output(speaker,size,hd,hdmi,usb):
  inputs=(speaker,size,hd,hdmi,usb)
  mycursor.execute(query,inputs)
  myresult = mycursor.fetchall()
  return myresult[0],myresult[1],myresult[2]
  
