import os
import random
class player:
    name = "none"          # Имя 
    money = 0              # Деньги
    health = 10            # Здоровье 
    def parameters_info(): # Вывод информации об характеристиках
        print("< < Статистика > >")
        print("Имя : " + player.name + "\n")
        print("Денежный баланс : " + str(player.money) + "\n")
        print("Здоровье : " + str(player.health))
    def dodge():

os.system("clear")
