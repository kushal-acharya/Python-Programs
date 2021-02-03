# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 16:03:56 2019

@author: User
"""

#glue things together and make them easier to see
#glues corresponding elements of lists together
list1= [1,2,3,4,5,6]
list2= ['one', 'two','there','four','five','six']
list3=['I','II','III','IV']
zipped= list(zip(list1, list2,list3))
print(zipped)
# if lists are not of equal length, python will truncate the extra elements
# output -> [(1, 'one', 'I'), (2, 'two', 'II'), (3, 'there', 'III'), (4, 'four', 'IV')]
#how to unzip
unzipped = list(zip(*zipped))
print(unzipped)
#output-> [(1, 2, 3, 4), ('one', 'two', 'there', 'four'), ('I', 'II', 'III', 'IV')]
#when is zipped most used?
for (l1,l2) in zip(list1,list2):
    print(l1)
    print(l2)

items=['Apple','Banana','Orange']
counts=[3,6,4]
price=[0.99,0.25,0.50]

sentences =[]
for (item,count,price) in zip(items,counts,price): # don't need to cast zip to a list 
    item, count, price = str(item), str(count), str(price)
    sentence = "I bought "+ count +" "+ item + "s at " + price +' cents each.'
    sentences.append(sentence)
print(sentences)
    
    