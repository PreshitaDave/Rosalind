#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 11:30:43 2021

@author: preshitadave
"""

from Bio import SeqIO

fasta_file = SeqIO.parse(open('/Users/preshitadave/Documents/PythonScripts/Rosalind/rosalind_gc.txt'), 'fasta')

GC = {}

def gc_content(sequence):
    C = sequence.count('C')
    G = sequence.count('G')
    return (100*(C+G)/len(sequence))
    
for fasta in fasta_file:
    GC[fasta.id] = gc_content(fasta.seq)
    
max_key = max(GC, key=GC.get)
print(max_key)
print(GC[max_key])