# spot mode (локальная уборка)
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.patches import Rectangle

# параметры комнаты
room = (16, 10)

# препятствия в комнате
obstacles = [
    Rectangle((-1, 7), 4, 3, facecolor="blue"),
    Rectangle((5, -1), 4, 3, facecolor="blue"),
    Rectangle((10, 5), 3, 5, facecolor="blue"),
]

# параметры робота
pos_xy = [7, 6]
path = [tuple(pos_xy)]
directions = [(0, 1), (-1, 0), (0, -1), (1, 0)]
steps = [1, 2]
current_direction = 0
current_step_size = steps[current_direction]
steps_taken = 0

# создание фигуры и осей
fig, ax = plt.subplots()
ax.set_xlim(-1, room[0])
ax.set_ylim(-1, room[1])
ax.set_title("Робот-пылесос")

# обновление позиции робота
def new_pos(frame):
    global pos_xy, current_direction, current_step_size, steps_taken

    pos_xy[0] += directions[current_direction][0]
    pos_xy[1] += directions[current_direction][1]
    path.append(tuple(pos_xy))
    steps_taken += 1

    if steps_taken >= current_step_size:
        current_direction = (current_direction + 1) % len(directions)
        steps_taken = 0

        if current_direction % 2 == 0:
            current_step_size += 1

    ax.clear()
    ax.set_xlim(-1, room[0])
    ax.set_ylim(-1, room[1])
    ax.set_title("Робот-пылесос")

    for obstacle in obstacles:
        ax.add_patch(obstacle)

    path_x, path_y = zip(*path)
    ax.plot(path_x, path_y, marker="o", color="green")
    ax.plot(pos_xy[0], pos_xy[1], marker="o", color="red", markersize=35)

# создание анимации движения робота
ani = animation.FuncAnimation(fig, new_pos, frames=42, interval=400, repeat=False)

plt.show()
