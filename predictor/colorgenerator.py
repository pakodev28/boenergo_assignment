from random import randint, shuffle


def get_color_list(min_value, max_value, color):
    """Создает список повторяющихся строк с заданным цветом(color),
    колличество в диапазоне от min_value до ma_value."""
    color_amount = randint(min_value, max_value)
    color_list = [color] * color_amount
    return color_list


def get_three_color_string():
    """Создает список из 100 строк, в которых записаны 3 цвета
    (green, red, blue) в разных колличествах"""
    total_count = 100
    green_arr = get_color_list(5, 7, "green")
    red_arr = get_color_list(1, 4, "red")
    blue_arr_count = total_count - len(green_arr) - len(red_arr)
    blue_arr = get_color_list(blue_arr_count, blue_arr_count, "blue")
    three_colors_arr = green_arr + red_arr + blue_arr
    shuffle(three_colors_arr)
    three_colors_arr_to_string = ",".join(three_colors_arr)
    return three_colors_arr_to_string
