# -*- coding: utf-8 -*-
"""

@author: User
"""
#creating email address text scraper #patterns in text and strings(basic idea)
import re #regular expression operations #for picking up patterns in text and strings scraping it)
text = "A random string, MyName123@website.com, some more random text"
pattern=re.compile("A random string") #matches pattern and puts that match in here
result= pattern.search(text)
print(result)
#next try
text = "A random string, MyName123@website.com, some more random text"
pattern=re.compile("[ArC]") #matches pattern and puts that match in here
result= pattern.search(text)# picks only the first match, and discards the rest
print(result)
#can put in range as well
text = "A random string, MyName123@website.com, some more random text"
pattern=re.compile("[a-c]") #matches pattern and puts that match in here
result= pattern.search(text)# picks only the first match, and discards the rest
print(result)
#next try, matches beyond first, very cool
text = "A random string, MyName123@website.com, some more random text"
pattern=re.compile("[a-z]+") #works when we add +
result= pattern.search(text)# picks only the first match, and discards the rest
print(result) #backslash is important for period and + sign and brackets
#new
text = "A random string, MyName123@website.com, some more random text, Your-Name123@website.com"
pattern=re.compile("[a-zA-Z0-9\.\-]+@[a-zA-Z0-9]+\.[a-zA-Z]+") #works when we add +
result= pattern.findall(text)# picks only the first match, and discards the rest
print(result)#use findall to pick all
