import unittest
from models.rectangle import Rectangle


class TestRectangleClass(unittest.TestCase):

    def test_constructor_with_width_and_height(self):
        rect = Rectangle(4, 6, 2, 3, 1)
        self.assertEqual(rect.id, 1)
        self.assertEqual(rect.width, 4)
        self.assertEqual(rect.height, 6)
        self.assertEqual(rect.x, 2)
        self.assertEqual(rect.y, 3)

    def test_width_property(self):
        rect = Rectangle(3, 5)
        rect.width = 8
        self.assertEqual(rect.width, 8)

        with self.assertRaises(TypeError):
            rect.width = "invalid"

        with self.assertRaises(ValueError):
            rect.width = -5

    def test_height_property(self):
        rect = Rectangle(4, 7)
        rect.height = 9
        self.assertEqual(rect.height, 9)

        with self.assertRaises(TypeError):
            rect.height = "invalid"

        with self.assertRaises(ValueError):
            rect.height = -3

    def test_x_property(self):
        rect = Rectangle(5, 8)
        rect.x = 3
        self.assertEqual(rect.x, 3)

        with self.assertRaises(ValueError):
            rect.x = -2

    def test_y_property(self):
        rect = Rectangle(6, 9)
        rect.y = 4
        self.assertEqual(rect.y, 4)

        with self.assertRaises(ValueError):
            rect.y = -1

    def test_area_method(self):
        rect = Rectangle(3, 4)
        self.assertEqual(rect.area(), 12)

    def test_update_method_with_args(self):
        rect = Rectangle(5, 7)
        rect.update(2, 8, 6, 3, 4)
        self.assertEqual(rect.id, 2)
        self.assertEqual(rect.width, 8)
        self.assertEqual(rect.height, 6)
        self.assertEqual(rect.x, 3)
        self.assertEqual(rect.y, 4)

    def test_update_method_with_kwargs(self):
        rect = Rectangle(5, 7)
        rect.update(id=2, width=8, height=6, x=3, y=4)
        self.assertEqual(rect.id, 2)
        self.assertEqual(rect.width, 8)
        self.assertEqual(rect.height, 6)
        self.assertEqual(rect.x, 3)
        self.assertEqual(rect.y, 4)

    def test_update_method_with_mixed_args_and_kwargs(self):
        rect = Rectangle(5, 7)
        rect.update(2, width=8, height=6)
        self.assertEqual(rect.id, 2)
        self.assertEqual(rect.width, 8)
        self.assertEqual(rect.height, 6)
        self.assertEqual(rect.x, 0)  # x is not provided, should not change
        self.assertEqual(rect.y, 0)  # y is not provided, should not change

    def test_to_dictionary_method(self):
        rect = Rectangle(4, 5, 2, 3, 1)
        result = rect.to_dictionary()
        expected = {'x': 2, 'y': 3, 'id': 1, 'height': 5, 'width': 4}
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
