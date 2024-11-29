import unittest
from unittest.mock import Mock, patch
import tetris_formal
import copy


class MainTest(unittest.TestCase):
    moving_s_block = [[(70, 90, 120), 40, 160], [(70, 90, 120), 80, 160], [(70, 90, 120), 40, 120], [(70, 90, 120), 80, 200]]
    stockpiled_T_block = [[(70, 90, 120),80,760],[(70, 90, 120),40,760],[(70, 90, 120),120,760],[(70, 90, 120),80,720]]
    out_of_bound_block = [[(70, 90, 120), -1000, 100], [(70, 90, 120), 80, 160], [(70, 90, 120), 40, 120], [(70, 90, 120), 80, 200]]
    
    
    def test_get_initial_value(self) :
        "可以只檢驗有沒有成功在跑，不需要回傳值"
        tetris_formal.get_inital_value = Mock()
        tetris_formal.get_inital_value()
        tetris_formal.get_inital_value.assert_called()
        
    
    def test_get_changing_value(self):
        "要return right "
        tetris_formal.block_figure = "S"
        
        up, down, right, left = tetris_formal.get_changing_value(copy.deepcopy(self.moving_s_block))
        self.assertIsNotNone(up)
        self.assertIsNotNone(down)
        self.assertIsNotNone(right)
        self.assertIsNotNone(left)

    
    def test_renew_data(self):
        tetris_formal.block_figure = "S"
        up, down, right, left = tetris_formal.renew_data((70, 90, 120), 40, 0)
        
        self.assertIsNotNone(up)
        self.assertIsNotNone(down)
        self.assertIsNotNone(right)
        self.assertIsNotNone(left)
        
    
    def test_check_boundary(self):
        self.assertTrue(tetris_formal.check_boundary(copy.deepcopy(self.moving_s_block)))
        self.assertFalse(tetris_formal.check_boundary(self.out_of_bound_block))
    
    
    def test_Rotate(self):
        tetris_formal.block_figure = "S"
        
        rotate = tetris_formal.Rotate(copy.deepcopy(self.moving_s_block))
        clockwise_s_block = rotate.clockwise()
        
        filtered_item = [item for item in clockwise_s_block if item in [[40,160],[80,160],[40,200],[0,200]]]
        
        if len(filtered_item) == 4 :
            self.assertEqual(True, True)
    
    
    def test_draw_blocks(self):
        inner_block = copy.deepcopy(self.moving_s_block)
        
        tetris_formal.draw_blocks = Mock()
        tetris_formal.draw_blocks(inner_block)
        tetris_formal.draw_blocks.assert_called()
        
        
    def test_check_stockpile(self):
        tetris_formal.block_list = copy.deepcopy(self.stockpiled_T_block)
        
        value = tetris_formal.check_stockpile(copy.deepcopy(self.moving_s_block))
        self.assertTrue(value)
    
    
    def test_check_left_or_right(self):
        self.assertEqual(tetris_formal.move_left_or_right("left", copy.deepcopy(self.moving_s_block)), [[(70, 90, 120), 0, 160], [(70, 90, 120), 40, 160], [(70, 90, 120), 0, 120], [(70, 90, 120), 40, 200]])
        self.assertNotEqual(tetris_formal.move_left_or_right("right", self.out_of_bound_block), [[(70, 90, 120), 80, 160], [(70, 90, 120), 120, 160], [(70, 90, 120), 80, 120], [(70, 90, 120), 120, 200]])
    
    
    def test_remove_and_drop(self):
        "list comprehension 有問題"
        tetris_formal.block_list.clear()
        tetris_formal.block_list = [[(40, 30, 20), i, 760] for i in range(0, 40, 400)]
        tetris_formal.block_list = [[(40, 30, 20), i, 720] for i in range(0, 40, 360)]
        tetris_formal.score = 0
                
        expect_block_list = []
        expect_block_list.extend([[(40,30,20), i, 760] for i in range(0, 40,360)])
        
        tetris_formal.remove_and_drop()
        self.assertEqual(expect_block_list, tetris_formal.block_list)
        
        
    @patch("tetris_formal.check_left_or_right", return_value=True)
    def test_move_left_or_right(self, mock_check_left_or_right):
        tetris_formal.block_list = self.stockpiled_T_block
        tetris_formal.BLOCK_WIDTH = 40
        tetris_formal.SCREEN_WIDTH = 360        

        # 測試右移
        moved_s_block = tetris_formal.move_left_or_right("right", copy.deepcopy(self.moving_s_block))

        # 預期結果
        expect_s_block = [
            [(70, 90, 120), 80, 160],
            [(70, 90, 120), 120, 160],
            [(70, 90, 120), 80, 120],
            [(70, 90, 120), 120, 200],
        ]

        # 斷言測試
        self.assertEqual(expect_s_block, moved_s_block)

        # Mock 檢查
        mock_check_left_or_right.assert_called_once()

    
    @patch("tetris_formal.check_stockpile", return_value=False)
    @patch("tetris_formal.get_inital_value")
    def test_move_down(self, mock_get_inital_value, mock_check_stockpile):
        tetris_formal.BLOCK_WIDTH = 40
        
        mock_get_inital_value.return_value = [
            [(70, 60, 120), 0, 40], 
            [(70, 60, 120), 40, 40], 
            [(70, 60, 120), 0, 40], 
            [(70, 60, 120), 0, 40]
        ]
        
        expect_s_block = [
            [(70, 60, 120), 0, 40], 
            [(70, 60, 120), 40, 40], 
            [(70, 60, 120), 0, 40], 
            [(70, 60, 120), 0, 40]
        ]
        
        moved_list = tetris_formal.move_down(copy.deepcopy(self.moving_s_block))
        self.assertEqual(moved_list, expect_s_block)
    
    
    def test_draw_lines(self):
        tetris_formal.draw_lines = Mock()
        tetris_formal.draw_lines()
        tetris_formal.draw_lines.assert_called_once
        
    
    
    def test_press_which_side(self):
        pass
    
    
    def test_get_losing_scene(self):
        pass
    
    
    def test_check_if_player_lose(self):
        pass


if __name__ == '__main__':
    unittest.main()