import numpy as np
import doctest

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

#создает начальную разметку из условия
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
			if(q[i][j].sum()==0):
				flag=0
	return flag

#вычеркивание
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
						if(sosed[i2][j2]==1 and (not(i==i2 and j==j2))):
							q[i2][j2][np.nonzero(q[i][j])[0][0]]=0
	return q


#алгоритм вычеркивания
def simple_solve(q):
	'''
	>>> q=create_q(np.zeros((9,9),int))
	>>> simple_solve(q)
	3
	>>> a=np.zeros((9,9),int)
	>>> a[0]=[1,2,3,4,5,6,7,8,0]
	>>> a[1]=[0,0,0,0,0,0,0,0,9]
	>>> simple_solve(create_q(a))
	2
	'''
	solved=0
	#print("CONDITION")
	#show(make_board(q))
	q=update_q(q)
	if(check(q)==0):
		solved=2
		#print("Zadacha ne reshaema")
	else:
		it=0
		while(solved==0):
			if(q.sum()==81):
				solved=1
				#print("SOLVED!")
				show(make_board(q))
				break
			else:
				q_temp=q+1
				q1=q_temp-1
				q=update_q(q)
				if(np.all(q1==q)):
					#print("q({0})=q({1})".format(it+1,it))
					#print("q = q_prev")
					#show(make_board(q))
					solved=3
					break
	#show(make_board(q))
	return solved

#алгоритм решения, пробует подставлять в неопределившиеся объекты конкретные цифры, идет дальше или откатывается назад
def hard_solve(q):
	print("CONDITION")
	show(make_board(q))
	if(simple_solve(q)==1):
		print("FULL SOLVED! :D")
	elif(simple_solve(q)==2):
		print("CAN NOT SOLVE ;(")
	else:
		print("CONTINUE SOLVING...")
		show(make_board(q))
		global_q_temp=q.copy()
		for i in range(9):
			for j in range(9):
				if(q[i][j].sum()>1):
					q_copy=q[i][j].copy()
					q_temp=q[i][j].copy()
					for k in range(9):
						if(q_copy[k]==1):
							for k1 in range(9):
								if(k!=k1):
									q_temp[k1]=0
							global_q_temp[i][j]=q_temp
							if(not check(global_q_temp)):
								#print("ne katit")
								q[i][j][k]=0
								q_temp=q_copy.copy()
								q_copy[k]=0
							else:
								q_temp[k]=0
						global_q_temp[i][j]=q[i][j]
					if(check(q)):
						q=hard_solve(q)
	return q
if __name__ == '__main__':
	doctest.testmod()
