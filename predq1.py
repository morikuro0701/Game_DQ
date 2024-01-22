import pyxel

SCENE_TITLE = 0	#タイトル画面
SCENE_START = 1 #スタート画面
SCENE_CASTLE = 2 #お城
SCENE_FIELD1 = 3 #フィールド
SCENE_BATTLE = 4 #戦闘画面

check =[(0,0),(1,0),(0,1),(1,1),#レンガ -1
        (2,0),(3,0),(2,1),(3,1),#草原 -1
        (6,0),(7,0),(6,1),(7,1),#森  -2
        (6,2),(7,2),(6,3),(7,3),#毒沼 -1
        (2,4),(3,4),(2,5),(3,5),#砂漠 -2
        (4,4),(5,4),(4,5),(5,5),#ダメージ床 -1 
        (6,4),(7,4),(6,5),(7,5),#橋 -1
        (0,6),(1,6),(0,7),(1,7),#下り階段
        (2,6),(3,6),(2,7),(3,7),#小山 -3
        (6,6),(7,6),(6,7),(7,7),#洞窟 
        (0,8),(1,8),(0,9),(1,9),#登り階段
        (2,8),(3,8),(2,9),(3,9),#お城
        (4,8),(5,8),(4,9),(5,9),#街
        ]
damage1 =[(6,2),(7,2),(6,3),(7,3)]#毒沼 -1
damage3 =[(4,4),(5,4),(4,5),(5,5)]#ダメージ床 -1 
enca1 =[(0,0),(1,0),(0,1),(1,1),#レンガ -1
        (2,0),(3,0),(2,1),(3,1),#草原 -1
        (6,2),(7,2),(6,3),(7,3),#毒沼 -1
        (4,4),(5,4),(4,5),(5,5),#ダメージ床 -1 
        (6,4),(7,4),(6,5),(7,5),#橋 -1
        ]
enca2 =[(6,0),(7,0),(6,1),(7,1),#森  -2
        (2,4),(3,4),(2,5),(3,5),#砂漠 -2
        ]
enca3 =[(2,6),(3,6),(2,7),(3,7),]#小山 -3

