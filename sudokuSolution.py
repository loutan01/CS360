from hashSet import HashSet

def sudokuSolver(file):
    rawPuzzle = open(file, 'r')
   
    
    sudokuMatrix = [[None for x in range(9)] for y in range(9)]

    
    lineCount = 0
    for line in rawPuzzle:
        rawInput = line.split()
        valueCount = 0
        
        for value in rawInput:
                        
            if value == 'x':                
                sudokuMatrix[lineCount][valueCount] = HashSet().add(x for x in range(1,10))
            else:
                sudokuMatrix[lineCount][valueCount] = HashSet().add(value)
                
    
            valueCount +=1
            
            
        lineCount += 1
        
        print(sudokuMatrix[0][1])
 
    
def main():
    sudokuSolver('sudoku1.txt')




if __name__ == "__main__":
    main()
