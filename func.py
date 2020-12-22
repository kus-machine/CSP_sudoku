import numpy as np
import doctest

#функция вывода на экран матрицы 9 на 9
def show(a):
	'''
	>>> show(1)
	False

	>>> show(np.ones((9,9),int))
	<----------------------->
	| 1 1 1 | 1 1 1 | 1 1 1 |
	| 1 1 1 | 1 1 1 | 1 1 1 |
	| 1 1 1 | 1 1 1 | 1 1 1 |
	|-------|-------|-------|
	| 1 1 1 | 1 1 1 | 1 1 1 |
	| 1 1 1 | 1 1 1 | 1 1 1 |
	| 1 1 1 | 1 1 1 | 1 1 1 |
	|-------|-------|-------|
	| 1 1 1 | 1 1 1 | 1 1 1 |
	| 1 1 1 | 1 1 1 | 1 1 1 |
	| 1 1 1 | 1 1 1 | 1 1 1 |
	<----------------------->
	<BLANKLINE>
	True

	'''
	if(np.shape(a)!=(9,9)):
		return False
	else:
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
		return True

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

#возвращает 0 если задача НЕрешаема
def check(q):
	'''
	give a wrong board:
	>>> a=np.zeros((9,9),int)
	>>> a[0]=np.array([1,2,3,4,5,6,7,8,0])
	>>> a[1]=np.array([0,0,0,0,0,0,0,0,9])
	>>> check(update_q(create_q(a)))
	0

	give a good board:
	>>> a=np.array([[4,2,6,8,1,9,5,7,3],[9,8,3,5,7,4,2,1,6],[5,1,7,2,3,6,4,8,9],[1,5,8,3,4,2,9,6,7],[7,4,2,9,6,8,1,3,5],[3,6,9,7,5,1,8,4,2],[2,7,4,6,8,5,3,9,1],[8,3,5,1,9,7,6,2,4],[6,9,1,4,2,3,7,5,0]])
	>>> check(update_q(create_q(a)))
	1

	'''
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
	'''
	full filled board:
	>>> a=np.array([[4,2,6,8,1,9,5,7,3],[9,8,3,5,7,4,2,1,6],[5,1,7,2,3,6,4,8,9],[1,5,8,3,4,2,9,6,7],[7,4,2,9,6,8,1,3,5],[3,6,9,7,5,1,8,4,2],[2,7,4,6,8,5,3,9,1],[8,3,5,1,9,7,6,2,4],[6,9,1,4,2,3,7,5,8]])
	>>> create_q(a).sum()
	81
	>>> create_q(a)[0][0]
	array([0, 0, 0, 1, 0, 0, 0, 0, 0])
	
	enpty board:
	>>> b=np.zeros((9,9),int)
	>>> create_q(b).sum()
	729

	fill one gate:
	>>> b[0]=np.array([1, 0, 0, 0 , 0, 0, 0, 0, 0])
	>>> create_q(b).sum()
	721
	>>> create_q(b)[0][0]
	array([1, 0, 0, 0, 0, 0, 0, 0, 0])
	>>> create_q(b)[0][1]
	array([1, 1, 1, 1, 1, 1, 1, 1, 1])
	'''
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
	'''
	>>> a=np.zeros((9,9),int)
	>>> a[0]=np.array([1,0,0,0,0,0,0,0,0])
	>>> create_q(a)[0]
	array([[1, 0, 0, 0, 0, 0, 0, 0, 0],
	       [1, 1, 1, 1, 1, 1, 1, 1, 1],
	       [1, 1, 1, 1, 1, 1, 1, 1, 1],
	       [1, 1, 1, 1, 1, 1, 1, 1, 1],
	       [1, 1, 1, 1, 1, 1, 1, 1, 1],
	       [1, 1, 1, 1, 1, 1, 1, 1, 1],
	       [1, 1, 1, 1, 1, 1, 1, 1, 1],
	       [1, 1, 1, 1, 1, 1, 1, 1, 1],
	       [1, 1, 1, 1, 1, 1, 1, 1, 1]])
	>>> update_q(create_q(a))[0]
	array([[1, 0, 0, 0, 0, 0, 0, 0, 0],
	       [0, 1, 1, 1, 1, 1, 1, 1, 1],
	       [0, 1, 1, 1, 1, 1, 1, 1, 1],
	       [0, 1, 1, 1, 1, 1, 1, 1, 1],
	       [0, 1, 1, 1, 1, 1, 1, 1, 1],
	       [0, 1, 1, 1, 1, 1, 1, 1, 1],
	       [0, 1, 1, 1, 1, 1, 1, 1, 1],
	       [0, 1, 1, 1, 1, 1, 1, 1, 1],
	       [0, 1, 1, 1, 1, 1, 1, 1, 1]])
	'''
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

