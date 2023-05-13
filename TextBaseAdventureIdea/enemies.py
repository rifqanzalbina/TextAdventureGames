""" Text adventure game
    @insta = @rifqanzalbina
    @year  = 2018
"""
__author__ = "rifqanzalbina"


class Enemy:
    def __init__(self):
        raise NotImplementedError("DO not create raw Enemy objects.")

    def __str__(self):
        return self.name

    def is_alive(self):
        return self.hp > 0


class GiantSpider(Enemy):
    def __init__(self):
        self.name = " Giant Spider"
        self.hp = 10
        self.damage = 2


class Ogre(Enemy):
    def __init__(self):
        self.name = "Ogre"
        self.hp = 30
        self.damage = 10


class BatColony(Enemy):
    def __init__(self):
        self.name = "Colony of Bats"
        self.hp = 100
        self.damage = 4


class RockMonster(Enemy):
    def __init__(self):
        self.name = "Rock Monster"
        self.hp = 80
        self.damage = 15

class BigBird(Enemy):
    def __init__(self):
        self.name = "Big Bird Monster"
        self.hp = 100
        self.damage = 20

class DevilMan(Enemy):
    def __init__(self):
        self.name = "Devil Man"
        self.hp = 200
        self.damage = 15