#!/usr/bin/python3
# test_base.py
"""contains unittests for base.py."""
import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase_instantiation(unittest.TestCase):
    """testing instantiation of Base class."""

    def test_no_arguments(self):
        a = Base()
        b = Base()
        self.assertEqual(a.id, b.id - 1)

    def test_three_objs(self):
        a = Base()
        b = Base()
        c = Base()
        self.assertEqual(a.id, c.id - 2)

    def test_no_id(self):
        a = Base(None)
        b = Base(None)
        self.assertEqual(a.id, b.id - 1)

    def test_new_id(self):
        self.assertEqual(10, Base(10).id)

    def test_instances_after_unique_id(self):
        a = Base()
        b = Base(12)
        c = Base()
        self.assertEqual(a.id, c.id - 1)

    def test_id(self):
        a = Base(12)
        a.id = 15
        self.assertEqual(15, a.id)

    def test_instances_private(self):
        with self.assertRaises(AttributeError):
            print(Base(10).__nb_instances)

    def test_string_id(self):
        self.assertEqual("hi", Base("hi").id)

    def test_imaginary_id(self):
        self.assertEqual(complex(7), Base(complex(7)).id)

    def test_dict_id(self):
        self.assertEqual({"a": 4, "b": 5}, Base({"a": 4, "b": 5}).id)

    def test_list(self):
        self.assertEqual([1, 2], Base([1, 2]).id)

    def test_tuple(self):
        self.assertEqual((1, 7), Base((1, 7)).id)

    def test_set_id(self):
        self.assertEqual({1, 2, 3}, Base({1, 2, 3}).id)

    def test_two_args(self):
        with self.assertRaises(TypeError):
            Base(1, 2)


class TestBase_to_json_string(unittest.TestCase):
    """tests to_json_string method of Base class."""

    def test_rectangle_type(self):
        r = Rectangle(10, 7, 2)
        self.assertEqual(str, type(Base.to_json_string([r.to_dictionary()])))

    def test_rectangle_one_dict(self):
        r = Rectangle(10, 7, 2, 8, 6)
        self.assertTrue(len(Base.to_json_string([r.to_dictionary()])) == 53)

    def test_rectangle_two_dicts(self):
        a = Rectangle(2, 3, 5, 19, 2)
        b = Rectangle(4, 2, 4, 1, 12)
        list_dicts = [a.to_dictionary(), b.to_dictionary()]
        self.assertTrue(len(Base.to_json_string(list_dicts)) == 106)

    def test_square_type(self):
        a = Square(10, 2, 3, 4)
        self.assertEqual(str, type(Base.to_json_string([a.to_dictionary()])))

    def test_one_dict(self):
        a = Square(10, 2, 3, 4)
        self.assertTrue(len(Base.to_json_string([a.to_dictionary()])) == 39)

    def test_to_json_string_square_two_dicts(self):
        a = Square(10, 2, 3, 4)
        b = Square(4, 5, 21, 2)
        list_dicts = [a.to_dictionary(), b.to_dictionary()]
        self.assertTrue(len(Base.to_json_string(list_dicts)) == 78)

    def test_to_json_string_empty_list(self):
        self.assertEqual("[]", Base.to_json_string([]))

    def test_none(self):
        self.assertEqual("[]", Base.to_json_string(None))

    def test_no_args(self):
        with self.assertRaises(TypeError):
            Base.to_json_string()

    def test_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Base.to_json_string([], 1)


class TestBase_save_to_file(unittest.TestCase):
    """tests save_to_file method of Base class."""

    @classmethod
    def tearDown(self):
        """Deletes created files."""
        try:
            os.remove("Rectangle.json")
        except IOError:
            pass
        try:
            os.remove("Square.json")
        except IOError:
            pass
        try:
            os.remove("Base.json")
        except IOError:
            pass

    def test_one_rectangle(self):
        r = Rectangle(10, 7, 2, 8, 5)
        Rectangle.save_to_file([r])
        with open("Rectangle.json", "r") as doc:
            self.assertTrue(len(doc.read()) == 53)

    def test_two_rectangles(self):
        a = Rectangle(10, 7, 2, 8, 5)
        b = Rectangle(2, 4, 1, 2, 3)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as doc:
            self.assertTrue(len(doc.read()) == 105)

    def test_one_square(self):
        a = Square(10, 7, 2, 8)
        Square.save_to_file([a])
        with open("Square.json", "r") as doc:
            self.assertTrue(len(doc.read()) == 39)

    def test_two_squares(self):
        a = Square(10, 7, 2, 8)
        b = Square(8, 1, 2, 3)
        Square.save_to_file([a, b])
        with open("Square.json", "r") as doc:
            self.assertTrue(len(doc.read()) == 77)

    def test_Nonee(self):
        Square.save_to_file(None)
        with open("Square.json", "r") as f:
            self.assertEqual("[]", f.read())

    def test_empty_list(self):
        Square.save_to_file([])
        with open("Square.json", "r") as doc:
            self.assertEqual("[]", doc.read())

    def test_moree_than_one_arg(self):
        with self.assertRaises(TypeError):
            Square.save_to_file([], 1)


