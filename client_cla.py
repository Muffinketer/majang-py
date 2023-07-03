import pygame
import math

pygame.init()


def draw_card(card_val, card):
    if card_val == 110:
        card = pygame.image.load("image/m1.jpg")
    elif card_val == 120:
        card = pygame.image.load("image/m2.jpg")
    elif card_val == 130:
        card = pygame.image.load("image/m3.jpg")
    elif card_val == 140:
        card = pygame.image.load("image/m4.jpg")
    elif card_val == 150:
        card = pygame.image.load("image/m5.jpg")
    elif card_val == 155:
        card = pygame.image.load("image/m5_d.jpg")
    elif card_val == 160:
        card = pygame.image.load("image/m6.jpg")
    elif card_val == 170:
        card = pygame.image.load("image/m7.jpg")
    elif card_val == 180:
        card = pygame.image.load("image/m8.jpg")
    elif card_val == 190:
        card = pygame.image.load("image/m9.jpg")

    elif card_val == 210:
        card = pygame.image.load("image/t1.jpg")
    elif card_val == 220:
        card = pygame.image.load("image/t2.jpg")
    elif card_val == 230:
        card = pygame.image.load("image/t3.jpg")
    elif card_val == 240:
        card = pygame.image.load("image/t4.jpg")
    elif card_val == 250:
        card = pygame.image.load("image/t5.jpg")
    elif card_val == 255:
        card = pygame.image.load("image/t5_d.jpg")
    elif card_val == 260:
        card = pygame.image.load("image/t6.jpg")
    elif card_val == 270:
        card = pygame.image.load("image/t7.jpg")
    elif card_val == 280:
        card = pygame.image.load("image/t8.jpg")
    elif card_val == 290:
        card = pygame.image.load("image/t9.jpg")

    elif card_val == 310:
        card = pygame.image.load("image/s1.jpg")
    elif card_val == 320:
        card = pygame.image.load("image/s2.jpg")
    elif card_val == 330:
        card = pygame.image.load("image/s3.jpg")
    elif card_val == 340:
        card = pygame.image.load("image/s4.jpg")
    elif card_val == 350:
        card = pygame.image.load("image/s5.jpg")
    elif card_val == 355:
        card = pygame.image.load("image/s5_d.jpg")
    elif card_val == 360:
        card = pygame.image.load("image/s6.jpg")
    elif card_val == 370:
        card = pygame.image.load("image/s7.jpg")
    elif card_val == 380:
        card = pygame.image.load("image/s8.jpg")
    elif card_val == 390:
        card = pygame.image.load("image/s9.jpg")

    elif card_val == 410:
        card = pygame.image.load("image/east.jpg")
    elif card_val == 420:
        card = pygame.image.load("image/south.jpg")
    elif card_val == 430:
        card = pygame.image.load("image/west.jpg")
    elif card_val == 440:
        card = pygame.image.load("image/north.jpg")

    elif card_val == 510:
        card = pygame.image.load("image/baek.jpg")
    elif card_val == 520:
        card = pygame.image.load("image/bal.jpg")
    elif card_val == 530:
        card = pygame.image.load("image/jung.jpg")

    elif card_val == 660:
        card = pygame.image.load("image/blank.png")

    else:
        card = pygame.image.load("image/hide.jpg")

    cardr = card.get_rect()

    return card


def input_pos(arr, where, cx, cy):
    x: int = 0
    y: int = 0

    if where == 1:
        x = 250
        y = 715 - cy
        for i in range(14):
            arr[i][0] += x
            arr[i][1] += y
            x += cx + 3
            if i == 13:
                arr[i][0] += 20


    elif where == 2:
        x = 1275 - cy
        y = 530
        for i in range(14):
            arr[i][0] += x
            arr[i][1] += y
            y -= cx + 3
            if i == 13:
                arr[i][1] -= 10
                arr[i][2] = 660

    elif where == 3:
        x = 850
        y = 3
        for i in range(14):
            arr[i][0] += x
            arr[i][1] += y
            x -= cx + 3
            if i == 13:
                arr[i][0] -= 10
                arr[i][2] = 660

    elif where == 4:
        x = 3
        y = 100
        for i in range(14):
            arr[i][0] += x
            arr[i][1] += y
            y += cx + 3
            if i == 13:
                arr[i][1] += 10
                arr[i][2] = 660

    elif where == 5:
        x = 530
        y = 435
        for i in range(3):
            for j in range(1,7):
                arr[i][(j*4)-4] += x
                arr[i][(j*4)-3] += y
                x += cx + 3
            x = 530
            y += cy + 3

    elif where == 6:
        x = 730
        y = 400
        for i in range(3):
            for j in range(1, 7):
                arr[i][(j * 4) - 4] += x
                arr[i][(j * 4) - 3] += y
                y -= cx + 3
            y = 400
            x += cy + 3

    elif where == 7:
        x = 695
        y = 185
        for i in range(3):
            for j in range(1, 7):
                arr[i][(j * 4) - 4] += x
                arr[i][(j * 4) - 3] += y
                x -= cx + 3
            x = 695
            y -= cy + 3

    elif where == 8:
        x = 480
        y = 235
        for i in range(3):
            for j in range(1, 7):
                arr[i][(j * 4) - 4] += x
                arr[i][(j * 4) - 3] += y
                y += cx + 3
            y = 235
            x -= cy + 3

def move_card(move_arr,play_arr,button_val):
    del move_arr[3]
    move_arr.insert(2,0)
    for i in range(3):
        move_arr[i] = play_arr[button_val][i]
    del play_arr[button_val][3]
    play_arr[button_val].insert(2,0)
    play_arr[button_val][2] = 660

def call_moving(move_arr,drop_arr,drop_val):
    result = [0,0]
    arr_i = 0
    arr_j = 0

    arr_i += ( (drop_val + 1) / 3 ) / 2
    if (drop_val + 1) == 6 or (drop_val + 1) == 12 or (drop_val + 1) == 18:
        arr_i -= 1
    arr_j += ( (drop_val + 1) * 4 ) - (24 * arr_i)
    result[0] += move_arr[0] - drop_arr[arr_i][(arr_j - 4)]
    result[1] += move_arr[1] - drop_arr[arr_i][(arr_j - 3)]
    if result[0] < 0:
        result[0] *= -1
    if result[1] < 0:
        result[1] *= -1

    return result



pygame.quit()
