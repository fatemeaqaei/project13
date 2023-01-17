import arcade
col_space = 27
row_space = 27
left_padding = 115
bottom_padding = 115

class World(arcade.Window):
    def __init__(self):
        super().__init__(width=1000,height=700,title="loop")
        arcade.set_background_color(arcade.color.WHITE)

    def on_draw(self):
        arcade.start_render()
        self.Square = Square(self)

class Square(arcade.Sprite):
    def __init__(self,World):
        super().__init__()
        for row in range(10):
            for column in range(10):
                x = left_padding + column * col_space 
                y = bottom_padding + row * row_space 
                if row % 2 == 0 :
                    if column % 2 == 0 :
                        arcade.draw_rectangle_filled(x, y, 14 , 14, arcade.color.BLUE , tilt_angle=45)
                    else :
                        arcade.draw_rectangle_filled(x, y, 14 , 14, arcade.color.RED , tilt_angle=45)
                else :
                    if column % 2 == 0 :
                        arcade.draw_rectangle_filled(x, y, 14 , 14, arcade.color.RED , tilt_angle=45)
                    else :
                        arcade.draw_rectangle_filled(x, y, 14 , 14, arcade.color.BLUE , tilt_angle=45)


window = World()
arcade.run()