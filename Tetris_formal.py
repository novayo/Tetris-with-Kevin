"""This is the code relating to Tetris with the blocks displaying pictures or colors. """

# pylint: disable=no-member

import sys
import random
import pygame
import relative_path


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

######### 這是用來更新FPS的
time = 0  # 順便配合幀數 # pylint: disable = invalid-name # This is a mutable variable
fps_speed = 100  # pylint: disable = invalid-name # This is a mutable variable

score = 0  # pylint: disable = invalid-name # This is a mutable variable


class BlockBase:  # pylint: disable=too-few-public-methods # 因為這是用於繼承的，重點不是他的fnc
    """各個方塊的初始條件"""

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def color_or_picture(self, parameter, picture_root):
        """50%的機率選定會出現照片還是顏色，其中照片和顏色都是在其他方塊的class裡匯入的"""

        preference = random.choice(["color", "picture"])

        if preference == "color":
            color = parameter

        elif preference == "picture":
            color = pygame.image.load(picture_root)
            color = pygame.transform.scale(color, (40, 40))
            color.blit(color, (self.x, self.y))

        return color


class TBlock(BlockBase):
    """上下左右的紀錄是為了之後旋轉時，能辨別它的上下左右的各個方塊的所在位置的座標是什麼。"""

    def get_direction(self, color):
        """設定移動方塊的上下左右位置"""

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
        """隨機選擇要顏色還是圖片"""

        color = self.color_or_picture(
            (100, 90, 200), relative_path.block_picture_path[0]
        )

        return color


class LBlock(BlockBase):
    """上下左右的紀錄是為了之後旋轉時，能辨別它的上下左右的各個方塊的所在位置的座標是什麼。"""

    def get_direction(self, color):
        """設定移動方塊的上下左右位置"""

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
        """隨機選擇要顏色還是圖片"""

        color = self.color_or_picture(
            (70, 90, 120), relative_path.block_picture_path[1]
        )

        return color


class JBlock(BlockBase):
    """上下左右的紀錄是為了之後旋轉時，能辨別它的上下左右的各個方塊的所在位置的座標是什麼。"""

    def get_direction(self, color):
        """設定移動方塊的上下左右位置"""

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
        """隨機選擇要顏色還是圖片"""

        color = self.color_or_picture(
            (20, 90, 90), relative_path.block_picture_path[2]
        )

        return color


class IBlock(BlockBase):
    """上下左右的紀錄是為了之後旋轉時，能辨別它的上下左右的各個方塊的所在位置的座標是什麼。"""

    def get_direction(self, color):
        """設定移動方塊的上下左右位置"""

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
        """隨機選擇要顏色還是圖片"""

        color = self.color_or_picture(
            (70, 90, 120), relative_path.block_picture_path[3]
        )

        return color


class OBlock(BlockBase):
    """上下左右的紀錄是為了之後旋轉時，能辨別它的上下左右的各個方塊的所在位置的座標是什麼。"""

    def get_direction(self, color):
        """設定移動方塊的上下左右位置"""

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
        """隨機選擇要顏色還是圖片"""

        color = self.color_or_picture(
            (170, 90, 220), relative_path.block_picture_path[4]
        )

        return color


class SBlock(BlockBase):
    """上下左右的紀錄是為了之後旋轉時，能辨別它的上下左右的各個方塊的所在位置的座標是什麼。"""

    def get_direction(self, color):
        """設定移動方塊的上下左右位置"""

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
        """隨機選擇要顏色還是圖片"""

        color = self.color_or_picture(
            (70, 90, 120), relative_path.block_picture_path[5]
        )

        return color


class ZBlock(BlockBase):
    """上下左右的紀錄是為了之後旋轉時，能辨別它的上下左右的各個方塊的所在位置的座標是什麼。"""

    def get_direction(self, color):
        """設定移動方塊的上下左右位置"""

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
        """隨機選擇要顏色還是圖片"""

        color = self.color_or_picture(
            (20, 220, 120), relative_path.block_picture_path[6]
        )

        return color


