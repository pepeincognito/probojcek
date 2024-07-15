#!/usr/bin/env python3

import random
from proboj import *
from constants import *

def priechodne(p : Block):
    return p >= Block.VOLNO

class MyPlayer(ProbojPlayer):
    def init(self):
        self.bomb = None
        self.safe = None
        pass
    
    def findSafe(self,y,x):
        queue = [(y,x,0)]
        visited = set()
        while queue:
            vrchol = queue.pop(0)
            time = vrchol[2]
            if vrchol[0] != y and vrchol[1] != x: return ((vrchol[0],vrchol[1]))
            visited.add((vrchol[0,vrchol[1]]))
            for sused in [(y+1,x),(y-1,x),(y,x+1),(y,x-1)]:
                try:
                    if self.stav.teren.data[sused[0]][sused[1]] in [Block.VOLNO, Block.START, Block.BONUS] and not self.stav.teren.data[sused[0]][sused[1]] in visited and time<6:
                        queue.append((sused[0],sused[1],time+1))
                except: ...
        return None
    
    def findBomb(self,y,x):
        queue = [(y,x)]
        visited = set()
        while queue:
            vrchol = queue.pop(0)
            safe = self.findSafe(vrchol)
            if safe != None:
                self.safe = safe
                self.bomb = vrchol
                return()
            visited.add(vrchol)
            for sused in [(y+1,x),(y-1,x),(y,x+1),(y,x-1)]:
                try:
                    if self.stav.teren.data[sused[0]][sused[1]] in [Block.VOLNO, Block.START, Block.BONUS] and not self.stav.teren.data[sused[0]][sused[1]] in visited:
                        queue.append(sused)
                except: ...
        return None
    
    def chod(y,x):
        queue = [(y,x,0)]
        visited = set()
        while queue:
            vrchol = queue.pop(0)
            time = vrchol[2]
            if vrchol[0] != y and vrchol[1] != x: return ((vrchol[0],vrchol[1]))
            visited.add((vrchol[0,vrchol[1]]))
            for sused in [(y+1,x),(y-1,x),(y,x+1),(y,x-1)]:
                try:
                    if self.stav.teren.data[sused[0]][sused[1]] in [Block.VOLNO, Block.START, Block.BONUS] and not self.stav.teren.data[sused[0]][sused[1]] in visited and time<6:
                        queue.append((sused[0],sused[1],time+1))
                except: ...
        return None

    def getMove(self):
        ### Tu vypocitajte tah
        self.log(f"Zaciatok tahu {self.stav.cas}")

        ### Informacie o vasom hracovi su v self.stav.hraci[0]
        ja = self.stav.hraci[0]
        x = ja.x
        y = ja.y

        if self.bomb == None and self.safe == None:
            self.findBomb(y,x)
        elif self.bomb == None:...
            
        
        if (self.stav.teren.data_lower[y][x] == BlockLower.NETHERITE):
            self.log("Som na netherite")
            return (Smer.NIKAM, False)

        return (random.choice(list(Smer)), False)

if __name__ == "__main__":
    myPlayer = MyPlayer()
    main(myPlayer)