import unittest
import sys
import tetris_formal as T


class MainTest(unittest.TestCase):
    moving_s_block = [[(70, 90, 120), 40, 160], [(70, 90, 120), 80, 160], [(70, 90, 120), 40, 120], [(70, 90, 120), 80, 200]]
    temp_list_2 = [[(70, 90, 120), 40, -50], [(70, 90, 120), 80, 160], [(70, 90, 120), 40, 120], [(70, 90, 120), 80, 200]]
    temp_list_3 = [[(70, 90, 120), 40, 1000], [(70, 90, 120), 80, 160], [(70, 90, 120), 40, 120], [(70, 90, 120), 80, 200]]
    
    def test_get_initial_value(self) :
        "可以只檢驗有沒有成功在跑，不需要回傳值"
        pass
    
    def test_get_changing_value(self):
        pass
    
    def test_renew_data(self):
        pass
    
    def test_check_boundary(self):
        self.assertTrue(T.check_boundary(self.moving_s_block))
        self.assertFalse(T.check_boundary(self.temp_list_2))
        self.assertFalse(T.check_boundary(self.temp_list_3))
    
    def test_Rotate(self):
        pass
    
    def test_draw_blocks(self):
        pass
    
    def test_check_stockpile(self):
        pass
    
    def test_check_left_or_right(self):
        self.assertEqual(T.move_left_or_right("left", self.moving_s_block), [[(70, 90, 120), 0, 160], [(70, 90, 120), 40, 160], [(70, 90, 120), 0, 120], [(70, 90, 120), 40, 200]])
        self.assertEqual(T.move_left_or_right("right", self.temp_list_1), [[(70, 90, 120), 80, 160], [(70, 90, 120), 120, 160], [(70, 90, 120), 80, 120], [(70, 90, 120), 120, 200]])
    
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