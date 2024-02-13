#!/usr/bin/python3
"""
The BaseModel Tests

This file contains unittests for the BaseModel class models package.

To run the test, use the following command:
    python3 -m unittest tests.test_models.test_base_model

To run the entire test suite, use the following command:
    python3 -m unittest discover tests
"""

# import the unittest module for writing and running unit tests
import unittest

# import the doctest module for testing docstrings
import doctest

# import the pycodestyle module for checking code style compliance
import pycodestyle

# import the datetime class from the datetime mod for working with timestamps
from datetime import datetime

# import the BaseModel class from the base_model module
from models.base_model import BaseModel

# import the base_model module from the models package
from models import base_model


class TestDocumentation(unittest.TestCase):
    """Test documentation for BaseModel class."""

    def test_module_docstring(self):
        """Test if the module has a docstring."""

        self.assertIsNotNone(BaseModel.__doc__)
        doctest.testmod(base_model, verbose=True)

    def test_class_docstring(self):
        """Test if the class has a docstring."""

        self.assertIsNotNone(BaseModel.__doc__)

    def test_base_model_methods_docstrings(self):
        """Test if BaseModel methods have docstrings."""
        methods_to_test = [
            BaseModel.__init__,
            BaseModel.__str__,
            BaseModel.save,
            BaseModel.to_dict
            ]

        for method in methods_to_test:
            with self.subTest(method=method):
                self.assertIsNotNone(method.__doc__)

    def test_no_blank_lines_in_docstrings(self):
        """Test if there are no unnecessary blank lines in docstrings."""

        for item in [
            BaseModel,
            BaseModel.__init__,
            BaseModel.__str__,
            BaseModel.save,
            BaseModel.to_dict,
        ]:
            docstring = item.__doc__
            if docstring:
                self.assertNotIn(
                    "\n\n\n",
                    docstring,
                    f"Too many blank lines in {item.__name__}'s docstring",
                )
                self.assertNotIn(
                    "\n\n\n\n",
                    docstring,
                    f"Too many consecutive blank lines in {item.__name__}'s "
                    f"docstring",
                )


class TestPycodestyle(unittest.TestCase):
    """Test Pycodestyle compliance for the project."""

    def test_pycodestyle(self):
        """Check if the code follows Pycodestyle conventions."""

        # create a Pycodestyle StyleGuide object
        style_checker = pycodestyle.StyleGuide()

        # check Pycodestyle for the specified files
        result = style_checker.check_files(
            ["models/base_model.py", "tests/test_models/test_base_model.py"]
        )

        # assert that there are no style issues
        self.assertEqual(
            result.total_errors, 0, "Found code style errors (and warning)."
        )


class TestBaseModel(unittest.TestCase):
    """Test cases for the BaseModel class."""

    @classmethod
    def setUpClass(cls):
        """Setup method executed before any test method in the class."""

        # create an instance of BaseModel for testing
        cls.model = BaseModel()

    @classmethod
    def tearDownClass(cls):
        """Cleanup method executed after all test methods in the class."""

        # delete the BaseModel instance after all tests are completed
        del cls.model

    def test_base_model_class(self):
        """Test BaseModel class."""

        # check if the BaseModel class has the expected methods
        self.assertTrue(hasattr(BaseModel, "__init__"))
        self.assertTrue(hasattr(BaseModel, "__str__"))
        self.assertTrue(hasattr(BaseModel, "save"))
        self.assertTrue(hasattr(BaseModel, "to_dict"))

    def test_initialization(self):
        """Test initialization of the BaseModel."""

        # create a new instance of BaseModel
        # to ensure independence between tests
        model = BaseModel()

        # check if the instance is of type BaseModel
        self.assertIsInstance(model, BaseModel)

        # check attribute existence
        self.assertTrue(hasattr(model, "id"))
        self.assertTrue(hasattr(model, "created_at"))
        self.assertTrue(hasattr(model, "updated_at"))

        # check data types of id, created_at, and updated_at attributes
        # to ensure they are of the expected types (str and datetime)
        self.assertIsInstance(model.id, str)
        self.assertIsInstance(model.created_at, datetime)
        self.assertIsInstance(model.updated_at, datetime)

    def test_string_representation(self):
        """Test string representation of the BaseModel."""

        # get the string representation of the BaseModel instance
        string_repr = str(self.model)

        # check if the class name, instance id, and dictionary
        # representation are present in the string representation
        self.assertIn(type(self.model).__name__, string_repr)
        self.assertIn(f"({self.model.id})", string_repr)
        self.assertIn(str(self.model.__dict__), string_repr)

    def test_save_method(self):
        """Test the save method of the BaseModel."""

        # record the original value of updated_at
        original_updated_at = self.model.updated_at

        # call the save method to update updated_at
        self.model.save()

        # assert that updated_at has been updated
        self.assertNotEqual(original_updated_at, self.model.updated_at)

    def test_to_dict_method(self):
        """Test the to_dict method of the BaseModel."""

        model_dict = self.model.to_dict()

        # check if the result is a dictionary
        self.assertIsInstance(model_dict, dict)

        # check the value of the '__class__' key
        self.assertIn("__class__", model_dict)
        self.assertEqual(model_dict["__class__"], "BaseModel")

        # additional checks for expected keys if needed
        expected_keys = ["id", "created_at", "updated_at"]
        for key in expected_keys:
            with self.subTest(key=key):
                self.assertIn(key, model_dict)
