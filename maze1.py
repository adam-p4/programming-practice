'''
You are at position [0, 0] in maze NxN and you can only move in one of the four cardinal directions (i.e. North, East, South, West). 
Return true if you can reach position [N-1, N-1] or false otherwise.
'''
import itertools
import time
start_time = time.time()

def path_finder(maze):
    maze = maze.split()
    N = len(maze) # size of the NxN grid
    if N == 1:
        return True
    pos = [0, 0] # current position in the maze[y][x]
    goal_pos = [N-1, N-1]

    visited =[[0 for i in range(N)] for i in range(N)] #NxN grid of zeros
    moves_tried = [[[] for i in range(N)] for i in range(N)] #NxN grid of empty lists
    
    visited[0][0] = 1
    
    visited_set = set(itertools.chain.from_iterable(visited)) # contains elements from {0, 1, 2}

    while visited_set != {0,2}: # haven't exhausted all possibilities yet

        if set(moves_possible(maze, pos, N)) == set(moves_tried[pos[0]][pos[1]]): # all moves have been tried from this pos
            visited[pos[0]][pos[1]] = 2 # no new moves from this square
            visited_set = set(itertools.chain.from_iterable(visited)) # update
            if visited_set != {0,2}:
                pos = teleport(visited, N)
            else:
                return False
        else:
            for move in moves_possible(maze, pos, N):
                if move not in moves_tried[pos[0]][pos[1]]:
                    moves_tried[pos[0]][pos[1]].append(move) # document the move

                    pos = move_pos(pos, move) # change position
                    moves_tried[pos[0]][pos[1]].append(reverse_move(move)) # documents reverse move as tried


                    if pos == [N-1, N-1]: # maze exit reached
                        return True
                    
                    
                    if visited[pos[0]][pos[1]] == 0: # first time at this position
                        visited[pos[0]][pos[1]] = 1 # mark as visited
                        visited_set = set(itertools.chain.from_iterable(visited)) # update

                    elif visited[pos[0]][pos[1]] == 1: # don't go to already visited space if u can avoid it
                        pos = move_pos(pos, reverse_move(move))

                    elif visited[pos[0]][pos[1]] == 2: # have already exhausted this position
                        visited_set = set(itertools.chain.from_iterable(visited)) # update
                        if visited_set != {0,2}:
                            pos = teleport(visited, N)
                        else:
                            return False
                    break
                        
    return False

def reverse_move(move): # reverses the move direction
    if move == 'up':
        return 'down'
    if move == 'down':
        return 'up'
    if move == 'left':
        return 'right'
    if move == 'right':
        return 'left'
    

def move_pos(pos, move): # moves the position according to the move direction
    if move == 'up':
        pos[0] = pos[0] - 1
    if move == 'down':
        pos[0] = pos[0] + 1
    if move == 'left':
        pos[1] = pos[1] - 1
    if move == 'right':
        pos[1] = pos[1] + 1
    return pos

def moves_possible(maze, pos, N): # puts all possible moves from given position in a list
    movement_possible = []
    #right
    if pos[1]+1 in range(0,N) and maze[pos[0]][pos[1]+1] != 'W':
        movement_possible.append('right')
    #down
    if pos[0]+1 in range(0,N) and maze[pos[0]+1][pos[1]] != 'W':
        movement_possible.append('down')
    #up
    if pos[0]-1 in range(0,N) and maze[pos[0]-1][pos[1]] != 'W':
        movement_possible.append('up')
    #left
    if pos[1]-1 in range(0,N) and maze[pos[0]][pos[1]-1] != 'W':
        movement_possible.append('left')
    return movement_possible
    

def teleport(visited, N): # teleports to a non-exhausted visited node
    for i in range(N-1, -1, -1): # starts from closest to N-1
        for j in range(N-1, -1, -1):
            if visited[i][j] == 1: 
                return [i, j] # new position
                


# Tests
a = "\n".join(["...W.",
               "..W..",
               ".W...",
               ".W...",
               "..W.."])


b = "\n".join([
          ".W...",
          ".W...",
          ".W.W.",
          "...W.",
          "...W."])


print(path_finder(b))
print("--- %s seconds ---" % (time.time() - start_time))
