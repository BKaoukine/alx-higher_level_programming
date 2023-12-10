import unittest
from models.rectangle import Rectangle

class TestRectangleClass(unittest.TestCase):

    def setUp(self):
        self.rectangle = Rectangle(5, 3, 2, 1, id=1)

    def test_constructor_with_id(self):
        self.assertEqual(self.rectangle.id, 1)
        self.assertEqual(self.rectangle.width, 5)
        self.assertEqual(self.rectangle.height, 3)
        self.assertEqual(self.rectangle.x, 2)
        self.assertEqual(self.rectangle.y, 1)

    def test_constructor_without_id(self):
        new_rectangle = Rectangle(8, 6, 3, 4)
        self.assertNotEqual(self.rectangle.id, new_rectangle.id)
        self.assertEqual(new_rectangle.width, 8)
        self.assertEqual(new_rectangle.height, 6)
        self.assertEqual(new_rectangle.x, 3)
        self.assertEqual(new_rectangle.y, 4)

    def test_width_property(self):
        self.rectangle.width = 10
        self.assertEqual(self.rectangle.width, 10)

        with self.assertRaises(TypeError):
            self.rectangle.width = "invalid"

        with self.assertRaises(ValueError):
            self.rectangle.width = -5

    def test_height_property(self):
        self.rectangle.height = 8
        self.assertEqual(self.rectangle.height, 8)

        with self.assertRaises(TypeError):
            self.rectangle.height = "invalid"

        with self.assertRaises(ValueError):
            self.rectangle.height = -3

    def test_x_property(self):
        self.rectangle.x = 3
        self.assertEqual(self.rectangle.x, 3)

        with self.assertRaises(ValueError):
            self.rectangle.x = -2

    def test_y_property(self):
        self.rectangle.y = 4
        self.assertEqual(self.rectangle.y, 4)

        with self.assertRaises(ValueError):
            self.rectangle.y = -1

    def test_area_method(self):
        self.assertEqual(self.rectangle.area(), 15)

    def test_display_method(self):
        # Assuming stdout is captured for testing
        with captured_output() as (out, _):
            self.rectangle.display()
        output = out.getvalue().strip()
        self.assertEqual(output, "  #####\n  #####\n  #####")

    def test_update_method_with_args(self):
        self.rectangle.update(2, 8, 6, 3, 4)
        self.assertEqual(self.rectangle.id, 2)
        self.assertEqual(self.rectangle.width, 8)
        self.assertEqual(self.rectangle.height, 6)
        self.assertEqual(self.rectangle.x, 3)
        self.assertEqual(self.rectangle.y, 4)

    def test_update_method_with_kwargs(self):
        self.rectangle.update(id=2, width=8, height=6, x=3, y=4)
        self.assertEqual(self.rectangle.id, 2)
        self.assertEqual(self.rectangle.width, 8)
        self.assertEqual(self.rectangle.height, 6)
        self.assertEqual(self.rectangle.x, 3)
        self.assertEqual(self.rectangle.y, 4)

    def test_update_method_with_mixed_args_and_kwargs(self):
        self.rectangle.update(2, width=8, height=6)
        self.assertEqual(self.rectangle.id, 2)
        self.assertEqual(self.rectangle.width, 8)
        self.assertEqual(self.rectangle.height, 6)
        self.assertEqual(self.rectangle.x, 2)  # x is not provided, should not change
        self.assertEqual(self.rectangle.y, 1)  # y is not provided, should not change


if __name__ == '__main__':
    unittest.main()
