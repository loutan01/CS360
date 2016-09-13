class clearableList:
    def __init__(self,size):
        self.size = size
        self.items = [None] * self.size
        self.count = 0
    
    def append(self,item):
        if self.count == len(self.items):
            self.items = [None] * self.size
            self.count = 0
        else:
            self.items[self.count] = item
            self.count +=1
    
    def __getitem__(self,item):
        if item in self.items:
            return True
        else:
            return None or False
def main():
    
    clearableTest = clearableList(10)
    
    for count in clearableTest:
        clearableTest.append(count)
        test = clearableTest[count]
        #print(type(test))
        #print(test)

        
if __name__ == "__main__":
    main()     