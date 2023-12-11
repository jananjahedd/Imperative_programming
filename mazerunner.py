"""
File: mazerunner.py
Author: j.jahed@student.rug.nl
Description: This program calculates the longest sequence of pellets that pacman can consume that is uninterrupted by an empty square. The maze for each round is gicen by
user unout where # is walls, . is pellets, @ is pacman and space is an empty cell. 
"""

# A function to find the position of the pacman 
def pacman_position(maze):
    for i, row in enumerate(maze):
        for j, cell in enumerate(row):
            if cell == '@':
                return (i, j)
    return None

# A function to determine all the valid positions which means it's not a wall
def valid_position(x, y, maze):
    rows = len(maze)
    cols = len(maze[0])
    if 0 <= x < rows and 0 <= y < cols and maze[x][y] != '#':
        return valid_position

# A function to calcluate the longest sequence pacman can take taking the pacman position and valid position into account
def longest_sequence(maze):
    #this variable keeps track of the maximum length 
    max_length = 0
    p_position = pacman_position(maze)
    #https://www.w3schools.com/python/ref_func_set.asp
    checked = set()

    #for the case where there is no pacman 
    if p_position is None:
        print("")

    #A recursive function to check all the possibilities pacman has and calculating the maxmimum length of it 
    def move(position, sequence_length):
        #https://docs.python.org/3/reference/simple_stmts.html - I would get an error if the variale was nto non local and global since it's a nested function 
        nonlocal max_length

        #checks if a longer sequence is found and if so keeps updating the maximum length 
        if max_length < sequence_length:
            max_length = sequence_length
        checked.add(position)

        #These are all the possible moves for the pacman since it can go only up and down left and right 1 block at a time
        possibilities = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        #If pacman hasnt visited a cell and the movement is valid and that position isnt empty and has a pellet (.) then move to that sequence 
        for x_move, y_move in possibilities:
            x = position[0] + x_move
            y = position[1] + y_move
            
            if valid_position(x, y, maze) and (x, y) not in checked:
                if maze[x][y] == '.':
                    move((x, y), sequence_length + 1)
        #update checked so it keeps track of what it checked and what it didnt 
        checked.remove(position)  
    #This is the initial position and it moves from the intiial position and the length of that is 0
    move(p_position, 0)
    return max_length

#initializing a maze and getting user input row by row and adding it to the maze 
maze = []
#https://www.quora.com/How-I-can-take-input-in-a-row-and-doing-operation-with-that-in-Python-such-2-3-4-5-as-a-input-and-making-a-list-while-taking-input-2-2-3-5-4-9-5
while True:
    try:
        #https://docs.python.org/3.4/library/stdtypes.html?
        row = input().strip()
        if not row:
            break
        maze.append(row)

    except EOFError:
        break
#getting results by calling the function  
result = longest_sequence(maze)
print(result)
