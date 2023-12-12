import unittest
from models.base import Base
from models.square import Square
from models.rectangle import Rectangle
import os

class TestBaseClass(unittest.TestCase):

    def test_constructor_with_id(self):
        obj = Base(id=5)
        self.assertEqual(obj.id, 5)

    def test_constructor_without_id(self):
        obj1 = Base()
        obj2 = Base()
        self.assertEqual(obj1.id, 1)
        self.assertEqual(obj2.id, 2)

    def test_to_json_string_method(self):
        result = Base.to_json_string([{'id': 1, 'name': 'John'}, {'id': 2, 'name': 'Alice'}])
        expected = '[{"id": 1, "name": "John"}, {"id": 2, "name": "Alice"}]'
        self.assertEqual(result, expected)

    def test_save_to_file_method(self):
        filename = f"{Base.__name__}.json"
        with open(filename, 'r') as file:
            content = file.read()
        self.assertEqual(content, '[]')

    def test_from_json_string_method(self):
        json_string = '[{"id": 1, "name": "John"}, {"id": 2, "name": "Alice"}]'
        result = Base.from_json_string(json_string)
        expected = [{'id': 1, 'name': 'John'}, {'id': 2, 'name': 'Alice'}]
        self.assertEqual(result, expected)

    def test_create_method_rectangle(self):
        result = Base.create(Rectangle, id=1, width=3, height=4)
        self.assertEqual(result.id, 1)
        self.assertEqual(result.width, 3)
        self.assertEqual(result.height, 4)

    def test_create_method_square(self):
        result = Base.create(Square, id=1, size=5)
        self.assertEqual(result.id, 1)
        self.assertEqual(result.size, 5)

    def test_load_from_file_method(self):
        filename = f"{Base.__name__}.json"
        with open(filename, 'w') as file:
            file.write('[{"id": 1, "width": 3, "height": 4}, {"id": 2, "size": 5}]')

        result = Base.load_from_file(Rectangle)
        self.assertEqual(len(result), 2)
        self.assertIsInstance(result[0], Rectangle)
        self.assertEqual(result[0].id, 1)
        self.assertEqual(result[0].width, 3)
        self.assertEqual(result[0].height, 4)

    def tearDown(self):
        filename = f"{Base.__name__}.json"
        if os.path.exists(filename):
            os.remove(filename)


if __name__ == '__main__':
    unittest.main()
