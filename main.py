"""
@author: mSlusser
@class: CS-4850 Foundations of AI
@project: Final
@projct_description:
@file_name: main.py
@file_description:
"""
# Imports
from typing import Optional
import numpy as np

# Classes
class block(object):
    # Class Functions
    def __init__(self, name: Optional[str] = None, location: Optional[int] = 0, position: Optional[int] = -1):
        self.label = name
        self.location = location
        self.position = position

    def __str__(self) -> str:
        if self.position != -1:
            return f'Block {self.label} is in L{self.location} at position {self.position}.'
        else:
            if self.label is None:
                return f'No block is currently held by the arm: it is over L{self.location}.'
            else:
                return f'Block {self.label} is held by the arm at L{self.location}.'

    def __repr__(self) -> str:
        return self.label

    def __eq__(self, __o: object) -> bool:
        if self.location != __o.location:
            return False
        if self.label != __o.label:
            return False
        if self.position != __o.position:
            return False
        return True

    def __ne__(self, __o: object) -> bool:
        if self.location == __o.location:
            if self.label == __o.label:
                if self.position == __o.position:
                    return False
        return True

    # Block RELATIONSHIPS
    def above(self, block: Optional[object] = None, location: Optional[int|list[object]] = None) -> bool:
        if block is not None:
            if self.location == block.location:
                if self.position > block.position:
                    return True
                else:
                    if self.position == -1:
                        return True # arm above location case
                    return False
            else:
                #print(f'block {self.label} is not in the same stack as block {block.label}')
                return False
        else:
            #print('block is None')
            pass
        if location is not None:
            if type(location) == int:
                if self.location == location:
                    #print(f'block {self.label} is above location L{location+1}(int)')
                    return True
                else:
                    return False
            if type(location) == list:
                if location[self.position]:
                    #print(f'block {self.label} is in this stack')
                    return True
                else:
                    #print(f'block {self.label} is not in this stack')
                    return False
        else:
            #print('Location is None')
            pass

    def on(self, block: object)-> bool: 
        if self.location == block.location:
            if self.position != block.position-1:
                return False
            else:
                return True
        else:
            #print(f'block {self.label} is not in the same stack as block {block.label}')
            return False

    def clear(self, location:list[object])-> bool:
        if self != location[self.position]:
            #print(f'block {self.label} (pos: L{self.location},{self.position}) is not in this stack')
            #printLocation(location)
            return False
        try:
            if location[self.position+1]:
                #print(f'block found at self.positin+1: {location[self.position+1]}')
                return False
        except IndexError:
            #print(f'no block found at self.position+1')
            return True

    def table(self)-> bool:
        if self.position != 0:
            #print(f'block {self.label} is not on the table (pos: L{self.location},{self.position})')
            return False
        else:
            #print(f'block {self.label} is on the table at loc: L{self.location}')
            return True

