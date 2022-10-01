"""
Program to perform Gaussian Elemination on given "m x n" matrix/verter.
"""
class Gaussian:
    def __init__(self):
        self.m=None
        self.n=None
        self.matrix=list()

    def create_matrix(self) -> None:
        """
        utility function to create matrix of size m x n
        ----------
        Return Type: List
        """
        print("Enter the dimensions of the matrix:-")
        try:
            self.m= int(input("Enter number of rows(m): "))
            self.n= int(input("Enter number of columns(n): "))
            self.matrix= [[0 for i in range(self.n)] for j in range(self.m)]

        except:
            print("Please enter correct values")
            print()
            return self.create_matrix()

    def input_matrix(self):
        """
        utility function to take values of matrix
        ------
        Return Type: None
        """
        try:
            for i in range(self.m):
                for j in range(self.n):
                    self.matrix[i][j]=int(input("Enter {:d}-{:d}th element: ".format(i+1, j+1)))
        except:
            print("Please enter correct values")
            print()
            self.input_matrix()

    def display_marix(self):
        print()
        for row in self.matrix:
            print(row)

if __name__ == '__main__':
    matrix=Gaussian()
    matrix.create_matrix()
    matrix.input_matrix()
    matrix.display_marix()