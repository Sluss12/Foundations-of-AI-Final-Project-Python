class block:
    def __init__(self):
        self.location = -1
        self.position = -1
    
    # Block RELATIONSHIPS
    def above(self, block B): # returns true if block self is above block B
        pass
    
    def above(self, location Li): # returns true if block self is above location Li
        pass
    
    def on(self, block B):# returns true if block self is on block B
        pass
    
    def clear(self):# returns true if block self has no block on self
        pass
    
    def table(self): # return true if block self is on the table (pos 0 in stack)
        pass

class state:
    def __init__(self):
        L1 = []
        L2 = []
        L3 = []
        self.locations = [L1, L2, L3]
    
    # State Actions
    def build(self, L1, L2, L3):
        self.locations[0] = L1
        self.locations[1] = L2
        self.locations[3] = L3
        
    
    # Block Actions
    def pickUp(self, block Li, location loc):
        pass
    
    def putDown(self, block Li, location loc):
        pass
    
    def stack(self, block Li, location loc):
        pass
    
    def unstack(self, block Li, location loc):
        pass
    
    def move(self, block Li, location start, location end):
        pass