class state(object):
    # Class Functions
    def __init__(self, L1: Optional[list[block]] = [], L2: Optional[list[block]] = [], L3: Optional[list[block]] = [], 
                 arm: Optional[block] = block()):
        self.locations = [L1, L2, L3]
        self.arm = arm

    def __str__(self) -> str:
        tallestStack = self.findTallestStack()
        #print(f'Tallest stack: {tallestStack}')
        bar = ' | '
        emptySpace = '_'
        newLine = '\n'
        lineBuilder = ""
        lineBuilder += newLine
        remainingLineCounter = np.size(self.locations[tallestStack])
        # check arm
        lineBuilder += self.printArm() + newLine
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
        lineBuilder += stackLabels()
        return lineBuilder

    def __repr__(self) -> str:
        tallestStack = self.findTallestStack()
        bar = ' | '
        emptySpace = '_'
        newLine = '\n'
        lineBuilder = ""
        remainingLineCounter = np.size(self.locations[tallestStack])
        if remainingLineCounter != 0:
            lineBuilder += newLine
        # check arm
        lineBuilder += f'{self.arm}' + newLine
        lineBuilder += self.printArm()
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

    def __eq__(self, __o: object) -> bool:
        for x in range(3): # each stack
            if self.locations[x] != __o.locations[x]:
                return False
            if self.arm != __o.arm:
                return False
        return True

    def __ne__(self, __o: object) -> bool:
        for x in range(3): # each stack
            if (self.locations[x] != __o.locations[x]) or (self.arm != __o.arm):
                return True
        return False

    def printArm(self) -> str:
        if self.arm.label is None:
            label = ' '
        else:
            label = self.arm.label
        if self.arm.location == 0:
            return f' -|{label}|--------- '
        if self.arm.location == 1:
            return f' -----|{label}|----- '
        if self.arm.location == 2:
            return f' ---------|{label}|- '
            

    def print(self):
        tallestStack = self.findTallestStack()
        print(f'The tallest stack of bricks is stack {tallestStack}, this stack is {np.size(self.locations[tallestStack])} bricks tall.')
        print(f'Stack 1: {np.size(self.locations[0])}\nStack 2: {np.size(self.locations[1])}\nStack 3: {np.size(self.locations[2])}')
        bar = " | "
        emptySpace = '_'
        print(self.printArm())
        remainingLineCounter = np.size(self.locations[tallestStack])
        while(remainingLineCounter > 0): # loop to print each line
            remainingLineCounter -= 1
            listCounter = 0
            lineBuilder = ""
            lineBuilder += bar
            #print(f'Remaining Line Count = {lineCounter}')
            while(listCounter <= 2): # loop through each list
                if remainingLineCounter < np.size(self.locations[listCounter]): 
                    #print(f'This space is block {blockLabel}')
                    blockLabel = self.locations[listCounter][remainingLineCounter].label
                    lineBuilder += blockLabel
                else: 
                    #print("This space is blank")
                    lineBuilder += emptySpace
                lineBuilder += bar
                listCounter += 1
            print(f'{lineBuilder}')
        print(stackLabels())

    def findTallestStack(self) -> int:
        size_L0 = np.size(self.locations[0])
        size_L1 = np.size(self.locations[1])
        size_L2 = np.size(self.locations[2])
        #print(f'l0: {size_L0}\nl1: {size_L1}\nl2: {size_L2}\n')
        tallestStack = -1
        if size_L0 == size_L1 or size_L0 == size_L2:
            tallestStack = 0
        if size_L1 == size_L2:
            tallestStack = 1
        if size_L0 > size_L1:
            if size_L0 > size_L2:
                tallestStack = 0
            elif size_L2 > size_L0: 
                tallestStack = 2
        if size_L1 > size_L0:
            if size_L1 > size_L2:
                tallestStack = 1
            elif size_L2 > size_L1:
                tallestStack = 2
        return tallestStack

    def findShortestStack(self) -> int:
        size_L0 = np.size(self.locations[0])
        size_L1 = np.size(self.locations[1])
        size_L2 = np.size(self.locations[2])
        #print(f'l0: {size_L0}\nl1: {size_L1}\nl2: {size_L2}\n')
        shortestStack = -1
        if size_L0 == size_L1 or size_L0 == size_L2:
            shortestStack = 0
        if size_L1 == size_L2:
            shortestStack = 1
        if size_L0 < size_L1:
            if size_L0 < size_L2:
                shortestStack = 0
            elif size_L2 < size_L0: 
                shortestStack = 2
        if size_L1 < size_L0:
            if size_L1 < size_L2:
                shortestStack = 1
            elif size_L2 < size_L1:
                shortestStack = 2
        return shortestStack

    def isArmEmpty(self) -> bool:
        if self.arm == block(location=0): 
            return True
        if self.arm == block(location=1):
            return True
        if self.arm == block(location=2):
            return True
        return False # arm is not empty

    # State Actions
    def build(self, L1: Optional[list[block]] = None, L2: Optional[list[block]] = None, L3: Optional[list[block]] = None,  arm: Optional[block] = None, State: Optional[object] = None):
        newState = state(self.locations[0],self.locations[1],self.locations[2], self.arm)
        if State is type(self):
            newState.locations[0] = State.locations[0]
            newState.locations[1] = State.locations[1]
            newState.locations[2] = State.locations[2]
            newState.arm = State.arm
        else:
            if L1 is not None:
                newState.locations[0] = L1
            else:
                newState.locations[0] = self.locations[0]
            if L2 is not None:
                newState.locations[1] = L2
            else:
                newState.locations[1] = self.locations[1]
            if L3 is not None:
                newState.locations[2] = L3
            else:
                newState.locations[2] = self.locations[2]
            if arm is not None:
                newState.arm = arm
            else:
                newState.arm = self.arm
        return newState

    # State Change Actions
    def pickUp(self, location: int):
        if not self.isArmEmpty():
            print(f'block could not be picked up: arm is not empty\n{self.arm}')
            return False
        else:
            if not self.arm.above(location=location):
                print(f'could not pick up: arm not above block')
                return False
            else:
                if np.size(self.locations[location]) == 0:
                    print(f'block could not be picked up: no block not found at given location L{location}')
                    return False
                else:
                    self.arm = self.locations[location].pop()
                    self.arm.position = -1
                    return True

    def putDown(self, location: int):
        if self.isArmEmpty():
            print(f'cannot putdown, arm is empty')
            return False
        else:
            if not self.arm.above(location=location):
                print(f'cannot putdown, block is not above given location')
                return False
            else:
                if np.size(self.locations[location]) != 0:
                    print(f'cannot putdown onto block')
                    return False
                else:
                    self.locations[location].insert(np.size(self.locations[location]), block(self.arm.label,location, 0))
                    self.arm.label = None
                    return True
                    #print(f'block putDown')

    def stack(self, location: int):
        if self.isArmEmpty():
            print(f'cannot stack, arm is empty')
            return False
        else:
            if not self.arm.above(location=location):
                print(f'cannot stack, block is not above given location')
                return False
            else:
                if np.size(self.locations[location]) == 0:
                    print(f'cannot stack onto table')
                    return False
                else:
                    self.locations[location].insert(np.size(self.locations[location]), block(self.arm.label,location, 0))
                    self.arm.label = None
                    return True
                    #print(f'block putDown')

    def unstack(self, location: int):
        if not self.isArmEmpty():
            print(f'could not unstack: arm is not empty\n{self.arm}')
            return False
        else:
            if not self.arm.above(location=location):
                print(f'could not stack: arm not above block')
                return False
            else:
                if np.size(self.locations[location]) == 0:
                    print(f'could not unstack: block is on table')
                else:
                    self.arm = self.locations[location].pop()
                    self.arm.position = -1


    def move(self, start_location: int, end_location: int):
        if self.arm.location != start_location:
            print(f'ERROR: arm is not at start_location L{start_location}. Cannot move block.\n{self.arm}')
            return False
        else:
            #print(f'Moving block {block.label} to location L{end_location}')
            self.arm.location=end_location
            return True

    def noop(self):
        pass

