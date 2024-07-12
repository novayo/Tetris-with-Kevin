import pygame
import sys
import random

######### 初始化pygame
pygame.init()  

######### 建立背景
background = pygame.display.set_mode((400, 800)) 
FPS = pygame.time.Clock()

######### 更改變數名，避免與Python內建的list類型重名
block_list = []   






######### 顏色
def dispense_color():
    return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)


######### 畫出在底部的所有方塊
def draw_block():
    
    for block in block_list:
        pygame.draw.rect(background, block[0], pygame.Rect(block[1], block[2], 40, 40))  # 顏色只能用tuple
        


   
def check_stockpile() :
      
        
        if len(block_list) > 0 :
            
            for block in block_list :
                
                if temp_list[1] == block[1] and temp_list[2] + 40 == block[2] :
                    return False
                
                
            ######### 不能用else，因為一個不成立的話就直接跳回去
            ######### 如果全檢查完，if都不成立的話，再往下跑就可以return True 
            return True


        else :
            return True



def check_left_or_right(left_or_right) :

        ######### 這一行是必要的，因為第一輪時block_list啥都沒有
        if len(block_list) > 0 :
            
            ######### 如果右邊有方塊時，能任意往左，這樣可以縮減程式碼
            if left_or_right == 'left' :              
                num = - 40
                
            elif  left_or_right == 'right' :
                num = + 40
            
            
            for block in block_list:
                if temp_list[2]  == block[2] and (temp_list[1] + num == block[1]) :
                    
                    return False
            ######### 不能用else，因為一個不成立的話就直接跳回去
            ######### 如果全檢查完，if都不成立的話，再往下跑就可以return True
            return True
        
        else :
            return True
                
                
        



    

def remove_and_drop():
    global block_list
    pop_list = []
    drop_list = []
   
    ######### 消除 #########
    
    
    ######### 如果y值一樣 ->加入pop_list
    ######### 如果pop_list有10個，才會消除block_list，否則pop_list重置
    for block_1 in block_list :
        for block_2 in block_list :
           
            if block_1[2] == block_2[2]:
               pop_list.append(block_2)
            
        
        if len(pop_list) == 10 :
            
            for pop in pop_list :
            
                block_list.remove(pop)
        
            pop_list.clear()
            
    
            ######### 下面沒方塊會往下墜 #########


            ######### 建立在有消除時才會往下墜
            ######### 先依據y值由大排到小，再檢查那個值是否在block_list裡，沒有的話就往下墜
            
            for block_3 in block_list :
                for block_4 in block_list :
                    if block_3[1] == block_4[1] :
                        
                        drop_list.append(block_4[2])
                
                while (block_3[2] + 40 not in drop_list) and block_3[2] < 760 :
                    block_3[2] += 40
                
                drop_list.clear()
                
            
        ######### 如果len(pop_list) < 10，表示奈那一行沒滿，所以要清除資料再檢查下一個位置的     
        else :
            pop_list.clear()
                
                    
                







def move_left_or_right(left_or_right):
     
    ######### 先檢查
    if check_left_or_right(left_or_right) :
        
        
        ######### 檢驗是往左還往右
        if left_or_right == 'left' :
            change_in_x = -40
    
        elif left_or_right == 'right':
            change_in_x = 40
            
            
        ######### 這裡有設置邊界  
        if 0 <= temp_list[1] + change_in_x <= 360  :
          temp_list[1] += change_in_x
       
   
                
  
  

def move_down() :
   
    if check_stockpile() and temp_list[2] < 760  :
        
        temp_list[2] += 40
  
    else :
        
        block_list.append(temp_list) 
        
        ######### 原先方塊駐足後要更新方塊：讓新方塊從頂部降落
        renew_data()
        
            
   
    
    
    
    
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
                        
                        
                    elif event.key == pygame.K_DOWN :
                        
                        return 'down'
    



        
           

def renew_data() :
    global temp_list,delay,flag
    
    flag = True
    
    ######### delay要記得歸零，不然後面delay太多會處理太多資料
    delay = 0
    x = random.randrange(0, 361, 40)
    y = 0
    color_tuple = dispense_color()
    temp_list = [color_tuple,x,y]



######### 只能先放在這裡，因為要放在函式下面
renew_data()

while True:
    
    ######### It should be called once per frame
    FPS.tick(600)
    
    
    ######### 配合幀數
    delay += 1         
   
   
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
    
    else :
        flag = False
    

    
    
    ######### 這裡不加else:flag = False，因為在大部分情況下，上面的就顯示flag = False，所以下面有需要才會是flag = True
    if delay % 60 == 0 :
        move_down()
        flag = True
    
        

    
   
    ######### 用flag來確認是否要更新畫面
    if flag :
        bg_color = (30, 30, 30)
        background.fill(bg_color)  # 畫背景 黑色
        head = pygame.Rect(temp_list[1], temp_list[2], 40, 40)
        pygame.draw.rect(background, temp_list[0], head)
        remove_and_drop()
        draw_block()
        pygame.display.flip()
    
    
            
    
  
   
     
            
               

           
   
   
   
  