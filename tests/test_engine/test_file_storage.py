#!/usr/bin/python3
"""
The FileStorage Tests

This file contains unit tests for the FileStorage module.

To run the test, use the following command:
    python3 -m unittest tests.test_engine.test_file_storage

To run the entire test suite, use the following command:
    python3 -m unittest discover tests
"""

# import the unittest module for creating and running test cases
import unittest

# import the doctest module for testing documentation embedded in docstrings
import doctest

# import the pycodestyle module for checking code style compliance
import pycodestyle

# import the json module for handling JSON data
import json

# import the file_storage module from the models.engine package
from models.engine import file_storage

# import the FileStorage class from the file_storage module
from models.engine.file_storage import FileStorage

# import the BaseModel class from the models.base_model module
from models.base_model import BaseModel


class TestDocumentation(unittest.TestCase):
    """
    Test documentation for the FileStorage class.
    """

    def test_module_docstring(self):
        """Test if the module has a docstring."""

        self.assertIsNotNone(FileStorage.__doc__)
        doctest.testmod(file_storage, verbose=True)

    def test_class_docstring(self):
        """Test if the class has a docstring."""

        self.assertIsNotNone(FileStorage.__doc__)

    def test_file_storage_properties_docstring(self):
        """Test if the file_storage_properties method has a docstring."""

        self.assertIsNotNone(FileStorage.file_path.__doc__)
        self.assertIsNotNone(FileStorage.objects.__doc__)

    def test_file_storage_methods_docstrings(self):
        """Test if FileStorage methods have docstrings."""
        methods_to_test = [
            FileStorage.all,
            FileStorage.new,
            FileStorage.save,
            FileStorage.reload
            ]

        for method in methods_to_test:
            with self.subTest(method=method):
                self.assertIsNotNone(method.__doc__)

    def test_no_blank_lines_in_docstrings(self):
        """Test if there are no unnecessary blank lines in docstrings."""

        for item in [
            FileStorage,
            FileStorage.all,
            FileStorage.new,
            FileStorage.save,
            FileStorage.reload,
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
    """
    Test Pycodestyle compliance for the project.
    """

    def test_pycodestyle(self):
        """Check if the code follows Pycodestyle conventions."""

        # create a Pycodestyle StyleGuide object
        style_checker = pycodestyle.StyleGuide()

        # check Pycodestyle for the specified files
        result = style_checker.check_files(
            [
                "models/engine/file_storage.py",
                "tests/test_engine/test_file_storage.py",
            ]
        )

        # assert that there are no style issues
        self.assertEqual(
            result.total_errors, 0, "Found code style errors (and warning)."
        )


class TestFileStorage(unittest.TestCase):
    """
    Test cases for the FileStorage class.
    """

    @classmethod
    def setUpClass(cls):
        """Setup method executed before any test method in the class."""

        # create an instance of FileStorage for testing
        cls.storage = FileStorage()

    @classmethod
    def tearDownClass(cls):
        """Cleanup method executed after all test methods in the class."""

        # delete the FileStorage instance after all tests are completed
        del cls.storage

    def test_file_storage_properties(self):
        """Test the properties of the FileStorage class."""

        # check if the file_path property is set correctly
        self.assertEqual(self.storage.file_path, "file.json")

        # check if the objects property is a dictionary
        self.assertIsInstance(self.storage.objects, dict)

    def test_file_storage_class(self):
        """Test the FileStorage class."""

        # check if the FileStorage class has the expected methods
        self.assertTrue(hasattr(FileStorage, "all"))
        self.assertTrue(hasattr(FileStorage, "new"))
        self.assertTrue(hasattr(FileStorage, "save"))
        self.assertTrue(hasattr(FileStorage, "reload"))

    def test_all_method(self):
        """Test the all method of the FileStorage class."""

        # check if the all method returns a dictionary
        objects = self.storage.all()
        self.assertIsInstance(objects, dict)

    def test_new_method(self):
        """Test the new method of the FileStorage class."""

        # create a new BaseModel instance
        model = BaseModel()

        # add the model to the storage
        self.storage.new(model)

        # check if the key for the model exists in the storage objects
        key = f"{type(model).__name__}.{model.id}"
        self.assertIn(key, self.storage.objects)

    def test_save_method(self):
        """Test the save method of the FileStorage class."""

        # create a new BaseModel instance
        model = BaseModel()

        # add the model to the storage
        self.storage.new(model)

        # save the storage to a file
        self.storage.save()

        # open the file and load its content
        with open(self.storage.file_path, "r", encoding="utf-8") as file:
            data = json.load(file)

        # check if the key for the model exists in the loaded data
        key = f"{type(model).__name__}.{model.id}"
        self.assertIn(key, data)

        # test saving when no objects are present
        self.storage.save()

    def test_reload_method(self):
        """Test the reload method of the FileStorage class."""

        # create a new BaseModel instance
        model = BaseModel()

        # add the model to the storage
        self.storage.new(model)

        # save the storage to a file
        self.storage.save()

        # reload the storage from the file
        self.storage.reload()

        # check if the key for the model exists
        # in the reloaded storage objects
        key = f"{type(model).__name__}.{model.id}"
        self.assertIn(key, self.storage.objects)