def get_inital_value():
    """
    初始化資料
    先隨機分配要生成哪一種
    再把值傳進去病得出上下左右的真正值
    之後再選擇要哪一種
    """

    global block_figure  # pylint: disable = global-variable-undefined #因為這是指用於此檔案的，不會有外部檔案引用

    ######### 初始資料，這是方塊剛生成時會用到的
    x = random.randrange(0, 361, BLOCK_WIDTH)
    y = 0
    block_attributes = TBlock(x, y)  # pylint為了要避免出錯而必須要在if前設置預設值

    block_figure = random.choice(["T", "L", "I", "J", "O", "S", "Z"])

    match block_figure:
        case "T":
            block_attributes = TBlock(x, y)

        case "L":
            block_attributes = LBlock(x, y)

        case "I":
            block_attributes = IBlock(x, y)

        case "J":
            block_attributes = JBlock(x, y)

        case "O":
            block_attributes = OBlock(x, y)

        case "S":
            block_attributes = SBlock(x, y)

        case "Z":
            block_attributes = ZBlock(x, y)

    color = block_attributes.get_color()

    up, down, right, left = renew_data(color, x, y)
    side_attributes = random.choice([up, down, left, right])

    ######### 檢查x值是否有超出邊界，如果有的話這個函數就再重跑一次
    if not check_boundary(side_attributes):
        side_attributes = get_inital_value()

    return side_attributes


def get_changing_value(moving_list):
    """得到移動方塊的上下左右值

    已經生成的方塊，在要更換方向（變左遍右等）需要更新color,x,y,temp_list
    初始資料，這是方塊剛生成時會用到的這樣下面的self.up......才會依據現在的x,y值進行判定
    Rotate在判定時才知道self.up......是啥
    """
    color = moving_list[0][0]
    x = moving_list[0][1]
    y = moving_list[0][2]

    up, down, right, left = renew_data(color, x, y)

    return up, down, right, left


def renew_data(color, x, y):
    """用來更新上下左右的地方"""

    new_block = None

    match block_figure:
        case "T":
            new_block = TBlock(x, y)

        case "L":
            new_block = LBlock(x, y)

        case "I":
            new_block = IBlock(x, y)

        case "J":
            new_block = JBlock(x, y)

        case "O":
            new_block = OBlock(x, y)

        case "S":
            new_block = SBlock(x, y)

        case "Z":
            new_block = ZBlock(x, y)

    up, down, right, left = new_block.get_direction(color)

    return up, down, right, left


def check_boundary(moving_list):
    """
    檢查剛生成的、旋轉完會不會超出邊界的方塊
    確認剛生成時方塊會不會超出範圍
    俄羅斯方塊都是四個方塊組成的
    """
    if (
        moving_list[0][1] < 0
        or moving_list[1][1] < 0
        or moving_list[2][1] < 0
        or moving_list[3][1] < 0
    ):
        return False

    if (
        moving_list[0][1] > 360
        or moving_list[1][1] > 360
        or moving_list[2][1] > 360
        or moving_list[3][1] > 360
    ):
        return False

    ######### 為了確認旋轉、生成後會不會撞到其他方塊
    if len(block_list) > 0:
        for rotating_block in block_list:
            for objects in moving_list:
                if (
                    objects[1] + BLOCK_WIDTH == rotating_block[1]
                    or objects[1] - BLOCK_WIDTH == rotating_block[1]
                ) and objects[2] == rotating_block[2]:
                    return False

    return True


class Rotate:
    """旋轉方塊"""

    def __init__(self, local_temp_list):
        """輸入外面的temp_list"""

        ######### 更新self.up......讓下面的可以知道現在temp_list的真正上下左右是啥
        self.up, self.down, self.right, self.left = get_changing_value(local_temp_list)

        self.local_temp_list = local_temp_list
        self.oringinal_list = local_temp_list

    def clockwise(self):
        """順時針旋轉"""

        if self.local_temp_list == self.up:
            self.local_temp_list = self.right

        elif self.local_temp_list == self.down:
            self.local_temp_list = self.left

        elif self.local_temp_list == self.right:
            self.local_temp_list = self.down

        elif self.local_temp_list == self.left:
            self.local_temp_list = self.up

        ######### 如果超出邊界的話，就回歸原本的
        if not check_boundary(self.local_temp_list):
            self.local_temp_list = self.oringinal_list

        return self.local_temp_list

    def counterclockwise(self):
        """逆順時針旋轉"""

        if self.local_temp_list == self.up:
            self.local_temp_list = self.left

        elif self.local_temp_list == self.down:
            self.local_temp_list = self.right

        elif self.local_temp_list == self.right:
            self.local_temp_list = self.up

        elif self.local_temp_list == self.left:
            self.local_temp_list = self.down

        if not check_boundary(self.local_temp_list):
            self.local_temp_list = self.oringinal_list

        return self.local_temp_list


