#!/usr/bin/python3
"""Defines unittests for models/amenty.py.

Unittest classes:
    TestAmenity_instantiation
    TestAmenity_save
    TestAmenity_to_dict
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.amenty import Amenity


class TestAmenity_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the Amenity class."""

    def test_no_args_instantiates(self):
        self.assertEqual(Amenity, type(Amenity()))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(Amenity(), models.storage.all().values())

    def test_id_is_public_str(self):
        self.assertEqual(str, type(Amenity().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Amenity().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Amenity().updated_at))

    def test_name_is_public_class_attribute(self):
        amenty = Amenity()
        self.assertEqual(str, type(Amenity.name))
        self.assertIn("name", dir(Amenity()))
        self.assertNotIn("name", amenty.__dict__)

    def test_two_amenities_unique_ids(self):
        amenity_1 = Amenity()
        amenity_2 = Amenity()
        self.assertNotEqual(amenity_1.id, amenity_2.id)

    def test_two_amenities_different_created_at(self):
        amenity_1 = Amenity()
        sleep(0.05)
        amenity_2 = Amenity()
        self.assertLess(amenity_1.created_at, amenity_2.created_at)

    def test_two_amenities_different_updated_at(self):
        amenity_1 = Amenity()
        sleep(0.05)
        amenity_2 = Amenity()
        self.assertLess(amenity_1.updated_at, amenity_2.updated_at)

    def test_str_representation(self):
        d_time = datetime.today()
        d_time_repr = repr(d_time)
        amenty = Amenity()
        amenty.id = "123456"
        amenty.created_at = amenty.updated_at = d_time
        amenity_str = amenty.__str__()
        self.assertIn("[Amenity] (123456)", amenity_str)
        self.assertIn("'id': '123456'", amenity_str)
        self.assertIn("'created_at': " + d_time_repr, amenity_str)
        self.assertIn("'updated_at': " + d_time_repr, amenity_str)

    def test_args_unused(self):
        amenty = Amenity(None)
        self.assertNotIn(None, amenty.__dict__.values())

    def test_instantiation_with_kwargs(self):
        """instantiation with kwargs test method"""
        d_time = datetime.today()
        d_time_iso = d_time.isoformat()
        amenty = Amenity(id="345", created_at=d_time_iso, updated_at=d_time_iso)
        self.assertEqual(amenty.id, "345")
        self.assertEqual(amenty.created_at, d_time)
        self.assertEqual(amenty.updated_at, d_time)

    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            Amenity(id=None, created_at=None, updated_at=None)


class TestAmenity_save(unittest.TestCase):
    """Unittests for testing save method of the Amenity class."""

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
        amenty = Amenity()
        sleep(0.05)
        f_updated_at = amenty.updated_at
        amenty.save()
        self.assertLess(f_updated_at, amenty.updated_at)

    def test_two_saves(self):
        amenty = Amenity()
        sleep(0.05)
        f_updated_at = amenty.updated_at
        amenty.save()
        s_updated_at = amenty.updated_at
        self.assertLess(f_updated_at, s_updated_at)
        sleep(0.05)
        amenty.save()
        self.assertLess(s_updated_at, amenty.updated_at)

    def test_save_with_arg(self):
        amenty = Amenity()
        with self.assertRaises(TypeError):
            amenty.save(None)

    def test_save_updates_file(self):
        amenty = Amenity()
        amenty.save()
        amenity_id = "Amenity." + amenty.id
        with open("file.json", "r") as f:
            self.assertIn(amenity_id, f.read())


class TestAmenity_to_dict(unittest.TestCase):
    """Unittests for testing to_dict method of the Amenity class."""

    def test_to_dict_type(self):
        self.assertTrue(dict, type(Amenity().to_dict()))

    def test_to_dict_contains_correct_keys(self):
        amenty = Amenity()
        self.assertIn("id", amenty.to_dict())
        self.assertIn("created_at", amenty.to_dict())
        self.assertIn("updated_at", amenty.to_dict())
        self.assertIn("__class__", amenty.to_dict())

    def test_to_dict_contains_added_attributes(self):
        amenty = Amenity()
        amenty.middle_name = "Holberton"
        amenty.my_number = 98
        self.assertEqual("Holberton", amenty.middle_name)
        self.assertIn("my_number", amenty.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        amenty = Amenity()
        amenity_dict = amenty.to_dict()
        self.assertEqual(str, type(amenity_dict["id"]))
        self.assertEqual(str, type(amenity_dict["created_at"]))
        self.assertEqual(str, type(amenity_dict["updated_at"]))

    def test_to_dict_output(self):
        d_time = datetime.today()
        amenty = Amenity()
        amenty.id = "123456"
        amenty.created_at = amenty.updated_at = d_time
        tdict = {
            'id': '123456',
            '__class__': 'Amenity',
            'created_at': d_time.isoformat(),
            'updated_at': d_time.isoformat(),
        }
        self.assertDictEqual(amenty.to_dict(), tdict)

    def test_contrast_to_dict_dunder_dict(self):
        amenty = Amenity()
        self.assertNotEqual(amenty.to_dict(), amenty.__dict__)

    def test_to_dict_with_arg(self):
        amenty = Amenity()
        with self.assertRaises(TypeError):
            amenty.to_dict(None)


if __name__ == "__main__":
    unittest.main()
