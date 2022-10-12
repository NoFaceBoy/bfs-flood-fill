def unpack():
    import re
    file = open("resources/input.txt", "r")
    lines = file.readlines()
    color_picture = [line.split() for line in lines[3:]]
    row_size, column_size = re.findall("\\d+", lines[0])
    value_x, value_y = re.findall("\\d+", lines[1])
    new_color_value = re.findall("[A-Z]", lines[2])[0]
    return int(value_x), int(value_y), int(row_size), int(column_size), str(new_color_value), color_picture


row, column, width, height, color, img = unpack()


def flood_fill(picture, x, y, new_color):
    pixel_color = picture[x][y]
    queue = [(x, y)]
    visited = set()
    while len(queue) > 0:
        x, y = queue.pop(0)
        visited.add((x, y))
        if picture[x][y] == pixel_color:
            picture[x][y] = new_color
        for x, y in neighbors(picture, x, y, pixel_color):
            if (x, y) not in visited:
                queue.append((x, y))

    return picture


def neighbors(picture, x, y, pixel_color):
    variations = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
    return [(x, y) for x, y in variations if satisfies(picture, x, y, pixel_color)]


def satisfies(picture, x, y, pixel_color):
    return 0 <= x < width and 0 <= y < height and picture[x][y] == pixel_color


if [line.split() for line in open("resources/output.txt")] == flood_fill(img, row, column, color):
    for i in range(width):
        for j in range(height):
            print(img[i][j], end=' ')
        print()
    print("Color fill equals with output.txt")
else:
    print("Color fill is not the same as output.txt")