# Testing

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
    blocks = [a, b, c, d, e, f, g, h, i, j, k, m, n]
    default = state(blocks)
    return default

def testDefaultState(s:state):
    print('testDefaultState(s:state):')
    arm = block('l', 0, -1)
    s2 = state(s.locations[0], arm=arm)
    t = [state, s2]
    s.print()
    print("end state .print()")
    print("Printing Location L0:")
    printLocation(s.locations[0], s.arm)
    if s.isArmEmpty():
        print('arm is empty')
    else:
        print('arm is not empty')
    print(f'state test print(s):{s}')
    print(f'representation test print:{t}')
    print('END OF testDefaultState(s:state)\n\n\n')

def testBuildState():
    print('testBuildState():')
    buildStateTest = state(L1=[block("a", 0, 0), block("b", 0, 1)], L2=[block("c", 1, 0)], arm=block('d', 2, -1))
    copyBuildStateTest1 = buildStateTest.build()
    copyBuildStateTest2 = copyBuildStateTest1.build(L2=[])
    copyBuildStateTest3 = copyBuildStateTest2.build(State=copyBuildStateTest2)
    print(f'state 1:{buildStateTest}')
    print(f'copy of state 1:{copyBuildStateTest1}')
    print(f'copy of state 2:{copyBuildStateTest2}')
    print(f'copy of state 3:{copyBuildStateTest3}')
    state2 = buildStateTest.build(arm=block())
    print(f'state 2:{state2}')
    state3 = buildStateTest.build(L2=[])
    print(f'state 3:{state3}')
    print(f'state 1:{buildStateTest}')
    print('END OF testBuildState()\n\n\n')

