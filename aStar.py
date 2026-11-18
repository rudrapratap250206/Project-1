
import heapq

def heuristic(a, b):
    # Manhattan Distance
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def astar(maze, start, goal):
    rows = len(maze)
    cols = len(maze[0])

    open_list = []
    heapq.heappush(open_list, (0, start))

    came_from = {}
    g_score = {start: 0}

    while open_list:
        current = heapq.heappop(open_list)[1]

        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            path.reverse()
            return path

        # Up, Down, Left, Right
        neighbors = [
            (current[0] - 1, current[1]),
            (current[0] + 1, current[1]),
            (current[0], current[1] - 1),
            (current[0], current[1] + 1)
        ]

        for neighbor in neighbors:
            x, y = neighbor

            if (0 <= x < rows and 0 <= y < cols
                    and maze[x][y] == 0):

                tentative_g = g_score[current] + 1

                if tentative_g < g_score.get(neighbor, float('inf')):
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g

                    f_score = tentative_g + heuristic(neighbor, goal)

                    heapq.heappush(open_list, (f_score, neighbor))

    return None


# 0 = Free path, 1 = Obstacle
maze = [
    [0, 0, 0, 0, 0],
    [1, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]

start = (0, 0)
goal = (4, 4)

path = astar(maze, start, goal)

if path:
    print("Path found:")
    for position in path:
        print(position)

    print("\nShortest path length:", len(path) - 1)
else:
    print("No path found!")
