# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 11:36:14 2016

@author: cycleuser
"""

import codecs
##fin = open('words.txt','r+','utf-8')

fin = codecs.open('in.md','r+','utf-8')
fout = codecs.open('output.md', 'w','utf-8')
def has(word):
    for letter in word:
        if letter == '>':
            return False
    return True


line = fin.readline()

for line in fin:
    if(len(line)>3 and line[2]==">"):
        fout.write(line)
    if(len(line)>3 and line[0]==">" and line[2]!=">"):
        fout.write("\r\n"+line+"\r\n")
    else:
        fout.write(line)

fout.close()