class App:
    def __init__(self):#変数とか増やす
        pyxel.init(256,256)
        pyxel.load("music2.pyxres")
        #お試し枠
        self.battle_command_frag = False
        self.battle_command_x = 8
        self.battle_command_y = 2
        #お試し枠
        self.musicstrattime = -120
        self.encount_frag =pyxel.rndi(300,700)

        self.time_count = 0
        self.select_ui = 48 #名前選択のチカチカ
        self.character_ui = 64 #主人公のチカチカ

        self.menu_dis_x =8
        self.menu_dis_y =8
        self.canmove_frag = 0 #0が動ける 1がメニューの基本画面 100が戦闘画面 5が王様のお話
        self.levelup_frag = 2
        self.damege_frag = 0

        self.x_count = 0
        self.select_x = 0
        self.select_y = 0
        self.player_name_1_x = 8
        self.player_name_1_y = 56
        self.player_name_2_x = 8
        self.player_name_2_y = 56
        self.player_name_3_x = 8
        self.player_name_3_y = 56
        self.player_name_4_x = 8
        self.player_name_4_y = 56

        self.scroll_x = 0
        self.scroll_y = 0

        self.rada_flag = False

        self.gold = 50
        self.exp = 0
        self.level = 1
        self.character_hp_max = 15
        self.character_hp_now = 15
        self.character_mp_max = 0
        self.character_mp_now = 0
        self.character_pw = 4
        self.character_agi = 4

        #ここからスライム関連
        self.frag = False
        self.nom_command = 0 #コマンド？
        self.nom_suraimu_emg = 0#スライムがあらわれた！
        self.nom_attack = 0#⚪︎⚪︎⚪︎⚪︎の攻撃！
        self.nom_attack_time = -100
        self.a = 0
        self.b = 0
        self.c = 0
        self.d = 0
        self.n =10.5
        self.m =11.5
        self.player_attack =12.5
        self.player_attack_frag = False
        self.taosu = 13.5
        self.nom_taosu = 0
        self.back_frag = -100
        self.now_level = 0
        self.level_music =True

    def level_non(self):#LVと数値の処理
        if pyxel.btn(pyxel.KEY_L):#LVup
            if self.exp<=99888:
                self.exp += 10

        if 7<=self.exp<23 :#レベル2
            self.level = 2
            self.character_hp_max = 22
            self.character_mp_max = 0
            self.character_pw = 5
            self.character_agi = 4
            if self.levelup_frag == self.level:
                self.levelup_frag += 1
                self.character_hp_now = self.character_hp_max
                self.character_mp_now = self.character_mp_max
        if 23<=self.exp<47 :#レベル3
            self.level = 3
            self.character_hp_max = 24
            self.character_mp_max = 5
            self.character_pw = 7
            self.character_agi = 6
            if self.levelup_frag == self.level:
                self.levelup_frag += 1
                self.character_hp_now = self.character_hp_max
                self.character_mp_now = self.character_mp_max
        if 47<=self.exp<110 :#レベル4
            self.level = 4
            self.character_hp_max = 31
            self.character_mp_max = 16
            self.character_pw = 7
            self.character_agi = 8
            if self.levelup_frag == self.level:
                self.levelup_frag += 1
                self.character_hp_now = self.character_hp_max
                self.character_mp_now = self.character_mp_max
        if 110<=self.exp<220 :#レベル5
            self.level = 5
            self.character_hp_max = 35
            self.character_mp_max = 20
            self.character_pw = 12
            self.character_agi = 10
            if self.levelup_frag == self.level:
                self.levelup_frag += 1
                self.character_hp_now = self.character_hp_max
                self.character_mp_now = self.character_mp_max
        if 220<=self.exp<450 :#レベル6
            self.level = 6
            self.character_hp_max = 38
            self.character_mp_max = 24
            self.character_pw = 16
            self.character_agi = 10
            if self.levelup_frag == self.level:
                self.levelup_frag += 1
                self.character_hp_now = self.character_hp_max
                self.character_mp_now = self.character_mp_max
        if 450<=self.exp<800 :#レベル7
            self.level = 7
            self.character_hp_max = 40
            self.character_mp_max = 26
            self.character_pw = 18
            self.character_agi = 17
            if self.levelup_frag == self.level:
                self.levelup_frag += 1
                self.character_hp_now = self.character_hp_max
                self.character_mp_now = self.character_mp_max
        if 800<=self.exp<1300 :#レベル8
            self.level = 8
            self.character_hp_max = 46
            self.character_mp_max = 29
            self.character_pw = 22
            self.character_agi = 20
            if self.levelup_frag == self.level:
                self.levelup_frag += 1
                self.character_hp_now = self.character_hp_max
                self.character_mp_now = self.character_mp_max
        if 1300<=self.exp<2000 :#レベル9
            self.level = 9
            self.character_hp_max = 50
            self.character_mp_max = 36
            self.character_pw = 30
            self.character_agi = 22
            if self.levelup_frag == self.level:
                self.levelup_frag += 1
                self.character_hp_now = self.character_hp_max
                self.character_mp_now = self.character_mp_max
        if 2000<=self.exp<2900 :#レベル10
            self.level = 10
            self.character_hp_max = 54
            self.character_mp_max = 40
            self.character_pw = 35
            self.character_agi = 31
            if self.levelup_frag == self.level:
                self.levelup_frag += 1
                self.character_hp_now = self.character_hp_max
                self.character_mp_now = self.character_mp_max
        if 2900<=self.exp<4000 :#レベル11
            self.level = 11
            self.character_hp_max = 62
            self.character_mp_max = 50
            self.character_pw = 40
            self.character_agi = 35
            if self.levelup_frag == self.level:
                self.levelup_frag += 1
                self.character_hp_now = self.character_hp_max
                self.character_mp_now = self.character_mp_max
        if 4000<=self.exp<5500 :#レベル12
            self.level = 12
            self.character_hp_max = 63
            self.character_mp_max = 58
            self.character_pw = 48
            self.character_agi = 40
            if self.levelup_frag == self.level:
                self.levelup_frag += 1
                self.character_hp_now = self.character_hp_max
                self.character_mp_now = self.character_mp_max
        if 5500<=self.exp<7500 :#レベル13
            self.level = 13
            self.character_hp_max = 70
            self.character_mp_max = 64
            self.character_pw = 52
            self.character_agi = 48
            if self.levelup_frag == self.level:
                self.levelup_frag += 1
                self.character_hp_now = self.character_hp_max
                self.character_mp_now = self.character_mp_max
        if 7500<=self.exp<10000 :#レベル14
            self.level = 14
            self.character_hp_max = 78
            self.character_mp_max = 70
            self.character_pw = 60
            self.character_agi = 55
            if self.levelup_frag == self.level:
                self.levelup_frag += 1
                self.character_hp_now = self.character_hp_max
                self.character_mp_now = self.character_mp_max
        if 10000<=self.exp<13000 :#レベル15
            self.level = 15
            self.character_hp_max = 86
            self.character_mp_max = 72
            self.character_pw = 68
            self.character_agi = 64
            if self.levelup_frag == self.level:
                self.levelup_frag += 1
                self.character_hp_now = self.character_hp_max
                self.character_mp_now = self.character_mp_max
        if 13000<=self.exp<17000 :#レベル16
            self.level = 16
            self.character_hp_max = 92
            self.character_mp_max = 95
            self.character_pw = 72
            self.character_agi = 70
            if self.levelup_frag == self.level:
                self.levelup_frag += 1
                self.character_hp_now = self.character_hp_max
                self.character_mp_now = self.character_mp_max
        if 17000<=self.exp<21000 :#レベル17
            self.level = 17
            self.character_hp_max = 100
            self.character_mp_max = 100
            self.character_pw = 72
            self.character_agi = 78
            if self.levelup_frag == self.level:
                self.levelup_frag += 1
                self.character_hp_now = self.character_hp_max
                self.character_mp_now = self.character_mp_max
        if 21000<=self.exp<25000 :#レベル18
            self.level = 18
            self.character_hp_max = 115
            self.character_mp_max = 108
            self.character_pw = 85
            self.character_agi = 84
            if self.levelup_frag == self.level:
                self.levelup_frag += 1
                self.character_hp_now = self.character_hp_max
                self.character_mp_now = self.character_mp_max
        if 25000<=self.exp<29000 :#レベル19
            self.level = 19
            self.character_hp_max = 130
            self.character_mp_max = 115
            self.character_pw = 87
            self.character_agi = 86
            if self.levelup_frag == self.level:
                self.levelup_frag += 1
                self.character_hp_now = self.character_hp_max
                self.character_mp_now = self.character_mp_max
        if 29000<=self.exp<33000 :#レベル20
            self.level = 20
            self.character_hp_max = 138
            self.character_mp_max = 128
            self.character_pw = 95
            self.character_agi = 90
            if self.levelup_frag == self.level:
                self.levelup_frag += 1
                self.character_hp_now = self.character_hp_max
                self.character_mp_now = self.character_mp_max
        if 33000<=self.exp<37000 :#レベル21
            self.level = 21
            self.character_hp_max = 149
            self.character_mp_max = 135
            self.character_pw = 95
            self.character_agi = 90
            if self.levelup_frag == self.level:
                self.levelup_frag += 1
                self.character_hp_now = self.character_hp_max
                self.character_mp_now = self.character_mp_max
        if 37000<=self.exp< 41000:#レベル22
            self.level = 22
            self.character_hp_max = 158
            self.character_mp_max = 146
            self.character_pw = 97
            self.character_agi = 90
            if self.levelup_frag == self.level:
                self.levelup_frag += 1
                self.character_hp_now = self.character_hp_max
                self.character_mp_now = self.character_mp_max
        if 41000<=self.exp<45000 :#レベル23
            self.level = 23
            self.character_hp_max = 165
            self.character_mp_max = 153
            self.character_pw = 99
            self.character_agi = 94
            if self.levelup_frag == self.level:
                self.levelup_frag += 1
                self.character_hp_now = self.character_hp_max
                self.character_mp_now = self.character_mp_max
        if 45000<=self.exp<49000 :#レベル24
            self.level = 24
            self.character_hp_max = 170
            self.character_mp_max = 161
            self.character_pw = 103
            self.character_agi = 98
            if self.levelup_frag == self.level:
                self.levelup_frag += 1
                self.character_hp_now = self.character_hp_max
                self.character_mp_now = self.character_mp_max
        if 49000<=self.exp<53000 :#レベル25
            self.level = 25
            self.character_hp_max = 174
            self.character_mp_max = 161
            self.character_pw = 113
            self.character_agi = 100
            if self.levelup_frag == self.level:
                self.levelup_frag += 1
                self.character_hp_now = self.character_hp_max
                self.character_mp_now = self.character_mp_max
        if 53000<=self.exp<57000 :#レベル26
            self.level = 26
            self.character_hp_max = 180
            self.character_mp_max = 168
            self.character_pw = 117
            self.character_agi = 105
            if self.levelup_frag == self.level:
                self.levelup_frag += 1
                self.character_hp_now = self.character_hp_max
                self.character_mp_now = self.character_mp_max
        if 57000<=self.exp<61000 :#レベル27
            self.level = 27
            self.character_hp_max = 189
            self.character_mp_max = 175
            self.character_pw = 125
            self.character_agi = 107
            if self.levelup_frag == self.level:
                self.levelup_frag += 1
                self.character_hp_now = self.character_hp_max
                self.character_mp_now = self.character_mp_max
        if 61000<=self.exp<65000 :#レベル28
            self.level = 28
            self.character_hp_max = 195
            self.character_mp_max = 180
            self.character_pw = 130
            self.character_agi = 115
            if self.levelup_frag == self.level:
                self.levelup_frag += 1
                self.character_hp_now = self.character_hp_max
                self.character_mp_now = self.character_mp_max
        if 65000<=self.exp<70000 :#レベル29
            self.level = 29
            self.character_hp_max = 210
            self.character_mp_max = 200
            self.character_pw = 140
            self.character_agi = 130
            if self.levelup_frag == self.level:
                self.levelup_frag += 1
                self.character_hp_now = self.character_hp_max
                self.character_mp_now = self.character_mp_max
        if 90000<=self.exp :#レベル30
            self.level = 30
            self.character_hp_max = 512
            self.character_mp_max = 512
            self.character_pw = 256
            self.character_agi = 256
            if self.levelup_frag == self.level:
                self.levelup_frag += 1
                self.character_hp_now = self.character_hp_max
                self.character_mp_now = self.character_mp_max    

        self.level_10=(self.level%100)//10
        self.level_1=(self.level%10)//1

        self.gold_10000=(self.gold//10000)
        self.gold_1000=(self.gold%10000)//1000
        self.gold_100=(self.gold%1000)//100
        self.gold_10=(self.gold%100)//10
        self.gold_1=(self.gold%10)//1

        self.exp_10000=(self.exp//10000)
        self.exp_1000=(self.exp%10000)//1000
        self.exp_100=(self.exp%1000)//100
        self.exp_10=(self.exp%100)//10
        self.exp_1=(self.exp%10)//1

        self.character_hp_now_100 =(self.character_hp_now%1000)//100
        self.character_hp_now_10 =(self.character_hp_now%100)//10
        self.character_hp_now_1 =(self.character_hp_now%10)//1

        self.character_mp_now_100 =(self.character_mp_now%1000)//100
        self.character_mp_now_10 =(self.character_mp_now%100)//10
        self.character_mp_now_1 =(self.character_mp_now%10)//1

        self.character_pw_100 =(self.character_pw%1000)//100
        self.character_pw_10 =(self.character_pw%100)//10
        self.character_pw_1 =(self.character_pw%10)//1

        self.character_agi_100 =(self.character_agi%1000)//100
        self.character_agi_10 =(self.character_agi%100)//10
        self.character_agi_1 =(self.character_agi%10)//1

    def menu1(self):#メニュー画面表示
            pyxel.bltm(self.menu_dis_x,self.menu_dis_y,0,256,0,64,96)
            pyxel.blt(self.menu_dis_x + 16,self.menu_dis_y,1,self.player_name_1_x,self.player_name_1_y,8,8,0)
            pyxel.blt(self.menu_dis_x + 24,self.menu_dis_y,1,self.player_name_2_x,self.player_name_2_y,8,8,0)
            pyxel.blt(self.menu_dis_x + 32,self.menu_dis_y,1,self.player_name_3_x,self.player_name_3_y,8,8,0)
            pyxel.blt(self.menu_dis_x + 40,self.menu_dis_y,1,self.player_name_4_x,self.player_name_4_y,8,8,0)
            pyxel.blt(self.menu_dis_x + 40, self.menu_dis_y + 16, 1, self.level_10*8, 112, 8, 8, 0)
            pyxel.blt(self.menu_dis_x + 48, self.menu_dis_y + 16, 1, self.level_1*8, 112, 8, 8, 0)
            
            pyxel.blt(self.menu_dis_x + 32, self.menu_dis_y + 32, 1, self.character_hp_now_100*8, 112, 8, 8, 0)
            pyxel.blt(self.menu_dis_x + 40, self.menu_dis_y + 32, 1, self.character_hp_now_10*8, 112, 8, 8, 0)
            pyxel.blt(self.menu_dis_x + 48, self.menu_dis_y + 32, 1, self.character_hp_now_1*8, 112, 8, 8, 0)

            pyxel.blt(self.menu_dis_x + 32, self.menu_dis_y + 48, 1, self.character_mp_now_100*8, 112, 8, 8, 0)
            pyxel.blt(self.menu_dis_x + 40, self.menu_dis_y + 48, 1, self.character_mp_now_10*8, 112, 8, 8, 0)
            pyxel.blt(self.menu_dis_x + 48, self.menu_dis_y + 48, 1, self.character_mp_now_1*8, 112, 8, 8, 0)

            pyxel.blt(self.menu_dis_x + 16, self.menu_dis_y + 64, 1, self.gold_10000*8, 112, 8, 8, 0)
            pyxel.blt(self.menu_dis_x + 24, self.menu_dis_y + 64, 1, self.gold_1000*8, 112, 8, 8, 0)
            pyxel.blt(self.menu_dis_x + 32, self.menu_dis_y + 64, 1, self.gold_100*8, 112, 8, 8, 0)
            pyxel.blt(self.menu_dis_x + 40, self.menu_dis_y + 64, 1, self.gold_10*8, 112, 8, 8, 0)
            pyxel.blt(self.menu_dis_x + 48, self.menu_dis_y + 64, 1, self.gold_1*8, 112, 8, 8, 0)

            pyxel.blt(self.menu_dis_x + 16, self.menu_dis_y + 80, 1, self.exp_10000*8, 112, 8, 8, 0)
            pyxel.blt(self.menu_dis_x + 24, self.menu_dis_y + 80, 1, self.exp_1000*8, 112, 8, 8, 0)
            pyxel.blt(self.menu_dis_x + 32, self.menu_dis_y + 80, 1, self.exp_100*8, 112, 8, 8, 0)
            pyxel.blt(self.menu_dis_x + 40, self.menu_dis_y + 80, 1, self.exp_10*8, 112, 8, 8, 0)
            pyxel.blt(self.menu_dis_x + 48, self.menu_dis_y + 80, 1, self.exp_1*8, 112, 8, 8, 0)

    def comand(self):#戦闘のコマンド表示
        pyxel.bltm(self.menu_dis_x+16*8,self.menu_dis_y,0,40*8,0*8,14*8,6*8)#コマンドの枠
        pyxel.bltm(56,160,0,32*8,16*8,18*8,10*8)#メッセージの枠
        pyxel.blt(self.menu_dis_x+9*8+self.battle_command_x*8,self.menu_dis_y+self.battle_command_y*8,1,self.select_ui,96,8,8,0)

    def slaim_update(self):
        if pyxel.btnp(pyxel.KEY_SPACE) and self.battle_command_frag == True:
            if self.battle_command_x==8 and self.battle_command_y ==2:
                self.player_attack_frag = True
                self.nom_attack_time =pyxel.frame_count
                self.battle_command_frag = False

        if pyxel.btnp(pyxel.KEY_SPACE):
                self.n = self.massage_up(self.n)
                self.m = self.massage_up(self.m)
                self.player_attack = self.massage_up(self.player_attack)
                self.taosu = self.massage_up(self.taosu)
                print(self.player_attack_frag)

        if pyxel.frame_count % 1 ==0 and self.frag ==True and self.nom_suraimu_emg < 16:
            self.nom_suraimu_emg += 1
        if self.nom_suraimu_emg ==16:
            if pyxel.frame_count % 1 ==0 and self.frag ==True and self.nom_command < 16:
                self.nom_command += 1
        if self.nom_command == 15:
            self.battle_command_frag = True

        if pyxel.frame_count % 1 ==0 and self.player_attack_frag == True and self.nom_attack < 16:
            self.nom_attack += 1
            self.a=8
        if pyxel.frame_count==self.nom_attack_time+1:
            self.b=8
            pyxel.play(2,25)
        if pyxel.frame_count==self.nom_attack_time+2:
            self.c=8
        if pyxel.frame_count==self.nom_attack_time+3:
            self.d=8
        if self.nom_attack ==16:
            if pyxel.frame_count % 1 ==0 and  self.nom_taosu < 16:
                self.nom_taosu += 1
        if self.nom_taosu ==10:
            pyxel.stop(0)
            pyxel.stop(1)
            self.frag = False

        if self.nom_taosu ==15:
            pyxel.play(2,56)
            self.exp+=int(pyxel.rndi(10,20))
            self.gold+=int(pyxel.rndi(10,30))
            self.back_frag = pyxel.frame_count
        
        if self.now_level < self.level and self.level_music == True:
            self.level_music =False
            pyxel.stop(2)
            pyxel.play(3,0)

    def slaim_draw(self):
        if self.frag == True:
            pyxel.blt(120,140,0,0,64,16,16,0)
        pyxel.bltm(64,self.n*16,0,0*8,32*8,self.nom_suraimu_emg * 8,2*8)#スライムがあらわれた！
        pyxel.bltm(64,self.m*16,0,0*8,34*8,self.nom_command * 8,2*8)#コマンド？
        if self.player_attack_frag == True:
            pyxel.bltm(64,self.player_attack*16,0,0*8,36*8,self.nom_attack * 8,2*8)
            pyxel.blt(64,self.player_attack*16+8,1,self.player_name_1_x,self.player_name_1_y,8,self.a,0)
            pyxel.blt(72,self.player_attack*16+8,1,self.player_name_2_x,self.player_name_2_y,8,self.b,0)
            pyxel.blt(80,self.player_attack*16+8,1,self.player_name_3_x,self.player_name_3_y,8,self.c,0)
            pyxel.blt(88,self.player_attack*16+8,1,self.player_name_4_x,self.player_name_4_y,8,self.d,0)
            pyxel.bltm(64,self.taosu*16,0,0*8,42*8,self.nom_taosu * 8,2*8)
        
    def massage_up(self,a):#メッセージを上に送るやつ
        if pyxel.btnp(pyxel.KEY_SPACE) and not a <= -1:
            a -=1
            if a == 9.5:
                a = -1
        return a
    
    def run(self):#実行するところ
        self.scene = SCENE_TITLE
        pyxel.playm(0, loop=True)
        pyxel.run(self.update, self.draw)
        
    def update(self):#スクリーンとか増やす
      if pyxel.btnp(pyxel.KEY_Q):
         pyxel.quit()

      if self.scene == SCENE_TITLE:
            self.update_title_scene()
      elif self.scene == SCENE_START:
            self.update_start_scene()
      elif self.scene == SCENE_CASTLE:
            self.update_castle_scene()
      elif self.scene == SCENE_FIELD1:
            self.update_field1_scene()
      elif self.scene == SCENE_BATTLE:
            self.update_battle_scene()
    
    def update_title_scene(self):#タイトル
        if pyxel.btnp(pyxel.KEY_SPACE):
            pyxel.playm(2, loop = True)
            self.scene = SCENE_START
    
    def update_start_scene(self):#名前を決めるシーン
        if pyxel.frame_count % 10 == 0:#時間経過の文章
            self.time_count +=1
            if self.time_count % 2 == 0:
                self.select_ui = 48
            else:
                self.select_ui = 56
        
        if 0 < self.select_x <=144:
            if pyxel.btnp(pyxel.KEY_LEFT):
                pyxel.play(3,63)
                self.select_x -= 16
        if 0 <= self.select_x <144 and 0<= self.select_y <=64 or 0 <= self.select_x <128 and self.select_y == 80:
            if pyxel.btnp(pyxel.KEY_RIGHT):
                pyxel.play(3,63)
                self.select_x += 16
        if 0 < self.select_y <=80:
            if pyxel.btnp(pyxel.KEY_UP):
                pyxel.play(3,63)
                self.select_y -= 16
        if 0 <= self.select_x <=96 and 0 <= self.select_y <80 or 112 == self.select_x and 0<= self.select_y <64 or 128 == self.select_x and 0<= self.select_y <80 or 144 == self.select_x and 0<= self.select_y <64:
            if pyxel.btnp(pyxel.KEY_DOWN):
                pyxel.play(3,63)
                self.select_y += 16

        if self.select_x == 112 and self.select_y == 80:
                if pyxel.btnp(pyxel.KEY_RIGHT):
                   self.select_x += 16
                if pyxel.btnp(pyxel.KEY_LEFT):
                   self.select_x -= 16
        
        if pyxel.btnp(pyxel.KEY_SPACE):#表示位置を設定する
            pyxel.play(3,63)
            if (self.select_x == 96 and self.select_y == 80) and self.x_count > 0:
                self.x_count -=1
            elif (not(self.select_x == 128 and self.select_y == 80)
                  and not (self.select_x == 96 and self.select_y == 32)
                  and not (self.select_x == 96 and self.select_y == 64)
                  and not (self.select_x == 96 and self.select_y == 80)
                  and not (self.select_x == 128 and self.select_y == 32)
                  and not (self.select_x == 128 and self.select_y == 64)
                  and self.x_count < 4
                  ):
                self.x_count +=1

        if self.x_count == 0:#名前の1文字目の消去
            if pyxel.btnp(pyxel.KEY_SPACE):
                if (self.select_x == 96 and self.select_y == 80):#消去
                    self.player_name_1_x = 8
                    self.player_name_1_y = 56        

        if self.x_count == 1:#名前の1文字目の処理
            if pyxel.btnp(pyxel.KEY_SPACE):
                if (self.select_x == 96 and self.select_y == 80):#消去
                    self.player_name_2_x = 8
                    self.player_name_2_y = 56

                if (self.select_x == 0 and self.select_y == 0):#あ
                    self.player_name_1_x = 0
                    self.player_name_1_y = 0
                if (self.select_x == 16 and self.select_y == 0):#い
                    self.player_name_1_x = 8
                    self.player_name_1_y = 0
                if (self.select_x == 32 and self.select_y == 0):#う
                    self.player_name_1_x = 16
                    self.player_name_1_y = 0
                if (self.select_x == 48 and self.select_y == 0):#え
                    self.player_name_1_x = 24
                    self.player_name_1_y = 0
                if (self.select_x == 64 and self.select_y == 0):#お
                    self.player_name_1_x = 32
                    self.player_name_1_y = 0

                if (self.select_x == 0 and self.select_y == 16):#か
                    self.player_name_1_x = 0
                    self.player_name_1_y = 8
                if (self.select_x == 16 and self.select_y == 16):#き
                    self.player_name_1_x = 8
                    self.player_name_1_y = 8
                if (self.select_x == 32 and self.select_y == 16):#く
                    self.player_name_1_x = 16
                    self.player_name_1_y = 8
                if (self.select_x == 48 and self.select_y == 16):#け
                    self.player_name_1_x = 24
                    self.player_name_1_y = 8
                if (self.select_x == 64 and self.select_y == 16):#こ
                    self.player_name_1_x = 32
                    self.player_name_1_y = 8

                if (self.select_x == 0 and self.select_y == 32):#さ
                    self.player_name_1_x = 0
                    self.player_name_1_y = 16
                if (self.select_x == 16 and self.select_y == 32):#し
                    self.player_name_1_x = 8
                    self.player_name_1_y = 16
                if (self.select_x == 32 and self.select_y == 32):#す
                    self.player_name_1_x = 16
                    self.player_name_1_y = 16
                if (self.select_x == 48 and self.select_y == 32):#せ
                    self.player_name_1_x = 24
                    self.player_name_1_y = 16
                if (self.select_x == 64 and self.select_y == 32):#そ
                    self.player_name_1_x = 32
                    self.player_name_1_y = 16

                if (self.select_x == 0 and self.select_y == 48):#た
                    self.player_name_1_x = 0
                    self.player_name_1_y = 24
                if (self.select_x == 16 and self.select_y == 48):#ち
                    self.player_name_1_x = 8
                    self.player_name_1_y = 24
                if (self.select_x == 32 and self.select_y == 48):#つ
                    self.player_name_1_x = 16
                    self.player_name_1_y = 24
                if (self.select_x == 48 and self.select_y == 48):#て
                    self.player_name_1_x = 24
                    self.player_name_1_y = 24
                if (self.select_x == 64 and self.select_y == 48):#と
                    self.player_name_1_x = 32
                    self.player_name_1_y = 24

                if (self.select_x == 0 and self.select_y == 64):#な
                    self.player_name_1_x = 0
                    self.player_name_1_y = 32
                if (self.select_x == 16 and self.select_y == 64):#に
                    self.player_name_1_x = 8
                    self.player_name_1_y = 32
                if (self.select_x == 32 and self.select_y == 64):#ぬ
                    self.player_name_1_x = 16
                    self.player_name_1_y = 32
                if (self.select_x == 48 and self.select_y == 64):#ね
                    self.player_name_1_x = 24
                    self.player_name_1_y = 32
                if (self.select_x == 64 and self.select_y == 64):#の
                    self.player_name_1_x = 32
                    self.player_name_1_y = 32

                if (self.select_x == 0 and self.select_y == 80):#っ
                    self.player_name_1_x = 32
                    self.player_name_1_y = 88
                if (self.select_x == 16 and self.select_y == 80):#ゃ
                    self.player_name_1_x = 0
                    self.player_name_1_y = 88
                if (self.select_x == 32 and self.select_y == 80):#ゅ
                    self.player_name_1_x = 8
                    self.player_name_1_y = 88
                if (self.select_x == 48 and self.select_y == 80):#ょ
                    self.player_name_1_x = 16
                    self.player_name_1_y = 88
                if (self.select_x == 64 and self.select_y == 80):#濁点
                    self.player_name_1_x = 8
                    self.player_name_1_y = 96

                if (self.select_x == 80 and self.select_y == 0):#は
                    self.player_name_1_x = 0
                    self.player_name_1_y = 40
                if (self.select_x == 96 and self.select_y == 0):#ひ
                    self.player_name_1_x = 8
                    self.player_name_1_y = 40
                if (self.select_x == 112 and self.select_y == 0):#ふ
                    self.player_name_1_x = 16
                    self.player_name_1_y = 40
                if (self.select_x == 128 and self.select_y == 0):#へ
                    self.player_name_1_x = 24
                    self.player_name_1_y = 40
                if (self.select_x == 144 and self.select_y == 0):#ほ
                    self.player_name_1_x = 32
                    self.player_name_1_y = 40
                
                if (self.select_x == 80 and self.select_y == 16):#ま
                    self.player_name_1_x = 0
                    self.player_name_1_y = 48
                if (self.select_x == 96 and self.select_y == 16):#み
                    self.player_name_1_x = 8
                    self.player_name_1_y = 48
                if (self.select_x == 112 and self.select_y == 16):#む
                    self.player_name_1_x = 16
                    self.player_name_1_y = 48
                if (self.select_x == 128 and self.select_y == 16):#め
                    self.player_name_1_x = 24
                    self.player_name_1_y = 48
                if (self.select_x == 144 and self.select_y == 16):#も
                    self.player_name_1_x = 32
                    self.player_name_1_y = 48
                
                if (self.select_x == 80 and self.select_y == 32):#や
                    self.player_name_1_x = 0
                    self.player_name_1_y = 56
                if (self.select_x == 112 and self.select_y == 32):#ゆ
                    self.player_name_1_x = 16
                    self.player_name_1_y = 56
                if (self.select_x == 144 and self.select_y == 32):#よ
                    self.player_name_1_x = 32
                    self.player_name_1_y = 56

                if (self.select_x == 80 and self.select_y == 48):#ら
                    self.player_name_1_x = 0
                    self.player_name_1_y = 64
                if (self.select_x == 96 and self.select_y == 48):#り
                    self.player_name_1_x = 8
                    self.player_name_1_y = 64
                if (self.select_x == 112 and self.select_y == 48):#る
                    self.player_name_1_x = 16
                    self.player_name_1_y = 64
                if (self.select_x == 128 and self.select_y == 48):#れ
                    self.player_name_1_x = 24
                    self.player_name_1_y = 64
                if (self.select_x == 144 and self.select_y == 48):#ろ
                    self.player_name_1_x = 32
                    self.player_name_1_y = 64

                if (self.select_x == 80 and self.select_y == 64):#わ
                    self.player_name_1_x = 0
                    self.player_name_1_y = 72
                if (self.select_x == 112 and self.select_y == 64):#を
                    self.player_name_1_x = 16
                    self.player_name_1_y = 72
                if (self.select_x == 144 and self.select_y == 64):#ん
                    self.player_name_1_x = 32
                    self.player_name_1_y = 72

                if (self.select_x == 80 and self.select_y == 80):#半濁点
                    self.player_name_1_x = 0
                    self.player_name_1_y = 96

        if self.x_count == 2:#名前の2文字目の処理
            if pyxel.btnp(pyxel.KEY_SPACE):
                if (self.select_x == 96 and self.select_y == 80):#消去
                    self.player_name_3_x = 8
                    self.player_name_3_y = 56

                if (self.select_x == 0 and self.select_y == 0):#あ
                    self.player_name_2_x = 0
                    self.player_name_2_y = 0
                if (self.select_x == 16 and self.select_y == 0):#い
                    self.player_name_2_x = 8
                    self.player_name_2_y = 0
                if (self.select_x == 32 and self.select_y == 0):#う
                    self.player_name_2_x = 16
                    self.player_name_2_y = 0
                if (self.select_x == 48 and self.select_y == 0):#え
                    self.player_name_2_x = 24
                    self.player_name_2_y = 0
                if (self.select_x == 64 and self.select_y == 0):#お
                    self.player_name_2_x = 32
                    self.player_name_2_y = 0

                if (self.select_x == 0 and self.select_y == 16):#か
                    self.player_name_2_x = 0
                    self.player_name_2_y = 8
                if (self.select_x == 16 and self.select_y == 16):#き
                    self.player_name_2_x = 8
                    self.player_name_2_y = 8
                if (self.select_x == 32 and self.select_y == 16):#く
                    self.player_name_2_x = 16
                    self.player_name_2_y = 8
                if (self.select_x == 48 and self.select_y == 16):#け
                    self.player_name_2_x = 24
                    self.player_name_2_y = 8
                if (self.select_x == 64 and self.select_y == 16):#こ
                    self.player_name_2_x = 32
                    self.player_name_2_y = 8

                if (self.select_x == 0 and self.select_y == 32):#さ
                    self.player_name_2_x = 0
                    self.player_name_2_y = 16
                if (self.select_x == 16 and self.select_y == 32):#し
                    self.player_name_2_x = 8
                    self.player_name_2_y = 16
                if (self.select_x == 32 and self.select_y == 32):#す
                    self.player_name_2_x = 16
                    self.player_name_2_y = 16
                if (self.select_x == 48 and self.select_y == 32):#せ
                    self.player_name_2_x = 24
                    self.player_name_2_y = 16
                if (self.select_x == 64 and self.select_y == 32):#そ
                    self.player_name_2_x = 32
                    self.player_name_2_y = 16

                if (self.select_x == 0 and self.select_y == 48):#た
                    self.player_name_2_x = 0
                    self.player_name_2_y = 24
                if (self.select_x == 16 and self.select_y == 48):#ち
                    self.player_name_2_x = 8
                    self.player_name_2_y = 24
                if (self.select_x == 32 and self.select_y == 48):#つ
                    self.player_name_2_x = 16
                    self.player_name_2_y = 24
                if (self.select_x == 48 and self.select_y == 48):#て
                    self.player_name_2_x = 24
                    self.player_name_2_y = 24
                if (self.select_x == 64 and self.select_y == 48):#と
                    self.player_name_2_x = 32
                    self.player_name_2_y = 24

                if (self.select_x == 0 and self.select_y == 64):#な
                    self.player_name_2_x = 0
                    self.player_name_2_y = 32
                if (self.select_x == 16 and self.select_y == 64):#に
                    self.player_name_2_x = 8
                    self.player_name_2_y = 32
                if (self.select_x == 32 and self.select_y == 64):#ぬ
                    self.player_name_2_x = 16
                    self.player_name_2_y = 32
                if (self.select_x == 48 and self.select_y == 64):#ね
                    self.player_name_2_x = 24
                    self.player_name_2_y = 32
                if (self.select_x == 64 and self.select_y == 64):#の
                    self.player_name_2_x = 32
                    self.player_name_2_y = 32

                if (self.select_x == 0 and self.select_y == 80):#っ
                    self.player_name_2_x = 32
                    self.player_name_2_y = 88
                if (self.select_x == 16 and self.select_y == 80):#ゃ
                    self.player_name_2_x = 0
                    self.player_name_2_y = 88
                if (self.select_x == 32 and self.select_y == 80):#ゅ
                    self.player_name_2_x = 8
                    self.player_name_2_y = 88
                if (self.select_x == 48 and self.select_y == 80):#ょ
                    self.player_name_2_x = 16
                    self.player_name_2_y = 88
                if (self.select_x == 64 and self.select_y == 80):#濁点
                    self.player_name_2_x = 8
                    self.player_name_2_y = 96

                if (self.select_x == 80 and self.select_y == 0):#は
                    self.player_name_2_x = 0
                    self.player_name_2_y = 40
                if (self.select_x == 96 and self.select_y == 0):#ひ
                    self.player_name_2_x = 8
                    self.player_name_2_y = 40
                if (self.select_x == 112 and self.select_y == 0):#ふ
                    self.player_name_2_x = 16
                    self.player_name_2_y = 40
                if (self.select_x == 128 and self.select_y == 0):#へ
                    self.player_name_2_x = 24
                    self.player_name_2_y = 40
                if (self.select_x == 144 and self.select_y == 0):#ほ
                    self.player_name_2_x = 32
                    self.player_name_2_y = 40
                
                if (self.select_x == 80 and self.select_y == 16):#ま
                    self.player_name_2_x = 0
                    self.player_name_2_y = 48
                if (self.select_x == 96 and self.select_y == 16):#み
                    self.player_name_2_x = 8
                    self.player_name_2_y = 48
                if (self.select_x == 112 and self.select_y == 16):#む
                    self.player_name_2_x = 16
                    self.player_name_2_y = 48
                if (self.select_x == 128 and self.select_y == 16):#め
                    self.player_name_2_x = 24
                    self.player_name_2_y = 48
                if (self.select_x == 144 and self.select_y == 16):#も
                    self.player_name_2_x = 32
                    self.player_name_2_y = 48
                
                if (self.select_x == 80 and self.select_y == 32):#や
                    self.player_name_2_x = 0
                    self.player_name_2_y = 56
                if (self.select_x == 112 and self.select_y == 32):#ゆ
                    self.player_name_2_x = 16
                    self.player_name_2_y = 56
                if (self.select_x == 144 and self.select_y == 32):#よ
                    self.player_name_2_x = 32
                    self.player_name_2_y = 56

                if (self.select_x == 80 and self.select_y == 48):#ら
                    self.player_name_2_x = 0
                    self.player_name_2_y = 64
                if (self.select_x == 96 and self.select_y == 48):#り
                    self.player_name_2_x = 8
                    self.player_name_2_y = 64
                if (self.select_x == 112 and self.select_y == 48):#る
                    self.player_name_2_x = 16
                    self.player_name_2_y = 64
                if (self.select_x == 128 and self.select_y == 48):#れ
                    self.player_name_2_x = 24
                    self.player_name_2_y = 64
                if (self.select_x == 144 and self.select_y == 48):#ろ
                    self.player_name_2_x = 32
                    self.player_name_2_y = 64

                if (self.select_x == 80 and self.select_y == 64):#わ
                    self.player_name_2_x = 0
                    self.player_name_2_y = 72
                if (self.select_x == 112 and self.select_y == 64):#を
                    self.player_name_2_x = 16
                    self.player_name_2_y = 72
                if (self.select_x == 144 and self.select_y == 64):#ん
                    self.player_name_2_x = 32
                    self.player_name_2_y = 72

                if (self.select_x == 80 and self.select_y == 80):#半濁点
                    self.player_name_2_x = 0
                    self.player_name_2_y = 96

        if self.x_count == 3:#名前の3文字目の処理
            if pyxel.btnp(pyxel.KEY_SPACE):
                if (self.select_x == 96 and self.select_y == 80):#消去
                    self.player_name_4_x = 8
                    self.player_name_4_y = 56

                if (self.select_x == 0 and self.select_y == 0):#あ
                    self.player_name_3_x = 0
                    self.player_name_3_y = 0
                if (self.select_x == 16 and self.select_y == 0):#い
                    self.player_name_3_x = 8
                    self.player_name_3_y = 0
                if (self.select_x == 32 and self.select_y == 0):#う
                    self.player_name_3_x = 16
                    self.player_name_3_y = 0
                if (self.select_x == 48 and self.select_y == 0):#え
                    self.player_name_3_x = 24
                    self.player_name_3_y = 0
                if (self.select_x == 64 and self.select_y == 0):#お
                    self.player_name_3_x = 32
                    self.player_name_3_y = 0

                if (self.select_x == 0 and self.select_y == 16):#か
                    self.player_name_3_x = 0
                    self.player_name_3_y = 8
                if (self.select_x == 16 and self.select_y == 16):#き
                    self.player_name_3_x = 8
                    self.player_name_3_y = 8
                if (self.select_x == 32 and self.select_y == 16):#く
                    self.player_name_3_x = 16
                    self.player_name_3_y = 8
                if (self.select_x == 48 and self.select_y == 16):#け
                    self.player_name_3_x = 24
                    self.player_name_3_y = 8
                if (self.select_x == 64 and self.select_y == 16):#こ
                    self.player_name_3_x = 32
                    self.player_name_3_y = 8

                if (self.select_x == 0 and self.select_y == 32):#さ
                    self.player_name_3_x = 0
                    self.player_name_3_y = 16
                if (self.select_x == 16 and self.select_y == 32):#し
                    self.player_name_3_x = 8
                    self.player_name_3_y = 16
                if (self.select_x == 32 and self.select_y == 32):#す
                    self.player_name_3_x = 16
                    self.player_name_3_y = 16
                if (self.select_x == 48 and self.select_y == 32):#せ
                    self.player_name_3_x = 24
                    self.player_name_3_y = 16
                if (self.select_x == 64 and self.select_y == 32):#そ
                    self.player_name_3_x = 32
                    self.player_name_3_y = 16

                if (self.select_x == 0 and self.select_y == 48):#た
                    self.player_name_3_x = 0
                    self.player_name_3_y = 24
                if (self.select_x == 16 and self.select_y == 48):#ち
                    self.player_name_3_x = 8
                    self.player_name_3_y = 24
                if (self.select_x == 32 and self.select_y == 48):#つ
                    self.player_name_3_x = 16
                    self.player_name_3_y = 24
                if (self.select_x == 48 and self.select_y == 48):#て
                    self.player_name_3_x = 24
                    self.player_name_3_y = 24
                if (self.select_x == 64 and self.select_y == 48):#と
                    self.player_name_3_x = 32
                    self.player_name_3_y = 24

                if (self.select_x == 0 and self.select_y == 64):#な
                    self.player_name_3_x = 0
                    self.player_name_3_y = 32
                if (self.select_x == 16 and self.select_y == 64):#に
                    self.player_name_3_x = 8
                    self.player_name_3_y = 32
                if (self.select_x == 32 and self.select_y == 64):#ぬ
                    self.player_name_3_x = 16
                    self.player_name_3_y = 32
                if (self.select_x == 48 and self.select_y == 64):#ね
                    self.player_name_3_x = 24
                    self.player_name_3_y = 32
                if (self.select_x == 64 and self.select_y == 64):#の
                    self.player_name_3_x = 32
                    self.player_name_3_y = 32

                if (self.select_x == 0 and self.select_y == 80):#っ
                    self.player_name_3_x = 32
                    self.player_name_3_y = 88
                if (self.select_x == 16 and self.select_y == 80):#ゃ
                    self.player_name_3_x = 0
                    self.player_name_3_y = 88
                if (self.select_x == 32 and self.select_y == 80):#ゅ
                    self.player_name_3_x = 8
                    self.player_name_3_y = 88
                if (self.select_x == 48 and self.select_y == 80):#ょ
                    self.player_name_3_x = 16
                    self.player_name_3_y = 88
                if (self.select_x == 64 and self.select_y == 80):#濁点
                    self.player_name_3_x = 8
                    self.player_name_3_y = 96

                if (self.select_x == 80 and self.select_y == 0):#は
                    self.player_name_3_x = 0
                    self.player_name_3_y = 40
                if (self.select_x == 96 and self.select_y == 0):#ひ
                    self.player_name_3_x = 8
                    self.player_name_3_y = 40
                if (self.select_x == 112 and self.select_y == 0):#ふ
                    self.player_name_3_x = 16
                    self.player_name_3_y = 40
                if (self.select_x == 128 and self.select_y == 0):#へ
                    self.player_name_3_x = 24
                    self.player_name_3_y = 40
                if (self.select_x == 144 and self.select_y == 0):#ほ
                    self.player_name_3_x = 32
                    self.player_name_3_y = 40
                
                if (self.select_x == 80 and self.select_y == 16):#ま
                    self.player_name_3_x = 0
                    self.player_name_3_y = 48
                if (self.select_x == 96 and self.select_y == 16):#み
                    self.player_name_3_x = 8
                    self.player_name_3_y = 48
                if (self.select_x == 112 and self.select_y == 16):#む
                    self.player_name_3_x = 16
                    self.player_name_3_y = 48
                if (self.select_x == 128 and self.select_y == 16):#め
                    self.player_name_3_x = 24
                    self.player_name_3_y = 48
                if (self.select_x == 144 and self.select_y == 16):#も
                    self.player_name_3_x = 32
                    self.player_name_3_y = 48
                
                if (self.select_x == 80 and self.select_y == 32):#や
                    self.player_name_3_x = 0
                    self.player_name_3_y = 56
                if (self.select_x == 112 and self.select_y == 32):#ゆ
                    self.player_name_3_x = 16
                    self.player_name_3_y = 56
                if (self.select_x == 144 and self.select_y == 32):#よ
                    self.player_name_3_x = 32
                    self.player_name_3_y = 56

                if (self.select_x == 80 and self.select_y == 48):#ら
                    self.player_name_3_x = 0
                    self.player_name_3_y = 64
                if (self.select_x == 96 and self.select_y == 48):#り
                    self.player_name_3_x = 8
                    self.player_name_3_y = 64
                if (self.select_x == 112 and self.select_y == 48):#る
                    self.player_name_3_x = 16
                    self.player_name_3_y = 64
                if (self.select_x == 128 and self.select_y == 48):#れ
                    self.player_name_3_x = 24
                    self.player_name_3_y = 64
                if (self.select_x == 144 and self.select_y == 48):#ろ
                    self.player_name_3_x = 32
                    self.player_name_3_y = 64

                if (self.select_x == 80 and self.select_y == 64):#わ
                    self.player_name_3_x = 0
                    self.player_name_3_y = 72
                if (self.select_x == 112 and self.select_y == 64):#を
                    self.player_name_3_x = 16
                    self.player_name_3_y = 72
                if (self.select_x == 144 and self.select_y == 64):#ん
                    self.player_name_3_x = 32
                    self.player_name_3_y = 72

                if (self.select_x == 80 and self.select_y == 80):#半濁点
                    self.player_name_3_x = 0
                    self.player_name_3_y = 96

        if self.x_count == 4:#名前の4文字目の処理
            if pyxel.btnp(pyxel.KEY_SPACE):
                if (self.select_x == 0 and self.select_y == 0):#あ
                    self.player_name_4_x = 0
                    self.player_name_4_y = 0
                if (self.select_x == 16 and self.select_y == 0):#い
                    self.player_name_4_x = 8
                    self.player_name_4_y = 0
                if (self.select_x == 32 and self.select_y == 0):#う
                    self.player_name_4_x = 16
                    self.player_name_4_y = 0
                if (self.select_x == 48 and self.select_y == 0):#え
                    self.player_name_4_x = 24
                    self.player_name_4_y = 0
                if (self.select_x == 64 and self.select_y == 0):#お
                    self.player_name_4_x = 32
                    self.player_name_4_y = 0

                if (self.select_x == 0 and self.select_y == 16):#か
                    self.player_name_4_x = 0
                    self.player_name_4_y = 8
                if (self.select_x == 16 and self.select_y == 16):#き
                    self.player_name_4_x = 8
                    self.player_name_4_y = 8
                if (self.select_x == 32 and self.select_y == 16):#く
                    self.player_name_4_x = 16
                    self.player_name_4_y = 8
                if (self.select_x == 48 and self.select_y == 16):#け
                    self.player_name_4_x = 24
                    self.player_name_4_y = 8
                if (self.select_x == 64 and self.select_y == 16):#こ
                    self.player_name_4_x = 32
                    self.player_name_4_y = 8

                if (self.select_x == 0 and self.select_y == 32):#さ
                    self.player_name_4_x = 0
                    self.player_name_4_y = 16
                if (self.select_x == 16 and self.select_y == 32):#し
                    self.player_name_4_x = 8
                    self.player_name_4_y = 16
                if (self.select_x == 32 and self.select_y == 32):#す
                    self.player_name_4_x = 16
                    self.player_name_4_y = 16
                if (self.select_x == 48 and self.select_y == 32):#せ
                    self.player_name_4_x = 24
                    self.player_name_4_y = 16
                if (self.select_x == 64 and self.select_y == 32):#そ
                    self.player_name_4_x = 32
                    self.player_name_4_y = 16

                if (self.select_x == 0 and self.select_y == 48):#た
                    self.player_name_4_x = 0
                    self.player_name_4_y = 24
                if (self.select_x == 16 and self.select_y == 48):#ち
                    self.player_name_4_x = 8
                    self.player_name_4_y = 24
                if (self.select_x == 32 and self.select_y == 48):#つ
                    self.player_name_4_x = 16
                    self.player_name_4_y = 24
                if (self.select_x == 48 and self.select_y == 48):#て
                    self.player_name_4_x = 24
                    self.player_name_4_y = 24
                if (self.select_x == 64 and self.select_y == 48):#と
                    self.player_name_4_x = 32
                    self.player_name_4_y = 24

                if (self.select_x == 0 and self.select_y == 64):#な
                    self.player_name_4_x = 0
                    self.player_name_4_y = 32
                if (self.select_x == 16 and self.select_y == 64):#に
                    self.player_name_4_x = 8
                    self.player_name_4_y = 32
                if (self.select_x == 32 and self.select_y == 64):#ぬ
                    self.player_name_4_x = 16
                    self.player_name_4_y = 32
                if (self.select_x == 48 and self.select_y == 64):#ね
                    self.player_name_4_x = 24
                    self.player_name_4_y = 32
                if (self.select_x == 64 and self.select_y == 64):#の
                    self.player_name_4_x = 32
                    self.player_name_4_y = 32

                if (self.select_x == 0 and self.select_y == 80):#っ
                    self.player_name_4_x = 32
                    self.player_name_4_y = 88
                if (self.select_x == 16 and self.select_y == 80):#ゃ
                    self.player_name_4_x = 0
                    self.player_name_4_y = 88
                if (self.select_x == 32 and self.select_y == 80):#ゅ
                    self.player_name_4_x = 8
                    self.player_name_4_y = 88
                if (self.select_x == 48 and self.select_y == 80):#ょ
                    self.player_name_4_x = 16
                    self.player_name_4_y = 88
                if (self.select_x == 64 and self.select_y == 80):#濁点
                    self.player_name_4_x = 8
                    self.player_name_4_y = 96

                if (self.select_x == 80 and self.select_y == 0):#は
                    self.player_name_4_x = 0
                    self.player_name_4_y = 40
                if (self.select_x == 96 and self.select_y == 0):#ひ
                    self.player_name_4_x = 8
                    self.player_name_4_y = 40
                if (self.select_x == 112 and self.select_y == 0):#ふ
                    self.player_name_4_x = 16
                    self.player_name_4_y = 40
                if (self.select_x == 128 and self.select_y == 0):#へ
                    self.player_name_4_x = 24
                    self.player_name_4_y = 40
                if (self.select_x == 144 and self.select_y == 0):#ほ
                    self.player_name_4_x = 32
                    self.player_name_4_y = 40
                
                if (self.select_x == 80 and self.select_y == 16):#ま
                    self.player_name_4_x = 0
                    self.player_name_4_y = 48
                if (self.select_x == 96 and self.select_y == 16):#み
                    self.player_name_4_x = 8
                    self.player_name_4_y = 48
                if (self.select_x == 112 and self.select_y == 16):#む
                    self.player_name_4_x = 16
                    self.player_name_4_y = 48
                if (self.select_x == 128 and self.select_y == 16):#め
                    self.player_name_4_x = 24
                    self.player_name_4_y = 48
                if (self.select_x == 144 and self.select_y == 16):#も
                    self.player_name_4_x = 32
                    self.player_name_4_y = 48
                
                if (self.select_x == 80 and self.select_y == 32):#や
                    self.player_name_4_x = 0
                    self.player_name_4_y = 56
                if (self.select_x == 112 and self.select_y == 32):#ゆ
                    self.player_name_4_x = 16
                    self.player_name_4_y = 56
                if (self.select_x == 144 and self.select_y == 32):#よ
                    self.player_name_4_x = 32
                    self.player_name_4_y = 56

                if (self.select_x == 80 and self.select_y == 48):#ら
                    self.player_name_4_x = 0
                    self.player_name_4_y = 64
                if (self.select_x == 96 and self.select_y == 48):#り
                    self.player_name_4_x = 8
                    self.player_name_4_y = 64
                if (self.select_x == 112 and self.select_y == 48):#る
                    self.player_name_4_x = 16
                    self.player_name_4_y = 64
                if (self.select_x == 128 and self.select_y == 48):#れ
                    self.player_name_4_x = 24
                    self.player_name_4_y = 64
                if (self.select_x == 144 and self.select_y == 48):#ろ
                    self.player_name_4_x = 32
                    self.player_name_4_y = 64

                if (self.select_x == 80 and self.select_y == 64):#わ
                    self.player_name_4_x = 0
                    self.player_name_4_y = 72
                if (self.select_x == 112 and self.select_y == 64):#を
                    self.player_name_4_x = 16
                    self.player_name_4_y = 72
                if (self.select_x == 144 and self.select_y == 64):#ん
                    self.player_name_4_x = 32
                    self.player_name_4_y = 72

                if (self.select_x == 80 and self.select_y == 80):#半濁点
                    self.player_name_4_x = 0
                    self.player_name_4_y = 96


        #以下　次のシーンに行くところ
        if self.select_x + 48 == 176 and self.select_y + 96 == 176:
               if pyxel.btnp(pyxel.KEY_SPACE):
                    self.canmove_frag = 5
                    self.scroll_x = 80
                    self.scroll_y = -160
                    pyxel.playm(4, loop = True)
                    self.scene = SCENE_CASTLE

    def king_update(self):
        if pyxel.btnp(pyxel.KEY_SPACE):
            self.canmove_frag = 0
    def king_draw(self):
        pyxel.bltm(56,160,0,32*8,16*8,18*8,10*8)#メッセージの枠

    def update_castle_scene(self):#ラダトーム
        if pyxel.frame_count % 10 == 0 and self.canmove_frag == 0:#時間経過の文章
            self.time_count +=1
            if self.time_count % 2 == 0:
                self.character_ui = 64
            else:
                self.character_ui = 80
        
        App.level_non(self)
        
        if self.canmove_frag == 5:
            App.king_update(self)

        #以下歩行についてのやつ
        if pyxel.btnp(pyxel.KEY_C):
            pyxel.play(3,63)
            self.canmove_frag = 1
        if (pyxel.btnp(pyxel.KEY_X) 
            and self.canmove_frag == 1
            ):
            pyxel.play(3,63)
            self.canmove_frag = 0
        
        if self.canmove_frag == 0:#移動
            if pyxel.btn(pyxel.KEY_LEFT):
                move_f_left = pyxel.tilemap(2).pget(self.scroll_x/8+47,self.scroll_y/8+48)
                if move_f_left in check:
                    self.scroll_x -= 2

            elif pyxel.btn(pyxel.KEY_RIGHT):
                move_f_right = pyxel.tilemap(2).pget(self.scroll_x/8+49,self.scroll_y/8+48)
                if move_f_right in check:
                    self.scroll_x += 2

            elif pyxel.btn(pyxel.KEY_UP):
                move_f_up = pyxel.tilemap(2).pget(self.scroll_x/8+48,self.scroll_y/8+47)
                if move_f_up in check:
                    self.scroll_y -= 2

            elif pyxel.btn(pyxel.KEY_DOWN):
                move_f_down = pyxel.tilemap(2).pget(self.scroll_x/8+48,self.scroll_y/8+49)
                if move_f_down in check:
                    self.scroll_y += 2

        if self.scroll_x < -240 or 248 < self.scroll_x or self.scroll_y < -232:#外に出る
            self.scroll_x = 0
            self.scroll_y = 0
            pyxel.playm(1, loop = True)
            self.scene = SCENE_FIELD1

    def update_field1_scene(self):#フィールド
        if pyxel.frame_count % 10 == 0 and self.canmove_frag == 0:#時間経過の文章
            self.time_count +=1
            if self.time_count % 2 == 0:
                self.character_ui = 64
            else:
                self.character_ui = 80

        App.level_non(self)

        if pyxel.btnp(pyxel.KEY_C):
            pyxel.play(3,63)
            self.canmove_frag = 1
        if pyxel.btnp(pyxel.KEY_X):
            pyxel.play(3,63)
            self.canmove_frag = 0
        
        if self.canmove_frag == 0:#移動のプログラム
            if pyxel.btn(pyxel.KEY_LEFT):
                #print(3)
                move_f_left = pyxel.tilemap(1).pget(self.scroll_x/8+95,self.scroll_y/8+96)
                if move_f_left in check:
                    self.scroll_x -= 2
                if move_f_left in damage1:
                    self.damege_frag += 1
                    if self.damege_frag % 8 ==0:
                        if self.character_hp_now >1:
                            self.character_hp_now -= 1
                        else:
                            self.character_hp_now = 1
                #エンカウント
                if move_f_left in enca1:
                    self.encount_frag -= 1
                if move_f_left in enca2:
                    self.encount_frag -= 2
                if move_f_left in enca3:
                    self.encount_frag -= 3

            elif pyxel.btn(pyxel.KEY_RIGHT):
                move_f_right = pyxel.tilemap(1).pget(self.scroll_x/8+97,self.scroll_y/8+96)
                if move_f_right in check:
                    self.scroll_x += 2
                if move_f_right in damage1:
                    self.damege_frag += 1
                    if self.damege_frag % 8 ==0:
                        if self.character_hp_now >1:
                            self.character_hp_now -= 1
                        else:
                            self.character_hp_now = 1
                #エンカウント
                if move_f_right in enca1:
                    self.encount_frag -= 1
                if move_f_right in enca2:
                    self.encount_frag -= 2
                if move_f_right in enca3:
                    self.encount_frag -= 3

            elif pyxel.btn(pyxel.KEY_UP):
                move_f_up = pyxel.tilemap(1).pget(self.scroll_x/8+96,self.scroll_y/8+95)
                if move_f_up in check:
                    self.scroll_y -= 2
                if move_f_up in damage1:
                    self.damege_frag += 1
                    if self.damege_frag % 8 ==0:
                        if self.character_hp_now >1:
                            self.character_hp_now -= 1
                        else:
                            self.character_hp_now = 1
                #エンカウント
                if move_f_up in enca1:
                    self.encount_frag -= 1
                if move_f_up in enca2:
                    self.encount_frag -= 2
                if move_f_up in enca3:
                    self.encount_frag -= 3

            elif pyxel.btn(pyxel.KEY_DOWN):
                move_f_down = pyxel.tilemap(1).pget(self.scroll_x/8+96,self.scroll_y/8+97)
                if move_f_down in check:
                    self.scroll_y += 2
                if move_f_down in damage1:
                    self.damege_frag += 1
                    if self.damege_frag % 8 ==0:
                        if self.character_hp_now >1:
                            self.character_hp_now -= 1
                        else:
                            self.character_hp_now = 1
                #エンカウント
                if move_f_down in enca1:
                    self.encount_frag -= 1
                if move_f_down in enca2:
                    self.encount_frag -= 2
                if move_f_down in enca3:
                    self.encount_frag -= 3

        #ラダトームの出入り
        if self.scroll_x < -12 or 10 < self.scroll_x or self.scroll_y < -12 or 10 < self.scroll_y:
            self.rada_flag = True
        if -4 < self.scroll_x < 4 and  -4 < self.scroll_y < 4 and self.rada_flag == True:
                    self.scroll_x = -232
                    self.scroll_y = 0
                    self.rada_flag = False
                    pyxel.playm(4, loop = True)
                    self.scene = SCENE_CASTLE
        #ラダトームの出入り

        if (self.encount_frag < 0
            or pyxel.btnp(pyxel.KEY_B)
            ):
            self.encount_frag = 70000
            self.canmove_frag = 100
            self.musicstrattime = pyxel.frame_count
            self.now_level = self.level
            pyxel.stop(0)
            pyxel.stop(1)
            pyxel.play(2,17)
            pyxel.play(3,18)

        if pyxel.frame_count == self.musicstrattime + 60:
            self.frag = True
            pyxel.playm(3, loop = True)
            self.scene = SCENE_BATTLE

    def update_battle_scene(self):#戦闘画面
        App.level_non(self)
        if self.battle_command_frag == True:#コマンド操作

            if pyxel.frame_count % 10 == 0:#時間経過の文章
                self.time_count +=1
                if self.time_count % 2 == 0:
                    self.select_ui = 48
                else:
                    self.select_ui = 56

            if pyxel.btn(pyxel.KEY_LEFT):
                if self.battle_command_x == 14:
                    pyxel.play(3,63)
                    self.battle_command_x -=6
                else:
                    None
            if pyxel.btn(pyxel.KEY_RIGHT):
                if self.battle_command_x == 8:
                    pyxel.play(3,63)
                    self.battle_command_x +=6
                else:
                    None
            if pyxel.btn(pyxel.KEY_UP):
                if self.battle_command_y == 4:
                    pyxel.play(3,63)
                    self.battle_command_y -=2
                else:
                    None
            if pyxel.btn(pyxel.KEY_DOWN):
                if self.battle_command_y == 2:
                    pyxel.play(3,63)
                    self.battle_command_y +=2
                else:
                    None

    #if pyxel.btnp(pyxel.KEY_SPACE):
    #    self.battle_command_frag = False
        App.slaim_update(self)

        if (pyxel.btnp(pyxel.KEY_B) or
            pyxel.btnp(pyxel.KEY_SPACE) and self.battle_command_x==8 and self.battle_command_y ==4 or
            pyxel.frame_count == self.back_frag+60
            ):#フィールドに戻る
            self.encount_frag = pyxel.rndi(300,700)
            self.canmove_frag = 0
            self.battle_command_frag = False

            self.frag = False
            self.nom_command = 0 #コマンド？
            self.nom_suraimu_emg = 0#スライムがあらわれた！
            self.nom_attack = 0#⚪︎⚪︎⚪︎⚪︎の攻撃！
            self.nom_attack_time = -100
            self.a = 0
            self.b = 0
            self.c = 0
            self.d = 0
            self.n =10.5
            self.m =11.5
            self.player_attack =12.5
            self.player_attack_frag = False
            self.taosu = 13.5
            self.nom_taosu = 0
            self.back_frag = -100
            self.now_level = 0
            self.level_music =True

            pyxel.playm(1, loop = True)
            self.scene = SCENE_FIELD1
    
    def draw(self):#スクリーンとか増やす
      pyxel.cls(0)

      if self.scene == SCENE_TITLE:
            self.draw_title_scene()
      elif self.scene == SCENE_START:
            self.draw_start_scene()
      elif self.scene == SCENE_CASTLE:
            self.draw_castle_scene()
      elif self.scene == SCENE_FIELD1:
            self.draw_field1_scene()
      elif self.scene == SCENE_BATTLE:
            self.draw_battle_scene()

    def draw_title_scene(self):#タイトル
        pyxel.cls(1)
        pyxel.bltm(5, 0, 0, 64*8, 0, 256, 12*8,)
        pyxel.bltm(60,130,0,73*8,13*8,18*8,7*8)

    def draw_start_scene(self):#名前を決めるシーン
        pyxel.cls(0)
        pyxel.bltm(0, 0, 0, 0, 0, 256, 256, 0)
        pyxel.blt(48 + self.select_x, 96 + self.select_y, 1, self.select_ui, 96, 8, 8, 0)
        #pyxel.text(0,5,'x='+ str(self.select_x),4)
        #pyxel.text(0,10,'y='+ str(self.select_y),4)
        #pyxel.text(0,15,'x_c='+ str(self.x_count),4)

        pyxel.blt(78,72,1,self.player_name_1_x,self.player_name_1_y,8,8,0)
        pyxel.blt(88,72,1,self.player_name_2_x,self.player_name_2_y,8,8,0)
        pyxel.blt(98,72,1,self.player_name_3_x,self.player_name_3_y,8,8,0)
        pyxel.blt(108,72,1,self.player_name_4_x,self.player_name_4_y,8,8,0)

        #pyxel.blt(68+self.x_count*10,72,1,self.player_name_1_x,self.player_name_1_y,8,8,0)

    def draw_castle_scene(self):#ラダトーム
        pyxel.cls(13)
        pyxel.bltm(0,0,2,256 + self.scroll_x ,256 + self.scroll_y ,511 + self.scroll_x, 511 + self.scroll_x)
        pyxel.blt(128, 128, 0, self.character_ui, 64, 16, 16, 0)
        #pyxel.text(0,5,'x='+ str(self.scroll_x),7)
        #pyxel.text(0,10,'y='+ str(self.scroll_y),7)
        if self.canmove_frag == 1:
            App.menu1(self)

        if self.canmove_frag == 5:
            App.king_draw(self)
            #pyxel.bltm(56,160,0,32*8,16*8,18*8,10*8)#メッセージの枠
            
    def draw_field1_scene(self):#フィールド
        pyxel.cls(13)
        pyxel.bltm(0,0,1,640 + self.scroll_x ,640 + self.scroll_y ,895 + self.scroll_x, 895 + self.scroll_x)
        pyxel.blt(128, 128, 0, self.character_ui, 64, 16, 16, 0)
        #pyxel.text(0,5,'x='+ str(self.encount_frag),0)
        #pyxel.text(0,10,'y='+ str(self.scroll_y),0)


        if self.canmove_frag == 1:
            App.menu1(self)

    def draw_battle_scene(self):#戦闘画面
        pyxel.cls(0)
        App.menu1(self)
        App.comand(self)
        App.slaim_draw(self)


App().run()