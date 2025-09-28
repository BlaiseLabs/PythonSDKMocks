import unittest
from unittest.mock import MagicMock, patch

from google import genai

from sdk_mocks import MockManager

mock_file_path = "./mocks/genai_mock_data.json"  # Update to the correct file path


class TestMockedGenaiModule(unittest.TestCase):
    def setUp(self):
        """Load the mock configuration before running the tests."""
        self.mock_manager = MockManager(mock_file_path)
        self.mock_manager.apply_mocks()

    def tearDown(self):
        """Stop all mocks after the tests."""
        if self.mock_manager:
            self.mock_manager.stop_mocks()

    def test_mocked_client(self):
        """Test mocked google.genai.Client method."""

        # Call the mocked client
        result = genai.Client("test-api-key")

        # Verify the mock return value
        expected_response = self.mock_manager.mocks["mocked_modules"]["google.genai"]["methods"]["Client"]["return_value"]
        self.assertEqual(result, expected_response)

    def test_mocked_generate_content(self):
        """Test mocked google.genai Client.models.generate_content method."""

        # Patch the Client class independently from MockManager
        with patch("google.genai.Client") as mock_client_class:
            # Create a mock client instance
            mock_client_instance = MagicMock()
            mock_client_class.return_value = mock_client_instance

            # Set up the models.generate_content method chain
            expected_response = self.mock_manager.mocks["mocked_modules"]["google.genai"]["methods"]["Client"]["models"]["generate_content"]["return_value"]
            mock_client_instance.models.generate_content.return_value = expected_response

            # Create client and call generate_content
            client = genai.Client("test-api-key")
            result = client.models.generate_content(
                model="gemini-test-model", contents="test-prompt"
            )

            # Verify the mock return value
            self.assertIn("text", result)
            self.assertEqual(result["text"], expected_response["text"])

            # Verify that the method was called with correct arguments
            mock_client_instance.models.generate_content.assert_called_once_with(
                model="gemini-test-model", contents="test-prompt"
            )


# Running the updated tests
suite = unittest.TestSuite()
suite.addTest(TestMockedGenaiModule("test_mocked_client"))
suite.addTest(TestMockedGenaiModule("test_mocked_generate_content"))

runner = unittest.TextTestRunner()
runner.run(suite)
