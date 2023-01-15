import os
from os import system
import time
from data import *

chose = "none"
linux = "clear"
win = "cls"

start = False
print("Перед началом игры, укажи Свою Операционную систему")
sys = input("1)Windows 2)Linux \n:")
if sys == "1" or sys == "windows" or sys == "Windows":
    clear = win
elif sys == "2" or sys == "linux" or sys == "Linux":
    clear = linux

def game_skip():
    print("----")
    input()
    os.system(clear)

print("Желаешь начать игру ?")
game = input("1)Да 2)Нет \n:")
if game == "1" or game == "да" or game == "Да":
    start = True
    print("----")
    os.system(clear)
else:
    start = False
if start == True:
    while True:
        print("Выбери имя персонажа!")
        player.name = input(":")
        print("----")
        os.system(clear)
        print("Ты выбрал имя " + '"' + player.name + '"')
        while True:
            print("Оставишь это имя или все таки сменишь ?")
            try:
                chose = int(input("1)Оставлю, 2)Поменяю \n:"))
            except:
                print("Нужно ввести цыфру!")
                game_skip()
                continue
            finally:
                if chose == 1:
                    print("----")
                    os.system(clear)
                    cont = False
                    break
                elif chose == 2:
                    print("----")
                    os.system(clear)
                    cont = True
                    break
        if cont == False:
            del cont
            break
        elif cont == True:
            continue
    print("И так, ты остановился на имени " + '"' + player.name + '"')
    game_skip()
    print("Начнём игру!")
    time.sleep(0.5)
    os.system(clear)
    print("Ты встал с кровати , проверил часы")
    time.sleep(0.5)
    print("Ты --> [ Так, чуть не проспал ]")
    game_skip()
    print("Ты оделся и пошол на кухню в надежде на то что мама чтото приготовила.")
    game_skip()
    print("На кухне ты увидел маму.")
    game_skip()
    print("Она готовила плов.")
    game_skip()
    print("Ты был рад этому.")
    game_skip()
    print("Мама --> [" + player.name + ", хорошо что ты встал , мне как раз нужна помощь, иди собак покорми пожалуйста, и еще в магазин сходи за продуктами ]")
    game_skip()
    print("Ты --> [ Хорошо, мам! ]")
    game_skip()
    print("Ты пошол за собачьими мисками.")
    game_skip()
    print("Принёс их в дом и отсыпал в них еды для псов.")
    game_skip()
    print("Занёс им еду и подошел к маме с вопросом.")
    game_skip()
    print("Ты --> [ Мам! А что купить нужно ? ]")
    game_skip()
    print("Мама --> [ Две буханки хлеба, майонез, баночку кукурузки и баночку горошка  ]")
    game_skip()
    print("Мама --> [ Вот тебе деньги на продукты. ]")
    time.sleep(0.5)
    print("< < < Получено 100 грн > > >")
    time.sleep(0.5)
    player.money += 100
    print("Баланс : " + str(player.money) + " грн")
    game_skip()
    print("Ты --> [ Хорошо! Я пошол! ]")
    game_skip()
    print("Ты отправился в магазин.")
    game_skip()
    print("По дороге в магазин ты находишь на дороге 100 грн.")
    time.sleep(0.5)
    print("Взять их себе или оставить на дороге")
    time.sleep(0.5)
    print("1)Взять \n2)Оставить")
    time.sleep(0.5)
    while True:
        try:
            chose = int(input(":"))
        except:
            print("Введи цыфру!")
            time.sleep(0.5)
            continue
        finally:
            if chose == 1:
                cont = True
                player.money += 100
                print("Ты решаешь взять их себе")
                time.sleep(0.5)
                print("< < < Получено 100 грн > > >")
                time.sleep(0.5)
                print("Баланс : " + str(player.money) + " грн")
                game_skip()
                break
            elif chose == 2:
                cont = False
                print("Ты решил не брать эти деньги")
                time.sleep(0.5)
                print("Баланс : " + str(player.money) + " грн")
                game_skip()
                break
            elif chose < 1 or chose > 2:
                print("Введи число 1 или 2")
                time.sleep(0.5)
                continue
    print("Ты приходишь в магазин и говоришь продавщице .")
    game_skip()
    print("Ты --> [ Дайте пожалуйста 2 буханки хлеба , пачку майонеза, баночку кукурузки и горошка ]")
    game_skip()
    print("Продавщица --> [ С вас 155 грн! ]")
    game_skip()
    print("Баланс : " + str(player.money) + " грн")
    time.sleep(0.5)
    while True:
        if player.money >= 155:
            print("Вам хватает денег на продукты")
            time.sleep(0.5)
            print("Ты(в уме) --> [ Блин - еслиб я не подобрал те 100 гривен что я нашел, мне бы не хватило ]")
            game_skip()
            print("Баланс : " + str(player.money) + " грн")
            print("Ты расплачиваешся за продукты.")
            player.money -= 155
            time.sleep(0.5)
            print("< < < Отдано 155 грн > > >")
            time.sleep(0.5)
            print("Баланс : " + str(player.money) + " грн")
            game_skip()
            print("Ты уходишь с магазина неся продукты домой.")
            cont = 1
            break
        elif player.money < 155:
            print("Вам не хватает денег на продукты")
            time.sleep(0.5)
            print("Ты(в уме) --> [ Блин - не хватает. Мама дала недостаточно денег ]")
            game_skip()
            while True:
                print("1) Взять остальные продукты в долг,\n или\n 2) уйти с пустыми руками ?")
                try:
                    chose = int(input(":"))
                except:
                    print("Введите цыфру!")
                    continue
                finally:
                    if chose == 1:
                        print("Баланс : " + str(player.money) + " грн")
                        time.sleep(0.5)
                        player.money -= 155
                        time.sleep(1)
                        print("< < < Отдано 100 грн > > >")
                        print("< < < У вас долг : 55 грн > > >")
                        time.sleep(0.5)
                        print("Баланс : " + str(player.money) + " грн")
                        game_skip()
                        print("Вы ушли домой с продуктами")
                        game_skip()
                        print("Идя домой вы заметили, что тех денег которые вы нашли по дороге в магазин, уже нету\n, кто-то уже забрал их")
                        cont = 2
                        break
                    elif chose == 2:
                        print("Баланс : " + str(player.money) + " грн")
                        time.sleep(1)
                        print("Вы ушли думой без продуктов")
                        game_skip()
                        print("Идя домой вы заметили, что тех денег которые вы нашли по дороге в магазин, уже нету\n, кто-то уже забрал их")
                        cont = 3
                        break
                    elif chose < 1 or chose > 2:
                        print("Выберите цыфру 1 или 2")
                        continue
            break
    print("Ты пришол домой")
    game_skip()
    while True:
        if cont == 1:
            print("Баланс : " + str(player.money) + " грн")
            print("Ты --> [ Мам! ]")
            game_skip()
        elif cont == 2:
            print("Баланс : " + str(player.money) + " грн")
            print("Ты --> [ Мам! ]")
            game_skip()
            print("Баланс : " + str(player.money) + " грн")
            print("Мама --> [ Да? " + player.name + " Ты купил то, что я просила?")
            game_skip()
            print("Баланс : " + str(player.money) + " грн")
            print("Ты --> [ Да, я купил. Но тех денег что ты дала не хватило , поэтому я взял в долг те продукты , на которых не хватило денег ]")
            game_skip()
            print("Баланс : " + str(player.money) + " грн")
            print("Мама --> [ Охх, ладно, на 55 грн, пойди донеси]")
            time.sleep(0.5)
            player.money += 55
            print("< < < Получено 55 грн > > >")
            game_skip()
            print("Баланс : " + str(player.money) + " грн")
            print("Ты --> [ Хорошо, сейчас ]")
            game_skip()
            print("Ты пошел в магазин, отдавать долг")
            time.sleep(0.5)
            player.money -= 55
            print("< < < Отдано 55 грн > > >")
            break
        elif cont == 3:
            print("Баланс : " + str(player.money) + " грн")
            print("Ты --> [ Мам! ]")
            game_skip()