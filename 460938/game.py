# напиши здесь код основного окна игры# напиши здесь код основного окна игры
from direct.showbase.ShowBase import ShowBase
from mapmanager import Mapmanager
from hero import Hero
class Game(ShowBase):
    def __init__(self):
        self.land = Mapmanager()
        self.landLoad('land.txt')
        self.hero= Hero((x//2,y//2,z//2),self.land)
        base.camLens.setFov(90)
game= Game()
game.run()