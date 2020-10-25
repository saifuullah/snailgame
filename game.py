import arcade

class snailsGame(arcade.Window):


    #Function for initilization of backend 2D board array
    def initilizeBoard(self, rows, cols):
        board = []

        for i in range(cols):
            tempBoard = []
            for i in range(0, rows):
                tempBoard.append(0)
            board.append(tempBoard)

        return board



    def draw_horizental(self, grid_size, box_size, pixel):
        temp = box_size
        for i in range(1, grid_size):
            arcade.draw_line(0, box_size, (box_size*grid_size), box_size,  arcade.color.GRAY_BLUE, pixel)
            box_size = box_size + temp #temp is box size


    def draw_vertical(self, grid_size, box_size, pixel):
        temp = box_size
        for i in range(1, grid_size):
            arcade.draw_line(box_size, 0, box_size, (box_size*grid_size),  arcade.color.GRAY_BLUE, pixel)
            box_size = box_size + temp #temp is box size





    #Function for initilization of front-End board
    def initilizeGrid(self, board, botImage, humanImage):        
        SCREEN_HEIGHT = SCREEN_WIDTH = 600
        SCREEN_TITLE="Snails game"
        Back_img = None
        grid_size = int(len(board))
        pix = 3
        box_size=SCREEN_WIDTH/grid_size

        arcade.open_window(SCREEN_WIDTH,SCREEN_HEIGHT,SCREEN_TITLE)
        arcade.set_background_color(arcade.color.ANDROID_GREEN)
        arcade.start_render()

        #Background imag
        Back_img = arcade.load_texture("bk.jpg")
        arcade.draw_lrwh_rectangle_textured(0, 0,SCREEN_WIDTH, SCREEN_HEIGHT,Back_img)

        #Drawing lines
        self.draw_horizental(grid_size, box_size, pix)
        self.draw_vertical(grid_size, box_size, pix)
        
        #place both snails images at 1st place
        board[0][len(board)-1] = 1
        board[len(board)-1][0] = 2

        
        arcade.draw_lrwh_rectangle_textured(7,7, box_size-15, box_size-15, snail_pic)
        arcade.draw_lrwh_rectangle_textured(SCREEN_HEIGHT-box_size+7,SCREEN_HEIGHT-box_size+7, box_size-15, box_size-15, snake_pic)
        arcade.finish_render()




o = snailsGame()
snail_pic = arcade.load_texture("snail.png")
snake_pic = arcade.load_texture("snake.png")
x = o.initilizeBoard(10,10)
#print(x)
#print(len(x[0]))
o.initilizeGrid(x,snail_pic, snake_pic)
arcade.run()