#делает доступную  доску из q
def make_board(q):
	'''
	lets give almost empty q, just 2 elements can be uniquely defined (0,0) - 1,  and (0,2) - 6
	>>> q=np.ones((9,9,9),int)
	>>> q[0][0]=np.array([1, 0, 0, 0, 0, 0, 0, 0, 0])
	>>> q[0][2]=np.array([0, 0, 0, 0, 0, 1, 0, 0, 0])
	>>> q[1][1]=np.array([1, 1, 1, 1, 0, 0, 0, 0, 0])
	>>> make_board(q)[0]
	array([1, 0, 6, 0, 0, 0, 0, 0, 0])
	>>> make_board(q)[1]
	array([0, 0, 0, 0, 0, 0, 0, 0, 0])
	>>> make_board(q)[5]
	array([0, 0, 0, 0, 0, 0, 0, 0, 0])
	'''
	board=np.zeros((9,9),int)
	for i in range(9):
		for j in range(9):
			if(q[i][j].sum()==1):
				board[i][j]=int(np.nonzero(q[i][j])[0])+1
	return board

#подфункция решения с запоминанием разметки
def pod_solve(board):
	q=create_q(board)
	q=update_q(q)
	for i in range(9):
		for j in range(9):
			if(q[i][j].sum()>1):
				q_temp=q[i][j]
				for k in range(9):
					if(q[i][j][k]==1):
						for l in range(9):
							if(l!=k):
								q[i][j][l]=0
							else:
								temp_k=l
				board=make_board(q)
				if(solve(board)):
					return board
					break
				else:
					q[i][j]=q_temp
					q[i][j][temp_k]=0
					continue
	return board

#основная функция, алгоритм решения
def solve(board):
	'''
	>>> a=np.array([[4,2,6,8,1,9,5,7,3],[9,8,3,5,7,4,2,1,6],[5,1,7,2,3,6,4,8,9],[1,5,8,3,4,2,9,6,7],[7,4,2,9,6,8,1,3,5],[3,6,9,7,5,1,8,4,2],[2,7,4,6,8,5,3,9,1],[8,3,5,1,9,7,6,2,4],[6,9,1,4,2,3,7,5,8]])
	>>> print(solve(a))
	Condition:
	<----------------------->
	| 4 2 6 | 8 1 9 | 5 7 3 |
	| 9 8 3 | 5 7 4 | 2 1 6 |
	| 5 1 7 | 2 3 6 | 4 8 9 |
	|-------|-------|-------|
	| 1 5 8 | 3 4 2 | 9 6 7 |
	| 7 4 2 | 9 6 8 | 1 3 5 |
	| 3 6 9 | 7 5 1 | 8 4 2 |
	|-------|-------|-------|
	| 2 7 4 | 6 8 5 | 3 9 1 |
	| 8 3 5 | 1 9 7 | 6 2 4 |
	| 6 9 1 | 4 2 3 | 7 5 8 |
	<----------------------->
	<BLANKLINE>
	SOLVED!
	<----------------------->
	| 4 2 6 | 8 1 9 | 5 7 3 |
	| 9 8 3 | 5 7 4 | 2 1 6 |
	| 5 1 7 | 2 3 6 | 4 8 9 |
	|-------|-------|-------|
	| 1 5 8 | 3 4 2 | 9 6 7 |
	| 7 4 2 | 9 6 8 | 1 3 5 |
	| 3 6 9 | 7 5 1 | 8 4 2 |
	|-------|-------|-------|
	| 2 7 4 | 6 8 5 | 3 9 1 |
	| 8 3 5 | 1 9 7 | 6 2 4 |
	| 6 9 1 | 4 2 3 | 7 5 8 |
	<----------------------->
	<BLANKLINE>
	True
	
	lets give a bad board:
	>>> a=np.zeros((9,9),int)
	>>> a[0]=np.array([1,0,0,0,0,0,0,0,0])
	>>> a[1]=np.array([0,1,0,0,0,0,0,0,0])
	>>> solve(a)
	Condition:
	<----------------------->
	| 1     |       |       |
	|   1   |       |       |
	|       |       |       |
	|-------|-------|-------|
	|       |       |       |
	|       |       |       |
	|       |       |       |
	|-------|-------|-------|
	|       |       |       |
	|       |       |       |
	|       |       |       |
	<----------------------->
	<BLANKLINE>
	Check is BAD
	False
	
	'''
	print("Condition:")
	show(board)
	q=create_q(board)
	it=1
	solved=False
	while(True):
		if(q.sum()!=81):
			if(check(q)):
				print("Iteration ",it)
				q1=q+1
				q2=q1-1
				q=update_q(q)
				board=make_board(q)
				show(board)
				it+=1
				if(np.array_equal(q2,q)):
					print("q({0})=q({1})".format(it,it-1))
					if(solved==False):
						board=pod_solve(board)
						solved=True
					break
			else:
				#если вычеркивания дают 0
				print("Check is BAD")
				break
		else:
			print("SOLVED!")
			show(board)
			solved=True
			break
	return solved
doctest.testmod()