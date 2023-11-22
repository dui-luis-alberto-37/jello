#!/usr/bin/env python3
# by lgarciaorozco6@gmail.com
# GNU/GPL License

class Jello:

    def __inint__(self,water,flavor,grenetince,sugar,color,slides):
        self.water = water
        self.flavor = flavor
        self.grenetince = grenetince
        self.sugar = sugar
        self.color = color
        self.slides = slides

    def slide(self,flavor):
        if flavor in self.flavor:
            if self.slide > 0:
                self.slide -= 1
                return True
            else:
                return False
        else:
            return False



jello_limon = Jello(1,'limon',150,100,'green',10)
jello_strawberry = Jello(0.5,'strawberry',100,70,'red',5)

if jello_limon.slide('limon'):
    print('thank you')
