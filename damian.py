def find_path(tab, p, x, y):

	step=0
	kierunek = 0

	


	while(True):
		
		#warunek konca
		suma = 0
		break_me = False
		for i in range(n):
			if break_me:
				break;
			for j in range(n):
				if tab[i][j] == 0 or temp_tab[i][j] == 0 or (x != i and y != j):
					break_me = True
					break 

		if not break_me:
			print "udalo sie"
			return 

		if kierunek == 0:
			if y - 1 > 0:
				if tab[x][y-1] == 0 and temp_tab[x][y-1] == 0 and p[step][kierunek] == 0:#gora wolna:
					p[step][kierunek] = 1
					p[step+1][2] = 2
					temp_tab[x][y] = 1
					step = step + 1
					kierunek = 0
					y = y - 1
				else:
					p[step][0] = 3
					kierunek = kierunek + 1
			else:
				#wychodzimy za tablice
				p[step][kierunek] = 3
				kierunek = kierunek + 1

		elif kierunek == 1:
			if x + 1 < n:
				if tab[x+1][y] == 0 and temp_tab[x+1][y] == 0 and p[step][kierunek] == 0:#prawo wolna:
					p[step][kierunek] = 1
					p[step+1][3] = 2
					temp_tab[x][y] = 1
					step = step + 1
					kierunek = 0
					x = x + 1
				else:
					p[step][1] = 3
					kierunek = kierunek + 1
			else:
				#wychodzimy za tablice
				p[step][kierunek] = 3
				kierunek = kierunek + 1

		elif kierunek == 2:
			if y + 1 < n:
				if tab[x][y+1] == 0 and temp_tab[x][y+1] == 0 and p[step][kierunek] == 0:#dol wolny:
					p[step][kierunek] = 1
					p[step+1][0]      = 2
					temp_tab[x][y]    = 1
					step              = step + 1
					kierunek          = 0
					y = y + 1
				else:
					p[step][1] = 3
					kierunek   = kierunek + 1
			else:
				#wychodzimy za tablice
				p[step][kierunek] = 3
				kierunek = kierunek + 1
		elif kierunek == 3:
			if x -1  > 0:
				if tab[x-1][y] == 0 and temp_tab[x-1][y] == 0 and p[step][kierunek] == 0:#lewo wolne:
					p[step][kierunek] = 1
					p[step+1][1]      = 2
					temp_tab[x][y]    = 1
					step              = step + 1
					kierunek          = 0
					x = x - 1
				else:	
					if step == 0:
						print "NIEMOXLiwe"
						return;

					#powrot! 
					p[step][0] = 0
					p[step][1] = 0
					p[step][2] = 0
					p[step][3] = 0
					wyczysc_pop(x,y,step)						
					step = step - 1
					kierunek = 0
					
			else:
				#wychodzimy za tablice
				if step == 0:
					print "NIEMOXLiwe"
					return;

				#powrot
				p[step][0] = 0
				p[step][1] = 0
				p[step][2] = 0
				p[step][3] = 0
				wyczysc_pop(x,y,step)					
				step = step - 1
				kierunek = 0
				


def wyczysc_pop(x,y,step):
	if p[step-1][0] == 1:
		temp_tab[x][y-1] = 0
		p[step-1][0] = 3
	elif p[step-1][1] == 1:
		temp_tab[x-1][y] = 0
		p[step-1][1] = 3
	elif p[step-1][2] == 1:
		temp_tab[x][y+1] = 0
		p[step-1][2] = 3
	elif p[step-1][3] == 1:
		temp_tab[x+1][y] = 0
		p[step-1][3] = 3



if __name__ == "__main__":

	n = 3

	#0-gora
	#1-prawo
	#2-dol
	#3-lewo

	#0 - wolne 
	#1 - poszlismy
	#2 - powrot
	#3 - zajety

	tab = [[0,0,0],
		[0,0,0],
		[0,0,0]]

	temp_tab = [[0,0,0],[0,0,0],[0,0,0]]
	p = [list((0,)*4) for i in range(n*n)]

	x = 0
	y = 0

	find_path(tab, p, x, y)
	

