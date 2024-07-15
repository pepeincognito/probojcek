from enum import IntEnum

class Block(IntEnum):
    OKRAJ = 0
    OBSIDIAN = 1
    NETHERRACK = 2
    BOMBA = 3
    EMPTY = 4
    VOLNO = 5
    START = 6
    BONUS = 7

class BlockLower(IntEnum):
    NETHERITE = 0
    BEDROCK = 1
    EMPTY = 2

BONUS_POCET_TYPOV = 4

class BonusType(IntEnum):
    SILA = 0
    POCET = 1
    STIT = 2
    TAZENIE = 3

class Smer(IntEnum):
    NIKAM = -1
    HORE = 0
    VPRAVO = 1
    DOLE = 2
    VLAVO = 3