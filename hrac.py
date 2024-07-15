#!/usr/bin/env python3

import random
from proboj import *
from constants import *

def priechodne(p : Block):
    return p >= Block.VOLNO

class MyPlayer(ProbojPlayer):
    def init(self):
        ### Tu si mozete inicializovat nieco
        pass

    def getMove(self):
        ### Tu vypocitajte tah
        self.log(f"Zaciatok tahu {self.stav.cas}")

        ### Informacie o vasom hracovi su v self.stav.hraci[0]
        ja = self.stav.hraci[0]
        x = ja.x
        y = ja.y

        if (self.stav.teren.data_lower[y][x] == BlockLower.NETHERITE):
            self.log("Som na netherite")
            return (Smer.NIKAM, False)

        return (random.choice(list(Smer)), False)

if __name__ == "__main__":
    myPlayer = MyPlayer()
    main(myPlayer)
