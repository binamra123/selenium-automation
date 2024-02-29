class Move:
    def fwd(self):
        print("Move forward")

    def bwd(self):
        print("Move backward")

class Jump:
    def level1(self):
        print("Jump level1")
    
    def level2(self):
        print("Jump Level2")

class Mario(Move,Jump):
   pass


m = Mario()
m.fwd()
m.level1()
m.level2()
