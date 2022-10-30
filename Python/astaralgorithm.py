import sys

class Node():

	def __init__(self,state,parent,action,hue,path):
		self.state=state
		self.parent=parent
		self.action=action
		self.hue=hue
		self.path=path

class StackFrontier():

	def __init__(self):
		self.frontier=[]
	#adding node to frontier
	def add(self,node): 
		self.frontier.append(node)
	#checking if some state is already in frontier
	def contains_state(self,state): 
		result=any(node.state==state for node in self.frontier)
		return result
	#checking if frontier is empty
	def empty(self): 
		return len(self.frontier)==0
	#removing a node from frontier
	def remove(self): 
		if self.empty():
			raise exception("empty frontier")
		else:
			node=self.frontier[-1]
			self.frontier=self.frontier[:-1]
			return node

class QueueFrontier():
	#removing first element
	def remove(self):
		if self.empty():
			raise exception("empty frontier")
		else:
			node=self.frontier[0]
			self.frontier=self.frontier[1:]
			return node

class HeuristicFrontier(StackFrontier):

    def remove(self):
        if self.empty():
            raise Exception('empty frontier')
        else:
            lowest= self.frontier[0].heu
            node = self.frontier[0]
            remove=0
            try:
                #comparing for smallest h(n)
                for i in range(1,len(self.frontier)):
                    if self.frontier[i].heu<lowest:
                        lowest= self.frontier[i].heu
                        node = self.frontier[i]
                        remove=i
            except IndexError:
                pass
            self.frontier.pop(remove)
            return node

class StarFrontier(StackFrontier):

    def remove(self):
        if self.empty():
            raise Exception('empty frontier')
        else:
            # If only 1 node added to frontier
            lowest= self.frontier[0].heu+ self.frontier[0].path 
            node = self.frontier[0]
            remove=0
            try:
                # Comparing the nodes for lowest f(n) value
                for i in range(1,len(self.frontier)):
                    if self.frontier[i].heu+ self.frontier[i].path<lowest:
                        lowest= self.frontier[i].path+ self.frontier[i].heu
                        node = self.frontier[i]
                        remove=i
            except IndexError:
                pass
            self.frontier.pop(remove)
            return node


class Maze():

	def __init__(self,filename):
		with open(filename) as f:
			contents=f.read()
		#checking number of starting and ending points
		if contents.count("A")!=1:
			raise exception("maze must have exactly one start point")
		if contents.count("B")!=1:
			raise exception("maze must have exactly one end point")

		#counting height/width of maze
		contents=contents.splitlines()
		self.height=len(contents)
		self.width=max(len(line) for line in contents)

		#encountering walls(#)
		self.walls=[]
		for i in range(self.height):
			row=[]
			for j in range(self.width):
				try:
					if contents[i][j]=="A":
						self.start=(i,j)
						row.append(False)
					elif contents[i][j]=="B":
						self.goal=(i,j)
						row.append(False)
					elif contents[i][j]==" ":
						row.append(False)
					#element is a wall
					else:
						row.append(True)
				except IndexError:
					row.append(False)
			self.walls.append(row)

		self.solution=None


		def neighbors(self, state):
			row, col = state
			candidates = [
            ("up", (row - 1, col),self.add_tuple((row-1, col), self.goal)),
            ("down", (row + 1, col),self.add_tuple((row+1, col), self.goal)),
            ("left", (row, col - 1),self.add_tuple((row, col-1), self.goal)),
            ("right", (row, col + 1),self.add_tuple((row, col+1), self.goal))
        ]

 			result = []
		for action, (r, c) in candidates:
			if 0 <= r < self.height and 0 <= c < self.width and not self.walls[r][c]:
			result.append((action, (r, c),hue,path))
		return result

	def neighbors(self, state):
        row, col = state
        candidates = [
            ("up", (row - 1, col),self.add_tuple((row-1, col), self.goal)),
            ("down", (row + 1, col),self.add_tuple((row+1, col), self.goal)),
            ("left", (row, col - 1),self.add_tuple((row, col-1), self.goal)),
            ("right", (row, col + 1),self.add_tuple((row, col+1), self.goal))
        ]

        result = []
        for action, (r, c), hue in candidates:
            if 0 <= r < self.height and 0 <= c < self.width and not self.walls[r][c]:
                result.append((action, (r, c),hue,path))
        return result

    def add_tuple(self,t1,t2):
        return sum(list(tuple(map(lambda i, j: abs(i - j), t1, t2))))

	def solve(self):
		#finds a solution to the maze , if it exists

		#keep track of number of states opened
		self.num_explored=0
		#initialise the frontier to just the starting position
		start=Node(state=self.start,parent=None,action=None,hue=0,path=0)
		frontier=StarFrontier()
		frontier.add(start)

		#initialise an empty explored set
		self.explored=set()
		#keep looping until a solution is obtained
		while True:
			#if nothing left in frontier then no path
			if frontier.empty():
				raise exception("No Solution For This Maze")
			#choose a node from the frontier
			node=frontier.remove()
			self.num_explored+=1
			#if node is the goal then we have the solution
			if node.state==self.goal:
				actions=[]
				cells=[]
				while node.parent is not None:
					actions.append(node.action)
					cells.append(node.state)
					node=node.parent
				actions.reverse()
				cells.reverse()
				self.solution=(actions,cells)
				return 
			#mark node is explored
			self.explored.add(node.state)
			#add neighbor to frontier
			for action,state in self.neighbors(node.state,node.path):
				if not frontier.contains_state(state) and state not in self.explored:
					child=Node(state=state,parent=node,action=action,hue=heu,path=path)
					frontier.add(child)
	def print(self):
		solution=self.solution[1] if self.solution is not None else None
		print()
		for i,row in enumerate(self.walls):
			for j,col in enumerate(row):
				if col:
					print("x^",end="")
				elif (i,j)==self.start():
					print("A",end="")
				elif (i,j)==self.goal():
					print("B",end="")
				elif solution is not None and (i,j) in solution:
					print("*",end="")
				else:
					print(" ",end="")

			print()
		print()

	def output_image(self, filename, show_solution=True, show_explored=False):
        from PIL import Image, ImageDraw
        cell_size = 50
        cell_border = 2

        # Create a blank canvas
        img = Image.new(
            "RGBA",
            (self.width * cell_size, self.height * cell_size),
            "black"
        )
        draw = ImageDraw.Draw(img)

        solution = self.solution[1] if self.solution is not None else None
        for i, row in enumerate(self.walls):
            for j, col in enumerate(row):

                # Walls
                if col:
                    fill = (40, 40, 40)

                # Start
                elif (i, j) == self.start:
                    fill = (255, 0, 0)

                # Goal
                elif (i, j) == self.goal:
                    fill = (0, 171, 28)

                # Solution
                elif solution is not None and show_solution and (i, j) in solution:
                    fill = (220, 235, 113)

                # Explored
                elif solution is not None and show_explored and (i, j) in self.explored:
                    fill = (212, 97, 85)

                # Empty cell
                else:
                    fill = (237, 240, 252)

                # Draw cell
                draw.rectangle(
                    ([(j * cell_size + cell_border, i * cell_size + cell_border),
                      ((j + 1) * cell_size - cell_border, (i + 1) * cell_size - cell_border)]),
                    fill=fill
                )

        img.save(filename)

if len(sys.argv) != 2:
    sys.exit("Usage: python maze.py maze.txt")

m = Maze(sys.argv[1])
print("Maze:")
m.print()
print("Solving...")
m.solve()
print("States Explored:", m.num_explored)
print("Solution:")
m.print()
m.output_image("maze_star.png", show_explored=True)
