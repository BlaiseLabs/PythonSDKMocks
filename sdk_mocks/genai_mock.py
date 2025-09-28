from unittest.mock import patch, Mock
from google import genai

@patch('genai.Client')
def test_gemini_client(mock_client):
    mock_client.return_value = Mock(spec=genai.Client)

@patch("genai.models.generate_content")
def test_gemini_generate_content(mock_generate_content):
    mock_generate_content.return_value = Mock(spec=genai.models.generate_content)
