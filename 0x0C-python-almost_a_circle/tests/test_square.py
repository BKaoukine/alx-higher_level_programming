import unittest
from models.square import Square


class TestSquareClass(unittest.TestCase):

    def test_constructor_with_size(self):
        square = Square(5, 2, 3, 1)
        self.assertEqual(square.id, 1)
        self.assertEqual(square.size, 5)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 3)

    def test_width_property(self):
        square = Square(3)
        square.width = 7
        self.assertEqual(square.width, 7)

        with self.assertRaises(TypeError):
            square.width = "invalid"

        with self.assertRaises(ValueError):
            square.width = -5

    def test_size_property(self):
        square = Square(4)
        square.size = 9
        self.assertEqual(square.size, 9)

        with self.assertRaises(TypeError):
            square.size = "invalid"

        with self.assertRaises(ValueError):
            square.size = -2

    def test_update_method_with_args(self):
        square = Square(5)
        square.update(2, 8, 3, 4)
        self.assertEqual(square.id, 2)
        self.assertEqual(square.size, 8)
        self.assertEqual(square.x, 3)
        self.assertEqual(square.y, 4)

    def test_update_method_with_kwargs(self):
        square = Square(5)
        square.update(id=2, size=8, x=3, y=4)
        self.assertEqual(square.id, 2)
        self.assertEqual(square.size, 8)
        self.assertEqual(square.x, 3)
        self.assertEqual(square.y, 4)

    def test_update_method_with_mixed_args_and_kwargs(self):
        square = Square(5)
        square.update(2, size=8, x=3)
        self.assertEqual(square.id, 2)
        self.assertEqual(square.size, 8)
        self.assertEqual(square.x, 3)
        self.assertEqual(square.y, 0)  # y is not provided, should not change

    def test_to_dictionary_method(self):
        square = Square(6, 2, 3, 1)
        result = square.to_dictionary()
        expected = {'id': 1, 'size': 6, 'x': 2, 'y': 3}
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
