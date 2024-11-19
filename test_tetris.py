import unittest
import sys
import tetris_formal as T


class MainTest(unittest.TestCase):
    moving_s_block = [[(70, 90, 120), 40, 160], [(70, 90, 120), 80, 160], [(70, 90, 120), 40, 120], [(70, 90, 120), 80, 200]]
    temp_list_2 = [[(70, 90, 120), 40, -50], [(70, 90, 120), 80, 160], [(70, 90, 120), 40, 120], [(70, 90, 120), 80, 200]]
    temp_list_3 = [[(70, 90, 120), 40, 1000], [(70, 90, 120), 80, 160], [(70, 90, 120), 40, 120], [(70, 90, 120), 80, 200]]
    
    def test_check_boundary(self):
        self.assertTrue(T.check_boundary(self.moving_s_block))
        self.assertFalse(T.check_boundary(self.temp_list_2))
        self.assertFalse(T.check_boundary(self.temp_list_3))
    
    def test_check_left_or_right(self):
        self.assertEqual(T.move_left_or_right("left", self.moving_s_block), [[(70, 90, 120), 0, 160], [(70, 90, 120), 40, 160], [(70, 90, 120), 0, 120], [(70, 90, 120), 40, 200]])
        self.assertEqual(T.move_left_or_right("right", self.temp_list_1), [[(70, 90, 120), 80, 160], [(70, 90, 120), 120, 160], [(70, 90, 120), 80, 120], [(70, 90, 120), 120, 200]])
        

if __name__ == '__main__':
    unittest.main()