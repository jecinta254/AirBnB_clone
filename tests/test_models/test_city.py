#!/usr/bin/python3
"""Defines unittests for models/city.py.

Unittest classes:
    TestCity_instantiation
    TestCity_save
    TestCity_to_dict
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.city import City


class TestCity_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the City class."""

    def test_no_args_instantiates(self):
        self.assertEqual(City, type(City()))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(City(), models.storage.all().values())

    def test_id_is_public_str(self):
        self.assertEqual(str, type(City().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(City().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(City().updated_at))

    def test_state_id_is_public_class_attribute(self):
        cty = City()
        self.assertEqual(str, type(City.state_id))
        self.assertIn("state_id", dir(cty))
        self.assertNotIn("state_id", cty.__dict__)

    def test_name_is_public_class_attribute(self):
        cty = City()
        self.assertEqual(str, type(City.name))
        self.assertIn("name", dir(cty))
        self.assertNotIn("name", cty.__dict__)

    def test_two_cities_unique_ids(self):
        city_1 = City()
        city_2 = City()
        self.assertNotEqual(city_1.id, city_2.id)

    def test_two_cities_different_created_at(self):
        city_1 = City()
        sleep(0.05)
        city_2 = City()
        self.assertLess(city_1.created_at, city_2.created_at)

    def test_two_cities_different_updated_at(self):
        city_1 = City()
        sleep(0.05)
        city_2 = City()
        self.assertLess(city_1.updated_at, city_2.updated_at)

    def test_str_representation(self):
        d_time = datetime.today()
        d_time_repr = repr(d_time)
        cty = City()
        cty.id = "123456"
        cty.created_at = cty.updated_at = d_time
        city_str = cty.__str__()
        self.assertIn("[City] (123456)", city_str)
        self.assertIn("'id': '123456'", city_str)
        self.assertIn("'created_at': " + d_time_repr, city_str)
        self.assertIn("'updated_at': " + d_time_repr, city_str)

    def test_args_unused(self):
        cty = City(None)
        self.assertNotIn(None, cty.__dict__.values())

    def test_instantiation_with_kwargs(self):
        d_time = datetime.today()
        d_time_iso = d_time.isoformat()
        cty = City(id="345", created_at=d_time_iso, updated_at=d_time_iso)
        self.assertEqual(cty.id, "345")
        self.assertEqual(cty.created_at, d_time)
        self.assertEqual(cty.updated_at, d_time)

    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            City(id=None, created_at=None, updated_at=None)


class TestCity_save(unittest.TestCase):
    """Unittests for testing save method of the City class."""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_one_save(self):
        cty = City()
        sleep(0.05)
        f_updated_at = cty.updated_at
        cty.save()
        self.assertLess(f_updated_at, cty.updated_at)

    def test_two_saves(self):
        cty = City()
        sleep(0.05)
        f_updated_at = cty.updated_at
        cty.save()
        s_updated_at = cty.updated_at
        self.assertLess(f_updated_at, s_updated_at)
        sleep(0.05)
        cty.save()
        self.assertLess(s_updated_at, cty.updated_at)

    def test_save_with_arg(self):
        cty = City()
        with self.assertRaises(TypeError):
            cty.save(None)

    def test_save_updates_file(self):
        cty = City()
        cty.save()
        city_id = "City." + cty.id
        with open("file.json", "r") as f:
            self.assertIn(city_id, f.read())


class TestCity_to_dict(unittest.TestCase):
    """Unittests for testing to_dict method of the City class."""

    def test_to_dict_type(self):
        self.assertTrue(dict, type(City().to_dict()))

    def test_to_dict_contains_correct_keys(self):
        cty = City()
        self.assertIn("id", cty.to_dict())
        self.assertIn("created_at", cty.to_dict())
        self.assertIn("updated_at", cty.to_dict())
        self.assertIn("__class__", cty.to_dict())

    def test_to_dict_contains_added_attributes(self):
        cty = City()
        cty.middle_name = "Holberton"
        cty.my_number = 98
        self.assertEqual("Holberton", cty.middle_name)
        self.assertIn("my_number", cty.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        cty = City()
        city_dict = cty.to_dict()
        self.assertEqual(str, type(city_dict["id"]))
        self.assertEqual(str, type(city_dict["created_at"]))
        self.assertEqual(str, type(city_dict["updated_at"]))

    def test_to_dict_output(self):
        d_time = datetime.today()
        cty = City()
        cty.id = "123456"
        cty.created_at = cty.updated_at = d_time
        t_dict = {
            'id': '123456',
            '__class__': 'City',
            'created_at': d_time.isoformat(),
            'updated_at': d_time.isoformat(),
        }
        self.assertDictEqual(cty.to_dict(), tdict)

    def test_contrast_to_dict_dunder_dict(self):
        cty = City()
        self.assertNotEqual(cty.to_dict(), cty.__dict__)

    def test_to_dict_with_arg(self):
        cty = City()
        with self.assertRaises(TypeError):
            cty.to_dict(None)


if __name__ == "__main__":
    unittest.main()
