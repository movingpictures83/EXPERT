import random
import sys
from disk_struct import Disk
from page_replacement_algorithm import  page_replacement_algorithm
from CacheLinkedList import  CacheLinkedList
import numpy as np

import ExpertLearning
import ExpertLearning_v2

import PyIO
import PyPluMA

class EXPERTPlugin:
  def input(self, inputfile):
        self.parameters = PyIO.readParameters(inputfile)

  def run(self):
        pass

  def output(self, outputfile):
    n = int(self.parameters["n"])
    infile = open(PyPluMA.prefix()+"/"+self.parameters["infile"], 'r')
    kind = self.parameters["kind"]
    outfile = open(outputfile, 'w')
    outfile.write("cache size "+str(n))
    if (kind == "EexpertLearning"):
       expert = ExpertLearning.ExpertLearning(n)
    else:
       expert = ExpertLearning_v2.ExpertLearning_v2(n)
    page_fault_count = 0
    page_count = 0
    for line in infile:
        outfile.write("request: "+str(line))
        if expert.request(line) :
            page_fault_count += 1
        page_count += 1

    
    outfile.write("page count = "+str(page_count))
    outfile.write("\n")
    outfile.write("page faults = "+str(page_fault_count))
    outfile.write("\n")
