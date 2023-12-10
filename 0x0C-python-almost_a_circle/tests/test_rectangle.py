import unittest
from models.rectangle import Rectangle

class TestRectangleClass(unittest.TestCase):

    def test_constructor_with_id(self):
        rect = Rectangle(10, 20, 3, 4, id=1)
        self.assertEqual(rect.id, 1)
        self.assertEqual(rect.width, 10)
        self.assertEqual(rect.height, 20)
        self.assertEqual(rect.x, 3)
        self.assertEqual(rect.y, 4)

    def test_constructor_without_id(self):
        rect1 = Rectangle(15, 25, 2, 7)
        rect2 = Rectangle(30, 40)

        self.assertNotEqual(rect1.id, rect2.id)
        self.assertEqual(rect1.width, 15)
        self.assertEqual(rect1.height, 25)
        self.assertEqual(rect1.x, 2)
        self.assertEqual(rect1.y, 7)

        self.assertEqual(rect2.width, 30)
        self.assertEqual(rect2.height, 40)
        self.assertEqual(rect2.x, 0)
        self.assertEqual(rect2.y, 0)

    def test_property_setters(self):
        rect = Rectangle(10, 20, 3, 4)

        rect.width = 15
        rect.height = 25
        rect.x = 5
        rect.y = 8

        self.assertEqual(rect.width, 15)
        self.assertEqual(rect.height, 25)
        self.assertEqual(rect.x, 5)
        self.assertEqual(rect.y, 8)

if __name__ == '__main__':
    unittest.main()
