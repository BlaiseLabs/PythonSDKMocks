import unittest
from MockManager import MockManager
import os  # Import the module to be mocked

class TestOSMockMethodsExist(unittest.TestCase):
    def setUp(self):
        # Load the os mock configuration before running the tests
        self.mock_file = './mocks/os_mock_data.json'  # Update with the actual path to your os mocks JSON file
        self.module_name = 'os'
        self.mock_manager = MockManager(self.mock_file)
        self.mock_manager.apply_mocks()

    def tearDown(self):
        # Stop all mocks after the tests
        if self.mock_manager:
            self.mock_manager.stop_mocks()

    def test_methods_exist_in_module(self):
        """Test if the mocked methods exist in the os module."""
        methods_to_check = self.mock_manager.mocks.get("mocked_modules", {}).get(self.module_name, {}).get("methods", {})

        for method_name in methods_to_check:
            with self.subTest(method=method_name):
                print(f"Checking method: {self.module_name}.{method_name}")
                try:
                    # Use eval to check the existence of the method dynamically
                    eval(f"{self.module_name}.{method_name}")
                    method_exists = True
                except AttributeError:
                    method_exists = False

                self.assertTrue(method_exists, f"{self.module_name}.{method_name} method does not exist")


if __name__ == '__main__':
    suite = unittest.TestSuite()
    # Example usage with the os mock data we implemented earlier
    mock_file_path = './mocks/os_mock_data.json'  # Update with the path to the os mocks JSON
    module_name = 'os'

    suite.addTest(TestOSMockMethodsExist())
    runner = unittest.TextTestRunner()
    runner.run(suite)