def testStateComparitors():
    print(f'testStateComparitors():')
    testState = state(L1=[block("a", 0, 0), block("b", 0, 1)], L2=[block("c", 1, 0)], arm=block('d', 2, -1))
    copyTestState = testState.build()
    if testState == copyTestState:
        print(f'{testState}and{copyTestState}are equal')
    else:
        print(f'{testState}and{copyTestState}are NOT equal')
    if testState != copyTestState:
        print(f'{testState}and{copyTestState}are NOT equal(NE)')
    else:
        print(f'{testState}and{copyTestState}are equal(NE)')
    copyTestState = testState.build(arm=block())
    if testState == copyTestState:
        print(f'{testState}and{copyTestState}are equal')
    else:
        print(f'{testState}and{copyTestState}are NOT equal')
    if testState != copyTestState:
        print(f'{testState}and{copyTestState}are NOT equal(NE)')
    else:
        print(f'{testState}and{copyTestState}are equal(NE)')
    copyTestState = testState.build(L2=[])
    if testState == copyTestState:
        print(f'{testState}and{copyTestState}are equal')
    else:
        print(f'{testState}and{copyTestState}are NOT equal')
    if testState != copyTestState:
        print(f'{testState}and{copyTestState}are NOT equal(NE)')
    else:
        print(f'{testState}and{copyTestState}are equal(NE)')
    print(f'END OF testStateComparitors()\n\n\n')

def testPrintLocation():
    print('testPrintLocation():')
    blockA = block("a", 0, 0)
    blockB = block("b", 0, 1)
    L0 = [blockA, blockB]
    print("Printing Location L0:")
    printLocation(L0)
    print("Printing Location L2:")
    printLocation([])
    arm = block('d', 2, -1)
    print("Printing Location Arm:")
    printLocation(arm=arm)
    print("Printing Location Empty Arm:")
    printLocation(arm=block())
    print("Printing Location None:")
    printLocation()
    print('END OF testPrintLocation()\n\n\n')

def testEmptyArm():
    print('testEmptyArm():')
    emptyArmTestState = state(L1=[block("a", 0, 0), block("b", 0, 1)], L2=[block("c", 1, 0)], arm=block('d', 2, -1))
    print(f'state:{emptyArmTestState}')
    if emptyArmTestState.isArmEmpty():
        print(f'arm is empty\n{emptyArmTestState.arm}')
    else:
        print(f'arm is not empty\n{emptyArmTestState.arm}')
    emptyArmTestState.arm = block()
    print('Arm Reset to Empty')
    print(f'state:{emptyArmTestState}')
    if emptyArmTestState.isArmEmpty():
        print(f'arm is empty\n{emptyArmTestState.arm}')
    else:
        print(f'arm is not empty\n{emptyArmTestState.arm}')
    print('END OF testEmptyArm()\n\n\n')

def testBlock():
    print('testBlock():')
    blockA = block("a", 0, 0)
    blockB = block("b", 0, 1)
    blockC = block("c", 1, 0)
    L0 = [blockA, blockB]
    L1 = [blockC]
    arm = block('d', 2, -1)
    blockTestState = state(L0, L1, arm=arm)
    
    print(blockA)
    print(blockB)
    print(blockC)
    print('Block Comparison Operator Test:')
    if blockA == blockA: print("equals true pass")
    else: print("equals true fail")
    if blockA == blockB: print("equals false fail")
    else: print("equals false pass")
    if blockA != blockA: print("not-equals false fail")
    else: print("not-equals false pass")
    if blockA != blockB: print("not-equals true pass")
    else: print("not-equals true fail")
    
    print(f'Test State:{blockTestState}')
    print('END OF testBlock()\n\n\n')

