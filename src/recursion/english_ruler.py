def english_ruler(inches, depth):
    """
    A recursion example for drawing an Enlgish ruler
    :param inches: Number of inches
    :param depth: The depth of the markings within an inch
    :return: An English ruler drawing
    """
    draw_major_line(depth, 0)
    for i in range(1, inches + 1):
        draw_minor_line(depth - 1)
        draw_major_line(depth, i)


def draw_major_line(depth, inch=''):
    line = '-' * depth + ' ' + str(inch)
    print(line)


def draw_minor_line(depth):
    if depth > 0:
        draw_minor_line(depth - 1)
        draw_major_line(depth)
        draw_minor_line(depth - 1)