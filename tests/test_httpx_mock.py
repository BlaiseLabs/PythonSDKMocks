import unittest
from sdk_mocks import MockManager
import httpx


mock_file_path = "./mocks/httpx_mock_data_for_download.json"

class TestMockedHTTPXModule(unittest.TestCase):
    def setUp(self):
        # Load the mock configuration before running the tests
        self.mock_manager = MockManager(mock_file_path)
        self.mock_manager.apply_mocks()

    def tearDown(self):
        # Stop all mocks after the tests
        if self.mock_manager:
            self.mock_manager.stop_mocks()

    def test_mocked_httpx_get(self):
        """Test mocked httpx.get method."""

        response = httpx.get("https://api.example.com/users")

        expected_response = {
            "status_code": 200,
            "json": {"message": "Mocked GET response"},
            "text": "Mocked GET response as text",
            "headers": {"Content-Type": "application/json"}
        }

        self.assertEqual(response, expected_response)

    def test_mocked_httpx_post(self):
        """Test mocked httpx.post method."""
        response = httpx.post("https://api.example.com/users", json={"name": "John"})

        expected_response = {
            "status_code": 201,
            "json": {"message": "Mocked POST response"},
            "text": "Mocked POST response as text",
            "headers": {"Content-Type": "application/json"}
        }

        self.assertEqual(response, expected_response)

    def test_mocked_httpx_put(self):
        """Test mocked httpx.put method."""

        response = httpx.put("https://api.example.com/users/1", json={"name": "Jane"})

        expected_response = {
            "status_code": 200,
            "json": {"message": "Mocked PUT response"},
            "text": "Mocked PUT response as text",
            "headers": {"Content-Type": "application/json"}
        }

        self.assertEqual(response, expected_response)

    def test_mocked_httpx_delete(self):
        """Test mocked httpx.delete method."""
        response = httpx.delete("https://api.example.com/users/1")

        expected_response = {
            "status_code": 204,
            "json": None,
                "text": "Mocked DELETE response",
                "headers": {"Content-Type": "application/json"}
        }

        self.assertEqual(response, expected_response)

    def test_mocked_httpx_async_client_get(self):
        """Test mocked httpx.AsyncClient.get method."""
        if hasattr(httpx, 'AsyncClient'):
            response = httpx.AsyncClient.get("https://api.example.com/async/users")

            expected_response = {
                "status_code": 200,
                "json": {"message": "Mocked async GET response"},
                "text": "Mocked async GET response as text",
                "headers": {"Content-Type": "application/json"}
            }

            self.assertEqual(response, expected_response)
        else:
            self.skipTest("AsyncClient not available in mock")

    def test_mocked_httpx_async_client_post(self):
        """Test mocked httpx.AsyncClient.post method."""
        if hasattr(httpx, 'AsyncClient'):
            response = httpx.AsyncClient.post("https://api.example.com/async/users", json={"name": "Async User"})

            expected_response = {
                "status_code": 201,
                "json": {"message": "Mocked async POST response"},
                "text": "Mocked async POST response as text",
                "headers": {"Content-Type": "application/json"}
            }

            self.assertEqual(response, expected_response)
        else:
            self.skipTest("AsyncClient not available in mock")


suite = unittest.TestSuite()

suite.addTest(TestMockedHTTPXModule('test_mocked_httpx_get'))
suite.addTest(TestMockedHTTPXModule('test_mocked_httpx_post'))
suite.addTest(TestMockedHTTPXModule('test_mocked_httpx_put'))
suite.addTest(TestMockedHTTPXModule('test_mocked_httpx_delete'))
suite.addTest(TestMockedHTTPXModule('test_mocked_httpx_async_client_get'))
suite.addTest(TestMockedHTTPXModule('test_mocked_httpx_async_client_post'))

runner = unittest.TextTestRunner()
runner.run(suite)
