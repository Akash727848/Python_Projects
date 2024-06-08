def turn_right():
    turn_left()
    turn_left()
    turn_left()
def not_at_goal():
    while not at_goal():
        if front_is_clear():
            if right_is_clear():
                turn_right()
                move()
                continue
            if not right_is_clear():
                move()
                continue
        else:
            if right_is_clear():
                turn_right()
                move()
                continue
            else:
                turn_left()
                continue
not_at_goal()