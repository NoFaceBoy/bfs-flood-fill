picture = [line.split() for line in open('resources/input.txt')]


def flood_fill(picture, row, column, x, y, current_color, new_color):
    queue = [[x, y]]
    picture[x][y] = new_color

    while queue:
        current_pixel = queue.pop()

        pos_x = current_pixel[0]
        pos_y = current_pixel[1]

        if satisfies(picture, row, column, pos_x + 1, pos_y, current_color, new_color):
            picture[pos_x + 1][pos_y] = new_color
            queue.append([pos_x + 1, pos_y])

        if satisfies(picture, row, column, pos_x - 1, pos_y, current_color, new_color):
            picture[pos_x - 1][pos_y] = new_color
            queue.append([pos_x - 1, pos_y])

        if satisfies(picture, row, column, pos_x, pos_y + 1, current_color, new_color):
            picture[pos_x][pos_y + 1] = new_color
            queue.append([pos_x, pos_y + 1])

        if satisfies(picture, row, column, pos_x, pos_y - 1, current_color, new_color):
            picture[pos_x][pos_y - 1] = new_color
            queue.append([pos_x, pos_y - 1])

    return picture


def satisfies(picture, row, column, x, y, current_color, new_color):
    if (x or y) < 0 or x >= row or y >= column or picture[x][y] != current_color or picture[x][y] == new_color:
        return False
    return True


x = 3
y = 9

current_color = picture[x][y]

flood_fill(picture, 10, 10, x, y, current_color, "C")

if [line.split() for line in open('resources/output.txt')] == flood_fill(picture, 10, 10, x, y, current_color, "C"):
    for i in range(10):
        for j in range(10):
            print(picture[i][j], end=' ')
        print()
    print("Color flood equals with output.txt")
else:
    print("Color flood is not the same as output.txt")
