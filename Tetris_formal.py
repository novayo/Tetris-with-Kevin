import pygame
import sys
import random


######### 初始化pygame
pygame.init()  

######### 建立背景
background = pygame.display.set_mode((400, 800)) 
FPS = pygame.time.Clock()

######### 設定畫面上方的文字
pygame.display.set_caption("Tetris")


######### 更改變數名，避免與Python內建的list類型重名
block_list = []   






######### 記錄各種方塊的上下左右
class Block() :
    
    
    def T_block(color,x,y) :
        
    
        up = [[color,x,y ],[color,x+40,y ],[color,x-40,y ],[color,x,y -40]] 
        down = [[color,x,y],[color,x+40,y ],[color,x-40,y ],[color,x,y + 40 ]]
        right = [[color,x,y],[color,x,y -40],[color,x,y +40],[color,x+40,y ]]
        left = [[color,x,y ],[color,x,y -40],[color,x,y +40],[color,x-40,y ]]

        return up,down,right,left
    
    
    def L_block(color,x,y) :
        
        up = [[color,x,y ],[color,x+40,y ],[color,x-40,y ],[color,x+40,y -40]] 
        down = [[color,x,y],[color,x+40,y ],[color,x-40,y ],[color,x-40,y + 40 ]]
        right = [[color,x,y],[color,x,y -40],[color,x,y +40],[color,x+40,y+40 ]]
        left = [[color,x,y ],[color,x,y -40],[color,x,y +40],[color,x-40,y - 40 ]]
        
        
        return up,down,right,left
        
    
    def J_block(color,x,y) :
        
        
        up = [[color,x,y ],[color,x+40,y ],[color,x-40,y ],[color,x-40,y -40]] 
        down = [[color,x,y],[color,x+40,y ],[color,x-40,y ],[color,x+40,y + 40 ]]
        right = [[color,x,y],[color,x,y -40],[color,x,y +40],[color,x+40,y-40 ]]
        left = [[color,x,y ],[color,x,y -40],[color,x,y +40],[color,x-40,y + 40 ]]
        

        return up,down,right,left
    
    
    def I_block(color,x,y) :
        
        
        up = [[color,x,y],[color,x,y-40],[color,x,y+40],[color,x,y+80]]
        down = up
        right = [[color,x,y],[color,x-40,y],[color,x+40,y],[color,x+80,y]]
        left = right

        return up,down,right,left

    
    def O_block(color,x,y) :
        
        up = [[color,x,y],[color,x+40,y],[color,x,y+40],[color,x+40,y+40]]
        down = up
        right = up
        left = up

        return up,down,right,left

    
    def S_block(color,x,y) :
        
        up = [[color,x,y],[color,x-40,y],[color,x,y-40],[color,x+40,y-40]]
        down = up
        right = [[color,x,y],[color,x+40,y],[color,x,y-40],[color,x+40,y+40]]
        left = right

        return up,down,right,left
    
    
    def Z_block(color,x,y) :
        
        up = [[color,x,y],[color,x+40,y],[color,x,y-40],[color,x-40,y-40]]
        down = up
        right = [[color,x,y],[color,x-40,y],[color,x,y-40],[color,x-40,y+40]]
        left = right

        return up,down,right,left
    
    
    
    

   
