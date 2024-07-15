from dataclasses import dataclass
import sys
from typing import List
from constants import *

def _input_vec(single):
    N = int(input())
    L = []
    for _ in range(N):
        L.append(single())
    return L


@dataclass
class Teren:
    """
    Trieda popisujúca terén !!! indexuje se [y][x]
    * data - zoznam blokov na vrchu
    * data_lower - zoznam blokov na spodku
    """
    data: List[List[Block]]
    data_lower: List[List[BlockLower]]

    @staticmethod
    def input():
        return Teren(
            data=_input_vec(lambda: _input_vec(lambda: int(input()))),
            data_lower=_input_vec(lambda: _input_vec(lambda: int(input()))),
        )


@dataclass
class Mapa:
    """
    Trieda popisujúca mapu
    * pocet_hracov - počet hráčov na mape
    * width - šírka mapy
    * height - výška mapy
    * teren - terén mapy
    """
    pocet_hracov: int
    width: int
    height: int
    teren: Teren

    @staticmethod
    def input():
        n = int(input())
        w = int(input())
        h = int(input())
        t = Teren.input()
        return Mapa(pocet_hracov=n, width=w, height=h, teren=t)


@dataclass
class Hrac:
    """
    Trieda popisujúca hráča
    * skore - skóre hráča
    * x - x-ová súradnica hráča
    * y - y-ová súradnica hráča
    * jeZivy - či je hráč ešte nažive
    * pocetBomb - počet bomb hráča na mape
    * naMieste - počet kol, ktoré sa hráč nepohol
    * rychlostTazenia - počet kol, ktoré trvá vyťažiť netherite
    * maxPocetBomb - koľko bomb môže mať maximálne položených na mape
    * silaBomb - sila bomb hráča
    * maStit - koľko kol ešte má štít
    """
    _mapovanie: List[int]  # klienti nevidia
    skore: int
    x: int
    y: int
    jeZivy: bool
    pocetBomb: int  # pocet bomb hraca na mape
    naMieste: int  # pocet kol ktore sa hrac nepohol
    rychlostTazenia: int  # pocet kol ktore trva vytazit netherite

    maxPocetBomb: int  # kolko bomb moze mat maximalne polozenych na mape, meni sa
    silaBomb: int  # sila bomb daneho hraca, meni sa
    maStit: int  # kolko kol este ma stit

    @staticmethod
    def input():
        m = _input_vec(lambda: int(input()))
        skore = int(input())
        x = int(input())
        y = int(input())
        jeZivy = bool(int(input()))
        pocetBomb = int(input())
        naMieste = int(input())
        rychlostTazenia = int(input())
        maxPocetBomb = int(input())
        silaBomb = int(input())
        maStit = int(input())

        return Hrac(
            m, skore, x, y, jeZivy, pocetBomb, naMieste,
            rychlostTazenia, maxPocetBomb, silaBomb, maStit
        )


@dataclass
class Bonus:
    """
    Trieda popisujúca bonus
    * x - x-ová súradnica bonusu
    * y - y-ová súradnica bonusu
    * typ - typ bonusu
    """
    x: int
    y: int
    typ: BonusType

    @staticmethod
    def input():
        x = int(input())
        y = int(input())
        t = int(input())
        return Bonus(x, y, t)

@dataclass
class Bomba:
    """
    Trieda popisujúca bombu
    * kto - číslo hráča, ktorý bombu položil
    * x - x-ová súradnica bomby
    * y - y-ová súradnica bomby
    * timer - čas do výbuchu bomby
    * sila - dosah výbuchu bomby
    """
    kto: int
    x: int
    y: int
    timer: int
    sila: int

    @staticmethod
    def input():
        kto = int(input())
        x = int(input())
        y = int(input())
        timer = int(input())
        sila = int(input())
        return Bomba(kto, x, y, timer, sila)

@dataclass
class Stav:
    """
    Trieda popisujúca stav hry
    * hraci - zoznam hráčov
    * bonusy - zoznam bonusov na mape
    * bomby - zoznam bômb
    * teren - terén mapy (v tomto kole)
    * cas - číslo aktuálneho kola
    """
    hraci: List[Hrac]
    bonusy: List[Bonus]
    bomby: List[Bomba]
    teren: Teren
    cas: int

    @staticmethod
    def input():
        hraci = _input_vec(Hrac.input)
        bonusy = _input_vec(Bonus.input)
        bomby = _input_vec(Bomba.input)
        teren = Teren.input()
        cas = int(input())
        return Stav(hraci, bonusy, bomby, teren, cas)

class ProbojPlayer:
    """
    Táto trieda vykonáva ťahy v hre
    * mapa - objekt, ktorý reprezentuje mapu na začiatku hry
    * stav - objekt, ktorý stav hry v tomto kole
    """
    def __init__(self):
        self.mapa : Mapa
        self.stav : Stav

    def log(self, *args, **kwargs):
        """
        Funkcia na výpis debugovacích správ. !!! Nepoužívajte normálny print
        """
        print(*args, **kwargs, file=sys.stderr)

    def init(self):
        """
        Spustí sa hneď po načítaní mapy, môžete si tu inicializovať nejaké premenne
        """
        raise NotImplementedError

    def getMove(self) -> tuple[Smer, bool]:
        """
        Spúšťa sa každé kolo. Vracia váš ťah (smer, položenie bomby)
        """
        raise NotImplementedError


def main(p : ProbojPlayer):
    p.mapa = Mapa.input()
    print("Loaded map", file=sys.stderr)
    p.init()

    while True:
        try:
            p.stav = Stav.input()
            print("Loaded stav", file=sys.stderr)
        except EOFError:
            break
        move = p.getMove()
        print(int(move[0]))
        print(int(move[1]))
        print(".")
        sys.stdout.flush()
