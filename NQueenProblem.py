"""
Problem Name : Nqueen Puzzle.
Description : Try to create a backtacking recursive problem to place the Queen such a way that no other queens in the 
different rows can kill each other.This is generic code and can solve any N*N dimensions.
Version : Python 3.7.1
Code developed by : Manish Singh 
Date : 07/01/2020
Time space calculation : NA
""" 
    
"""creating a class and defining all the functions underneath it for object oriented """

class Nqueenproblem:

    def __init__(self,size):
     # initlization of the size of the problem and also calling the solve function.
        self.size= size
        print("Problem size is :",self.size)
        self.possiblity =0 
        self.solution()


    def solution(self):
        # creating a default list with -1 and calling the placeQueen function.
        positionlist = self.size* [-1] 
        self.placeQueen(positionlist,0)
        print("Number of solutions found is: " ,self.possiblity)   

    def placeQueen(self,positionlist,chessrow):
        # This is important backtrack recursive function and It will run in the loop until the safe poistion of queen determine.

        if chessrow == self.size:
            print(positionlist)
            self.possiblity += 1
        else:
            for chesscolumn in range(self.size):

                if self.safePlace(positionlist,chessrow,chesscolumn):
                    positionlist[chessrow]=chesscolumn
                    self.placeQueen(positionlist,chessrow + 1)

    def safePlace(self,positionlist,chessrow,chesscolumn):
        #This function is chekcing the safest position of the queen by checking in same column and left and right diagonals.
        for loop in range(chessrow):
            if positionlist[loop]==chesscolumn or \
                positionlist[loop] - loop == chesscolumn - chessrow or \
                positionlist[loop] + loop == chessrow + chesscolumn :
                return False

        return True            
        
def main():
    # calling the class with intilization and passing the argumennt.
    Nqueenproblem(8)

if __name__ == "__main__":
    main()