######### 獲取值的分類
class Get_value () :
    
    
    ######### 初始化資料
    def get_inital_value() :
        global block_figure
        
        
        ######### 初始資料，這是方塊剛生成時會用到的
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        x = random.randrange(0, 361, 40)
        y = 0
        
        
        ######### 先隨機分配要生成哪一種
        ######### 再把值傳進去病得出上下左右的真正值
        ######### 之後再選擇要哪一種
        block_figure = random.choice(['T','L','I','J','O','S','Z'])
        up,down,right,left = Get_value.renew_data(color,x,y)
        temp_list = random.choice([up,down,left,right] )
        
        
        ######### 檢查x值是否有超出邊界，如果有的話這個函數就再重跑一次
        if not Get_value.check_boundary(temp_list) :
            temp_list = Get_value.get_inital_value()

        
        return temp_list
    
    
    
    
    def get_changing_value(temp_list) :
        
        ######### 已經生成的方塊，在要更換方向（變左遍右等）需要更新color,x,y,temp_list
        ######### 初始資料，這是方塊剛生成時會用到的這樣下面的self.up......才會依據現在的x,y值進行判定
        ######### Rotate在判定時才知道self.up......是啥
        color = temp_list[0][0]
        x = temp_list[0][1]
        y = temp_list[0][2]
        
        up,down,right,left = Get_value.renew_data(color,x,y)
        
        
        return up,down,right,left
    
    
    
    ######### 用來更新上下左右的地方
    def renew_data(color,x,y) :
    
        if block_figure == 'T' :
           up,down,right,left = Block.T_block(color,x,y)
        
        if block_figure == 'L' :
           up,down,right,left = Block.L_block(color,x,y)
           
        if block_figure == 'I' :
           up,down,right,left = Block.I_block(color,x,y)
        
        if block_figure == 'J' :
           up,down,right,left = Block.J_block(color,x,y)
        
        if block_figure == 'O' :
           up,down,right,left = Block.O_block(color,x,y)
           
        if block_figure == 'S' :
           up,down,right,left = Block.S_block(color,x,y)
        
        if block_figure == 'Z' :
           up,down,right,left = Block.Z_block(color,x,y)
        
        
        return up,down,right,left
           
           
    ######### 檢查剛生成的、旋轉完會不會超出邊界的方塊
    def check_boundary(temp_list) :
        
        ######### 確認剛生成時方塊會不會超出範圍
        ######### 俄羅斯方塊都是四個方塊組成的
        if temp_list[0][1] < 0 or temp_list[1][1] < 0 or temp_list[2][1] < 0 or temp_list[3][1] < 0 :
            return False
        
        if temp_list[0][1] > 360 or temp_list[1][1] > 360 or temp_list[2][1] > 360 or temp_list[3][1] > 360 :
            return False

        ######### 為了確認旋轉、生成後會不會撞到其他方塊
        if len(block_list) > 0 :
            for block in block_list :
               for temp in temp_list :
                    if (temp[1] + 40 == block[1] or temp[1] - 40 == block[1]) and temp[2] == block[2]:
                        return False 
                    
        return True

    
    
    
    
    
######### 旋轉方塊
class Rotate() :
    
    
    ######### 輸入外面的temp_list
    def __init__(self,temp_list):
       
        ######### 更新self.up......讓下面的可以知道現在temp_list的真正上下左右是啥
        self.up,self.down,self.right,self.left = Get_value.get_changing_value(temp_list)
        
        self.temp_list = temp_list
        self.oringinal_list = temp_list
        
    ######### 順時針旋轉
    def clockwise(self) :
        
        
        
        if self.temp_list == self.up :
            self.temp_list = self.right
        
        elif self.temp_list == self.down :
            self.temp_list = self.left
        
        elif self.temp_list == self.right :
            self.temp_list = self.down
        
        elif self.temp_list == self.left :
            self.temp_list = self.up

        
        ######### 如果超出邊界的話，就回歸原本的
        if not Get_value.check_boundary(self.temp_list) :
            self.temp_list = self.oringinal_list
           
           
        return self.temp_list
    


    ######### 逆順時針旋轉
    def counterclockwise(self) :
        
        if self.temp_list == self.up :
            self.temp_list = self.left
        
        elif self.temp_list == self.down :
            self.temp_list = self.right
        
        elif self.temp_list == self.right :
            self.temp_list = self.up
        
        elif self.temp_list == self.left :
            self.temp_list = self.down
        
        if not Get_value.check_boundary(self.temp_list) :
           self.temp_list = self.oringinal_list
        
        return self.temp_list





        
        
                
               
                
            

    
            
            
            

######### 畫出在底部的所有方塊
def draw_block():
    
    for block in block_list:
        pygame.draw.rect(background, block[0],pygame.Rect(block[1], block[2], 40, 40))  
        


