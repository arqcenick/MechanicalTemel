# -*- coding: utf-8 -*-
import re
import string
import os
import codecs
import numpy as np
import time
import random

train = codecs.open('train.txt','w','UTF-8')
valid = codecs.open('valid.txt','w','UTF-8')

valid_ratio = 0.2
valid_content = ""
train_content = ""

for root, categories, files in os.walk("Fıkralar/", topdown=False):    
    for category in categories:    
        for root, folders, fikras in os.walk("Fıkralar/"+category+"/", topdown=False):
            print("There are " + str(len(fikras)) + " fıkra in \""+category + "\" category")
            validation_fikra_indices = random.sample(range(0,len(fikras)),int(np.ceil(len(fikras)*valid_ratio)))
            validation_fikras = [fikras[i] for i in validation_fikra_indices]
            
            training_fikra_indices = list(set(range(0,len(fikras))) - set(validation_fikra_indices))
            training_fikras = [fikras[i] for i in training_fikra_indices]
            
            for fikra in validation_fikras:
                fikra_file = codecs.open("Fıkralar/"+category+"/"+fikra,'r','UTF-8')
                content = fikra_file.read()
                new_content = ""

                for char in content:
                    if char.isalpha() or char.isdigit():
                        char.lower()
                        if char == "I":
                            char = "ı"
                        char = char.lower()
                        if char == "ß":
                            char = "ss"
                        elif char == "â":
                            char = "a"
                        elif char == "ê":
                            char = "e"
                        elif char == "î":
                            char = "ı"
                        elif char == "û":
                            char = "u"
                        elif char == "ú":
                            char = "ü"
                        new_content = new_content + char
                    else:
                        new_content = new_content + " "

                
##                regex = re.compile('[%s]' % re.escape(string.punctuation))
##                new_content = regex.sub(' ', content)
        
                valid_content += new_content + " #\n"

            for fikra in training_fikras:
                fikra_file = codecs.open("Fıkralar/"+category+"/"+fikra,'r','UTF-8')
                content = fikra_file.read()
                new_content = ""

                for char in content:
                    if char.isalpha() or char.isdigit():
                        char.lower()
                        if char == "I":
                            char = "ı"
                        char = char.lower()
                        if char == "ß":
                            char = "ss"
                        elif char == "â":
                            char = "a"
                        elif char == "ê":
                            char = "e"
                        elif char == "î":
                            char = "ı"
                        elif char == "û":
                            char = "u"
                        elif char == "ú":
                            char = "ü"
                        new_content = new_content + char
                    else:
                        new_content = new_content + " "

##                regex = re.compile('[%s]' % re.escape(string.punctuation))
##                new_content = regex.sub(' ', content)



                train_content += new_content + " #\n"

train.write(train_content)
valid.write(valid_content)

train.close()
valid.close()
