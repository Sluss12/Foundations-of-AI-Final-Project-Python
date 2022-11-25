"""
@author: mSlusser
@class: CS-4850 Foundations of AI
@project: Final
@projct_description:
@file_name: main.py
@file_description:
"""
import numpy as np
class block:
    def __init__(self):
        self.label = ""
        self.location = -1
        self.position = -1
    def __init__(self, name, position):
        self.label = name
        self.location = 0
        self.position = position
    def __init__(self, name, location, position):
        self.label = name
        self.location = location
        self.position = position

    # Block RELATIONSHIPS
    def above(self, block):
        print("returns true if block self is above block B")

    def above(self, location): 
        print("returns true if block self is above location Li")

    def on(self, block): 
        print("returns true if block self is on block B")

    def clear(self):
        print("returns true if block self has no block on self")

    def table(self):
        print("return true if block self is on the table (pos 0 in stack)")

class state:
    def __init__(self):
        L1 = []
        L2 = []
        L3 = []
        self.locations = [L1, L2, L3]
    def __init__(self, L1, L2, L3):
        L1 = []
        L2 = []
        L3 = []
        self.locations = [L1, L2, L3]

    # State Actions
    def build(self, L1, L2, L3):
        self.locations[0] = L1
        self.locations[1] = L2
        self.locations[3] = L3

    def print(self):
        size_L1 = np.size(self.locations[0])
        size_L2 = np.size(self.locations[1])
        size_L3 = np.size(self.locations[2])
        biggestStack = -1
        if size_L1 > size_L2:
            if size_L1 > size_L3:
                biggestStack = 0
            elif size_L3 > size_L1: 
                biggestStack = 2
        if size_L2 > size_L1:
            if size_L2 > size_L3:
                biggestStack = 1
            elif size_L3 > size_L2:
                biggestStack = 2
        lineBuilder = ""
        bar = " | "
        lineCounter = np.size(self.locations[biggestStack])
        listCounter = 0
        for line in range(lineCounter): # loop to print each line
            while(listCounter < 2): # loop through each list
                if lineCounter < self.locations[listCounter].count(): # if the lineCounter is less than the number of elements at this location there is a block to print
                    blockLabel = self.locations[listCounter][line].label
                    print(blockLabel)
                    # print the letter
                    lineBuilder += bar
                else: # if the lineCounter is greater than the number of elements at this location
                        # print a blank space 
                    pass
                
                listCounter += 1
            print
            # end for

    # Block Actions
    def pickUp(self, block, location):
        pass

    def putDown(self, block, location):
        pass

    def stack(self, block, location):
        pass

    def unstack(self, block, location):
        pass

    def move(self, block , start_location, end_location):
        pass

    def noop(self):
        pass


def buildLocation(Li, blocks):
    location = []
    location = Li
    for b in blocks:
        location.insert(b.position, b)
    
    return location

def buildDefaultState():
    a = block("a",0,0)
    b = block("b",0,1)
    c = block("c",0,2)
    d = block("d",0,3)
    e = block("e",0,4)
    f = block("f",0,5)
    g = block("g",0,6)
    h = block("h",0,7)
    i = block("i",0,8)
    j = block("j",0,9)
    k = block("k",0,10)
    m = block("m",0,11)
    n = block("n",0,12)
    blocks = [a, b, c, d, e, f, g, h, i, j, k, m, n]
    L1 = []
    L2 = []
    L3 = []
    L1 = buildLocation(L1, blocks)
    s1 = state(L1, L2, L3)
    s1.print()

buildDefaultState()