######### 檢查是否在底部或碰到其他方塊
def check_stockpile() :
      
       
        for temp in temp_list :
                if temp[2] >= 760 :
                    return False
                
                
        if len(block_list) > 0 :
            for temp in temp_list :    
                for block in block_list :
                    if temp[1] == block[1] and temp[2] + 40 == block[2] :
                        return False
                
                
            ######### 不能用else，因為一個不成立的話就直接跳回去
            ######### 如果全檢查完，if都不成立的話，再往下跑就可以return True 
            return True


        else :
            return True



######### 讓左右邊有方塊時，此方塊不會穿模
def check_left_or_right(left_or_right) :

        ######### 這一行是必要的，因為第一輪時block_list啥都沒有
        if len(block_list) > 0 :
            
            ######### 如果右邊有方塊時，能任意往左，這樣可以縮減程式碼
            if left_or_right == 'left' :              
                num = - 40
                
            elif  left_or_right == 'right' :
                num = + 40
            
            
            ######### 已經觸底的也不能移動了，不然是作弊
            for block in block_list:
                for temp in temp_list :
                    if (temp[2] == block[2] and (temp[1] + num == block[1])) or not check_stockpile():
                        return False
                    
                    
            ######### 不能用else，因為一個不成立的話就直接跳回去
            ######### 如果全檢查完，if都不成立的話，再往下跑就可以return True
            return True
        
        else :
            return True
                
                
       


def remove_and_drop():
   
    global block_list,score
    
    pop_list = []
    
    ######### remove 
    for block_1 in block_list :
        for block_2 in block_list :
        
            if block_1[2] == block_2[2]:
                pop_list.append(block_2)
            
       
        if len(pop_list) == 10 :
            
            
            ######### 記錄消除多少個方塊，算是分數
            score += 10
            for pop in pop_list :
            
                block_list.remove(pop)
            
            ######### 全部墜落
            for block in block_list :
                if block[2] < pop_list[0][2] :
                    block[2] += 40
            
            pop_list.clear()
            
            
        else :
            pop_list.clear()
   
                


                    
                   
                    
                    
                    
                    
        
            
    
    
    
    

def move_left_or_right(left_or_right):
    global temp_list
     
    ######### 先檢查
    if check_left_or_right(left_or_right) :
        
        
        ######### 檢驗是往左還往右
        if left_or_right == 'left' :
            change_in_x = -40
    
        elif left_or_right == 'right':
            change_in_x = 40
            
            
        ######### 這裡有設置邊界 
        for temp in temp_list :
            if 0 <= temp[1] + change_in_x <= 360  :
                flag = True
            
            else :
                flag = False
                break
            
        if flag :
            for temp in temp_list : 
                temp[1] += change_in_x
        
    
                
  



def move_down() :
   
    global temp_list
    
    
    if check_stockpile()  :
        
        for temp in temp_list :
            temp[2] += 40
  
    else :
        
        block_list.extend(temp_list) 
        
        ######### 重新生成新方塊
        temp_list = Get_value.get_inital_value()
        
        
        
       
######### 分隔線
def draw_lines() :
    
    for x in range(0,400,40) :
        pygame.draw.line(background, (253,253,253), (x,0), (x,800), 1)
    
    for y in range(0,800,40) :
        pygame.draw.line(background, (253,253,253), (0,y), (400,y), 1)
            
   
    
    
    
    
######### 放在這裡的原因為：pygame.event.get()只要用過那個事件，那個事件就會被刪除，所以要透過def，每次使用才會重新更新所有資訊
def press_which_side() :
    

    ######### 再次讀取事件
    for event in pygame.event.get(): 

                ######### 如果點視窗的叉叉
                if event.type == pygame.QUIT: 
                                      
                    ######### 離開pygame
                    pygame.quit()  
                                       
                    ######### 關閉程式
                    sys.exit()  
                    
                    
                if event.type == pygame.KEYDOWN:
                    
                                        
                    if event.key == pygame.K_LEFT:
                       
                        return 'left'
                         
                            
                    elif event.key == pygame.K_RIGHT:
                        
                        return 'right'
                    
                    elif event.key == pygame.K_DOWN:
                        
                        return 'down'
                        
                    
                    ######### 旋轉
                    elif event.key == pygame.K_1 :
                        
                        return 'rotate clockwise'
                        

                    elif event.key == pygame.K_2 :
                        
                        return 'rotate counterclockwise'
                        


