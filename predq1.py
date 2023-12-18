import pyxel

SCENE_TITLE = 0	#タイトル画面
SCENE_START = 1 #スタート画面
SCENE_CASTLE = 2 #お城
SCENE_FIELD1 = 3 #フィールド１

class Move:
    def __init__(self):
        self.scroll_x = 0
        self.scroll_y = 0

        self.player_x = 0
        self.player_y = 0

    def move(self):
        if pyxel.btn(pyxel.KEY_LEFT):
            self.scroll_x -= 2
        if pyxel.btn(pyxel.KEY_RIGHT):
            self.scroll_x += 2
        if pyxel.btn(pyxel.KEY_UP):
            self.scroll_y -= 2
        if pyxel.btn(pyxel.KEY_DOWN):
            self.scroll_y += 2

        self.player_x = 256 + self.scroll_x + 128
        self.player_y = 256 + self.scroll_y + 128

class App:
    def __init__(self):
        pyxel.init(256,256)
        pyxel.load("music2.pyxres")

        self.x_count = 0
        self.select_x = 0
        self.select_y = 0

        self.scroll_x = 0
        self.scroll_y = 0

        self.player_x = 0
        self.player_y = 0

    def run(self):
        self.scene = SCENE_TITLE
        pyxel.playm(0, loop=True)
        pyxel.run(self.update, self.draw)

    def update(self):
      if pyxel.btnp(pyxel.KEY_Q):
         pyxel.quit()

    #スクリーンを増やすところ 
      if self.scene == SCENE_TITLE:
            self.update_title_scene()
      elif self.scene == SCENE_START:
            self.update_start_scene()
      elif self.scene == SCENE_CASTLE:
            self.update_castle_scene()
      elif self.scene == SCENE_FIELD1:
            self.update_field1_scene()
    
    def update_title_scene(self):
        if pyxel.btnp(pyxel.KEY_SPACE):
            pyxel.playm(2, loop = True)
            self.scene = SCENE_START
    
    def update_start_scene(self):
        if 0 < self.select_x <=144:
            if pyxel.btnp(pyxel.KEY_LEFT):
                self.select_x -= 16
        if 0 <= self.select_x <144 and 0<= self.select_y <=64 or 0 <= self.select_x <128 and self.select_y == 80:
            if pyxel.btnp(pyxel.KEY_RIGHT):
                self.select_x += 16
        if 0 < self.select_y <=80:
            if pyxel.btnp(pyxel.KEY_UP):
                self.select_y -= 16
        if 0 <= self.select_x <=96 and 0 <= self.select_y <80 or 112 == self.select_x and 0<= self.select_y <64 or 128 == self.select_x and 0<= self.select_y <80 or 144 == self.select_x and 0<= self.select_y <64:
            if pyxel.btnp(pyxel.KEY_DOWN):
                self.select_y += 16

        if self.select_x == 112 and self.select_y == 80:
                if pyxel.btnp(pyxel.KEY_RIGHT):
                   self.select_x += 16
                if pyxel.btnp(pyxel.KEY_LEFT):
                   self.select_x -= 16
        
        if pyxel.btnp(pyxel.KEY_SPACE):#表示位置を設定する
            if (self.select_x == 96 and self.select_y == 80) and self.x_count > 0:
                self.x_count -=12
            elif not(self.select_x == 128 and self.select_y == 80) and not (self.select_x == 96 and self.select_y == 80) and self.x_count < 48:
                self.x_count +=12

        if self.select_x + 48 == 176 and self.select_y + 96 == 176:
               if pyxel.btnp(pyxel.KEY_SPACE):
                    pyxel.playm(4, loop = True)
                    self.scene = SCENE_CASTLE

    def update_castle_scene(self):

        #pyxel.tilemap(1).pget

        if pyxel.btn(pyxel.KEY_LEFT):
            self.scroll_x -= 2
        if pyxel.btn(pyxel.KEY_RIGHT):
            self.scroll_x += 2
        if pyxel.btn(pyxel.KEY_UP):
            self.scroll_y -= 2
        if pyxel.btn(pyxel.KEY_DOWN):
            self.scroll_y += 2

        self.player_x = 256 + self.scroll_x + 128
        self.player_y = 256 + self.scroll_y + 128

        #真ん中からスタートしないとめんどくさくなる。
        if self.player_x < 154 or 632 < self.player_x or self.player_y < 154:
            self.scroll_x = 0
            self.scroll_y = 0
            pyxel.playm(1, loop = True)
            self.scene = SCENE_FIELD1

    def update_field1_scene(self):
        #self.scroll_x = 0 ここで0にすると動けなくなる。
        #self.scroll_y = 0
        if pyxel.btn(pyxel.KEY_LEFT):
            self.scroll_x -= 2
        if pyxel.btn(pyxel.KEY_RIGHT):
            self.scroll_x += 2
        if pyxel.btn(pyxel.KEY_UP):
            self.scroll_y -= 2
        if pyxel.btn(pyxel.KEY_DOWN):
            self.scroll_y += 2



    def draw(self):
      pyxel.cls(0)

      if self.scene == SCENE_TITLE:
            self.draw_title_scene()
      elif self.scene == SCENE_START:
            self.draw_start_scene()
      elif self.scene == SCENE_CASTLE:
            self.draw_castle_scene()
      elif self.scene == SCENE_FIELD1:
            self.draw_field1_scene()

    def draw_title_scene(self):
        pyxel.cls(1)

    def draw_start_scene(self):
        pyxel.cls(0)
        pyxel.bltm(0, 0, 0, 0, 0, 256, 256, 0)
        pyxel.blt(48 + self.select_x, 96 + self.select_y, 1, 48, 96, 8, 8, 0)
        pyxel.text(0,5,'x='+ str(self.select_x),4)
        pyxel.text(0,10,'y='+ str(self.select_y),4)
        pyxel.text(0,15,'x_c='+ str(self.x_count),4)

        #for t in self.n_tx:
        pyxel.blt(68+self.x_count,72,1,0,0,8,8,0)

    def draw_castle_scene(self):
        pyxel.cls(13)
        pyxel.bltm(0,0,2,256 + self.scroll_x ,256 + self.scroll_y ,511 + self.scroll_x, 511 + self.scroll_x)
        pyxel.blt(128, 128, 0, 64, 64, 16, 16, 0)
        pyxel.text(0,5,'x='+ str(self.scroll_x),7)
        pyxel.text(0,10,'y='+ str(self.scroll_y),7)

    def draw_field1_scene(self):
        pyxel.cls(13)
        pyxel.bltm(0,0,1,640 + self.scroll_x ,640 + self.scroll_y ,895 + self.scroll_x, 895 + self.scroll_x)
        pyxel.blt(128, 128, 0, 64, 64, 16, 16, 0)
        pyxel.text(0,5,'x='+ str(self.scroll_x),7)
        pyxel.text(0,10,'y='+ str(self.scroll_y),7)
App().run()