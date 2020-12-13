import numpy as np

def show(a):
	#функция вывода на экран матрицы 9 на 9
	for i in range(len(a)):
		if(i==0):
			print("<----------------------->")
		if(i%3==0 and i!=0):
			print("|-------|-------|-------|")
		print("|",a[i][0],a[i][1],a[i][2],"|",a[i][3],a[i][4],a[i][5],"|",a[i][6],a[i][7],a[i][8],"|")
	print("<----------------------->\n")

def update_q(q,b):
	#обновляет матрицу достижимости меток, 1 если поле еще не заполнено, 0 если заполнено
	for i in range(9):
		for j in range(9):
			if(b[i][j]==0):
				q[i][j]=1
			else:
				q[i][j]=0
	return q
def neighbor(i,j):
	#функция соседства, выдает индексы соседей с элементом i,j
	a=np.zeros((9,9),int)
	for k in range(9):
		for l in range(9):
			if(k==i or l==j):
				a[k][l]=1
	if(i%3==0 and j%3==0):
		a[i][j]=a[i][j+1]=a[i][j+2]=a[i+1][j]=a[i+1][j+1]=a[i+1][j+2]=a[i+2][j]=a[i+2][j+1]=a[i+2][j+2]=1
	if(i%3==0 and j%3==1):
		a[i][j]=a[i][j+1]=a[i][j-1]=a[i+1][j]=a[i+1][j+1]=a[i+1][j-1]=a[i+2][j]=a[i+2][j+1]=a[i+2][j-1]=1
	if(i%3==0 and j%3==2):
		a[i][j]=a[i][j-1]=a[i][j-2]=a[i+1][j]=a[i+1][j-1]=a[i+1][j-2]=a[i+2][j]=a[i+2][j-1]=a[i+2][j-2]=1
	if(i%3==1 and j%3==0):
		a[i][j]=a[i][j+1]=a[i][j+2]=a[i+1][j]=a[i+1][j+1]=a[i+1][j+2]=a[i-1][j]=a[i-1][j+1]=a[i-1][j+2]=1
	if(i%3==1 and j%3==1):
		a[i][j]=a[i][j+1]=a[i][j-1]=a[i+1][j]=a[i+1][j+1]=a[i+1][j-1]=a[i-1][j]=a[i-1][j+1]=a[i-1][j-1]=1
	if(i%3==1 and j%3==2):
		a[i][j]=a[i][j-1]=a[i][j-2]=a[i-1][j]=a[i-1][j-1]=a[i-1][j-2]=a[i+1][j]=a[i+1][j-1]=a[i+1][j-2]=1
	if(i%3==2 and j%3==0):
		a[i][j]=a[i][j+1]=a[i][j+2]=a[i-2][j]=a[i-2][j+1]=a[i-2][j+2]=a[i-1][j]=a[i-1][j+1]=a[i-1][j+2]=1
	if(i%3==2 and j%3==1):
		a[i][j]=a[i][j+1]=a[i][j-1]=a[i-2][j]=a[i-2][j+1]=a[i-2][j-1]=a[i-1][j]=a[i-1][j+1]=a[i-1][j-1]=1
	if(i%3==2 and j%3==2):
		a[i][j]=a[i][j-1]=a[i][j-2]=a[i-1][j]=a[i-1][j-1]=a[i-1][j-2]=a[i-2][j]=a[i-2][j-1]=a[i-2][j-2]=1
	return a



def g(board,q,g):

	for i in len(board):
		for j in len(board[i]):
			i=0
	return 0

board=np.array([
    [5, 3, 0,    0, 7, 0,    0, 0, 0],
    [6, 0, 0,    1, 9, 5,    0, 0, 0],
    [0, 9, 8,    0, 0, 0,    0, 6, 0],

    [8, 0, 0,    0, 6, 0,    0, 0, 3],
    [4, 0, 0,    8, 0, 3,    0, 0, 1],
    [7, 0, 0,    0, 2, 0,    0, 0, 6],

    [0, 6, 0,    0, 0, 0,    2, 8, 0],
    [0, 0, 0,    4, 1, 9,    0, 0, 5],
    [0, 0, 0,    0, 8, 0,    0, 7, 9]
])
q=np.ones((9,9),int)
g=np.ones((9,9,9,9),int)
show(board)
q=update_q(q,board)
show(q)
#show(g)
show(neighbor(3,5))