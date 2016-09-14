import datetime 
import random
import time

class ClearableList:
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

    # Write an XML file with the results
    file = open("ListAccessTiming.xml","w")

    file.write('<?xml version="1.0" encoding="UTF-8" standalone="no" ?>\n')

    file.write('<Plot title=" List Element Append Time">\n')
        
    xmin = 500
    xmax = 100000    
    
    file.write('  <Axes>\n')
    file.write('    <XAxis min="'+str(xmin)+'" max="'+str(xmax)+'">List Size</XAxis>\n')
    file.write('    <YAxis min="'+str(0)+'" max="'+str(0.1)+'">Microseconds</YAxis>\n')
    file.write('  </Axes>\n')
    

    
    
    

    
    def clearableListAppendTime(size,xmax,xmin,color):
        #file.write('  <Sequence title="Access Time Distribution" color="blue">\n') 
        file.write('  <Sequence title="Append time for list of size '+str(size)+'" color="'+str(color)+'">\n')
        
        clearableList = ClearableList(size)
        
        # Record the list sizes in xList and the append time within
        # a list that size in yList for 100000 appends
        
        xList = []
        yList = []
        for x in range(xmin,xmax,1000):
            xList.append(x)
            
            starttime = datetime.datetime.now()
            clearableList.append(x)
            endtime = datetime.datetime.now()
            deltaT = endtime - starttime
            
            # Divide by 1000 for the average access time
            # But also multiply by 1000000 for microseconds.
            accessTime = deltaT.total_seconds() * 1000
    
            yList.append(accessTime)
            
            for i in range(len(xList)):   
                file.write('    <DataPoint x="'+str(xList[i])+'" y="'+str(yList[i])+'"/>\n')    
        
        file.write('  </Sequence>\n')
        
        
        
        
    clearableListAppendTime(100, xmax, xmin, "red")
    clearableListAppendTime(1000, xmax, xmin, "green")
    clearableListAppendTime(10000,xmax,xmin, "blue")
    file.write('</Plot>\n')
    file.close()

if __name__ == "__main__":
    main()