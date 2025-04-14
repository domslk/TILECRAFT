from const import screen

class Draw:
    @staticmethod
    def draw(texture, x,y):
        if texture:
            screen.blit(texture, (x, y))
