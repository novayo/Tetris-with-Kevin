""" 
This is the code relating to Tetris with the blocks displaying pictures or colors. 
"""

import sys
import random
import pygame


######### 初始化pygame
pygame.init()  # pylint: disable=E1101

######### 建立背景
background = pygame.display.set_mode((400, 800))
FPS = pygame.time.Clock()

######### 設定畫面上方的文字
pygame.display.set_caption("Tetris")


######### 更改變數名，避免與Python內建的list類型重名
block_list = []


######### 基本資料
SCREEN_LENGTH = (
    760  # 因為方塊的y值在左上角，所以方塊到最底層時時是800 - 40（方塊長度 = 40）
)
SCREEN_WIDTH = 360  # 因為方塊的x值在左上角，所以方塊到最右方是400 - 40（方塊長度 = 40）

BLOCK_WIDTH = 40


class InitializeData:
    """
    各個方塊的初始條件
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def color_or_picture(self, parameter, picture_root):
        """
        50%的機率選定會出現照片還是顏色，其中照片和顏色都是在其他方塊的class裡匯入的
        """

        preference = random.choice(["color", "picture"])

        if preference == "color":
            color = parameter

        elif preference == "picture":
            color = pygame.image.load(picture_root)
            color = pygame.transform.scale(color, (40, 40))
            color.blit(color, (self.x, self.y))

        return color


class TBlock(InitializeData):
    """
    上下左右的紀錄是為了之後旋轉時，能辨別它的上下左右的各個方塊的所在位置的座標是什麼。
    """

    def get_direction(self, color):
        """
        同上
        """
        up = [
            [color, self.x, self.y],
            [color, self.x + 40, self.y],
            [color, self.x - 40, self.y],
            [color, self.x, self.y - 40],
        ]
        down = [
            [color, self.x, self.y],
            [color, self.x + 40, self.y],
            [color, self.x - 40, self.y],
            [color, self.x, self.y + 40],
        ]
        right = [
            [color, self.x, self.y],
            [color, self.x, self.y - 40],
            [color, self.x, self.y + 40],
            [color, self.x + 40, self.y],
        ]
        left = [
            [color, self.x, self.y],
            [color, self.x, self.y - 40],
            [color, self.x, self.y + 40],
            [color, self.x - 40, self.y],
        ]

        return up, down, right, left

    def get_color(self):
        """
        同上
        """
        color = self.color_or_picture(
            (100, 90, 200), "/Users/coolguy/Documents/picture_for_T.jpg"
        )

        return color


class LBlock(InitializeData):
    """
    同上
    """

    def get_direction(self, color):
        """
        同上
        """
        up = [
            [color, self.x, self.y],
            [color, self.x + 40, self.y],
            [color, self.x - 40, self.y],
            [color, self.x + 40, self.y - 40],
        ]
        down = [
            [color, self.x, self.y],
            [color, self.x + 40, self.y],
            [color, self.x - 40, self.y],
            [color, self.x - 40, self.y + 40],
        ]
        right = [
            [color, self.x, self.y],
            [color, self.x, self.y - 40],
            [color, self.x, self.y + 40],
            [color, self.x + 40, self.y + 40],
        ]
        left = [
            [color, self.x, self.y],
            [color, self.x, self.y - 40],
            [color, self.x, self.y + 40],
            [color, self.x - 40, self.y - 40],
        ]
        return up, down, left, right

    def get_color(self):
        """
        同上
        """
        color = self.color_or_picture(
            (70, 90, 120), "/Users/coolguy/Documents/picture_for_L.jpg"
        )

        return color


class JBlock(InitializeData):
    """
    同上
    """

    def get_direction(self, color):
        """
        同上
        """

        up = [
            [color, self.x, self.y],
            [color, self.x + 40, self.y],
            [color, self.x - 40, self.y],
            [color, self.x - 40, self.y - 40],
        ]
        down = [
            [color, self.x, self.y],
            [color, self.x + 40, self.y],
            [color, self.x - 40, self.y],
            [color, self.x + 40, self.y + 40],
        ]
        right = [
            [color, self.x, self.y],
            [color, self.x, self.y - 40],
            [color, self.x, self.y + 40],
            [color, self.x + 40, self.y - 40],
        ]
        left = [
            [color, self.x, self.y],
            [color, self.x, self.y - 40],
            [color, self.x, self.y + 40],
            [color, self.x - 40, self.y + 40],
        ]

        return up, down, right, left

    def get_color(self):
        """
        同上
        """
        color = self.color_or_picture(
            (20, 90, 90), "/Users/coolguy/Documents/租房照片二.jpg"
        )

        return color


class IBlock(InitializeData):
    """
    同上
    """

    def get_direction(self, color):
        """
        同上
        """

        up = [
            [color, self.x, self.y],
            [color, self.x, self.y - 40],
            [color, self.x, self.y + 40],
            [color, self.x, self.y + 80],
        ]
        down = up
        right = [
            [color, self.x, self.y],
            [color, self.x - 40, self.y],
            [color, self.x + 40, self.y],
            [color, self.x + 80, self.y],
        ]
        left = right

        return up, down, right, left

    def get_color(self):
        """
        同上
        """
        color = self.color_or_picture(
            (70, 90, 120), "/Users/coolguy/Documents/租房照片一.jpg"
        )

        return color


class OBlock(InitializeData):
    """
    同上
    """

    def get_direction(self, color):
        """
        同上
        """
        up = [
            [color, self.x, self.y],
            [color, self.x + 40, self.y],
            [color, self.x, self.y + 40],
            [color, self.x + 40, self.y + 40],
        ]
        down = up
        right = up
        left = up

        return up, down, right, left

    def get_color(self):
        """
        同上
        """
        color = self.color_or_picture(
            (170, 90, 220), "/Users/coolguy/Documents/租房照片四.jpg"
        )

        return color


class SBlock(InitializeData):
    """
    同上
    """

    def get_direction(self, color):
        """
        同上
        """
        up = [
            [color, self.x, self.y],
            [color, self.x - 40, self.y],
            [color, self.x, self.y - 40],
            [color, self.x + 40, self.y - 40],
        ]
        down = up
        right = [
            [color, self.x, self.y],
            [color, self.x + 40, self.y],
            [color, self.x, self.y - 40],
            [color, self.x + 40, self.y + 40],
        ]
        left = right

        return up, down, right, left

    def get_color(self):
        """
        同上
        """
        color = self.color_or_picture(
            (70, 90, 120), "/Users/coolguy/Documents/租房照片五.jpg"
        )

        return color


class ZBlock(InitializeData):
    """
    同上
    """

    def get_direction(self, color):
        """
        同上
        """
        up = [
            [color, self.x, self.y],
            [color, self.x + 40, self.y],
            [color, self.x, self.y - 40],
            [color, self.x - 40, self.y - 40],
        ]
        down = up
        right = [
            [color, self.x, self.y],
            [color, self.x - 40, self.y],
            [color, self.x, self.y - 40],
            [color, self.x - 40, self.y + 40],
        ]
        left = right

        return up, down, right, left

    def get_color(self):
        """
        同上
        """
        color = self.color_or_picture(
            (20, 220, 120), "/Users/coolguy/Documents/租房照片二.jpg"
        )

        return color

    def get_color(self):
        num = random.randint(1, 2)

        if num == 1:
            color = (20, 220, 120)

        elif num == 2:

            color = pygame.image.load("/Users/coolguy/Documents/租房照片二.jpg")
            color = pygame.transform.scale(color, (40, 40))
            color.blit(color, (self.x, self.y))

        return color


def get_inital_value():
    """
    初始化資料
    """
    global block_figure

    ######### 初始資料，這是方塊剛生成時會用到的
    x = random.randrange(0, 361, BLOCK_WIDTH)
    y = 0

    block_figure = random.choice(["T", "L", "I", "J", "O", "S", "Z"])

    if block_figure == "T":
        block = TBlock(x, y)

    if block_figure == "L":
        block = LBlock(x, y)

    if block_figure == "I":
        block = IBlock(x, y)

    if block_figure == "J":
        block = JBlock(x, y)

    if block_figure == "O":
        block = OBlock(x, y)

    if block_figure == "S":
        block = SBlock(x, y)

    if block_figure == "Z":
        block = ZBlock(x, y)

    color = block.get_color()

    block_figure = random.choice(["T", "L", "I", "J", "O", "S", "Z"])

    if block_figure == "T":
        block = TBlock(x, y)

    if block_figure == "L":
        block = LBlock(x, y)

    if block_figure == "I":
        block = IBlock(x, y)

    if block_figure == "J":
        block = JBlock(x, y)

    if block_figure == "O":
        block = OBlock(x, y)

    if block_figure == "S":
        block = SBlock(x, y)

    if block_figure == "Z":
        block = ZBlock(x, y)

    color = block.get_color()

    """
    先隨機分配要生成哪一種
    再把值傳進去病得出上下左右的真正值
    之後再選擇要哪一種
    """
    up, down, right, left = renew_data(color, x, y)
    temp_list = random.choice([up, down, left, right])

    ######### 檢查x值是否有超出邊界，如果有的話這個函數就再重跑一次
    if not check_boundary(temp_list):
        temp_list = get_inital_value()

    return temp_list


def get_changing_value(temp_list):
    """
    已經生成的方塊，在要更換方向（變左遍右等）需要更新color,x,y,temp_list
    初始資料，這是方塊剛生成時會用到的這樣下面的self.up......才會依據現在的x,y值進行判定
    Rotate在判定時才知道self.up......是啥
    """
    color = temp_list[0][0]
    x = temp_list[0][1]
    y = temp_list[0][2]

    up, down, right, left = renew_data(color, x, y)

    return up, down, right, left


def renew_data(color, x, y):
    """
    用來更新上下左右的地方
    """

    if block_figure == "T":
        block = TBlock(x, y)

    if block_figure == "L":
        block = LBlock(x, y)

    if block_figure == "I":
        block = IBlock(x, y)

    if block_figure == "J":
        block = JBlock(x, y)

    if block_figure == "O":
        block = OBlock(x, y)

    if block_figure == "S":
        block = SBlock(x, y)

    if block_figure == "Z":
        block = ZBlock(x, y)

    up, down, right, left = block.get_direction(color)

    up, down, right, left = block.get_direction(color)

    return up, down, right, left


def check_boundary(temp_list):
    """
    檢查剛生成的、旋轉完會不會超出邊界的方塊
    """

    """
    確認剛生成時方塊會不會超出範圍
    俄羅斯方塊都是四個方塊組成的
    """
    if (
        temp_list[0][1] < 0
        or temp_list[1][1] < 0
        or temp_list[2][1] < 0
        or temp_list[3][1] < 0
    ):
        return False

    if (
        temp_list[0][1] > 360
        or temp_list[1][1] > 360
        or temp_list[2][1] > 360
        or temp_list[3][1] > 360
    ):
        return False

    ######### 為了確認旋轉、生成後會不會撞到其他方塊
    if len(block_list) > 0:
        for block in block_list:
            for temp in temp_list:
                if (
                    temp[1] + BLOCK_WIDTH == block[1]
                    or temp[1] - BLOCK_WIDTH == block[1]
                ) and temp[2] == block[2]:
                    return False

    return True


class Rotate:
    """
    旋轉方塊
    """

    def __init__(self, temp_list):
        """
        輸入外面的temp_list
        """

        ######### 更新self.up......讓下面的可以知道現在temp_list的真正上下左右是啥
        self.up, self.down, self.right, self.left = get_changing_value(temp_list)

        self.temp_list = temp_list
        self.oringinal_list = temp_list

    def clockwise(self):
        """
        順時針旋轉
        """

        if self.temp_list == self.up:
            self.temp_list = self.right

        elif self.temp_list == self.down:
            self.temp_list = self.left

        elif self.temp_list == self.right:
            self.temp_list = self.down

        elif self.temp_list == self.left:
            self.temp_list = self.up

        ######### 如果超出邊界的話，就回歸原本的
        if not check_boundary(self.temp_list):
            self.temp_list = self.oringinal_list

        return self.temp_list

    def counterclockwise(self):
        """
        逆順時針旋轉
        """

        if self.temp_list == self.up:
            self.temp_list = self.left

        elif self.temp_list == self.down:
            self.temp_list = self.right

        elif self.temp_list == self.right:
            self.temp_list = self.up

        elif self.temp_list == self.left:
            self.temp_list = self.down

        if not check_boundary(self.temp_list):
            self.temp_list = self.oringinal_list

        return self.temp_list


def draw_blocks(block):
    """
    畫出在底部的所有方塊或正在移動的方塊
    """

    if isinstance(block[0], tuple):
        pygame.draw.rect(
            background,
            block[0],
            pygame.Rect(block[1], block[2], BLOCK_WIDTH, BLOCK_WIDTH),
        )

    else:
        background.blit(block[0], (block[1], block[2]))


def check_stockpile():
    """
    檢查是否在底部或碰到其他方塊
    """

    for temp in temp_list:
        if temp[2] >= SCREEN_LENGTH:
            return False

    if len(block_list) > 0:
        for temp in temp_list:
            for block in block_list:
                if temp[1] == block[1] and temp[2] + BLOCK_WIDTH == block[2]:
                    return False

        ######### 不能用else，因為一個不成立的話就直接跳回去
        ######### 如果全檢查完，if都不成立的話，再往下跑就可以return True
        return True

    else:
        return True


def check_left_or_right(left_or_right):
    """
    讓左右邊有方塊時，此方塊不會穿模
    """

    ######### 這一行是必要的，因為第一輪時block_list啥都沒有
    if len(block_list) > 0:

        ######### 如果右邊有方塊時，能任意往左，這樣可以縮減程式碼
        if left_or_right == "left":
            num = -BLOCK_WIDTH

        elif left_or_right == "right":
            num = +BLOCK_WIDTH

        ######### 已經觸底的也不能移動了，不然是作弊
        for block in block_list:
            for temp in temp_list:
                if (
                    temp[2] == block[2] and (temp[1] + num == block[1])
                ) or not check_stockpile():
                    return False

        """
            不能用else，因為一個不成立的話就直接跳回去
            如果全檢查完，if都不成立的話，再往下跑就可以return True
            """
        return True

    else:
        return True


def remove_and_drop():
    """
    用來消除方塊，和消除整排後，方塊掉落的程式
    """

    global block_list, score

    pop_list = []

    ######### remove
    for block_1 in block_list:
        for block_2 in block_list:

            if block_1[2] == block_2[2]:
                pop_list.append(block_2)

        if len(pop_list) == 10:

            ######### 記錄消除多少個方塊，算是分數
            score += 10
            for pop in pop_list:

                block_list.remove(pop)

            ######### 全部墜落
            for block in block_list:
                if block[2] < pop_list[0][2]:
                    block[2] += BLOCK_WIDTH

            pop_list.clear()

        else:
            pop_list.clear()


def move_left_or_right(left_or_right):
    """
    讓方塊往左或往右移動
    """
    global temp_list

    ######### 先檢查
    if check_left_or_right(left_or_right):

        ######### 檢驗是往左還往右
        if left_or_right == "left":
            change_in_x = -BLOCK_WIDTH

        elif left_or_right == "right":
            change_in_x = +BLOCK_WIDTH

        ######### 這裡有設置邊界
        for temp in temp_list:
            if 0 <= temp[1] + change_in_x <= SCREEN_LENGTH:
                FLAG = True

            else:
                FLAG = False
                break

        if FLAG:
            for temp in temp_list:
                temp[1] += change_in_x


def move_down():
    """
    讓方塊往下掉
    """
    global temp_list

    if check_stockpile():

        for temp in temp_list:
            temp[2] += BLOCK_WIDTH

    else:

        block_list.extend(temp_list)

        ######### 重新生成新方塊
        temp_list = get_inital_value()


def draw_lines():
    """
    分隔線
    """

    for x in range(0, 400, BLOCK_WIDTH):
        pygame.draw.line(background, (253, 253, 253), (x, 0), (x, 800), 1)

    for y in range(0, 800, BLOCK_WIDTH):
        pygame.draw.line(background, (253, 253, 253), (0, y), (400, y), 1)


def press_which_side():
    """
    放在這裡的原因為：pygame.event.get()只要用過那個事件，那個事件就會被刪除，所以要透過def，每次使用才會重新更新所有資訊
    """

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

                return "left"

            elif event.key == pygame.K_RIGHT:

                return "right"

            elif event.key == pygame.K_DOWN:

                return "down"

            ######### 旋轉
            elif event.key == pygame.K_1:

                return "rotate clockwise"

            elif event.key == pygame.K_2:

                return "rotate counterclockwise"


def get_losing_scene():
    """
    如果堆到頂就輸了
    之後就困在這個畫面
    """
    global TIME

    ######### 創建字體對象 (字體名稱, 字體大小)
    bg_fill = (30, 30, 30)
    background.fill(bg_fill)

    font_1 = pygame.font.Font(None, 50)
    font_2 = pygame.font.Font(None, 30)
    font_3 = pygame.font.Font(None, 30)

    ######### 渲染文字 (文字內容, 是否平滑, 顏色)
    lose_surface = font_1.render("You lose", True, (255, 255, 255))  # 白色
    score_surface = font_2.render(
        "Elimination = {} blocks".format(score), True, (200, 50, 50)
    )
    time_surface = font_3.render(
        "Survive time = {} seconds".format(TIME / 60), True, (200, 50, 50)
    )

    ######### 獲取文字表面的矩形區域
    text_rect = lose_surface.get_rect()
    score_rect = score_surface.get_rect()
    time_rect = time_surface.get_rect()

    ######### 設定文字位置
    text_rect.center = (200, 400)  # 螢幕中央
    score_rect.center = (200, 500)
    time_rect.center = (200, 550)

    ######### 將文字表面渲染到背景上
    background.blit(lose_surface, text_rect)
    background.blit(score_surface, score_rect)
    background.blit(time_surface, time_rect)


def check_if_player_lose():
    """
    用來檢查玩家是否輸了
    """
    if len(block_list) > 0:
        for block in block_list:
            if block[2] < 0:
                return False

    return True


#########一開始要先設定temp_list
temp_list = get_inital_value()

######### 這是用來更新FPS的
TIME = 0  # 順便配合幀數
fps_speed = 100

score = 0

while True:

    """
    決定上下左右
    window_close()包含在裡頭
    """
    SIDE = press_which_side()

    ######### 檢查有沒有輸

    if not check_if_player_lose():
        get_losing_scene()

    ######### 沒輸的話的正常功能
    else:

        ######### FPS會增大（每一分鐘FPS增加20）
        TIME += 1

        if temp_list[0][2] == 0 and TIME % 3600 == 0:
            if fps_speed <= 500:
                fps_speed += 20

        ######### It should be called once per frame
        FPS.tick(fps_speed)

        ######## 根本不需要多個幾幀再顯示，人眼根本看不出區別
        if SIDE is not None:
            FLAG = True

            if SIDE == "left" or SIDE == "right":
                move_left_or_right(SIDE)

            elif SIDE == "down":

                SIDE = move_down()

            elif SIDE == "rotate clockwise":
                rotate = Rotate(temp_list)
                temp_list = rotate.clockwise()

            elif SIDE == "rotate counterclockwise":
                rotate = Rotate(temp_list)
                temp_list = rotate.counterclockwise()

        else:
            FLAG = False

        ######### 這裡不加else:FLAG = False，因為在大部分情況下，上面的就顯示FLAG = False，所以下面有需要才會是FLAG = True

        if TIME % 60 == 0:
            move_down()
            FLAG = True

        ######### 用FLAG來確認是否要更新畫面
        if FLAG:
            background_image = pygame.image.load(
                "/Users/coolguy/Documents/background.jpeg"
            )
            background.blit(background_image, (0, 0))  # 畫背景 黑色
            draw_lines()  # 畫分隔的實線

            """
            因為temp_list裡有數個值
            一個一個畫完後再更新畫面
            """
            for temp in temp_list:
                draw_blocks(temp)

            remove_and_drop()

            for block in block_list:
                draw_blocks(block)

            ######### 輸了也需要顯示畫面
    pygame.display.flip()
