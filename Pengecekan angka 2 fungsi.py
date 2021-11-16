# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 15:54:46 2021

@author: User
"""

bilangan = int(input('Masukkan Bilangan : '))
pangkat = 3
pembagi = 3

def hitung_pangkat(bilangan, pangkat) :
 if bilangan % 3 == 0 :    
  if pangkat > 1:
    return bilangan * hitung_pangkat(bilangan, pangkat - 1)
 else :
     print
 return bilangan    
hasil = hitung_pangkat(bilangan, pangkat)
print("Hasil = ",hasil) 
      
def habis_tiga(bilangan, pembagi) :
    if bilangan % 3 == 0 : 
        return bilangan % 3 == 0 
         
    else :
        print("Hasil = False")

hasil = habis_tiga(bilangan, pembagi)
