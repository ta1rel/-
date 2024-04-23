import random


class Player:
    def __init__(self, name):
        self.name = name
        self.level = 1
        self.health = 100

    def attack(self, enemy):
        damage = random.randint(5, 20)
        enemy.health -= damage
        print(f"{self.name} атакует {enemy.name} и наносит {damage} урона")

    def level_up(self):
        self.level += 1
        self.health += 20
        print(f"{self.name} повысил уровень! Теперь у него {self.health} здоровья")


class Enemy:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def attack(self, player):
        damage = random.randint(5, 15)
        player.health -= damage
        print(f"{self.name} атакует {player.name} и наносит {damage} урона")


player1 = Player("Игрок")
enemy1 = Enemy("Враг", 50)

while player1.health > 0 and enemy1.health > 0:
    print(f"Уровень игрока: {player1.level}, Здоровье игрока: {player1.health}")
    print(f"Здоровье врага: {enemy1.health}")

    command = input("Введите команду (attack/level up): ")

    if command == "attack":
        player1.attack(enemy1)
        if enemy1.health <= 0:
            print("Победа! Получен опыт!")
            player1.level_up()
            enemy1 = Enemy("Враг", 50)
    elif command == "level up":
        player1.level_up()
    else:
        print("Неверная команда, повторите попытку")

if player1.health <= 0:
    print("Игрок проиграл!")
else:
    print("Игрок победил!")

application_path = os.path.dirname(sys.executable)