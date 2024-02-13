def draw_figure(name, size):
    if name.lower() == "sqare":
        for i in range(size):
            print("* " * size)
    elif name.lower() == "triangle":
        for i in range(1, size + 1):
            print("* " * i)
    elif name.lower() == "rhombus":
        for i in range(1, size + 1):
            print(" " * (size - i) + "*" * (2 * i - 1))
        for i in range(size - 1, 0, -1):
            print(" " * (size - i) + "*" * (2 * i - 1))
    else:
        print('wrong figure name')
figure_name = input('figure name (sqare/triangle/rhombus): ')
figure_size = int(input('figure size: '))
draw_figure(figure_name, figure_size)