#!/usr/bin/python3
"""Test module for State class."""
from tests.test_models.test_base_model import test_basemodel
from models.state import State
from os import getenv

class test_state(test_basemodel):
    """Test class for the State model."""

    def __init__(self, *args, **kwargs):
        """Initialize the test class."""
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name_type(self):
        """Test that the type of 'name' attribute is a string."""
        new = self.value()
        self.assertEqual(type(new.name), str)

    def test_name_not_null(self):
        """Test that the 'name' attribute cannot be None."""
        new = self.value()
        with self.assertRaises(Exception):
            new.name = None  # This should raise an exception because it's nullable=False

    def test_cities_relationship(self):
        """Test the relationship between State and City."""
        new_state = self.value()
        if getenv("HBNB_TYPE_STORAGE") == "db":
            # For DB storage, ensure the cities relationship exists
            self.assertEqual(hasattr(new_state, 'cities'), True)
            self.assertEqual(type(new_state.cities), list)
        else:
            # For file storage, ensure the property method works
            self.assertEqual(type(new_state.cities), list)
            self.assertEqual(new_state.cities, [])  # Should be an empty list if no cities

    def test_state_has_id(self):
        """Test that a State has a unique id."""
        new_state = self.value()
        self.assertIsNotNone(new_state.id)
        self.assertEqual(type(new_state.id), str)
