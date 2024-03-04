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



class Base1:
    def __init__(self):
        print("Base1 class constructor")

    def base1_method(self):
        print("Base1 method")


class Base2:
    def __init__(self):
        print("Base2 class constructor")

    def base2_method(self):
        print("Base2 method")


class MultiDerived(Base1, Base2):
    # def __init__(self):
    #     super().__init__()  # Call constructor of Base1
    #     print("MultiDerived class constructor")

    # def derived_method(self):
    #     print("MultiDerived method")
 pass

multi_derived = MultiDerived()
multi_derived.base1_method()
multi_derived.base2_method()
# multi_derived.derived_method()