def draw_blocks(inner_block):
    """畫出在底部的所有方塊或正在移動的方塊"""

    if isinstance(inner_block[0], tuple):
        pygame.draw.rect(
            background,
            inner_block[0],
            pygame.Rect(inner_block[1], inner_block[2], BLOCK_WIDTH, BLOCK_WIDTH),
        )

    else:
        background.blit(inner_block[0], (inner_block[1], inner_block[2]))


def check_stockpile(local_temp_list):
    """檢查是否在底部或碰到其他方塊"""

    for objects in local_temp_list:
        if objects[2] >= SCREEN_LENGTH:
            return False

    if (  # pylint: disable = no-else-return # 這裡是必須要在後面加return True，因爲數量沒大於0的話就會有其他問題
        len(block_list) > 0
    ):
        for objects in local_temp_list:
            for moving_block in block_list:
                if (
                    objects[1] == moving_block[1]
                    and objects[2] + BLOCK_WIDTH == moving_block[2]
                ):
                    return False

        ######### 不能用else，因為一個不成立的話就直接跳回去
        ######### 如果全檢查完，if都不成立的話，再往下跑就可以return True
        return True

    else:
        return True  ######### 這裡 return True是為了讓剛開始block_list沒有值時方塊還能下墜（move_down fnc）


def check_left_or_right(left_or_right, local_temp_list):
    """讓左右邊有方塊時，此方塊不會穿模"""

    num = None

    ######### 這一行是必要的，因為第一輪時block_list啥都沒有
    if len(block_list) > 0:  # pylint: disable = no-else-return

        ######### 如果右邊有方塊時，能任意往左，這樣可以縮減程式碼
        if left_or_right == "left":
            num = -BLOCK_WIDTH

        elif left_or_right == "right":
            num = +BLOCK_WIDTH

        ######### 已經觸底的也不能移動了，不然是作弊
        for block_barrier in block_list:
            for objects in local_temp_list:
                if (
                    objects[2] == block_barrier[2]
                    and (objects[1] + num == block_barrier[1])
                ) or not check_stockpile(local_temp_list):
                    return False

    return True


def remove_and_drop():
    """用來消除方塊，和消除整排後，方塊掉落的程式"""

    global block_list, score  # pylint: disable = global-statement # 本檔案不會被其他檔案引用

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

            cobied_list = block_list
            ######### 全部墜落
            for rest_of_blocks in cobied_list:
                if rest_of_blocks[2] < pop_list[0][2]:
                    rest_of_blocks[2] += BLOCK_WIDTH

            block_list = cobied_list

        pop_list.clear()


def move_left_or_right(left_or_right, local_temp_list):
    """讓方塊往左或往右移動"""

    ######### 先檢查
    if check_left_or_right(left_or_right, local_temp_list):

        change_in_x = None

        ######### 檢驗是往左還往右
        if left_or_right == "left":
            change_in_x = -BLOCK_WIDTH

        elif left_or_right == "right":
            change_in_x = +BLOCK_WIDTH

        ######### 這裡有設置邊界
        for objects in local_temp_list:
            if 0 <= objects[1] + change_in_x <= SCREEN_WIDTH:
                inner_flag = True

            else:
                inner_flag = False
                break

        if inner_flag:
            for objects in local_temp_list:
                objects[1] += change_in_x

    return local_temp_list


def move_down(local_temp_list):
    """讓方塊往下掉"""

    if check_stockpile(local_temp_list):

        for objects in local_temp_list:
            objects[2] += BLOCK_WIDTH

    else:

        block_list.extend(local_temp_list)

        ######### 重新生成新方塊
        local_temp_list = get_inital_value()

    return local_temp_list


def draw_lines():
    """分隔線"""

    for x in range(0, 400, BLOCK_WIDTH):
        pygame.draw.line(background, (253, 253, 253), (x, 0), (x, 800), 1)

    for y in range(0, 800, BLOCK_WIDTH):
        pygame.draw.line(background, (253, 253, 253), (0, y), (400, y), 1)


