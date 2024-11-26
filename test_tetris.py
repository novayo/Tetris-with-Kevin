import unittest
from unittest.mock import Mock, patch
import tetris_formal


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
        
        up, down, right, left = tetris_formal.get_changing_value(self.moving_s_block)
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
        self.assertTrue(tetris_formal.check_boundary(self.moving_s_block))
        self.assertFalse(tetris_formal.check_boundary(self.out_of_bound_block))
    
    def test_Rotate(self):
        tetris_formal.block_figure = "S"
        rotate = tetris_formal.Rotate(self.moving_s_block)
        clockwise_s_block = rotate.clockwise()
        
        filtered_item = [item for item in clockwise_s_block if item in [[40,160],[80,160],[40,200],[0,200]]]
        
        if len(filtered_item) == 4 :
            self.assertEqual(True, True)
    
    def test_draw_blocks(self):
        inner_block = self.moving_s_block
        
        tetris_formal.draw_blocks = Mock()
        tetris_formal.draw_blocks(inner_block)
        tetris_formal.draw_blocks.assert_called()
        
    def test_check_stockpile(self):
        local_temp_list = self.moving_s_block
        tetris_formal.block_list = self.stockpiled_T_block
        
        value = tetris_formal.check_stockpile(local_temp_list)
        self.assertTrue(value)
    
    def test_check_left_or_right(self):
        self.assertEqual(tetris_formal.move_left_or_right("left", self.moving_s_block), [[(70, 90, 120), 0, 160], [(70, 90, 120), 40, 160], [(70, 90, 120), 0, 120], [(70, 90, 120), 40, 200]])
        self.assertNotEqual(tetris_formal.move_left_or_right("right", self.out_of_bound_block), [[(70, 90, 120), 80, 160], [(70, 90, 120), 120, 160], [(70, 90, 120), 80, 120], [(70, 90, 120), 120, 200]])
    
    def test_remove_and_drop(self):
        pass
    
    def test_move_left_or_right(self):
        pass
    
    def test_move_down(self):
        pass
    
    def test_draw_lines(self):
        pass
    
    def test_press_which_side(self):
        pass
    
    def test_get_losing_scene(self):
        pass
    
    def test_check_if_player_lose(self):
        pass

if __name__ == '__main__':
    unittest.main()