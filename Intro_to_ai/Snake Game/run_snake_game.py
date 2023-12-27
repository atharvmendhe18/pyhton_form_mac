import pyautogui
from che3ck_differcence import is_in_range


def give_direction(
    headX, headY, foodX, foodY, direction_of_head=None, snake_coordinates_list=None
):
    if direction_of_head == "up" or direction_of_head == "down":
        if not is_in_range(headX, foodX):
            if headX - foodX > 0:
                if direction_of_head != "left":
                    pyautogui.press("left")
            else:
                if direction_of_head != "rigth":
                    pyautogui.press("right")
        elif headY >= 615 or headY <= 10:
            if direction_of_head != "left":
                pyautogui.press("left")

    elif direction_of_head == "right" or direction_of_head == "left":
        if is_in_range(headX, foodX):
            if headY - foodY > 0:
                if direction_of_head != "up":
                    pyautogui.press("up")
            else:
                if direction_of_head != "down":
                    pyautogui.press("down")
        elif headX >= 615 or headX <= 10:
            if direction_of_head != "left":
                pyautogui.press("up")
