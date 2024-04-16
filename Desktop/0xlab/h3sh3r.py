#!/usr/bin/python

import hashlib
import os

if os == 'linux':
	os.system("clear")
	
if os == 'windows':
	os.system("cls")

print'''
h3sh3r tool written  by Achraf Chakir:
  _     ____      _     ____       
 | |   |___ \    | |   |___ \      
 | |__   __) |___| |__   __) |_ __ 
 | '_ \ |__ </ __| '_ \ |__ <| '__|
 | | | |___) \__ \ | | |___) | |   
 |_| |_|____/|___/_| |_|____/|_|   
                                   
                                                                                              
        aka 0xr41d3n
       Made in Morrocco with love
'''
print'''
for the moment that's what it's capable of : 

1) MD5 hash
2) SHA-1 hash
3) SHA-224 hash
4) SHA-256 hash
5) SHA-384 hash
6) SHA-512 hash
'''
x = raw_input(">")

if x == '1':
	mess = raw_input("txt to encrypt with MD5 : ")
	mdgen = hashlib.md5()
	mdgen.update(mess)
	rslt = mdgen.hexdigest()
	print ("that's your hash : " + rslt)
	
if x == '2':
	mess = raw_input("txt to encrypt with SHA-1 : ")
	sh1gen = hashlib.sha1()
	sh1gen.update(mess)
	rslt = sh1gen.hexdigest()
	print ("that's your hash : " + rslt)
	
if x == '3':
	mess = raw_input("txt to encrypt with SHA-224 : ")
	sh22gen = hashlib.sha224()
	sh22gen.update(mess)
	rslt = sh22gen.hexdigest()
	print ("that's your hash : " + rslt)
	
if x == '4':
	mess = raw_input("txt to encrypt with SHA-256 : ")
	sh25gen = hashlib.sha256()
	sh25gen.update(mess)
	rslt = sh25gen.hexdigest()
	print ("that's your hash" + rslt)
	
if x == '5':
	mess = raw_input("txt to encrypt with SHA-384 : ")
	sh38gen = hashlib.sha384()
	sh38gen.update(mess)
	rslt = sh38gen.hexdigest()
	print ("that's your hash" + rslt)
	
if x == '6':
	mess = raw_input("txt to encrypt with SHA-512 : ")
	sh51gen = hashlib.sha512()
	sh51gen.update(mess)
	rslt = sh51gen.hexdigest()
	print ("that's your hash" + rslt)
    
    