class TestBase_from_json_string(unittest.TestCase):
    """tests from_json_string method of Base class."""

    def test_type(self):
        list_input = [{"id": 9, "width": 1, "height": 3}]
        json_list_input = Rectangle.to_json_string(list_input)
        output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list, type(output))

    def test_None_rectangle(self):
        list_input = [{"id": 8, "width": 10, "height": 8, "x": 6}]
        json_list_input = Rectangle.to_json_string(list_input)
        output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_input, output)

    def test_square(self):
        list_input = [{"id": 9, "size": 5, "height": 7}]
        json_list_input = Square.to_json_string(list_input)
        output = Square.from_json_string(json_list_input)
        self.assertEqual(list_input, output)

    def test_two_squares(self):
        list_input = [
            {"id": 8, "size": 1, "height": 5},
            {"id": 5, "size": 6, "height": 4}
        ]
        json_list_input = Square.to_json_string(list_input)
        output = Square.from_json_string(json_list_input)
        self.assertEqual(list_input, output)

    def test_Noone(self):
        self.assertEqual([], Base.from_json_string(None))

    def test_empty_list(self):
        self.assertEqual([], Base.from_json_string("[]"))

    def test_no_args(self):
        with self.assertRaises(TypeError):
            Base.from_json_string()


class TestBase_create(unittest.TestCase):
    """tests create method of Base class."""

    def test_original(self):
        a = Rectangle(3, 5, 1, 2, 7)
        a_dictionary = a.to_dictionary()
        b = Rectangle.create(**a_dictionary)
        self.assertEqual("[Rectangle] (7) 1/2 - 3/5", str(a))

    def test_rectangle_new(self):
        a = Rectangle(3, 5, 1, 2, 7)
        a_dictionary = a.to_dictionary()
        b = Rectangle.create(**a_dictionary)
        self.assertEqual("[Rectangle] (7) 1/2 - 3/5", str(b))

    def test_square_original(self):
        a = Square(3, 5, 1, 7)
        a_dictionary = a.to_dictionary()
        b = Square.create(**a_dictionary)
        self.assertEqual("[Square] (7) 5/1 - 3", str(b))

    def test_square_new(self):
        a = Square(3, 5, 1, 7)
        a_dictionary = a.to_dictionary()
        b = Square.create(**a_dictionary)
        self.assertEqual("[Square] (7) 5/1 - 3", str(b))

    def test_create_square_equals(self):
        a = Square(3, 5, 1, 7)
        a_dictionary = a.to_dictionary()
        b = Square.create(**a_dictionary)
        self.assertNotEqual(a, b)


class TestBase_load_from_file(unittest.TestCase):
    """tests load_from_file_method of Base class."""

    @classmethod
    def tearDown(self):
        """Deletes created files."""
        try:
            os.remove("Rectangle.json")
        except IOError:
            pass
        try:
            os.remove("Square.json")
        except IOError:
            pass

    def test_first_rectangle(self):
        a = Rectangle(10, 7, 2, 8, 6)
        b = Rectangle(2, 4, 5, 6, 6)
        Rectangle.save_to_file([a, b])
        output = Rectangle.load_from_file()
        self.assertEqual(str(a), str(output[0]))

    def test_second_rectangle(self):
        a = Rectangle(10, 7, 2, 8, 6)
        b = Rectangle(2, 4, 5, 6, 7)
        Rectangle.save_to_file([a, b])
        output = Rectangle.load_from_file()
        self.assertEqual(str(b), str(output[1]))

    def test_rectangle_types(self):
        a = Rectangle(10, 7, 2, 8, 5)
        b = Rectangle(2, 4, 5, 6, 7)
        Rectangle.save_to_file([a, b])
        output = Rectangle.load_from_file()
        self.assertTrue(all(type(o) == Rectangle for o in output))

    def test_first_square(self):
        s1 = Square(5, 1, 3, 6)
        s2 = Square(9, 5, 2, 5)
        Square.save_to_file([s1, s2])
        list_squares_output = Square.load_from_file()
        self.assertEqual(str(s1), str(list_squares_output[0]))

    def test_second_square(self):
        a = Square(5, 1, 3, 7)
        b = Square(9, 5, 2, 2)
        Square.save_to_file([a, b])
        list_squares_output = Square.load_from_file()
        self.assertEqual(str(s2), str(list_squares_output[1]))

    def test_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Base.load_from_file([], 1)


if __name__ == "__main__":
    unittest.main()
