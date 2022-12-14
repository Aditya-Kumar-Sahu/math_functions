"""
Program to perform Gaussian Elemination on given "m x n" matrix/verter and convert in into its row echelon form.
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
                    self.matrix[i][j]=float(input("Enter {:d}-{:d}th element: ".format(i+1, j+1)))
        except:
            print("Please enter correct values")
            print()
            self.input_matrix()
        finally:
            print()

    def display_marix(self):
        """
        A utility function to display matrix
        ----------
        Return Type: None
        """
        print("--" + " "*(7*self.n-2) + "--")
        for i in range(self.m):
            print("|", end="")
            for j in range(self.n):
                print(" {:^5s} ".format(str(round(self.matrix[i][j], 2))), end="")
            print("|")
        print("--" + " "*(7*self.n-2) + "--")
        print()


    def divide(self, row, num):
        """
        function to divide an row by given number
        ----------
        Parameters-
        row: the row of matrix
        num: number to divide with
        ----------
        Return Type: None
        """
        for j in range(self.n):
            self.matrix[row-1][j]=self.matrix[row-1][j]/num

    def type1(self, row):
        """
        row operation type 1
        ----------
        Parameters:-
        row: row in which row operation is to be applied
        ----------
        Return Type: None
        """
        for j in range(self.n):
            if(self.matrix[row-1][j]!=0):
                self.divide(row, self.matrix[row-1][j])
                break

    def type2(self, row1, row2, coeff):
        """
        type 2 row operation
        ----------
        Paramaters:-
        row1: row in which operation is being applied
        row2: row of which multiple is used
        coeff: float value coeficient for multiple of row2
        ----------
        Return Type: None
        """
        for j in range(self.n):
            self.matrix[row1-1][j]=self.matrix[row1-1][j] + self.matrix[row2-1][j]*coeff

    def row_echlon(self):
        """
        function for converting matrix to its row echelon form
        ---------
        Return Type: None
        """
        for i in range(self.m):
            self.type1(i+1)
            for k in range(i+1, self.m):
                coeff=0
                for j in range(self.n):
                    if self.matrix[k][j]!=0:
                        coeff=self.matrix[k][j]
                        break
                if coeff!=0:
                    self.type2(k+1, i+1, -coeff)

if __name__ == '__main__':
    matrix=Gaussian()
    matrix.create_matrix()
    matrix.input_matrix()
    print("Given matrix:-")
    matrix.display_marix()
    matrix.row_echlon()
    print("Matrix in row ehelon form:-")
    matrix.display_marix()
