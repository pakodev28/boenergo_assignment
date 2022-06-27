from random import choice


def try_to_guess_color(color_arr, index_number):
    """С помощью метода random.choice() выбираем случайный цвет из списка."""
    guessed_color = choice(color_arr)
    guessed_color = guessed_color
    if guessed_color == color_arr[index_number - 1]:
        return {"guessed_color": guessed_color, "is_correct": True}
    return {"guessed_color": guessed_color, "is_correct": False}