def testBlockRelationships():
    print('testBlockRelationships():')
    blockA = block("a", 0, 0)
    blockB = block("b", 0, 1)
    blockC = block("c", 1, 0)
    blockD = block("d", 1, 1)
    L0 = [blockA, blockB]
    L1 = [blockC, blockD]
    arm = block('d', 2, -1)
    testState = state(L0, L1, arm=arm)
    # above tests
    print('ABOVE:')
    if blockA.above(blockB):
        print(f'blockA is above blockB')
    else:
        print(f'blockA is not above blockB')
    if blockD.above(blockA):
        print(f'blockD is above blockA')
    else:
        print(f'blockD is not above blockA')
    if blockB.above(blockA):
        print(f'blockB is above blockA')
    else:
        print(f'blockB is not above blockA')
    if blockA.above(location = L0):
        print(f'blockA is above L1')
    else: 
        print(f'blockA is not above L1')
    if blockA.above(location = 0):
        print(f'blockA is above L1(int)')
    else: 
        print(f'blockA is not above L1(int)')
    # on tests
    print('ON:')
    if blockA.on(blockB):
        print(f'blockA is on blockB')
    else:
        print(f'blockA is not no blockB')
    if blockB.on(blockA):
        print(f'blockB is on blockA')
    else:
        print(f'blockB is not on blockA')
    if blockA.on(blockA):
            print(f'blockA is on blockA')
    else:
        print(f'blockA is not on blockA')
    # clear tests
    print('CLEAR:')
    if blockA.clear(testState.locations[blockA.location]):
        print(f'blockA is clear')
    else:
        print(f'blockA is not clear')
    if blockB.clear(testState.locations[blockA.location]):
        print(f'blockB is clear')
    else:
        print(f'blockB is not clear')
    # table tests
    print('TABLE:')
    if blockA.table():
        print(f'blockA is on table')
    else:
        print(f'blockA is not on table')
    if blockB.table():
        print(f'blockB is on table')
    else:
        print(f'blockB is not on table')
    print(f'STATE:{testState}')
    print('END OF testBlockRelationships()\n\n\n')

def testMoveAction():
    print('testMoveAction():')
    blockA = block("a", 0, 0)
    blockB = block("b", 0, 1)
    blockC = block("c", 1, 0)
    L0 = [blockA, blockB]
    L1 = [blockC]
    arm = block('d', 2, -1)
    testState = state(L0, L1, arm=arm)
    print(f'STATE:{testState}')
    print('Move Test:')
    testState.move(0, 1)
    testState.move(0, 1 )
    testState.move(arm.location, 1)
    print(f'STATE:{testState}')
    print('END OF testMoveAction()\n\n\n')

def testPickUpAction():
    print('testPickupAction():')
    blockA = block("a", 0, 0)
    blockB = block("b", 0, 1)
    blockC = block("c", 1, 0)
    L0 = [blockA, blockB]
    L1 = [blockC]
    arm = block('d', 2, -1)
    testState = state(L0, L1, arm=arm)
    print(f'STATE:{testState}')
    testState.pickUp(blockA.location)
    testState.arm = block(location=1)
    print(f'STATE:{testState}')
    testState.pickUp(blockA.location)
    testState.arm = block(location=0)
    print(f'STATE:{testState}')
    testState.pickUp(blockA.location)
    testState.pickUp(blockB.location)
    print(f'STATE:{testState}')
    print('END OF testPickupAction()\n\n\n')

def testPutDownAction():
    print('testPutDownAction():')
    blockA = block("a", 0, 0)
    blockB = block("b", 0, 1)
    blockC = block("c", 1, 0)
    L0 = [blockA, blockB]
    L1 = [blockC]
    arm = block('d', 2, -1)
    testState = state(L0, L1, arm=arm)
    print(f'STATE:{testState}')
    testState.putDown(arm.location)
    print(f'STATE:{testState}')
    testState.move(2, 1)
    testState.pickUp(1)
    print(f'STATE:{testState}')
    testState.move(1, 2)
    testState.putDown(2)
    print(f'STATE:{testState}')
    print('END OF testPutDownAction()\n\n\n')