######### 如果堆到頂就輸了
######### 之後就困在這個畫面
def lose_the_game() :
    global time
    
    for block in block_list :
        if block[2] < 0 :
            
            ######### 之前是一秒60次
            time = time / 60
            
            
            ######### 創建字體對象 (字體名稱, 字體大小)
            while True :
                
                ######### 要可以按叉叉
                press_which_side() 
                
                bg_fill = (30,30,30)
                background.fill(bg_fill)
                
                font_1 = pygame.font.Font(None, 50)
                font_2 = pygame.font.Font(None, 30)
                font_3 = pygame.font.Font(None, 30)
                
                
                ######### 渲染文字 (文字內容, 是否平滑, 顏色)
                lose_surface = font_1.render('You lose', True, (255, 255, 255))  # 白色
                score_surface = font_2.render('Elimination = {} blocks'.format(score), True, (200, 50, 50)) 
                time_surface = font_3.render('Surive time = {} seconds'.format(time), True, (200, 50, 50)) 
                
                ######### 獲取文字表面的矩形區域
                text_rect = lose_surface.get_rect()
                score_rect = score_surface.get_rect()
                time_rect = time_surface.get_rect()
            
                ######### 設定文字位置
                text_rect.center = (200, 400)  # 螢幕中央
                score_rect.center = (200, 500)
                time_rect.center = (200,550)
                
                
                ######### 將文字表面渲染到背景上
                background.blit(lose_surface, text_rect)
                background.blit(score_surface, score_rect)
                background.blit(time_surface, time_rect)
                
                pygame.display.flip()
    
    



#########一開始要先設定temp_list
temp_list = Get_value.get_inital_value()

######### 這是用來更新FPS的
time = 0 # 順便配合幀數
fps_speed = 100

score = 0

while True:
    
    ######### 檢查有沒有輸
    lose_the_game()
    
    
    
    ######### FPS會增大（每一分鐘FPS增加20）
    time += 1 
    
    if temp_list[0][2] == 0 and time % 3600 == 0 :
        if fps_speed <= 500 :
            fps_speed  += 20
        
        
        
    ######### It should be called once per frame
    FPS.tick(fps_speed)
    
    
    
    ######### 決定上下左右
    ######### window_close()包含在裡頭
    side = press_which_side()
    
    
    ######## 根本不需要多個幾幀再顯示，人眼根本看不出區別
    if side is not None :
        flag = True
        
        if side == 'left' or side == 'right' :
            move_left_or_right(side)
        
        elif side == 'down' :
            
            side = move_down()
        
        elif side == 'rotate clockwise' :
            rotate = Rotate(temp_list)
            temp_list = rotate.clockwise()
            
        elif side == 'rotate counterclockwise' :
            rotate = Rotate(temp_list)
            temp_list = rotate.counterclockwise()

    else :
        flag = False
    

    
    
    ######### 這裡不加else:flag = False，因為在大部分情況下，上面的就顯示flag = False，所以下面有需要才會是flag = True
    if time % 60 == 0 :
        move_down()
        flag = True
    
        

    
   
    ######### 用flag來確認是否要更新畫面
    if flag :
        background_image = pygame.image.load('/Users/coolguy/Documents/cropped_background.jpeg')
        background.blit(background_image, (0, 0))  # 畫背景 黑色
        draw_lines() # 畫分隔的實線
        
        
        ######### 因為temp_list裡有數個值
        ######### 一個一個畫完後再更新畫面
        for temp in temp_list :
            head = pygame.Rect(temp[1], temp[2], 40, 40)
            pygame.draw.rect(background, temp[0], head)
            
        remove_and_drop()
        draw_block()
        pygame.display.flip()
    
    
            
    
  
   
     
            
               

           
   
   
   
  
