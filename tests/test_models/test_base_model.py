#!/usr/bin/python3
""" Test module for BaseModel """
import sys
from models.base_model import BaseModel
import unittest
import datetime
from uuid import UUID
import json
import os
import pycodestyle  # Ensure pycodestyle is imported


class test_basemodel(unittest.TestCase):
    """ Unit tests for BaseModel """

    def __init__(self, *args, **kwargs):
        """ Initialization """
        super().__init__(*args, **kwargs)
        self.name = 'BaseModel'
        self.value = BaseModel

    def setUp(self):
        """Setup method"""
        pass

    def tearDown(self):
        """Teardown method"""
        try:
            os.remove('file.json')
        except:
            pass

    def test_default(self):
        """Test default instance creation"""
        i = self.value()
        self.assertEqual(type(i), self.value)

    def test_kwargs(self):
        """Test instantiation with kwargs"""
        i = self.value()
        copy = i.to_dict()
        new = BaseModel(**copy)
        self.assertFalse(new is i)

    def test_kwargs_int(self):
        """Test instantiation with invalid kwargs"""
        i = self.value()
        copy = i.to_dict()
        copy.update({1: 2})
        with self.assertRaises(TypeError):
            new = BaseModel(**copy)

    def test_save(self):
        """Testing save method"""
        i = self.value()
        i.save()
        key = self.name + "." + i.id
        with open('file.json', 'r') as f:
            j = json.load(f)
            self.assertEqual(j[key], i.to_dict())

    def test_str(self):
        """Testing __str__ method"""
        i = self.value()
        self.assertEqual(str(i), '[{}] ({}) {}'.format(self.name, i.id,
                         i.__dict__))

    def test_todict(self):
        """Test to_dict method"""
        i = self.value()
        n = i.to_dict()
        self.assertEqual(i.to_dict(), n)

    def test_kwargs_none(self):
        """Test invalid kwargs"""
        n = {None: None}
        with self.assertRaises(TypeError):
            new = self.value(**n)

    def test_id(self):
        """Test id type"""
        new = self.value()
        self.assertEqual(type(new.id), str)

    def test_created_at(self):
        """Test created_at type"""
        new = self.value()
        self.assertEqual(type(new.created_at), datetime.datetime)

    # def test_updated_at(self):
    #     """Test updated_at changes after save"""
    #     new = self.value()
    #     new.save()  # Ensure updated_at is changed after save
    #     self.assertFalse(new.created_at == new.updated_at)

    def test_uuid(self):
        """Testing UUID uniqueness"""
        instance1 = BaseModel()
        instance2 = BaseModel()
        instance3 = BaseModel()
        list_instances = [instance1, instance2, instance3]
        for instance in list_instances:
            ins_uuid = instance.id
            with self.subTest(uuid=ins_uuid):
                self.assertIs(type(ins_uuid), str)
        self.assertNotEqual(instance1.id, instance2.id)
        self.assertNotEqual(instance1.id, instance3.id)
        self.assertNotEqual(instance2.id, instance3.id)

    def test_str_method(self):
        """Test __str__ method"""
        instance6 = BaseModel()
        string_output = "[BaseModel] ({}) {}".format(instance6.id,
                                                     instance6.__dict__)
        self.assertEqual(string_output, str(instance6))


if __name__ == "__main__":
    unittest.main()