def testStackAction():
    print('testStackAction():')
    blockA = block("a", 0, 0)
    blockB = block("b", 0, 1)
    blockC = block("c", 1, 0)
    L0 = [blockA, blockB]
    L1 = [blockC]
    arm = block('d', 2, -1)
    testState = state(L0, L1, [], arm)
    print(f'STATE:{testState}')
    testState.move(2, 1)
    testState.stack(1)
    print(f'STATE:{testState}')
    
    print('END OF testStackAction()\n\n\n')

def testUnstackAction():
    print('testUnstackAction():')
    blockA = block("a", 0, 0)
    blockB = block("b", 0, 1)
    blockC = block("c", 1, 0)
    L0 = [blockA, blockB]
    L1 = [blockC]
    arm = block('d', 2, -1)
    testState = state(L0, L1, arm=arm)
    print(f'STATE:{testState}')
    testState.unstack(blockA.location)
    testState.arm = block(location=1)
    print(f'Cleared arm and moved to L1')
    testState.unstack(blockA.location)
    testState.arm = block(location=0)
    print(f'Cleared arm and moved to L0')
    print(f'STATE:{testState}')
    testState.unstack(blockA.location)
    print(f'STATE:{testState}')
    testState.unstack(blockB.location)
    testState.arm = block(location=1)
    testState.unstack(blockC.location)
    print('END OF testUnstackAction()\n\n\n')

def testNoopAction():
    print('testNOOPAction():')
    blockA = block("a", 0, 0)
    blockB = block("b", 0, 1)
    blockC = block("c", 1, 0)
    L0 = [blockA, blockB]
    L1 = [blockC]
    arm = block('d', 2, -1)
    testState = state(L0, L1, arm=arm)
    print(f'STATE:{testState}')
    testState.noop()
    print(f'STATE:{testState}')
    print('END OF testNOOPAction()\n\n\n')

# Global Functions
def buildLocation(Li: Optional[list[block]] = [], blocks: Optional[list[block]] = []) -> list[block]:
    location = Li
    for b in blocks:
        location.insert(b.position, b)
    return location

def printLocation(location: Optional[list[block]] = None, arm: Optional[block] = None):
    bar = ' | '
    emptySpace = '_'
    newLine = '\n'
    lineBuilder = ""
    lineBuilder += newLine
    if arm is not None:
        # check arm
        lineBuilder += f'{arm}' + newLine
        if arm.label is None:
            lineBuilder += f'--| |--' + newLine
        else:
            lineBuilder += f'--|{arm.label}|--' + newLine
    if location is not None:
        remainingLineCounter = np.size(location)
        if remainingLineCounter == 0:
            lineBuilder += f'This location is empty'
            lineBuilder += newLine
        # check block stacks
        while(remainingLineCounter > 0): # loop to print each line
            remainingLineCounter -= 1
            lineBuilder += bar
            if remainingLineCounter < np.size(location): # if the lineCounter is less than the number of elements at this location there is a block to print
                blockLabel = location[remainingLineCounter].label
                lineBuilder += blockLabel
            else: # if the lineCounter is greater than the number of elements at this location print a blank space 
                lineBuilder += emptySpace
            lineBuilder += bar
            lineBuilder += newLine
    if location is None and arm is None:
        lineBuilder += f'No location to print.'
    print(lineBuilder)

def stackLabels() -> str:
        labels = ' | L0| L1| L2| \n'
        return labels

