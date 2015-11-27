__author__ = 'student'
class Matrix:
    def __init__(self,a,b=None):
        self._arr=[]
        if type(a) is list:
            self.m=len(a)
            if type(a[0]) is list:
                self.n=len(a[0])
            else:
                self.n=1
            for i in range(m):
                self._arr.append([])
                for j in range(n):
                    self._arr.append(a[i][j])
        else:
            if type(a) is tuple:
               (self.m,self.n)=a
            else:
                if not (type(a) is int and type(b) is int):
                    raise ValueError('Dimension is not int')
                self.m=a
                self.n=b
            if self.m<1 or self.n<1:
                raise ValueError('Dimension is invalid')
            for i in range(self.m):
                self._arr.append([])
                for j in range(self.n):
                    self._arr[i].append(0)

    def get_m(self):
        return self.m
    def get_n(self):
        return self.n
    def get_size(self):
        return (self.m,self.n)
    def get(self,i,j):
        return self._arr[i][j]
    def set(self,i,j,x):
        self._arr[i][j]=x

    def __eq__(self, other):
        result = True
        for i in range(self.m):
            for j in range(self.n):
                if self.get(i,j) != other.get(i,j):
                    result = False
                    break
            if result==False:
                break
        return result

    def __add__(self, other):
        A=Matrix(self.get_size())
        for i in range(self.m):
            for j in range(self.n):
                A.set(i, j, self.get(i,j)+other.get(i,j))
        return A
    def __sub__(self, other):
        A=Matrix(self.get_size())
        for i in range(self.m):
            for j in range(self.n):
                A.set(i, j, self.get(i,j)-other.get(i,j))
        return A

    def __mul__(self, other):
        if type(other) is int or type(other) is float: # умн матрицы на число
            A=Matrix(self.get_size())
            for i in range(self.m):
                for j in range(self.n):
                    A.set(i, j, self.get(i,j)*other)
            return A
        else: # умножение матриц
            if type(other) is Matrix:
                A=Matrix(self.get_m(),other.get_n())
                for i in range(self.m):
                    for j in range(other.get_n()):
                        tmp=0
                        for r in range(self.n):
                            tmp+=self.get(i,r)*other.get(r,j)
                        A.set(i,j,tmp)
                return A

    def __truediv__(self, other):
        A=Matrix(self.get_size())
        for i in range(self.m):
            for j in range(self.n):
                A.set(i, j, self.get(i,j)/other)
        return A


    def transpose(self):
        A=Matrix(self.get_n(),self.get_m())
        for i in range(self.m):
            for j in range(self.n):
                A.set(j,i,self.get(i,j))
        return A
    def determinant(self):
        '''
        рекурсивно вычисляем определитель
        '''
        if len(self._arr)==1:
           # для простоты считаем что мартрица квадратная
            return self._arr[0][0]
        elif len(self._arr)==2:
            return self._arr[0][0]*self._arr[1][1]-self._arr[0][1]*self._arr[1][0]
        else:
            result=0
            for i in range(len(self._arr[0])):
                A=self._arr.copy()
                A.pop(0) # вычеркиваем первую строку
                for j in range(len(A)): # вычеркиваем i столбец
                    A[0].pop(j)
                result+=self._arr[0][i]*(-1)**(i)*Matrix(A).determinant()
            return result

    def invert(self):
        pass
    #FIXME
        # заменить каждый элемент на алгебраическое дополнение
        A=Matrix(self.get_n(),self.get_m())
#        for i in range(self.m):
#            for j in range(self.n):

        # транспонировать порученную матрицу
        # разделить матрицу на число - определитель исходной матрицы






