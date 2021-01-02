from itertools import product


def solve_sudoku(puzzle):
    for (row ,col) in product(range(0,9), repeat =2):
        if puzzle[row][col] == 0:# find an unassined cell
            for num in range (1,10) :
                allowed =True # check if number is alloed in row/col/box
                for i in range (0,9):
                    if (puzzle[i][col] == num) or (puzzle[row][i] == num):
                        allowed = False ; break
                for(i,j) in product(range(0,3) , repeat =2):
                    if puzzle[row-row%3+i][col-col%3+j] == num:
                        allowed= False ;break

                if allowed :
                    puzzle[row][col]= num
                    if trial := solve_sudoku(puzzle) :
                        return trial
                    else :
                        puzzle[row][col ] = 0
            return False #cold not place a number
    return puzzle
                
def print_sudoku(puzzle):
    #replace zeros ith dashes
    puzzle= [['*' if num == 0 else num for num in row]for row in puzzle ]
    print()
    for row in range(0,9):
        if((row % 3 == 0) and (row !=0)):
            print('-'*33)#draw horizental line
        for col in range (0,9):
            if((col % 3 == 0)and (col!= 0)):
                print('|', end ='')#dra vertical ligne
            print('',puzzle[row][col],'', end='')
        print()
    print()
            
            

puzzle=[[8, 1, 0, 0, 3, 0, 0, 2, 7], 
        [0, 6, 2, 0, 5, 0, 0, 9, 0], 
        [0, 7, 0, 0, 0, 0, 0, 0, 0], 
        [0, 9, 0, 6, 0, 0, 1, 0, 0], 
        [1, 0, 0, 0, 2, 0, 0, 0, 4], 
        [0, 0, 8, 0, 0, 5, 0, 7, 0], 
        [0, 0, 0, 0, 0, 0, 0, 8, 0], 
        [0, 2, 0, 0, 1, 0, 7, 5, 0], 
        [3, 8, 0, 0, 7, 0, 0, 4, 2]]

print_sudoku(puzzle)

print_sudoku(solve_sudoku(puzzle))

