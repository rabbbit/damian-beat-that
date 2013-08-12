#0 - up
#1 - right
#2 - down
#3 - left

#0 - free
#1 - go to
#2 - went from
#3 - occupied

def find_path(tab, p, x, y):

	step=0
	direction = 0

	n = len(tab)

	while(True):
		#end condition
		suma = 0
		break_me = False
		for j in range(n):
			if break_me:
				break;
			for i in range(n):
				if x == i and y == j:
					continue
				if tab[j][i] == 0 and temp_tab[j][i] == 0:
					break_me = True
					break 

		if not break_me:
			print "Success"
			print_path(p)
			return 

		if direction == 0:
			if y - 1 >= 0:
				if tab[y-1][x] == 0 and temp_tab[y-1][x] == 0 and p[step][direction] == 0:#up free
					print 'Go x=%s, y=%s, direction=%s, step=%s' % (x, y, direction, step)
					p[step][direction] = 1
					p[step+1][2]       = 2
					temp_tab[y][x]     = 1
					step               = step + 1
					direction          = 0
					y                  = y - 1
				else:
					print 'Field occupied x=%s, y=%s, direction=%s, step=%s' % (x, y, direction, step)
					p[step][0] = 3
					direction  = direction + 1
			else:
				print 'Out of table x=%s, y=%s, direction=%s, step=%s' % (x, y, direction, step)
				p[step][direction] = 3
				direction          = direction + 1


		elif direction == 1:
			if x + 1 < n:
				if tab[y][x+1] == 0 and temp_tab[y][x+1] == 0 and p[step][direction] == 0:#right free
					print 'Go x=%s, y=%s, direction=%s, step=%s' % (x, y, direction, step)
					p[step][direction] = 1
					p[step+1][3]       = 2
					temp_tab[y][x]     = 1
					step               = step + 1
					direction          = 0
					x                  = x + 1
				else:
					print 'Field occupied x=%s, y=%s, direction=%s, step=%s' % (x, y, direction, step)
					p[step][1] = 3
					direction  = direction + 1
			else:
				print 'Out of table x=%s, y=%s, direction=%s, step=%s' % (x, y, direction, step)
				p[step][direction] = 3
				direction          = direction + 1


		elif direction == 2:
			if y + 1 < n:
				if tab[y+1][x] == 0 and temp_tab[y+1][x] == 0 and p[step][direction] == 0:#down free
					print 'Go x=%s, y=%s, direction=%s, step=%s' % (x, y, direction, step)
					p[step][direction] = 1
					p[step+1][0]       = 2
					temp_tab[y][x]     = 1
					step               = step + 1
					direction          = 0
					y = y + 1
				else:
					print 'Field occupied x=%s, y=%s, direction=%s, step=%s' % (x, y, direction, step)
					p[step][1] = 3
					direction  = direction + 1
			else:
				print 'Out of table x=%s, y=%s, direction=%s, step=%s' % (x, y, direction, step)
				p[step][direction] = 3
				direction          = direction + 1

		elif direction == 3:
			if x - 1  >= 0:
				if tab[y][x-1] == 0 and temp_tab[y][x-1] == 0 and p[step][direction] == 0:#left free
					print 'Go x=%s, y=%s, direction=%s, step=%s' % (x, y, direction, step)
					p[step][direction] = 1
					p[step+1][1]       = 2
					temp_tab[y][x]     = 1
					step               = step + 1
					direction          = 0
					x = x - 1
				else:	
					print 'Field occupied x=%s, y=%s, direction=%s, step=%s' % (x, y, direction, step)
					if step == 0:
						print "Impossible!"
						return;
					#go back! 
					x, y, step, direction = step_back(x,y,step)
			else:
				print 'Out of table x=%s, y=%s, direction=%s, step=%s' % (x, y, direction, step)

				if step == 0:
					print "Impossible!"
					return;

				#go back
				x, y, step, direction = step_back(x,y,step)
			
def step_back(x,y,step):
	p[step][0] = 0
	p[step][1] = 0
	p[step][2] = 0
	p[step][3] = 0
	x,y = clear_prev(x,y,step)						
	step = step - 1
	direction = 0

	return x, y, step, direction


def clear_prev(x,y,step):
	if p[step-1][0] == 1: #up
		temp_tab[y+1][x] = 0
		p[step-1][0] = 3
		y = y + 1
	elif p[step-1][1] == 1: #rigt
		temp_tab[y][x-1] = 0
		p[step-1][1] = 3
		x = x - 1
	elif p[step-1][2] == 1: #down
		temp_tab[y-1][x] = 0
		p[step-1][2] = 3
		y = y - 1
	elif p[step-1][3] == 1:#left
		temp_tab[y][x+1] = 0
		p[step-1][3] = 3
		x = x + 1
	return x,y

def print_path(p):
	for i in p:
		if i[0] == 1:
			print "up"
		if i[1] == 1:
			print "right"
		if i[2] == 1:
			print "down"
		if i[3] == 1:
			print "left"



if __name__ == "__main__":

	tab = [[0,0,0,0],
		   [0,0,1,0],
		   [0,0,1,1],
		   [0,0,1,1]]


	temp_tab = [list((0,)*len(tab[0])) for i in range(len(tab))]
	p = [list((0,)*4) for i in range(len(tab)*len(tab[0]))]

	x = 0
	y = 0

	find_path(tab, p, x, y)

