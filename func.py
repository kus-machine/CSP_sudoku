import numpy as np
import doctest

#функция вывода на экран матрицы 9 на 9
def show(a):
	a=a.tolist()
	for i in range(9):
		for j in range(9):
			if(a[i][j]==0):
				a[i][j]=' '
	for i in range(len(a)):
		if(i==0):
			print("<----------------------->")
		if(i%3==0 and i!=0):
			print("|-------|-------|-------|")
		print("|",a[i][0],a[i][1],a[i][2],"|",a[i][3],a[i][4],a[i][5],"|",a[i][6],a[i][7],a[i][8],"|")
	print("<----------------------->\n")

#функция соседства, выдает матрицу, еденицы в которой - соседи с элементом i,j
def neighbor(i,j):
	'''
	функция соседства, выдает матрицу, еденицы в которой - соседи с элементом i,j
	>>> neighbor(0,0)
	array([[1, 1, 1, 1, 1, 1, 1, 1, 1],
	       [1, 1, 1, 0, 0, 0, 0, 0, 0],
	       [1, 1, 1, 0, 0, 0, 0, 0, 0],
	       [1, 0, 0, 0, 0, 0, 0, 0, 0],
	       [1, 0, 0, 0, 0, 0, 0, 0, 0],
	       [1, 0, 0, 0, 0, 0, 0, 0, 0],
	       [1, 0, 0, 0, 0, 0, 0, 0, 0],
	       [1, 0, 0, 0, 0, 0, 0, 0, 0],
	       [1, 0, 0, 0, 0, 0, 0, 0, 0]])
	'''
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

#создает функцию q
def create_q(board):
	q=np.ones((9,9,9),int)
	#все qt(k) где k - заполнено - ставим в 0 (кроме заполненного)
	for i in range(9):
		for j in range(9):
			if(board[i][j]!=0):
				for l in range(9):
					if(board[i][j]-1!=l):
						q[i][j][l]=0
	return q
#возвращает 0 если задача НЕрешаема
def sertif(q):
	flag=1
	#фиксируем объект(клетку)
	for i in range(9):
		for j in range(9):
			sosedi=neighbor(i,j)
			#по всем соседям этого объекта (кроме него самого)
			for i1 in range(9):
				for j1 in range(9):

					if(sosedi[i1][j1]==1 and (i!=i1 or j!=j1)):
						#по всем ненулевым меткам фикс объекта:
						flag1=0
						for l in range(9):
							#по всем меткам соседей фикс объекта:
							for l1 in range(9):
								if(l!=l1 and q[i][j][l]*q[i1][j1][l1]==1):
									flag1=1
						flag*=flag1
	return flag

#создает функцию q
def create_q(board):
	q=np.ones((9,9,9),int)
	#все qt(k) где k - заполнено - ставим в 0 (кроме заполненного)
	for i in range(9):
		for j in range(9):
			if(board[i][j]!=0):
				for l in range(9):
					if(board[i][j]-1!=l):
						q[i][j][l]=0
	return q
#алгоритм вычеркивания
def update_q(q):
	#фиксируем элемент с доски
	for i in range(9):
		for j in range(9):
			#находим для него всех соседей
			sosed=neighbor(i,j)
			#проходимся по всем незаполненным соседям для фиксированого выше элемента и деактивируем у них метки с числом как у фиксированного выше элемента
			if(q[i][j].sum()==1):
				for i2 in range(9):
					for j2 in range(9):
						if(sosed[i2][j2]==1 and q[i2][j2].sum()>1):
							q[i2][j2][int(np.nonzero(q[i][j])[0])]=0
	return q

def solve(board):
	print("Condition:")
	show(board)
	q=create_q(board)
	q=update_q(q)
	it=0
	while(True):
		if(sertif(q)):
			print("Iteration ",it)
			print("Sertificate is 1")
			q1=q+1
			q2=q1-1
			q=update_q(q)
			for i in range(9):
				for j in range(9):
					if(q[i][j].sum()==1):
						board[i][j]=int(np.nonzero(q[i][j])[0])+1
			show(board)
			it+=1
			if(np.array_equal(q2,q)):
				print("q({0})=q({1})".format(it,it-1))
				#show(board)
				break
		else:
			print("Sertificate is 0")
			break
#doctest.testmod()