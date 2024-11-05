def get_gradient(x_1, y_1, x_2, y_2):
    return (y_2 - y_1)/(x_2 - x_1)

print(get_gradient(0, 0, 1, 1))
print(get_gradient(5, 4, -8, 3))
