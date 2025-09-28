from unittest.mock import Mock, patch

from google import genai


@patch("genai.Client")
def mock_gemini_client(mock_client):
    mock_client.return_value = Mock(spec=genai.Client)


@patch("genai.Client.models.generate_content")
def mock_gemini_generate_content(mock_generate_content):
    mock_generate_content.return_value = Mock(spec=genai.Client.models.generate_content)
