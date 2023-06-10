'''
You are at position [0, 0] in maze NxN and you can only move in one of the four cardinal directions (i.e. North, East, South, West). 
Return true if you can reach position [N-1, N-1] or false otherwise.

V2: Check for wall connection like game of hex
'''



def path_finder(maze):
    maze = matrixify(maze)
    N = len(maze) # size of the NxN grid
    if N == 1:
        return True
    for i in range(N):
        if maze[i][0] == 'W':
            maze[i][0] = 'M'
            color_neighbors(maze, i, 0, N)

        if maze[N-1][i] == 'W':
            maze[N-1][i] = 'M'
            color_neighbors(maze, N-1, i, N)

    for i in range(N):
        if maze[0][i] == 'M':
            return False
        if maze[i][N-1] == 'M':
            return False
        
    return True



def color_neighbors(maze, i, j, N):
    if i-1 in range(N):
        if maze[i-1][j] == 'W':
                maze[i-1][j] = 'M'
                color_neighbors(maze, i-1, j, N)

        if j-1 in range(N): # corner 1
            if maze[i-1][j-1] == 'W':
                maze[i-1][j-1] = 'M'
                color_neighbors(maze, i-1, j-1, N)
            if maze[i][j-1] == 'W':
                maze[i][j-1] = 'M'
                color_neighbors(maze, i, j-1, N)
        if j+1 in range(N): # corner 2
            if maze[i-1][j+1] == 'W':
                maze[i-1][j+1] = 'M'
                color_neighbors(maze, i-1, j+1, N)
            if maze[i][j+1] == 'W':
                maze[i][j+1] = 'M'
                color_neighbors(maze, i, j+1, N)
#-----------------
    if i+1 in range(N):
        if maze[i+1][j] == 'W':
                maze[i+1][j] = 'M'
                color_neighbors(maze, i+1, j, N)

        if j-1 in range(N): # corner 3
            if maze[i+1][j-1] == 'W':
                maze[i+1][j-1] = 'M'
                color_neighbors(maze, i+1, j-1, N)
            if maze[i][j-1] == 'W':
                maze[i][j-1] = 'M'
                color_neighbors(maze, i, j-1, N)
        
        if j+1 in range(N): # corner 4
            if maze[i+1][j+1] == 'W':
                maze[i+1][j+1] = 'M'
                color_neighbors(maze, i+1, j+1, N)
            if maze[i][j+1] == 'W':
                maze[i][j+1] = 'M'
                color_neighbors(maze, i, j+1, N)

    

def matrixify(maze):
    ls = []
    full_ls = []
    for i in maze:
        if i =='\n':
            full_ls.append(ls)
            ls = []
        else:
            ls.append(i)
    full_ls.append(ls)
    return full_ls



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

print(path_finder(a))

