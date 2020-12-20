import numpy as np
import doctest
"""
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
первый индекс - индекс строки, второй - столбец
board[3][7] - 4я строка, 8й столбец
"""

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
def check(board):
	bad=False
	for i in range(9):
		for j in range(9):
			if(board[i][j]<0 or board[i][j]>9):
				bad=True
			sosedi=neighbor(i,j)
			for i1 in range(9):
				for j1 in range(9):
					if(sosedi[i1][j1]==1 and board[i1][j1]!=0):
						if(i!=i1 or j!=j1):
							if(board[i][j]==board[i1][j1]):
								bad=True
	if(bad):
		print("BAD BOARD")
	return bad
#функция обновляет функции g & q
def update_g_q(board,g,q):
	for i in range(9):
		for j in range(9):
			if(board[i][j]!=0):
				for l in range(9):
					q[i][j][l]=0
	#фиксируем элемент с доски
	for i1 in range(9):
		for j1 in range(9):
			#находим для него всех соседей
			sosed=neighbor(i1,j1)
			#проходимся по всем соседям и НЕсоседям для фиксированого выше элемента
			for i2 in range(9):
				for j2 in range(9):
					if(board[i1][j1]!=0):
						#для заполненных НЕсоседей убираем все связи кроме текущей
						#работает правильно
						if(sosed[i2][j2]==0 and board[i2][j2]!=0):
							for k1 in range(9):
								for k2 in range(9):
									if((k1!=board[i1][j1]-1 or k2!=board[i2][j2]-1) and (k2!=board[i1][j1]-1 or k1!=board[i2][j2]-1)):
										g[i1][j1][i2][j2][k1][k2]=0
										#g[i2][j2][i1][j1][k1][k2]=0
						#для пустых НЕсоседей ничего не трогаем
						
						#для соседей:
						if(sosed[i2][j2]==1):
							#для заполненных соседей
							#работает правильно
							if(board[i2][j2]!=0):
								for k1 in range(9):
									for k2 in range(9):
										if((k1!=board[i1][j1]-1 or k2!=board[i2][j2]-1) and (k2!=board[i1][j1]-1 or k1!=board[i2][j2]-1)):
											g[i1][j1][i2][j2][k1][k2]=0
											g[i2][j2][i1][j1][k2][k1]=0
							#для пустых соседей убираем связь цифры в i1,j1 с такой же меткой в i2,j2, а так же обновляем достижимость в q
							#работает правильно
							if(board[i2][j2]==0):
								for k1 in range(9):
									for k2 in range(9):
										if(k1!=board[i1][j1]-1 or k2==board[i1][j1]-1):
											g[i1][j1][i2][j2][k1][k2]=0
											g[i2][j2][i1][j1][k2][k1]=0
											q[i2][j2][board[i1][j1]-1]=0

	return g,q

def simple_solve(board):
	if(not check(board)):
		q=np.ones((9,9,9),int)
		g=np.ones((9,9,9,9,9,9),int)
		show(board)
		g,q=update_g_q(board,g,q)
		it=0

		while(True):
			#костыль, в одну строку нельзя "запомнить" последний массив и чтобы не было выхода из цикла
			q1=q+1
			q2=q1-1
			for i in range(9):
				for j in range(9):
					if(q[i][j].sum()==1):
						board[i][j]=int(np.nonzero(q[i][j])[0])+1
						q[i][j]=0
			it+=1
			print("ITERATION ",it)
			show(board)
			g,q=update_g_q(board,g,q)
			if(np.array_equal(q2,q)):
				print("q({0})=q({1})".format(it,it-1))
				if(np.count_nonzero(board)<81):
					print("однозначное решение не найдено")
				break
	return board



#условие для которого будет решение
board=np.array([
    [5, 3, 0,    0, 7, 0,    0, 0, 0],
    [6, 0, 0,    1, 9, 5,    0, 0, 0],
    [0, 9, 8,    0, 0, 0,    0, 6, 0],

    [8, 0, 0,    0, 6, 0,    0, 0, 3],
    [4, 0, 0,    8, 0, 3,    0, 0, 1],
    [7, 0, 0,    0, 2, 0,    0, 0, 6],

    [0, 6, 0,    0, 0, 0,    2, 8, 0],
    [0, 0, 0,    4, 1, 9,    0, 0, 5],
    [0, 0, 0,    0, 8, 0,    0, 7, 9]])
#условие, для которого решений несколько и нет одного однозначного, который получают алгоритмом вычеркивания
board2=np.array([
    [5, 0, 0,    0, 7, 0,    0, 0, 0],
    [6, 0, 0,    1, 9, 5,    0, 0, 0],
    [0, 9, 8,    0, 0, 0,    0, 6, 0],

    [8, 0, 0,    0, 6, 0,    0, 0, 3],
    [4, 0, 0,    8, 0, 3,    0, 0, 1],
    [7, 0, 0,    0, 2, 0,    0, 0, 6],

    [0, 6, 0,    0, 0, 0,    2, 0, 0],
    [0, 0, 0,    4, 1, 0,    0, 0, 5],
    [0, 0, 0,    0, 8, 0,    0, 7, 0]])
#условие, с которым алгоритм справится за один заход
board1=np.array([
    [4,2,6,8,1,9,5,7,3],
    [9,8,0,5,7,4,2,1,6],
    [5,1,7,2,3,6,4,8,9],

    [1,5,8,3,0,0,9,6,7],
    [7,4,2,9,6,8,1,3,5],
    [3,6,9,7,5,1,8,4,2],

    [2,0,4,6,8,5,3,9,1],
    [8,3,5,1,9,7,6,2,4],
    [6,9,1,4,2,3,7,5,0]])

simple_solve(board)

