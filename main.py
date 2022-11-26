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

    def __str__(self) -> str:
        if self.position != -1:
            return f'Block {self.label} is in L{self.location} at position {self.position}.'
        else:
            if self.label != '':
                return f'Block {self.label} is held by the arm at L{self.location}.'
            else:
                f'No block is currently held by the arm. It is over location L{self.location}.'
    def __repr__(self) -> str:
        return self.label
class state:
    def __init__(self, L1, L2, L3, arm):
        self.locations = [L1, L2, L3]
        self.arm = arm

    def __str__(self) -> str:
        tallestStack = self.findTallestStack()
        bar = ' | '
        emptySpace = '_'
        newLine = '\n'
        lineBuilder = ""
        lineBuilder += newLine
        remainingLineCounter = np.size(self.locations[tallestStack])
        # check arm
        if self.arm.label != '':
            lineBuilder += f'Block {self.arm.label} is held by the arm at L{self.arm.location}.'
        else:
            lineBuilder += f'No block is currently held by the arm. It is over location L{self.arm.location}.\n'
        # check block stacks
        while(remainingLineCounter > 0): # loop to print each line
            remainingLineCounter -= 1
            listCounter = 0
            lineBuilder += bar
            while(listCounter <= 2): # loop through each list
                if remainingLineCounter < np.size(self.locations[listCounter]): # if the lineCounter is less than the number of elements at this location there is a block to print
                    blockLabel = self.locations[listCounter][remainingLineCounter].label
                    lineBuilder += blockLabel
                else: # if the lineCounter is greater than the number of elements at this location print a blank space 
                    lineBuilder += emptySpace
                lineBuilder += bar
                listCounter += 1
            lineBuilder += newLine
        return lineBuilder

    def __repr__(self) -> str:
        tallestStack = self.findTallestStack()
        bar = ' | '
        emptySpace = '_'
        newLine = '\n'
        lineBuilder = ""
        lineBuilder += newLine
        remainingLineCounter = np.size(self.locations[tallestStack])
        # check arm
        if self.arm.label != '':
            lineBuilder += f'Block {self.arm.label} is held by the arm at L{self.arm.location}.'
        else:
            lineBuilder += f'No block is currently held by the arm. It is over location L{self.arm.location}.'
        # check block stacks
        lineBuilder += newLine
        while(remainingLineCounter > 0): # loop to print each line
            remainingLineCounter -= 1
            listCounter = 0
            lineBuilder += bar
            while(listCounter <= 2): # loop through each list
                if remainingLineCounter < np.size(self.locations[listCounter]): # if the lineCounter is less than the number of elements at this location there is a block to print
                    blockLabel = self.locations[listCounter][remainingLineCounter].label
                    lineBuilder += blockLabel
                else: # if the lineCounter is greater than the number of elements at this location print a blank space 
                    lineBuilder += emptySpace
                lineBuilder += bar
                listCounter += 1
            lineBuilder += newLine
        return lineBuilder

    def findTallestStack(self):
        size_L1 = np.size(self.locations[0])
        size_L2 = np.size(self.locations[1])
        size_L3 = np.size(self.locations[2])
        tallestStack = -1
        if size_L1 > size_L2:
            if size_L1 > size_L3:
                tallestStack = 0
            elif size_L3 > size_L1: 
                tallestStack = 2
        if size_L2 > size_L1:
            if size_L2 > size_L3:
                tallestStack = 1
            elif size_L3 > size_L2:
                tallestStack = 2
        return tallestStack

    # State Actions
    def build(self, L1, L2, L3):
        self.locations[0] = L1
        self.locations[1] = L2
        self.locations[2] = L3

    def print(self):
        tallestStack = self.findTallestStack()
        print(f'The tallest stack of bricks is stack {tallestStack}, this stack is {np.size(self.locations[tallestStack])} bricks tall.')
        print(f'Stack 1: {np.size(self.locations[0])}\nStack 2: {np.size(self.locations[1])}\nStack 3: {np.size(self.locations[2])}')
        bar = " | "
        emptySpace = '_'
        remainingLineCounter = np.size(self.locations[tallestStack])
        while(remainingLineCounter > 0): # loop to print each line
            remainingLineCounter -= 1
            listCounter = 0
            lineBuilder = ""
            lineBuilder += bar
            #print(f'Remaining Line Count = {lineCounter}')
            while(listCounter <= 2): # loop through each list
                if remainingLineCounter < np.size(self.locations[listCounter]): # if the lineCounter is less than the number of elements at this location there is a block to print
                    # print the letter
                    #print(f'This space is block {blockLabel}')
                    blockLabel = self.locations[listCounter][remainingLineCounter].label
                    lineBuilder += blockLabel
                else: # if the lineCounter is greater than the number of elements at this location print a blank space 
                    #print("This space is blank")
                    lineBuilder += emptySpace
                lineBuilder += bar
                listCounter += 1
            print(f'{lineBuilder}')

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
    location = Li
    for b in blocks:
        location.insert(b.position, b)
    return location

def buildDefaultState() -> state:
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
    print("Blocks made")
    blocks = [a, b, c, d, e, f, g, h, i, j, k, m, n]
    arm = block('', 0, -1)
    L1 = buildLocation([], blocks)
    L2 = []
    L3 = []
    print("Locations Built")
    s1 = state(L1, L2, L3, arm)
    return s1

def testDefaultState(s):
    arm = block('l', 0, -1)
    s2 = state(s.locations[0], s.locations[1], s.locations[2], arm)
    t = [state, s2]
    print("state")
    s.print()
    print("end stae print()")
    print(f'state test print:{s}')
    print(f'representation test print:{t}')

s1 = buildDefaultState()
testDefaultState(s1)