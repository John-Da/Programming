from network import Network

def it(self):
    self.update()
    
def update(self):
    self.rect = (self.x, self.y, self.width, self.height)

def read_pos(str):
    str = str.split(",")
    return int(str[0]), int(str[1])

def make_pos(tup):
    return str(tup[0]) + "," + str(tup[1])


def redrawWindow(player2):
    player2.draw()
    ...
# main def
n = Network()
startPos = read_pos(n.getPos())

p = Player(startPos[0], startPos[1]) # player 1st
p2 = Player(0, 0) # player 2nd

while True:
    p2Pos = read_pos(n.send(make_pos(p.x, p.y)))
    p2.x = p2Pos[0]
    p2.y = p2Pos[1]
    p2.update()

    redrawWindow(p2)