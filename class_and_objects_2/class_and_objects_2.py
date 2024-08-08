class Turtle(object):
    
    def __init__(self, x, y, s):
        self.x_poz = x
        self.y_poz = y
        self.s_shag = s
        
    def go_up(self):
        up = int(input("На сколько подняться вверх: \n"))
        self.y_poz += up
    
    def go_down(self):
        down = int(input("На сколько спуститься вниз: \n"))
        self.y_poz -= down
    
    def go_left(self):
        left = int(input("На сколько переместиться в лево: \n"))
        self.x_poz -= left
        
    def go_right(self):
        right = int(input("На сколько переместиться в право: \n"))
        self.x_poz += right
    
    def evolve(self):
        print("Теперь вы ходите на большее количество клеток \n")
        self.s_shag += 1
       
    def degrade(self):
        print("Ой теперь вы ходите на меньшее количество клеток \n")
        if self.s_shag <= 0:
            print("Вы больше не можете ходить:")
        else:
            self.s_shag -= 1
            
    def count_moves(self, x2, y2):
        return print(f"Клеток до места по X: {self.x_poz - x2} по Y: {self.y_poz - y2}")


turtle1 = Turtle(10, 10, 3)

turtle1.go_up()
turtle1.go_down()
turtle1.go_left()
turtle1.go_right()
turtle1.evolve()
turtle1.degrade()
turtle1.count_moves(3, 4)


