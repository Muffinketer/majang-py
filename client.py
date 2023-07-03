import pygame
import random
import client_cla

s_wid = 1280
s_hei = 720

playc_x: int = 50
playc_y: int = 75

enm_x: int = 30
enm_y: int = 45

temp_x: int = 0
temp_y: int = 0

event_val = 0
turn_val: int = 1

menu_bt = [0,0]

mv_obj10_pos = [50,50]
mv_obj11_pos = [300,50]
mv_obj12_pos = [550,50]
mv_obj13_pos = [800,50]
mv_obj14_pos = [1050,50]
mv_obj15_pos = [1300,50]

mv_obj20_pos = [200,180]
mv_obj21_pos = [450,180]
mv_obj22_pos = [700,180]
mv_obj23_pos = [950,180]
mv_obj24_pos = [1200,180]
mv_obj25_pos = [1450,180]

mv_obj30_pos = [50,310]
mv_obj31_pos = [300,310]
mv_obj32_pos = [550,310]
mv_obj33_pos = [800,310]
mv_obj34_pos = [1050,310]
mv_obj35_pos = [1300,310]

mv_obj40_pos = [200,440]
mv_obj41_pos = [450,440]
mv_obj42_pos = [700,440]
mv_obj43_pos = [950,440]
mv_obj44_pos = [1200,440]
mv_obj45_pos = [1450,440]

mv_obj50_pos = [50,570]
mv_obj51_pos = [300,570]
mv_obj52_pos = [550,570]
mv_obj53_pos = [800,570]
mv_obj54_pos = [1050,570]
mv_obj55_pos = [1300,570]

drop0_val: int = 0
drop1_val: int = 0
drop2_val: int = 0
drop3_val: int = 0

val: int = 999
moving_leng: int = 0

allcard = [110,120,130,140,150,160,170,180,190, 210,220,230,240,250,260,270,280,290, 310,320,330,340,350,360,370,380,390, 410,420,430,440, 510,520,530, 110,120,130,140,150,160,170,180,190, 210,220,230,240,250,260,270,280,290, 310,320,330,340,350,360,370,380,390, 410,420,430,440, 510,520,530, 110,120,130,140,150,160,170,180,190, 210,220,230,240,250,260,270,280,290, 310,320,330,340,350,360,370,380,390, 410,420,430,440, 510,520,530, 110,120,130,140,155,160,170,180,190, 210,220,230,240,255,260,270,280,290, 310,320,330,340,355,360,370,380,390, 410,420,430,440, 510,520,530]

play1 = []
for i in range(14):
    play1.append(0)
enemy2 = []
for i in range(14):
    enemy2.append(0)
enemy3 = []
for i in range(14):
    enemy3.append(0)
enemy4 = []
for i in range(14):
    enemy4.append(0)
dora = []
for i in range(10):
    dora.append(0)
flower = []
for i in range(4):
    flower.append(0)

drop0_chg: int = 0
drop1_chg: int = 0

move_tmp: int = 0
movec_x: int = 0
movec_y: int = 0
move_pos = [0,0,660,0]

turn = True

play_pos = []
for i in range(14):
    line = []
    for j in range(4):
        line.append(0)
    play_pos.append(line)

enemy_pos1 = []
for i in range(14):
    line = []
    for j in range(4):
        line.append(0)
    enemy_pos1.append(line)

enemy_pos2 = []
for i in range(14):
    line = []
    for j in range(4):
        line.append(0)
    enemy_pos2.append(line)

enemy_pos3 = []
for i in range(14):
    line = []
    for j in range(4):
        line.append(0)
    enemy_pos3.append(line)


drop_pos0 = []
for i in range(3):
    line = []
    for j in range(24):
        line.append(0)
    drop_pos0.append(line)

drop_pos1 = []
for i in range(3):
    line = []
    for j in range(24):
        line.append(0)
    drop_pos1.append(line)

drop_pos2 = []
for i in range(3):
    line = []
    for j in range(24):
        line.append(0)
    drop_pos2.append(line)

drop_pos3 = []
for i in range(3):
    line = []
    for j in range(24):
        line.append(0)
    drop_pos3.append(line)

button = []
for i in range(24):
    button.append(0)

ym_lst = random.sample(allcard,14)


for i in range(14):
    play_pos[i][2] += ym_lst[i]

x_pos = 0
y_pos = 0

client_cla.input_pos(play_pos, 1, playc_x, playc_y)
client_cla.input_pos(enemy_pos1, 2, enm_x, enm_y)
client_cla.input_pos(enemy_pos2, 3, enm_x, enm_y)
client_cla.input_pos(enemy_pos3, 4, enm_x, enm_y)

client_cla.input_pos(drop_pos0, 5, enm_x, enm_y)
client_cla.input_pos(drop_pos1, 6, enm_x, enm_y)
client_cla.input_pos(drop_pos2, 7, enm_x, enm_y)
client_cla.input_pos(drop_pos3, 8, enm_x, enm_y)

