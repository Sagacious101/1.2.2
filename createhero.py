from random import choice, randint


first_name = ("Жран", "Жмых", "Бром", "Дин", "Ван", "Грим")
last_name = ("Дикий", "Ужасный", "Яросный", "Угрюмый", "Вонючий", "Свирепый", "Старый")




def make_hero(
name=None,
hp_curret=None,
hp_max=20,
lvl=0,
xp_next=None,
xp_curret=0,
ATK_base=1,
ATK_weapon=None,
weapon=None,
defense_base=0,
defense_shield=0,
defense_armor=0,
shield=None,
armor=None,
luck=1,
inventory=None,
money=None
) -> list:

    """
    Герой - это список
    [0] name - имя персонажа
    [1] hp_max - максимальное здоровье
    [2] hp_curret - текущее здоровье, контролирует игру
    [3] lvl - текущий уровень игрока (изначально 1)
    [4] xp_next - кол-во опыта для след. lvl
    [5] xp_curret - опыт сейчас
    [6] ATK_base - сила атаки без оружия
    [7] ATK_now - сила атаки с оружием
    [9] weapon - оружие
    [10] defense_base - защита без снаряжения
    [11] defense_now - защита с снаряжением
    [12] shield - щит
    [13] armor - доспехи
    [14] luck - удача
    [15] inventory - инвентарь
    [16] money - монеты
    """
    if not name:
        name = choice(first_name) + " " + choice(last_name)
    if not hp_curret:
        hp_curret = hp_max
    if not money:
        money = randint(1, 5)
    if not ATK_weapon:
        ATK_curret = ATK_base
    if not defense_shield and not defense_armor:
        defense_curret = defense_base
    if not inventory:
        inventory = []
    if not xp_next:
        xp_next = 234 + 234 * (lvl * 2)

    return [
        name,
        hp_max,
        hp_curret,
        lvl,
        xp_next,
        xp_curret,
        ATK_base,
        ATK_weapon,
        ATK_curret,
        weapon,
        defense_base,
        defense_shield,
        defense_armor,
        defense_curret,
        shield,
        armor,
        luck,
        inventory,
        money
    ]

def show_hero(hero):
    name = hero[0]
    hp_max = hero[1]
    hp_curret = hero[2]
    lvl = hero[3]
    xp_next = hero[4]
    xp_curret = hero[5]
    ATK_base = hero[6]
    ATK_weapon = hero[7]
    ATK_curret = hero[8]
    weapon = hero[9]
    defense_base = hero[10]
    defense_shield = hero[11]
    defense_armor = hero[12]
    defense_curret = hero[13]
    shield = hero[14]
    armor = hero[15]
    luck = hero[16]
    inventory = hero[17]
    money = hero[18]

    print("Персонаж:\n")
    print(f"Имя: {name}")
    print(f"HP: {hp_curret}/{hp_max}")
    print(f"Уровень: {lvl}")
    print(f"XP: {xp_curret}/{xp_next}")
    print(f"ATK: {ATK_curret}")
    print(f"Оружие: {weapon}")
    print(f"Защита: {defense_curret}")
    print(f"Щит: {shield}")
    print(f"Броня: {armor}")
    print(f"Удача: {luck}")
    print(f"Монеты: {money}\n")
    print("Инвентарь:\n")
    if not hero[17]:
        print("Пустой\n")
    else:
        print(*hero[17])
        print(" ")

def levelup(hero: list) -> None:
    while hero[5] >= hero[4]:
        hero[3] += 1
        hero[4] = 234 + 234 * (hero[3])
        print(f"Поздравляем! {hero[1]} достиг {hero[3]} уровня.\n")
        print("Распределите характеристики:\n")
        print(f"1.Увеличить HP {hero[2]}/{hero[1]} + 5")
        print(f"2.Увеличить ATK {hero[6]} + 1")
        print(f"3.Увеличить Защиту {hero[10]} + 1\n")
        plus = input("Введите номер выбора и нажмите ENTER: ")
        if plus == "1":
            hero[1] += 5
            hero[2] += 5
        elif plus == "2":
            hero[6] += 1
        elif plus == "3":
            hero[10] += 1
        if not hero[7]:
            hero[8] = hero[6]

def buy_item(hero: list, item, price: int) -> None:
    if hero[18] >= price:
        hero[18] -= price
        hero[17].append(item)
        print(f"{hero[0]} купил {item} за {price} монет!\n")
    else:
        print(f"{hero[0]} не хватило {price - hero[18]} монет!\n")

def consume_item(hero: list, idx: int) -> None:
    if idx <= len(hero[17]) - 1 and idx > -1:
        print(f"{hero[0]} употребил {hero[17][idx]}\n")
        if hero[17][idx] == "зелье":
            hero[17].pop(0)
            hero[2] += 10
            if hero[2] > hero[1]:
                hero[2] = hero[1]
        elif hero[17][idx] == "яблоко":
            pass
    else:
        print("Нет такого предмета")

def play_dice(hero: list, bet: int) -> None:
    if bet > 0:
        if hero[18] >= bet:
            hero_score = randint (2, 12)
            casino_score = randint(2, 12)
            print(f"{hero[0]} выбросил {hero_score}")
            print(f"Трактирщик выбросил {casino_score}\n")
            if hero_score > casino_score:
                hero[18] += bet
                print(f"{hero[0]} победил и забирает {bet} монет!\n")
            elif hero_score < casino_score:
                hero[18] -= bet
                print(f"{hero[0]} проиграл {bet} монет\n")
            else:
                print("Ничья\n")

        else:
            print(f" У {hero[0]} нет столько монет!\n")
    else:
        print("Такая ставка не возможна! Ставки начинааются от 1 монеты!")

def start_fight(hero: list) -> None:
    """
    TODO:
        Нужен противник
        Обмен ударами с противником, пока игрок и противник живы
        Итог боя: проигрыш или победа
        Победа: добавить опыта от врага, забрать предметы врага в инвентарь
        Проигрыш: закончить игру
    """
    pass





