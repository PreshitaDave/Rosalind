# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
file=open("demofile.txt","r")
content = file.readlines()
names = []
value = []
for i in range(0,len(content),2):
    l1=content[i][1:len(content[i])-1]
    l2=content[i+1]
    g=l2.count('G')
    c=l2.count('C')
    percent=100*(g+c)/len(l2)
    names.append(l1)
    value.append(percent)
maxpercent=value.index(max(value))
print(names[maxpercent],value[maxpercent])