def press_which_side():  # pylint: disable = inconsistent-return-statements
    """放在這裡的原因為：pygame.event.get()只要用過那個事件，那個事件就會被刪除，所以要透過def，每次使用才會重新更新所有資訊"""

    ######### 再次讀取事件
    for event in pygame.event.get():

        ######### 如果點視窗的叉叉
        if event.type == pygame.QUIT:  # -member

            ######### 離開pygame
            pygame.quit()  # -member

            ######### 關閉程式
            sys.exit()

        if event.type == pygame.KEYDOWN:  # -member

            if event.key == pygame.K_LEFT:  # -member

                return "left"

            if event.key == pygame.K_RIGHT:  # -member

                return "right"

            if event.key == pygame.K_DOWN:  # -member

                return "down"

            ######### 旋轉
            if event.key == pygame.K_1:  # -member

                return "rotate clockwise"

            if event.key == pygame.K_2:  # -member

                return "rotate counterclockwise"


def get_losing_scene(losing_time):
    """
    如果堆到頂就輸了
    之後就困在這個畫面
    """

    survive_time = losing_time / 60
    ######### 創建字體對象 (字體名稱, 字體大小)
    bg_fill = (30, 30, 30)
    background.fill(bg_fill)

    font_1 = pygame.font.Font(None, 50)
    font_2 = pygame.font.Font(None, 30)
    font_3 = pygame.font.Font(None, 30)

    ######### 渲染文字 (文字內容, 是否平滑, 顏色)
    WHITE_COLOR = (  # pylint: disable = invalid-name # This is a not mutable
        255,
        255,
        255,
    )
    lose_surface = font_1.render("You lose", True, WHITE_COLOR)  # 白色
    score_surface = font_2.render(f"Elimination = {score} blocks", True, (200, 50, 50))
    time_surface = font_3.render(
        f"Survive time = {survive_time} seconds", True, (200, 50, 50)
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
    """用來檢查玩家是否輸了"""

    if len(block_list) > 0:
        for block_y_location in block_list:
            if block_y_location[2] < 0:
                return False

    return True


if __name__ == "__main__":
    #########一開始要先設定temp_list
    temp_list = get_inital_value()

    while True:

        SIDE = press_which_side()  # 決定上下左右，window_close()包含在裡頭

        ######### 檢查有沒有輸

        if not check_if_player_lose():
            get_losing_scene(time)

        ######### 沒輸的話的正常功能
        else:

            ######### FPS會增大（每一分鐘FPS增加20）
            time += 1

            if temp_list[0][2] == 0 and time % 3600 == 0:
                if fps_speed <= 500:
                    fps_speed += 20

            ######### It should be called once per frame
            FPS.tick(fps_speed)

            ######## 根本不需要多個幾幀再顯示，人眼根本看不出區別
            if SIDE is not None:
                flag = True  # pylint: disable = invalid-name # 這是變數

                if SIDE in ("left", "right"):
                    temp_list = move_left_or_right(SIDE, temp_list)

                elif SIDE == "down":

                    temp_list = move_down(
                        temp_list
                    )  # pylint: disable = assignment-from-no-return # 那個fnc有return

                elif SIDE == "rotate clockwise":
                    rotate = Rotate(temp_list)
                    temp_list = rotate.clockwise()

                elif SIDE == "rotate counterclockwise":
                    rotate = Rotate(temp_list)
                    temp_list = rotate.counterclockwise()

            else:
                flag = False  # pylint: disable = invalid-name

            ######### 這裡不加else:flag = False，因為在大部分情況下，上面的就顯示fkag = False，所以下面有需要才會是flag = True

            if time % 60 == 0:
                temp_list = move_down(temp_list)
                flag = True  # pylint: disable = invalid-name

            ######### 用flag來確認是否要更新畫面
            if flag:
                background_image = pygame.image.load(
                    relative_path.background_picture_path
                )
                background.blit(background_image, (0, 0))  # 畫背景 黑色
                draw_lines()  # 畫分隔的實線

                for (
                    temp
                ) in temp_list:  # 因為temp_list裡有數個值，一個一個畫完後再更新畫面
                    draw_blocks(temp)

                remove_and_drop()

                for block in block_list:
                    draw_blocks(block)

                ######### 輸了也需要顯示畫面
        pygame.display.flip()
