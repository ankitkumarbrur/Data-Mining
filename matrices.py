class Matrix :

    def __init__(self,m,n):
        self.n = n
        self.m = m
        self.mat = []


    def input_matrix(self):
        for i in range(self.m):
            row = []
            for j in range(self.n):
                row.append(int(input("Enter matrix element :")))
            self.mat.append(row)

    def print_matrix(self):
        print("\nResultant Matrix :\n")
        for i in range(self.m):
            print(self.mat[i])
        # print(*self.mat)

    def add_matrix(self,mat2):
        res = Matrix(self.m,self.n)
        if self.m != mat2.m or self.n != mat2.n :
            print("Matrices can't be added!!")
        for i in range(self.m):
            temp = []
            for j in range(self.n):
                print(self.mat[i][j])
                print(mat2.mat[i][j])
                res1=self.mat[i][j] + mat2.mat[i][j]
                print(res1)
                temp.append(res1)
            res.mat.append(temp)
        return res
                

def main():
    g=-1
    while g!=0 :
        print("\n\nMenu:\n\n0.exit\n1.Add two matrices\n3.Subtract two matrices\n4.Multiply two matrices\n4.Transpose a matrix")
        g=int(input("Enter your response :"))

        if g == 1:
            m=int(input("\nEnter number of rows :"))
            n=int(input("\nEnter number of cols :"))
            mat1 = Matrix(m,n)
            mat2 = Matrix(m,n)

            print("\n\nEnter First matrix")
            mat1.input_matrix()
            print("\n\nEnter second matrix")
            mat2.input_matrix()

            result = mat1.add_matrix(mat2)

            result.print_matrix()
            # print(*result.mat)

main()