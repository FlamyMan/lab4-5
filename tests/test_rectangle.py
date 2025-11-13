import unittest

from rectangle import rectangle

class TestRectangleArea(unittest.TestCase):
    def test_zero_area(self):
        rect = rectangle(0, 0)
        self.assertEqual(rect.area(), 0)
    
    def test_area_4x12(self):
        rect = rectangle(4, 12)
        self.assertEqual(rect.area(), 48)

    def test_area_12x4(self):
        rect = rectangle(12, 4)
        self.assertEqual(rect.area(), 48)

    def test_area_1x12(self):
        rect = rectangle(1, 12)
        self.assertEqual(rect.area(), 12)
    
    def test_area_neg_4x3(self):
        rect = rectangle(-4, 3)
        self.assertEqual(rect.area(), 12)

    def test_area_4x_neg_3(self):
        rect = rectangle(4, -3)
        self.assertEqual(rect.area(), 12)

    def test_area_neg_4x_neg_3(self):
        rect = rectangle(-4, -3)
        self.assertEqual(rect.area(), 12)
    
    def test_height_width_switch_does_not_matter_1(self):
        x = 15
        y = 12
        rect_xy = rectangle(x, y)
        rect_yx = rectangle(y, x)
        self.assertEqual(rect_xy.area(), rect_yx.area())

    def test_height_width_switch_does_not_matter_2(self):
        x = 2
        y = 3
        rect_xy = rectangle(x, y)
        rect_yx = rectangle(y, x)
        self.assertEqual(rect_xy.area(), rect_yx.area())
    
    def test_height_width_switch_does_not_matter_3(self):
        x = 7
        y = 77
        rect_xy = rectangle(x, y)
        rect_yx = rectangle(y, x)
        self.assertEqual(rect_xy.area(), rect_yx.area())
    
    def test_dont_care_sign_x_1(self):
        x = 2
        y = 6
        rect = rectangle(x, y)
        rect_neg_x = rectangle(-x, y)
        self.assertEqual(rect.area(), rect_neg_x.area())

    def test_dont_care_sign_x_2(self):
        x = 7
        y = 9
        rect = rectangle(x, y)
        rect_neg_x = rectangle(-x, y)
        self.assertEqual(rect.area(), rect_neg_x.area())

    def test_dont_care_sign_x_3(self):
        x = 9
        y = 3
        rect = rectangle(x, y)
        rect_neg_x = rectangle(-x, y)
        self.assertEqual(rect.area(), rect_neg_x.area())
    
    def test_dont_care_sign_y_1(self):
        x = 2
        y = 6
        rect = rectangle(x, y)
        rect_neg_y = rectangle(x, -y)
        self.assertEqual(rect.area(), rect_neg_y.area())

    def test_dont_care_sign_y_2(self):
        x = 7
        y = 9
        rect = rectangle(x, y)
        rect_neg_y = rectangle(x, -y)
        self.assertEqual(rect.area(), rect_neg_y.area())

    def test_dont_care_sign_y_3(self):
        x = 9
        y = 3
        rect = rectangle(x, y)
        rect_neg_y = rectangle(x, -y)
        self.assertEqual(rect.area(), rect_neg_y.area())
    
    def test_dont_care_sign_both_1(self):
        x = 10
        y = 11
        rect = rectangle(x, y)
        rect_neg = rectangle(-x, -y)
        self.assertEqual(rect.area(), rect_neg.area())

    def test_dont_care_sign_both_2(self):
        x = 79
        y = 12
        rect = rectangle(x, y)
        rect_neg = rectangle(-x, -y)
        self.assertEqual(rect.area(), rect_neg.area())
    
    def test_dont_care_sign_both_3(self):
        x = 44
        y = 3
        rect = rectangle(x, y)
        rect_neg = rectangle(-x, -y)
        self.assertEqual(rect.area(), rect_neg.area())

class TestRectanglePerimeter(unittest.TestCase):
    def test_perimeter_12x3(self):
        x = 12
        y = 3
        rect = rectangle(x, y)
        self.assertEqual(rect.perimeter(), 30)

    def test_perimeter_3x2(self):
        x = 3
        y = 2
        rect = rectangle(x, y)
        self.assertEqual(rect.perimeter(), 10)
    
    def test_perimeter_11x17(self):
        x = 11
        y = 17
        rect = rectangle(x, y)
        self.assertEqual(rect.perimeter(), 56)
    
    def test_dont_care_switch_1(self):
        x = 11
        y = 2
        rect_xy = rectangle(x, y)
        rect_yx = rectangle(y, x)
        self.assertEqual(rect_xy.perimeter(), rect_yx.perimeter())
    
    def test_dont_care_switch_2(self):
        x = 73
        y = 90
        rect_xy = rectangle(x, y)
        rect_yx = rectangle(y, x)
        self.assertEqual(rect_xy.perimeter(), rect_yx.perimeter())

    def test_dont_care_switch_3(self):
        x = 32
        y = 16
        rect_xy = rectangle(x, y)
        rect_yx = rectangle(y, x)
        self.assertEqual(rect_xy.perimeter(), rect_yx.perimeter())

    def sign_dont_care_sign_x(self):
        x = 11
        y = 16
        rect_xy = rectangle(x, y)
        rect_neg_x = rectangle(-x, y)
        self.assertEqual(rect_xy.perimeter(), rect_neg_x.perimeter())
    
    def sign_dont_care_sign_y(self):
        x = 11
        y = 16
        rect_xy = rectangle(x, y)
        rect_neg_y = rectangle(x, -y)
        self.assertEqual(rect_xy.perimeter(), rect_neg_y.perimeter())
    
    