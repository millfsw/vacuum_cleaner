# spot (по всей комнате)
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
pos_xy = [2, 2]
path = [tuple(pos_xy)]
steps = [1, 2]
step = 1

# параметры для первой спирали
directions1 = [(0, 1), (-1, 0), (0, -1), (1, 0)]
current_direction1 = 0
current_step_size1 = steps[current_direction1]
steps_taken1 = 0
spiral1 = True

# параметры для второй спирали
directions2 = [(0, 1), (-1, 0), (0, -1), (1, 0)]
current_direction2 = 0
current_step_size2 = steps[current_direction2]
steps_taken2 = 0
spiral2 = False

# параметры для третьей спирали
directions3 = [(0, 1), (-1, 0), (0, -1), (1, 0)]
current_direction3 = 0
current_step_size3 = steps[current_direction3]
steps_taken3 = 0
spiral3 = False

# создание фигуры и осей
fig, ax = plt.subplots()
ax.set_xlim(-1, room[0])
ax.set_ylim(-1, room[1])
ax.set_title("Робот-пылесос")

# обновление позиции робота
def new_pos(frame):
    global pos_xy, current_direction1, current_step_size1, steps_taken1, spiral1, current_direction2, current_step_size2, steps_taken2, spiral2, spiral3, current_direction3, current_step_size3, steps_taken3

    if pos_xy[0] == 0 and pos_xy[1] == 5:
        pos_xy[1] += step
        path.append(tuple(pos_xy))
        spiral1 = False

    if pos_xy[0] == 0 and pos_xy[1] == 6:
        spiral1 = False
        for _ in range(7):
            pos_xy[0] += step
            path.append(tuple(pos_xy))

    if pos_xy[0] == 7 and pos_xy[1] == 6:
        spiral2 = True

    if pos_xy[0] == 10 and pos_xy[1] == 4:
        spiral2 = False
        for _ in range(2):
            pos_xy[0] += step
            path.append(tuple(pos_xy))

    if pos_xy[0] == 12 and pos_xy[1] == 4:
        pos_xy[1] -= step
        pos_xy[1] -= step
        path.append(tuple(pos_xy))

    if pos_xy[0] == 12 and pos_xy[1] == 2:
        spiral3 = True

    if pos_xy[0] == 14 and pos_xy[1] == 4:
        spiral3 = False
        for _ in range(5):
            pos_xy[1] += step
            path.append(tuple(pos_xy))
        pos_xy[0] += step
        path.append(tuple(pos_xy))
        for _ in range(4):
            pos_xy[1] -= step
            path.append(tuple(pos_xy))
        for _ in range(5):
            pos_xy[1] -= step
            path.append(tuple(pos_xy))

    if spiral1:
        pos_xy[0] += directions1[current_direction1][0]
        pos_xy[1] += directions1[current_direction1][1]
        path.append(tuple(pos_xy))
        steps_taken1 += 1

        if steps_taken1 >= current_step_size1:
            current_direction1 = (current_direction1 + 1) % len(directions1)
            steps_taken1 = 0

            if current_direction1 % 2 == 0:
                current_step_size1 += 1

    if spiral2:
        pos_xy[0] += directions2[current_direction2][0]
        pos_xy[1] += directions2[current_direction2][1]
        path.append(tuple(pos_xy))
        steps_taken2 += 1

        if steps_taken2 >= current_step_size2:
            current_direction2 = (current_direction2 + 1) % len(directions2)
            steps_taken2 = 0

            if current_direction2 % 2 == 0:
                current_step_size2 += 1

    if spiral3:
        pos_xy[0] += directions3[current_direction3][0]
        pos_xy[1] += directions3[current_direction3][1]
        path.append(tuple(pos_xy))
        steps_taken3 += 1

        if pos_xy[0] == 12 and pos_xy[1] == 4:
            pos_xy[0] -= step
            path.append(tuple(pos_xy))

        if pos_xy[0] == 10 and pos_xy[1] == 4:
            for _ in range(3):
                pos_xy[1] -= step
                path.append(tuple(pos_xy))
            current_direction3 += 1

        if pos_xy[0] == 13 and pos_xy[1] == 0:
            pos_xy[0] += step
            path.append(tuple(pos_xy))

        if steps_taken3 >= current_step_size3:
            current_direction3 = (current_direction3 + 1) % len(directions3)
            steps_taken3 = 0

            if current_direction3 % 2 == 0:
                current_step_size3 += 1

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
ani = animation.FuncAnimation(fig, new_pos, frames=200, interval=400, repeat=False)

plt.show()
