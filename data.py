import os
import random


def parameters_info():  # Вывод информации об характеристиках
    print("< < Статистика > >")
    print(f"Имя --> {player.name}")
    print(f"Баланс --> {player.money}")
    print(f"Здоровье --> {player.health}")
    print(f"Болезни --> {player.disease}")


class player:
    name = "none"  # Имя
    money = 0  # Деньги
    health = 10  # Здоровье
    disease = []  # Болезни
    stat = {
        "name": name,
        "money": money,
        "health": health,
        "disease": disease
    }


class games:
    class permissions:
        basketball = {
            "level_1": True,
            "level_2": False,
            "level_3": False,
            "level_4": False,
            "level_5": False,
            "level_6": False,
            "level_7": False,
            "level_8": False,
            "level_9": False,
            "level_10": False
        }
        football = {
            "level_1": True,
            "level_2": False,
            "level_3": False,
            "level_4": False,
            "level_5": False,
            "level_6": False,
            "level_7": False,
            "level_8": False,
            "level_9": False,
            "level_10": False
        }
        golf = {
            "level_1": True,
            "level_2": False,
            "level_3": False,
            "level_4": False,
            "level_5": False,
            "level_6": False,
            "level_7": False,
            "level_8": False,
            "level_9": False,
            "level_10": False
        }
        quess_the_number = {
            "level_1": True,
            "level_2": False,
            "level_3": False,
            "level_4": False,
            "level_5": False,
            "level_6": False,
            "level_7": False,
            "level_8": False,
            "level_9": False,
            "level_10": False
        }
        puzzles = {
            "level_1": True,
            "level_2": False,
            "level_3": False,
            "level_4": False,
            "level_5": False,
            "level_6": False,
            "level_7": False,
            "level_8": False,
            "level_9": False,
            "level_10": False
        }

    basket = permissions.basketball
    foot = permissions.football
    glf = permissions.golf
    q_t_n = permissions.quess_the_number
    puz = permissions.puzzles

    def basketball(self):
        bb = True
        while bb:
            if self == "1":
                if games.basket["level_1"]:
                    print("Начало игры")
                else:
                    print("Уровень заблокирован!")
            if self == "2":
                if games.basket["level_2"]:
                    print("Начало игры")
                else:
                    print("Уровень заблокирован")
            if self == "3":
                if games.basket["level_3"]:
                    print("Начало игры")
                else:
                    print("Уровень заблокирован")
            if self == "4":
                if games.basket["level_4"]:
                    print("Начало игры")
                else:
                    print("Уровень заблокирован")
            if self == "5":
                if games.basket["level_5"]:
                    print("Начало игры")
                else:
                    print("Уровень заблокирован")
            if self == "6":
                if games.basket["level_6"]:
                    print("Начало игры")
                else:
                    print("Уровень заблокирован")
            if self == "7":
                if games.basket["level_7"]:
                    print("Начало игры")
                else:
                    print("Уровень заблокирован")
            if self == "8":
                if games.basket["level_8"]:
                    print("Начало игры")
                else:
                    print("Уровень заблокирован")
            if self == "9":
                if games.basket["level_9"]:
                    print("Начало игры")
                else:
                    print("Уровень заблокирован")
            if self == "10":
                if games.basket["level_10"]:
                    print("Начало игры")
                else:
                    print("Уровень заблокирован")

    def football(self):
        fb = True
        while fb:
            if self == "1":
                if games.foot["level_1"]:
                    print("Начало игры")
                else:
                    print("Уровень заблокирован")
            if self == "2":
                if games.foot["level_2"]:
                    print("Начало игры")
                else:
                    print("Уровень заблокирован")
            if self == "3":
                if games.foot["level_3"]:
                    print("Начало игры")
                else:
                    print("Уровень заблокирован")
            if self == "4":
                if games.foot["level_4"]:
                    print("Начало игры")
                else:
                    print("Уровень заблокирован")
            if self == "5":
                if games.foot["level_5"]:
                    print("Начало игры")
                else:
                    print("Уровень заблокирован")
            if self == "6":
                if games.foot["level_6"]:
                    print("Начало игры")
                else:
                    print("Уровень заблокирован")
            if self == "7":
                if games.foot["level_7"]:
                    print("Начало игры")
                else:
                    print("Уровень заблокирован")
            if self == "8":
                if games.foot["level_8"]:
                    print("Начало игры")
                else:
                    print("Уровень заблокирован")
            if self == "9":
                if games.foot["level_9"]:
                    print("Начало игры")
                else:
                    print("Уровень заблокирован")
            if self == "10":
                if games.foot["level_10"]:
                    print("Начало игры")
                else:
                    print("Уровень заблокирован")

    def golf(self):
        gf = True
        while gf:
            if self == "1":
                if games.glf["level_1"]:
                    print("Начало игры")
                else:
                    print("Уровень заблокирован!")
            if self == "2":
                if games.glf["level_2"]:
                    print("Начало игры")
                else:
                    print("Уровень заблокирован!")
            if self == "3":
                if games.glf["level_3"]:
                    print("Начало игры")
                else:
                    print("Уровень заблокирован!")
            if self == "4":
                if games.glf["level_4"]:
                    print("Начало игры")
                else:
                    print("Уровень заблокирован!")
            if self == "5":
                if games.glf["level_6"]:
                    print("Начало игры")
                else:
                    print("Уровень заблокирован!")
            if self == "7":
                if games.glf["level_7"]:
                    print("Начало игры")
                else:
                    print("Уровень заблокирован!")
            if self == "8":
                if games.glf["level_8"]:
                    print("Начало игры")
                else:
                    print("Уровень заблокирован!")
            if self == "9":
                if games.glf["level_9"]:
                    print("Начало игры")
                else:
                    print("Уровень заблокирован!")
            if self == "10":
                if games.glf["level_10"]:
                    print("Начало игры")
                else:
                    print("Уровень заблокирован!")

    def quess_the_number(self):
        qtn = True
        while qtn:
            if self == "1":
                if games.q_t_n["level_1"]:
                    print("Начало игры")
                else:
                    print("Уровень заблокирован")
            if self == "2":
                if games.q_t_n["level_2"]:
                    print("Начало игры")
                else:
                    print("Уровень заблокирован")
            if self == "3":
                if games.q_t_n["level_3"]:
                    print("Начало игры")
                else:
                    print("Уровень заблокирован")
            if self == "4":
                if games.q_t_n["level_4"]:
                    print("Начало игры")
                else:
                    print("Уровень заблокирован")
            if self == "5":
                if games.q_t_n["level_5"]:
                    print("Начало игры")
                else:
                    print("Уровень заблокирован")
            if self == "6":
                if games.q_t_n["level_6"]:
                    print("Начало игры")
                else:
                    print("Уровень заблокирован")
            if self == "7":
                if games.q_t_n["level_7"]:
                    print("Начало игры")
                else:
                    print("Уровень заблокирован")
            if self == "8":
                if games.q_t_n["level_8"]:
                    print("Начало игры")
                else:
                    print("Уровень заблокирован")
            if self == "9":
                if games.q_t_n["level_9"]:
                    print("Начало игры")
                else:
                    print("Уровень заблокирован")
            if self == "10":
                if games.q_t_n["level_10"]:
                    print("Начало игры")
                else:
                    print("Уровень заблокирован")

    def puzzles(self):
        pz = True
        while pz:
            if self == "1":
                if games.puz["level_1"]:
                    print("Начало игры")
                else:
                    print("Уровень заблокирован!")
            if self == "2":
                if games.puz["level_2"]:
                    print("Начало игры")
                else:
                    print("Уровень заблокирован!")
            if self == "3":
                if games.puz["level_3"]:
                    print("Начало игры")
                else:
                    print("Уровень заблокирован!")
            if self == "4":
                if games.puz["level_4"]:
                    print("Начало игры")
                else:
                    print("Уровень заблокирован!")
            if self == "5":
                if games.puz["level_5"]:
                    print("Начало игры")
                else:
                    print("Уровень заблокирован!")
            if self == "6":
                if games.puz["level_6"]:
                    print("Начало игры")
                else:
                    print("Уровень заблокирован!")
            if self == "7":
                if games.puz["level_7"]:
                    print("Начало игры")
                else:
                    print("Уровень заблокирован!")
            if self == "8":
                if games.puz["level_8"]:
                    print("Начало игры")
                else:
                    print("Уровень заблокирован!")
            if self == "9":
                if games.puz["level_9"]:
                    print("Начало игры")
                else:
                    print("Уровень заблокирован!")
            if self == "10":
                if games.puz["level_10"]:
                    print("Начало игры")
                else:
                    print("Уровень заблокирован!")
