# -*- coding: utf-8 -*-
"""
Created on Wed Mar 12 12:43:27 2025

@author: Admin
"""

#Q1
import re
txt = "The Future Institute of Engineering And Management"
x=re.search("^The", txt)
print(x)
#Q2
import re
txt = "The Future Institute of Engineering And Mgmt"
x=re.search("Mgmt$", txt)
print(x)
#Q3
import re
txt = "The rain in India"
x = re.findall("The", txt)
print(x)
#Q4
import re
txt = "The rain in Theater Road"
x = re.findall("The", txt)
print(x)
#Q5
import re
txt = "The rain in Theater Road"
x = re.search("The", txt)
print(x)
#Q6
import re
matches = re.findall('the','the rain Theater road',flags=re.IGNORECASE)
for match in matches:
 print(match)
#Q7
import re
matches = re.finditer('the','the rain Theater road',flags=re.IGNORECASE)
for i in matches:
 print(i)
