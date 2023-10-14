

import turtle
from random import randint

class Circuito():
    corredores: list[turtle.Turtle] = []
    __colores = ["aliceblue", "antiquewhite", "aqua", "aquamarine", "azure", "beige", "bisque", "blanchedalmond", "blueviolet", "burlywood", "cadetblue", "chartreuse", "chocolate", "coral", "cornflowerblue", "cornsilk", "crimson", "darkblue", "darkcyan", "darkgoldenrod", "darkgray", "darkgreen", "darkkhaki", "darkmagenta", "darkolivegreen","darkorange", "darkorchid", "darkred", "darksalmon", "darkseagreen", "darkslateblue", "darkslategray", "darkturquoise", "darkviolet", "deeppink", "deepskyblue", "dimgray", "dodgerblue", "firebrick", "floralwhite", "forestgreen", "fuchsia", "gainsboro", "ghostwhite", "gold", "goldenrod", "gray", "greenyellow", "honeydew", "hotpink", "indianred", "indigo", "ivory", "khaki", "lavender", "lavenderblush", "lawngreen", "lemonchiffon", "lightblue", "lightcoral", "lightcyan", "lightgoldenrodyellow", "lightgreen", "lightpink", "lightsalmon", "lightseagreen", "lightskyblue", "lightslategray", "lightsteelblue", "lightyellow", "lime", "limegreen", "linen", "magenta", "maroon", "mediumaquamarine", "mediumblue", "mediumorchid", "mediumpurple", "mediumseagreen", "mediumslateblue", "mediumspringgreen", "mediumturquoise", "mediumvioletred", "midnightblue", "mintcream", "mistyrose", "moccasin", "navajowhite", "navy", "oldlace", "olive", "olivedrab", "orangered", "orchid", "palegoldenrod", "palegreen", "paleturquoise", "palevioletred", "papayawhip", "peachpuff", "peru", "pink", "plum", "powderblue", "purple", "red", "rosybrown", "royalblue", "saddlebrown", "salmon", "sandybrown", "seagreen", "seashell", "sienna", "silver", "skyblue", "slateblue","slategray", "snow", "springgreen", "steelblue", "tan", "teal", "thistle", "tomato", "turquoise", "violet", "wheat", "whitesmoke", "yellowgreen"]
    
    def __init__(self, width, height, numTurtles):
        print(len(self.__colores))
        self.__numTurtles = numTurtles
        self.__screen = turtle.Screen()
        self.__screen.setup(width, height)
        self.__screen.bgcolor('lightgrey')
        self.__startline = -width/2 + 15
        self.__finishline = width/2 - 40
        self.__spaces= height/numTurtles
        self.__lines=numTurtles-1
        self.__create_lines()
        self.__createRunners()
        self.__competition()
    def __create_lines(self):
        start_n_finish = turtle.Turtle()
        
        start_n_finish.ht()
        start_n_finish.speed(500)
        start_n_finish.pu()
        start_n_finish.setx(self.__startline +20)
        start_n_finish.sety(-self.__spaces*self.__numTurtles/2)
        start_n_finish.pd()
        start_n_finish.sety(self.__spaces*self.__numTurtles/2)
        start_n_finish.pu()
        start_n_finish.setx(self.__finishline)
         
        start_n_finish.pd()
        start_n_finish.sety(-self.__spaces*self.__numTurtles/2)
        for i in range(self.__lines):
            new_lines =  turtle.Turtle()
            
            new_lines.ht()
            new_lines.speed(500)
            new_lines.pu()
            new_lines.setx(self.__startline -20)
            new_lines.sety((i-((self.__lines/2)-0.5))*self.__spaces)
            new_lines.pd()
            new_lines.setx(self.__finishline)
    def __createRunners(self):
        for i in range(self.__numTurtles):
            new_turtle =  turtle.Turtle()
            new_turtle.ht()
            new_turtle.pu()
            new_turtle.speed(500)
            new_turtle.shape('turtle')
            new_turtle.color(self.__colores[i])
            new_turtle.setx(self.__startline)
            new_turtle.sety((i-((self.__numTurtles/2)-0.5))*self.__spaces)
            new_turtle.st()

            self.corredores.append(new_turtle)
            new_turtle.speed(1)
            print(round(new_turtle.ycor(), 5))
    def __competition(self):
        hayGanador=False
        madness=0.1
        while not hayGanador:
            madness +=0.1
            for tortuguita in self.corredores:
                indice = self.corredores.index(tortuguita)
                tortuguita.speed(100)
                avance=randint(1,int(self.__spaces))
                rotation=randint(-int(madness),int(madness))
               
                
                tortuguita.left(rotation)
                tortuguita.fd(avance)
                if round(tortuguita.ycor(), 5)>(indice-((self.__lines/2)-0.5))*self.__spaces:
                    print('-choque arriba-',tortuguita.color()[0],(indice-((self.__lines/2)-0.5))*self.__spaces,round(tortuguita.ycor(), 5))
                    tortuguita.bk(avance/2)
                    print(tortuguita.heading())
                    tortuguita.right(2*tortuguita.heading())
                    tortuguita.fd(avance/2)
                    print(tortuguita.heading())
                if round(tortuguita.ycor(), 5)<(indice-1-((self.__lines/2)-0.5))*self.__spaces:
                    print('-choque abajo-',tortuguita.color()[0],(indice-((self.__lines/2)-0.5))*self.__spaces,round(tortuguita.ycor(), 5))
                    tortuguita.bk(avance/2)
                    print(tortuguita.heading())
                    tortuguita.left(2*(360-tortuguita.heading()))
                    tortuguita.fd(avance/2)
                    print(tortuguita.heading())
                if round(tortuguita.xcor(), 5)<self.__startline:
                    print('-choque atras-',tortuguita.color()[0],(indice-((self.__lines/2)-0.5))*self.__spaces,round(tortuguita.ycor(), 5))
                    print(tortuguita.heading())
                    tortuguita.bk(avance)
                    tortuguita.left(-180)
                    print(tortuguita.heading())
                if round(tortuguita.xcor(), 5) > self.__finishline:
                    tortuguita.write("WINNER ---->>>     ", align="right",font=("Arial", 36, "normal"))
                    print('ganador',tortuguita.color())
                    hayGanador=True
                    break
        
if __name__== '__main__':
    circuito = Circuito(1900, 1000, 29)
