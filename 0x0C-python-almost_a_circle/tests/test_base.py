import unittest

class TestBaseClass(unittest.TestCase):

    def test_init_with_id(self):
        obj = Base(id=5)
        self.assertEqual(obj.id, 5)

    def test_init_without_id(self):
        obj1 = Base()
        obj2 = Base()

        self.assertNotEqual(obj1.id, obj2.id)
        self.assertEqual(obj1.id + 1, obj2.id)

if __name__ == '__main__':
    unittest.main()
