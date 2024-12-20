# zigzag mode (уборка зигзагом)
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.patches import *

# параметры комнаты
room = (16, 10)

# препятствия в комнате
obstacles = [
    Rectangle((-1, 7), 4, 3, facecolor="blue"),
    Rectangle((5, -1), 4, 3, facecolor="blue"),
    Rectangle((10, 5), 3, 5, facecolor="blue"),
]

# параметры робота
pos_xy = [0, 0]
path = [tuple(pos_xy)]
direction = 1
step = 1

# создание фигуры и осей
fig, ax = plt.subplots()
ax.set_xlim(-1, room[0])
ax.set_ylim(-1, room[1])
ax.set_title("Робот-пылесос")

# обновление позиции робота
def new_pos(frame):
    global pos_xy, direction

    pos_xy[1] += direction

    if str(pos_xy[0]) in "0123" and pos_xy[1] >= 7:
        pos_xy[1] = 6
        pos_xy[0] += step
        direction = -1

    if str(pos_xy[0]) in "56789" and pos_xy[1] <= 2:
        pos_xy[1] = 3
        pos_xy[0] += step
        direction = 1

    if (
        pos_xy[0] == 10 or pos_xy[0] == 11 or pos_xy[0] == 12 or pos_xy[0] == 13
    ) and pos_xy[1] >= 5:
        pos_xy[1] = 4
        pos_xy[0] += step
        direction = -1

    if pos_xy[0] == 10 and pos_xy[1] == 4:
        direction = -1

    if pos_xy[0] == 14 and pos_xy[1] == 0:
        direction = 1

    if pos_xy[1] >= room[1]:
        pos_xy[1] = room[1] - 1
        pos_xy[0] += step
        direction = -1
    elif pos_xy[1] < 0:
        pos_xy[1] = 0
        pos_xy[0] += step
        direction = 1

    if pos_xy[0] >= room[0]:
        pos_xy[0] = room[0] - 1
    elif pos_xy[0] < 0:
        pos_xy[0] = 0

    path.append(tuple(pos_xy))

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
ani = animation.FuncAnimation(fig, new_pos, frames=117, interval=400, repeat=False)

plt.show()