for i in range(3):
    for j in range(1,7):
        drop_pos0[i][(j * 4) - 2] = 660
        drop_pos1[i][(j * 4) - 2] = 660
        drop_pos2[i][(j * 4) - 2] = 660
        drop_pos3[i][(j * 4) - 2] = 660

pygame.init()

screen = pygame.display.set_mode((s_wid, s_hei))
pygame.display.set_caption("pymajang")
clock = pygame.time.Clock()

roll = False

while not roll:

    while event_val == 0:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                roll = True
                event_val = 9
            if event.type == pygame.MOUSEMOTION:
                x_pos, y_pos = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and x_pos > 380 and y_pos > 560 and x_pos < 580 and y_pos < 660:
                    menu_bt[0] += 1
                if event.button == 1 and x_pos > 690 and y_pos > 560 and x_pos < 890 and y_pos < 660:
                    menu_bt[1] += 1
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1 and x_pos > 380 and y_pos > 560 and x_pos < 580 and y_pos < 660:
                    menu_bt[0] += 1
                if event.button == 1 and x_pos > 690 and y_pos > 560 and x_pos < 890 and y_pos < 660:
                    menu_bt[1] += 1

        if menu_bt[0] >= 2:
            event_val = 1
            menu_bt[0] = 0
        if menu_bt[1] >= 2:
            event_val = 9
            roll = True
            menu_bt[1] = 0

        backg = pygame.image.load("image_s/start_bg.jpg")
        screen.fill((0, 0, 0))
        screen.blit(backg, (0, 0))

        mv_obj10 = pygame.image.load("image_s/move01.jpg")
        mv_obj10_r = mv_obj10.get_rect()
        mv_obj11 = pygame.image.load("image_s/move01.jpg")
        mv_obj11_r = mv_obj11.get_rect()
        mv_obj12 = pygame.image.load("image_s/move01.jpg")
        mv_obj12_r = mv_obj12.get_rect()
        mv_obj13 = pygame.image.load("image_s/move01.jpg")
        mv_obj13_r = mv_obj13.get_rect()
        mv_obj14 = pygame.image.load("image_s/move01.jpg")
        mv_obj14_r = mv_obj14.get_rect()
        mv_obj15 = pygame.image.load("image_s/move01.jpg")
        mv_obj15_r = mv_obj15.get_rect()

        mv_obj20 = pygame.image.load("image_s/move02.jpg")
        mv_obj20_r = mv_obj20.get_rect()
        mv_obj21 = pygame.image.load("image_s/move02.jpg")
        mv_obj21_r = mv_obj21.get_rect()
        mv_obj22 = pygame.image.load("image_s/move02.jpg")
        mv_obj22_r = mv_obj22.get_rect()
        mv_obj23 = pygame.image.load("image_s/move02.jpg")
        mv_obj23_r = mv_obj23.get_rect()
        mv_obj24 = pygame.image.load("image_s/move02.jpg")
        mv_obj24_r = mv_obj24.get_rect()
        mv_obj25 = pygame.image.load("image_s/move02.jpg")
        mv_obj25_r = mv_obj25.get_rect()

        mv_obj30 = pygame.image.load("image_s/move03.jpg")
        mv_obj30_r = mv_obj30.get_rect()
        mv_obj31 = pygame.image.load("image_s/move03.jpg")
        mv_obj31_r = mv_obj31.get_rect()
        mv_obj32 = pygame.image.load("image_s/move03.jpg")
        mv_obj32_r = mv_obj32.get_rect()
        mv_obj33 = pygame.image.load("image_s/move03.jpg")
        mv_obj33_r = mv_obj33.get_rect()
        mv_obj34 = pygame.image.load("image_s/move03.jpg")
        mv_obj34_r = mv_obj34.get_rect()
        mv_obj35 = pygame.image.load("image_s/move03.jpg")
        mv_obj35_r = mv_obj35.get_rect()

        mv_obj40 = pygame.image.load("image_s/move02.jpg")
        mv_obj40_r = mv_obj40.get_rect()
        mv_obj41 = pygame.image.load("image_s/move02.jpg")
        mv_obj41_r = mv_obj41.get_rect()
        mv_obj42 = pygame.image.load("image_s/move02.jpg")
        mv_obj42_r = mv_obj42.get_rect()
        mv_obj43 = pygame.image.load("image_s/move02.jpg")
        mv_obj43_r = mv_obj43.get_rect()
        mv_obj44 = pygame.image.load("image_s/move02.jpg")
        mv_obj44_r = mv_obj44.get_rect()
        mv_obj45 = pygame.image.load("image_s/move02.jpg")
        mv_obj45_r = mv_obj45.get_rect()

        mv_obj50 = pygame.image.load("image_s/move01.jpg")
        mv_obj50_r = mv_obj50.get_rect()
        mv_obj51 = pygame.image.load("image_s/move01.jpg")
        mv_obj51_r = mv_obj51.get_rect()
        mv_obj52 = pygame.image.load("image_s/move01.jpg")
        mv_obj52_r = mv_obj52.get_rect()
        mv_obj53 = pygame.image.load("image_s/move01.jpg")
        mv_obj53_r = mv_obj53.get_rect()
        mv_obj54 = pygame.image.load("image_s/move01.jpg")
        mv_obj54_r = mv_obj54.get_rect()
        mv_obj55 = pygame.image.load("image_s/move01.jpg")
        mv_obj55_r = mv_obj55.get_rect()

        startb = pygame.image.load("image_s/start_bt.jpg")
        startb_r = startb.get_rect()
        startb = pygame.transform.scale(startb,(200, 100))
        exitb = pygame.image.load("image_s/exit_bt.jpg")
        exitb_r = exitb.get_rect()
        exitb = pygame.transform.scale(exitb, (200, 100))

        mv_obj10_pos[0] -= 2
        mv_obj11_pos[0] -= 2
        mv_obj12_pos[0] -= 2
        mv_obj13_pos[0] -= 2
        mv_obj14_pos[0] -= 2
        mv_obj15_pos[0] -= 2

        mv_obj20_pos[0] -= 2
        mv_obj21_pos[0] -= 2
        mv_obj22_pos[0] -= 2
        mv_obj23_pos[0] -= 2
        mv_obj24_pos[0] -= 2
        mv_obj25_pos[0] -= 2

        mv_obj30_pos[0] -= 2
        mv_obj31_pos[0] -= 2
        mv_obj32_pos[0] -= 2
        mv_obj33_pos[0] -= 2
        mv_obj34_pos[0] -= 2
        mv_obj35_pos[0] -= 2

        mv_obj40_pos[0] -= 2
        mv_obj41_pos[0] -= 2
        mv_obj42_pos[0] -= 2
        mv_obj43_pos[0] -= 2
        mv_obj44_pos[0] -= 2
        mv_obj45_pos[0] -= 2

        mv_obj50_pos[0] -= 2
        mv_obj51_pos[0] -= 2
        mv_obj52_pos[0] -= 2
        mv_obj53_pos[0] -= 2
        mv_obj54_pos[0] -= 2
        mv_obj55_pos[0] -= 2

        screen.blit(mv_obj10, (mv_obj10_pos[0], mv_obj10_pos[1]))
        screen.blit(mv_obj11, (mv_obj11_pos[0], mv_obj11_pos[1]))
        screen.blit(mv_obj12, (mv_obj12_pos[0], mv_obj12_pos[1]))
        screen.blit(mv_obj13, (mv_obj13_pos[0], mv_obj13_pos[1]))
        screen.blit(mv_obj14, (mv_obj14_pos[0], mv_obj14_pos[1]))
        screen.blit(mv_obj15, (mv_obj15_pos[0], mv_obj15_pos[1]))

        screen.blit(mv_obj20, (mv_obj20_pos[0], mv_obj20_pos[1]))
        screen.blit(mv_obj21, (mv_obj21_pos[0], mv_obj21_pos[1]))
        screen.blit(mv_obj22, (mv_obj22_pos[0], mv_obj22_pos[1]))
        screen.blit(mv_obj23, (mv_obj23_pos[0], mv_obj23_pos[1]))
        screen.blit(mv_obj24, (mv_obj24_pos[0], mv_obj24_pos[1]))
        screen.blit(mv_obj25, (mv_obj25_pos[0], mv_obj25_pos[1]))

        screen.blit(mv_obj30, (mv_obj30_pos[0], mv_obj30_pos[1]))
        screen.blit(mv_obj31, (mv_obj31_pos[0], mv_obj31_pos[1]))
        screen.blit(mv_obj32, (mv_obj32_pos[0], mv_obj32_pos[1]))
        screen.blit(mv_obj33, (mv_obj33_pos[0], mv_obj33_pos[1]))
        screen.blit(mv_obj34, (mv_obj34_pos[0], mv_obj34_pos[1]))
        screen.blit(mv_obj35, (mv_obj35_pos[0], mv_obj35_pos[1]))

        screen.blit(mv_obj40, (mv_obj40_pos[0], mv_obj40_pos[1]))
        screen.blit(mv_obj41, (mv_obj41_pos[0], mv_obj41_pos[1]))
        screen.blit(mv_obj42, (mv_obj42_pos[0], mv_obj42_pos[1]))
        screen.blit(mv_obj43, (mv_obj43_pos[0], mv_obj43_pos[1]))
        screen.blit(mv_obj44, (mv_obj44_pos[0], mv_obj44_pos[1]))
        screen.blit(mv_obj45, (mv_obj45_pos[0], mv_obj45_pos[1]))

        screen.blit(mv_obj50, (mv_obj50_pos[0], mv_obj50_pos[1]))
        screen.blit(mv_obj51, (mv_obj51_pos[0], mv_obj51_pos[1]))
        screen.blit(mv_obj52, (mv_obj52_pos[0], mv_obj52_pos[1]))
        screen.blit(mv_obj53, (mv_obj53_pos[0], mv_obj53_pos[1]))
        screen.blit(mv_obj54, (mv_obj54_pos[0], mv_obj54_pos[1]))
        screen.blit(mv_obj55, (mv_obj55_pos[0], mv_obj55_pos[1]))

        screen.blit(startb, (380, 560))
        screen.blit(exitb, (690, 560))

        pygame.display.update()

        if mv_obj10_pos[0] <= -200:
            mv_obj10_pos[0] = 1300
        if mv_obj11_pos[0] <= -200:
            mv_obj11_pos[0] = 1300
        if mv_obj12_pos[0] <= -200:
            mv_obj12_pos[0] = 1300
        if mv_obj13_pos[0] <= -200:
            mv_obj13_pos[0] = 1300
        if mv_obj14_pos[0] <= -200:
            mv_obj14_pos[0] = 1300
        if mv_obj15_pos[0] <= -200:
            mv_obj15_pos[0] = 1300

        if mv_obj20_pos[0] <= -50:
            mv_obj20_pos[0] = 1450
        if mv_obj21_pos[0] <= -50:
            mv_obj21_pos[0] = 1450
        if mv_obj22_pos[0] <= -50:
            mv_obj22_pos[0] = 1450
        if mv_obj23_pos[0] <= -50:
            mv_obj23_pos[0] = 1450
        if mv_obj24_pos[0] <= -50:
            mv_obj24_pos[0] = 1450
        if mv_obj25_pos[0] <= -50:
            mv_obj25_pos[0] = 1450

        if mv_obj30_pos[0] <= -200:
            mv_obj30_pos[0] = 1300
        if mv_obj31_pos[0] <= -200:
            mv_obj31_pos[0] = 1300
        if mv_obj32_pos[0] <= -200:
            mv_obj32_pos[0] = 1300
        if mv_obj33_pos[0] <= -200:
            mv_obj33_pos[0] = 1300
        if mv_obj34_pos[0] <= -200:
            mv_obj34_pos[0] = 1300
        if mv_obj35_pos[0] <= -200:
            mv_obj35_pos[0] = 1300

        if mv_obj40_pos[0] <= -50:
            mv_obj40_pos[0] = 1450
        if mv_obj41_pos[0] <= -50:
            mv_obj41_pos[0] = 1450
        if mv_obj42_pos[0] <= -50:
            mv_obj42_pos[0] = 1450
        if mv_obj43_pos[0] <= -50:
            mv_obj43_pos[0] = 1450
        if mv_obj44_pos[0] <= -50:
            mv_obj44_pos[0] = 1450
        if mv_obj45_pos[0] <= -50:
            mv_obj45_pos[0] = 1450

        if mv_obj50_pos[0] <= -200:
            mv_obj50_pos[0] = 1300
        if mv_obj51_pos[0] <= -200:
            mv_obj51_pos[0] = 1300
        if mv_obj52_pos[0] <= -200:
            mv_obj52_pos[0] = 1300
        if mv_obj53_pos[0] <= -200:
            mv_obj53_pos[0] = 1300
        if mv_obj54_pos[0] <= -200:
            mv_obj54_pos[0] = 1300
        if mv_obj55_pos[0] <= -200:
            mv_obj55_pos[0] = 1300

        clock.tick(60)

    backg = 0

    while event_val == 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                roll = True
                event_val = 9
            if event.type == pygame.MOUSEMOTION:
                x_pos, y_pos = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN and turn_val == 1:
                if event.button == 1 and x_pos > 250 and x_pos < 300 and y_pos > 640 and y_pos < 715:
                    button[0] += 1
                if event.button == 1 and x_pos > 303 and x_pos < 353 and y_pos > 640 and y_pos < 715:
                    button[1] += 1
                if event.button == 1 and x_pos > 356 and x_pos < 406 and y_pos > 640 and y_pos < 715:
                    button[2] += 1
                if event.button == 1 and x_pos > 409 and x_pos < 459 and y_pos > 640 and y_pos < 715:
                    button[3] += 1
                if event.button == 1 and x_pos > 462 and x_pos < 512 and y_pos > 640 and y_pos < 715:
                    button[4] += 1
                if event.button == 1 and x_pos > 515 and x_pos < 565 and y_pos > 640 and y_pos < 715:
                    button[5] += 1
                if event.button == 1 and x_pos > 568 and x_pos < 618 and y_pos > 640 and y_pos < 715:
                    button[6] += 1
                if event.button == 1 and x_pos > 621 and x_pos < 671 and y_pos > 640 and y_pos < 715:
                    button[7] += 1
                if event.button == 1 and x_pos > 674 and x_pos < 724 and y_pos > 640 and y_pos < 715:
                    button[8] += 1
                if event.button == 1 and x_pos > 727 and x_pos < 777 and y_pos > 640 and y_pos < 715:
                    button[9] += 1
                if event.button == 1 and x_pos > 780 and x_pos < 830 and y_pos > 640 and y_pos < 715:
                    button[10] += 1
                if event.button == 1 and x_pos > 833 and x_pos < 883 and y_pos > 640 and y_pos < 715:
                    button[11] += 1
                if event.button == 1 and x_pos > 886 and x_pos < 936 and y_pos > 640 and y_pos < 715:
                    button[12] += 1
                if event.button == 1 and x_pos > 959 and x_pos < 1009 and y_pos > 640 and y_pos < 715:
                    button[13] += 1

            if event.type == pygame.MOUSEBUTTONUP and turn_val == 1:
                if event.button == 1 and x_pos > 250 and x_pos < 300 and y_pos > 640 and y_pos < 715:
                    button[0] += 1
                if event.button == 1 and x_pos > 303 and x_pos < 353 and y_pos > 640 and y_pos < 715:
                    button[1] += 1
                if event.button == 1 and x_pos > 356 and x_pos < 406 and y_pos > 640 and y_pos < 715:
                    button[2] += 1
                if event.button == 1 and x_pos > 409 and x_pos < 459 and y_pos > 640 and y_pos < 715:
                    button[3] += 1
                if event.button == 1 and x_pos > 462 and x_pos < 512 and y_pos > 640 and y_pos < 715:
                    button[4] += 1
                if event.button == 1 and x_pos > 515 and x_pos < 565 and y_pos > 640 and y_pos < 715:
                    button[5] += 1
                if event.button == 1 and x_pos > 568 and x_pos < 618 and y_pos > 640 and y_pos < 715:
                    button[6] += 1
                if event.button == 1 and x_pos > 621 and x_pos < 671 and y_pos > 640 and y_pos < 715:
                    button[7] += 1
                if event.button == 1 and x_pos > 674 and x_pos < 724 and y_pos > 640 and y_pos < 715:
                    button[8] += 1
                if event.button == 1 and x_pos > 727 and x_pos < 777 and y_pos > 640 and y_pos < 715:
                    button[9] += 1
                if event.button == 1 and x_pos > 780 and x_pos < 830 and y_pos > 640 and y_pos < 715:
                    button[10] += 1
                if event.button == 1 and x_pos > 833 and x_pos < 883 and y_pos > 640 and y_pos < 715:
                    button[11] += 1
                if event.button == 1 and x_pos > 886 and x_pos < 936 and y_pos > 640 and y_pos < 715:
                    button[12] += 1
                if event.button == 1 and x_pos > 959 and x_pos < 1009 and y_pos > 640 and y_pos < 715:
                    button[13] += 1

        backg = pygame.image.load("image/backg.jpg")
        screen.fill((0, 0, 0))
        screen.blit(backg, (0, 0))

        if turn_val == 0:
            random.shuffle(allcard)


        if turn_val == 1:
            if button[0] >= 2:
                client_cla.move_card(move_pos,play_pos,0)
                button[0] = 0
                move_tmp += 1
            if move_tmp == 1:
                move_pos[0] += 15
                move_pos[1] -= 13
            if move_pos[0] >= 530 and move_tmp == 1:
                move_pos[0] = 530
                move_pos[1] = 435
                drop0_val += 1
                move_tmp = 0
                drop0_chg = 1

            if button[1] >= 2:
                client_cla.move_card(move_pos,play_pos,1)
                button[1] = 0
                move_tmp += 1
            if move_tmp == 2:
                move_pos[0] += 15
                move_pos[1] -= 13
            if move_pos[0] >= 530 and move_tmp == 2:
                move_pos[0] = 530
                move_pos[1] = 435
                drop0_val += 1
                move_tmp = 0
                drop0_chg = 1

            if button[2] >= 2:
                client_cla.move_card(move_pos,play_pos,2)
                button[2] = 0
                move_tmp += 1
            if move_tmp == 2:
                move_pos[0] += 15
                move_pos[1] -= 13
            if move_pos[0] >= 530 and move_tmp == 2:
                move_pos[0] = 530
                move_pos[1] = 435
                drop0_val += 1
                move_tmp = 0
                drop0_chg = 1

            if button[3] >= 2:
                client_cla.move_card(move_pos,play_pos,3)
                button[3] = 0
                move_tmp += 1
            if move_tmp == 2:
                move_pos[0] += 15
                move_pos[1] -= 13
            if move_pos[0] >= 530 and move_tmp == 2:
                move_pos[0] = 530
                move_pos[1] = 435
                drop0_val += 1
                move_tmp = 0
                drop0_chg = 1

            if button[4] >= 2:
                client_cla.move_card(move_pos,play_pos,4)
                button[4] = 0
                move_tmp += 1
            if move_tmp == 2:
                move_pos[0] += 15
                move_pos[1] -= 13
            if move_pos[0] >= 530 and move_tmp == 2:
                move_pos[0] = 530
                move_pos[1] = 435
                drop0_val += 1
                move_tmp = 0
                drop0_chg = 1

            if button[5] >= 2:
                client_cla.move_card(move_pos,play_pos,5)
                button[5] = 0
                move_tmp += 1
            if move_tmp == 2:
                move_pos[0] += 15
                move_pos[1] -= 13
            if move_pos[0] >= 530 and move_tmp == 2:
                move_pos[0] = 530
                move_pos[1] = 435
                drop0_val += 1
                move_tmp = 0
                drop0_chg = 1

            if button[6] >= 2:
                client_cla.move_card(move_pos,play_pos,6)
                button[6] = 0
                move_tmp += 1
            if move_tmp == 2:
                move_pos[0] += 15
                move_pos[1] -= 13
            if move_pos[0] >= 530 and move_tmp == 2:
                move_pos[0] = 530
                move_pos[1] = 435
                drop0_val += 1
                move_tmp = 0
                drop0_chg = 1

            if button[7] >= 2:
                client_cla.move_card(move_pos,play_pos,7)
                button[7] = 0
                move_tmp += 1
            if move_tmp == 2:
                move_pos[0] += 15
                move_pos[1] -= 13
            if move_pos[0] >= 530 and move_tmp == 2:
                move_pos[0] = 530
                move_pos[1] = 435
                drop0_val += 1
                move_tmp = 0
                drop0_chg = 1

            if button[8] >= 2:
                client_cla.move_card(move_pos, play_pos,8)
                button[8] = 0
                move_tmp += 1
            if move_tmp == 2:
                move_pos[0] += 15
                move_pos[1] -= 13
            if move_pos[0] >= 530 and move_tmp == 2:
                move_pos[0] = 530
                move_pos[1] = 435
                drop0_val += 1
                move_tmp = 0
                drop0_chg = 1

            if button[9] >= 2:
                client_cla.move_card(move_pos,play_pos,9)
                button[9] = 0
                move_tmp += 1
            if move_tmp == 2:
                move_pos[0] += 15
                move_pos[1] -= 13
            if move_pos[0] >= 530 and move_tmp == 2:
                move_pos[0] = 530
                move_pos[1] = 435
                drop0_val += 1
                move_tmp = 0
                drop0_chg = 1

            if button[10] >= 2:
                client_cla.move_card(move_pos,play_pos,10)
                button[10] = 0
                move_tmp += 1
            if move_tmp == 2:
                move_pos[0] += 15
                move_pos[1] -= 13
            if move_pos[0] >= 530 and move_tmp == 2:
                move_pos[0] = 530
                move_pos[1] = 435
                drop0_val += 1
                move_tmp = 0
                drop0_chg = 1

            if button[11] >= 2:
                client_cla.move_card(move_pos,play_pos,11)
                button[11] = 0
                move_tmp += 1
            if move_tmp == 2:
                move_pos[0] += 15
                move_pos[1] -= 13
            if move_pos[0] >= 530 and move_tmp == 2:
                move_pos[0] = 530
                move_pos[1] = 435
                drop0_val += 1
                move_tmp = 0
                drop0_chg = 1

            if button[12] >= 2:
                client_cla.move_card(move_pos,play_pos,12)
                button[12] = 0
                move_tmp += 1
            if move_tmp == 2:
                move_pos[0] += 15
                move_pos[1] -= 13
            if move_pos[0] >= 530 and move_tmp == 2:
                move_pos[0] = 530
                move_pos[1] = 435
                drop0_val += 1
                move_tmp = 0
                drop0_chg = 1

            if button[13] >= 2:
                client_cla.move_card(move_pos, play_pos,13)
                button[13] = 0
                move_tmp += 14
            if move_tmp == 14:
                move_pos[0] -= 20
                move_pos[1] -= 10
            if move_pos[0] <= 530 and move_tmp == 14:
                move_pos[0] = 530
                move_pos[1] = 435
                drop0_val += 1
                move_tmp = 0
                drop0_chg = 1

            if drop0_val > 0 and drop0_chg == 1:
                if drop0_val < 7:
                    del drop_pos0[0][(drop0_val*4)-1]
                    drop_pos0[0].insert((drop0_val*4)-2,0)
                    drop_pos0[0][(drop0_val*4)-2] = move_pos[2]
                elif drop0_val < 13:
                    del drop_pos0[1][((drop0_val-6) * 4) - 1]
                    drop_pos0[1].insert(((drop0_val-6) * 4) - 2, 0)
                    drop_pos0[1][((drop0_val-6) * 4) - 2] = move_pos[2]
                elif drop0_val < 19:
                    del drop_pos0[2][((drop0_val-12) * 4) - 1]
                    drop_pos0[2].insert(((drop0_val-12) * 4) - 2, 0)
                    drop_pos0[2][((drop0_val-12) * 4) - 2] = move_pos[2]
                del move_pos[3]
                move_pos.insert(2,0)
                move_pos[2] = 660
                drop0_chg = 0
                turn_val += 1

        if turn_val == 2:
            if move_tmp == 0:
                move_pos[0] = enemy_pos1[13][0]
                move_pos[1] = enemy_pos1[13][1]
                del move_pos[3]
                move_pos.insert(2,0)
                move_pos[2] = 530
                move_tmp += 20

            if move_tmp == 20:
                move_pos[0] -= 20
                move_pos[1] += 10
            if move_pos[0] <= 700 and move_tmp == 20:
                move_pos[0] = drop_pos1[0][0]
                move_pos[1] = drop_pos1[0][1]
                drop1_val += 1
                drop0_chg = 1
                move_tmp = 0

            if drop1_val > 0 and drop0_chg == 1:
                if drop1_val < 7:
                    del drop_pos1[0][(drop1_val*4)-1]
                    drop_pos1[0].insert((drop1_val*4)-2,0)
                    drop_pos1[0][(drop1_val*4)-2] = move_pos[2]
                elif drop1_val < 13:
                    del drop_pos1[1][((drop1_val-6) * 4) - 1]
                    drop_pos1[1].insert(((drop1_val-6) * 4) - 2, 0)
                    drop_pos1[1][((drop1_val-6) * 4) - 2] = move_pos[2]
                elif drop1_val < 19:
                    del drop_pos1[2][((drop1_val-12) * 4) - 1]
                    drop_pos1[2].insert(((drop1_val-12) * 4) - 2, 0)
                    drop_pos1[2][((drop1_val-12) * 4) - 2] = move_pos[2]
                del move_pos[3]
                move_pos.insert(2,0)
                move_pos[2] = 660
                drop0_chg = 0
                turn_val += 1

        if turn_val == 3:
            if move_tmp == 0:
                move_pos[0] = enemy_pos2[13][0]
                move_pos[1] = enemy_pos2[13][1]
                del move_pos[3]
                move_pos.insert(2,0)
                move_pos[2] = 530
                move_tmp += 20

            if move_tmp == 20:
                move_pos[0] += 20
                move_pos[1] += 10
            if move_pos[0] <= 900 and move_tmp == 20:
                move_pos[0] = drop_pos2[0][0]
                move_pos[1] = drop_pos2[0][1]
                drop2_val += 1
                drop0_chg = 1
                move_tmp = 0

            if drop2_val > 0 and drop0_chg == 1:
                if drop2_val < 7:
                    del drop_pos2[0][(drop2_val*4)-1]
                    drop_pos2[0].insert((drop2_val*4)-2,0)
                    drop_pos2[0][(drop2_val*4)-2] = move_pos[2]
                elif drop2_val < 13:
                    del drop_pos2[1][((drop2_val-6) * 4) - 1]
                    drop_pos2[1].insert(((drop2_val-6) * 4) - 2, 0)
                    drop_pos2[1][((drop2_val-6) * 4) - 2] = move_pos[2]
                elif drop2_val < 19:
                    del drop_pos2[2][((drop2_val-12) * 4) - 1]
                    drop_pos2[2].insert(((drop2_val-12) * 4) - 2, 0)
                    drop_pos2[2][((drop2_val-12) * 4) - 2] = move_pos[2]
                del move_pos[3]
                move_pos.insert(2,0)
                move_pos[2] = 660
                drop0_chg = 0
                turn_val += 1

        if turn_val == 4:
            if move_tmp == 0:
                move_pos[0] = enemy_pos2[13][0]
                move_pos[1] = enemy_pos2[13][1]
                del move_pos[3]
                move_pos.insert(2,0)
                move_pos[2] = 530
                move_tmp += 20

            if move_tmp == 20:
                move_pos[0] += 20
                move_pos[1] += 10
            if move_pos[0] <= 900 and move_tmp == 20:
                move_pos[0] = drop_pos2[0][0]
                move_pos[1] = drop_pos2[0][1]
                drop3_val += 1
                drop0_chg = 1
                move_tmp = 0

            if drop3_val > 0 and drop0_chg == 1:
                if drop3_val < 7:
                    del drop_pos3[0][(drop3_val*4)-1]
                    drop_pos3[0].insert((drop3_val*4)-2,0)
                    drop_pos3[0][(drop3_val*4)-2] = move_pos[2]
                elif drop3_val < 13:
                    del drop_pos3[1][((drop3_val-6) * 4) - 1]
                    drop_pos3[1].insert(((drop3_val-6) * 4) - 2, 0)
                    drop_pos3[1][((drop3_val-6) * 4) - 2] = move_pos[2]
                elif drop3_val < 19:
                    del drop_pos3[2][((drop3_val-12) * 4) - 1]
                    drop_pos3[2].insert(((drop3_val-12) * 4) - 2, 0)
                    drop_pos3[2][((drop3_val-12) * 4) - 2] = move_pos[2]
                del move_pos[3]
                move_pos.insert(2,0)
                move_pos[2] = 660
                drop0_chg = 0
                turn_val = 1

        if turn_val >= 4:
            turn_val = 0

        for i in range(14):
            ym_lst[i] = play_pos[i][2]
        ym_lst.sort()
        for i in range(14):
            play_pos[i][2] = ym_lst[i]

        screen.blit(backg, (0, 0))

        for i in range(14):
            play_pos[i][3] = client_cla.draw_card(play_pos[i][2], play_pos[i][3])
            play_pos[i][3] = pygame.transform.scale(play_pos[i][3], (playc_x, playc_y))
            screen.blit(play_pos[i][3], (play_pos[i][0], play_pos[i][1]))

        for i in range(14):
            enemy_pos1[i][3] = client_cla.draw_card(enemy_pos1[i][2], enemy_pos1[i][3])
            enemy_pos1[i][3] = pygame.transform.scale(enemy_pos1[i][3], (enm_x, enm_y))
            enemy_pos1[i][3] = pygame.transform.rotate(enemy_pos1[i][3], 90)
            screen.blit(enemy_pos1[i][3], (enemy_pos1[i][0], enemy_pos1[i][1]))

        for i in range(14):
            enemy_pos2[i][3] = client_cla.draw_card(enemy_pos2[i][2], enemy_pos2[i][3])
            enemy_pos2[i][3] = pygame.transform.scale(enemy_pos2[i][3], (enm_x, enm_y))
            screen.blit(enemy_pos2[i][3], (enemy_pos2[i][0], enemy_pos2[i][1]))

        for i in range(14):
            enemy_pos3[i][3] = client_cla.draw_card(enemy_pos3[i][2], enemy_pos3[i][3])
            enemy_pos3[i][3] = pygame.transform.scale(enemy_pos3[i][3], (enm_x, enm_y))
            enemy_pos3[i][3] = pygame.transform.rotate(enemy_pos3[i][3], 90)
            screen.blit(enemy_pos3[i][3], (enemy_pos3[i][0], enemy_pos3[i][1]))

        for i in range(3):
            for j in range(1,7):
                drop_pos0[i][(j*4)-1] = client_cla.draw_card(drop_pos0[i][(j*4)-2], drop_pos0[i][(j*4)-1])
                drop_pos0[i][(j*4)-1] = pygame.transform.scale(drop_pos0[i][(j*4)-1], (enm_x,enm_y))
                screen.blit(drop_pos0[i][(j*4)-1], (drop_pos0[i][(j*4)-4], drop_pos0[i][(j*4)-3]))

        for i in range(3):
            for j in range(1,7):
                drop_pos1[i][(j*4)-1] = client_cla.draw_card(drop_pos1[i][(j*4)-2], drop_pos1[i][(j*4)-1])
                drop_pos1[i][(j*4)-1] = pygame.transform.scale(drop_pos1[i][(j*4)-1], (enm_x,enm_y))
                drop_pos1[i][(j*4)-1] = pygame.transform.rotate(drop_pos1[i][(j*4)-1], 90)
                screen.blit(drop_pos1[i][(j*4)-1], (drop_pos1[i][(j*4)-4], drop_pos1[i][(j*4)-3]))

        for i in range(3):
            for j in range(1,7):
                drop_pos2[i][(j*4)-1] = client_cla.draw_card(drop_pos2[i][(j*4)-2], drop_pos2[i][(j*4)-1])
                drop_pos2[i][(j*4)-1] = pygame.transform.scale(drop_pos2[i][(j*4)-1], (enm_x,enm_y))
                screen.blit(drop_pos2[i][(j*4)-1], (drop_pos2[i][(j*4)-4], drop_pos2[i][(j*4)-3]))

        for i in range(3):
            for j in range(1,7):
                drop_pos3[i][(j*4)-1] = client_cla.draw_card(drop_pos3[i][(j*4)-2], drop_pos3[i][(j*4)-1])
                drop_pos3[i][(j*4)-1] = pygame.transform.scale(drop_pos3[i][(j*4)-1], (enm_x,enm_y))
                drop_pos3[i][(j*4)-1] = pygame.transform.rotate(drop_pos3[i][(j*4)-1], 90)
                screen.blit(drop_pos3[i][(j*4)-1], (drop_pos3[i][(j*4)-4], drop_pos3[i][(j*4)-3]))

        move_pos[3] = client_cla.draw_card(move_pos[2], move_pos[3])
        move_pos[3] = pygame.transform.scale(move_pos[3], (enm_x,enm_y))

        if turn_val == 2:
            move_pos[3] = pygame.transform.rotate(move_pos[3], 90)
        if turn_val == 3:
            move_pos[3] = pygame.transform.rotate(move_pos[3], 180)
        if turn_val == 4:
            move_pos[3] = pygame.transform.rotate(move_pos[3], 270)

        screen.blit(move_pos[3], (move_pos[0],move_pos[1]))

        scpanel = pygame.image.load("image/score.jpg")
        scpanel_r = scpanel.get_rect()
        scpanel = pygame.transform.scale(scpanel, (200, 200))
        screen.blit(scpanel, (527, 233))

        pygame.display.update()
        clock.tick(60)

pygame.quit()
