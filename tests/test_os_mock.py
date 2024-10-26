import unittest
from MockManager import MockManager
import os 


mock_file_path = "./mocks/os_mock_data.json"  # Update to the correct file path


class TestMockedOSModule(unittest.TestCase):
    def setUp(self):
        # Load the mock configuration before running the tests
        self.mock_manager = MockManager(mock_file_path)
        self.mock_manager.apply_mocks()

    def tearDown(self):
        # Stop all mocks after the tests
        if self.mock_manager:
            self.mock_manager.stop_mocks()

    def test_mocked_listdir(self):
        """Test mocked os.listdir method."""
        response = os.listdir("/mocked/path")
        self.assertEqual(response, ["file1.txt", "file2.txt", "folder1"])

    def test_mocked_mkdir(self):
        """Test mocked os.mkdir method."""
        os.mkdir("/mocked/path", mode=0o755, exist_ok=True)

    def test_mocked_remove(self):
        """Test mocked os.remove method."""
        os.remove("/mocked/path/to/file.txt")

    def test_mocked_stat(self):
        """Test mocked os.stat method."""
        stat_result = os.stat("/mocked/path/to/file.txt")
        self.assertEqual(stat_result["st_size"], 1024)

    def test_mocked_getcwd(self):
        """Test mocked os.getcwd method."""
        current_dir = os.getcwd()
        self.assertEqual(current_dir, "/mocked/current/directory")

    def test_mocked_path_exists(self):
        """Test mocked os.path.exists method."""
        path_exists = os.path.exists("/mocked/path/to/file.txt")
        self.assertTrue(path_exists)


# Running the updated tests
suite = unittest.TestSuite()
suite.addTest(TestMockedOSModule('test_mocked_listdir'))
suite.addTest(TestMockedOSModule('test_mocked_mkdir'))
suite.addTest(TestMockedOSModule('test_mocked_remove'))
suite.addTest(TestMockedOSModule('test_mocked_stat'))
suite.addTest(TestMockedOSModule('test_mocked_getcwd'))
suite.addTest(TestMockedOSModule('test_mocked_path_exists'))

runner = unittest.TextTestRunner()
runner.run(suite)