def hDiff(start:state, end:state):
    # Heuristic Difference - this heuristic calculates the number of blocks that are currently not in the correct 'position'.
    cost = 0
    location = 0
    while location < 3:
        position = 0
        endHeight = np.size(end.locations[location])
        #print(f'Shorter: {shorter}')
        while position < endHeight:
            #print(f'Current location: {location}\nCurrent Position: {position}')
            try:
                if start.locations[location][position] != end.locations[location][position]:
                    #print(f'blocks are not equal. start:{start.locations[location][position]} end:{end.locations[location][position]}')
                    cost += 1
            except IndexError:
                cost += 1
            position += 1
        startHeight = np.size(start.locations[location])
        location += 1
    # if not start.isArmEmpty():
    #     cost += 2
    # if not end.isArmEmpty():
    #     cost += 1
    return cost

def getUserState() -> state:
    correct = 'n'
    while correct != 'y':
        stacks = [],[],[]
        i = 0
        for stack in stacks:
            blocks = input(f'Starting from the bottom, what blocks are in L{i}? (comma separate labels \'a, b, c\'):\n')
            blockLabels = blocks.split(",")
            pos = 0
            if blocks != '':
                for label in blockLabels:
                    #print(block(label,i,pos))
                    stack.append(block(label.strip(),i,pos))
                    pos += 1
                printLocation(stack)
            else:
                print("This stack is empty!")
            i += 1
            # end for
        armLabel = input('What block is in the arm?\n')
        arm = block()
        if armLabel != '':
            arm.label=armLabel
        armLocation = input('What is the location of the arm? (Pick One: 0, 1, 2)\n')
        arm.location=int(armLocation)
        userState = state(stacks[0], stacks[1], stacks[2], arm)
        print(f'{userState}')
        correct = input('Does this state look correct? (y/n)\n')
        # end while
    return userState

def run(start:state, end:state):
    while (start != end):
        do(start, end)
        pass

def do(currentState:state, endState:state):
    bufferState = currentState.build(currentState)
    i = 0
    shortest = bufferState.findShortestStack()
    tallest = bufferState.findTallestStack()
    middle = 0
    i = 1
    while i < 3:
        if middle == shortest or middle == tallest:
            middle += 1
        i += 1
    # end while
    print(f's:{shortest}m:{middle}t:{tallest}')
    
    if np.size(bufferState.locations[shortest]) != 0:
        pass
    
    while i < 3:
        if bufferState.pickUp(i):
            print(f'current to end ({i}): {hDiff(currentState, endState)}')
            print(f'buffer to end ({i}): {hDiff(bufferState, endState)}')
        elif bufferState.putDown(i):
            print(f'current to end ({i}): {hDiff(currentState, endState)}')
            print(f'buffer to end ({i}): {hDiff(bufferState, endState)}')
        i += 1
        
    # end while
    

# Main
# defaultStateTester = buildDefaultState()
# testDefaultState(defaultStateTester)
# testBuildState()
# testPrintLocation()
# testEmptyArm()
# testBlock()
# testStateComparitors()
# testBlockRelationships()
# testMoveAction()
# testPickUpAction()
# testPutDownAction()
# testStackAction()
# testUnstackAction()
# testNoopAction()


print('Enter Starting State:')
# s1 = state(L1=[block("a", 0, 0), block("b", 0, 1)], L2=[block("c", 1, 0)], arm=block('d', 2, -1))
s1 = getUserState()
print('\nStart State Accepted.\n\nEnter Ending State:')
s2 = getUserState()
# s2 = state(L1=[block("d", 0, 0), block("c", 0, 1)], L2=[block("b", 1, 0)], L3=[block("a", 2, 0)], arm=block(None, 1, -1))
print(f'\n\n\n\nStart State:{s1}\nEnd State:{s2}')
# s3 = state(L1=[block("d", 0, 0), block("c", 0, 1),block("a", 2, 0)], L2=[block("b", 1, 0)], L3=[], arm=block(None, 1, -1))
# print(f'Third State:{s3}')

print("Cost 1 to 2:",hDiff(s1, s2))
print("Cost 2 to 1:",hDiff(s2, s1))
# print("Cost 1 to 3:",hDiff(s1, s3))
# print("Cost 2 to 3:",hDiff(s2, s3))
# print("Cost 3 to 2:",hDiff(s3, s2))
# print("Cost 3 to 3:",hDiff(s3, s3))

#run(s1, s2)