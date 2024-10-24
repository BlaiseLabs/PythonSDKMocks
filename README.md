# Python SDK Mocks

Welcome to the **Python SDK Mocks** project! This library provides pre-built mock implementations of popular SDKs to help developers streamline testing workflows. The project is part of Hacktoberfest and welcomes contributions from the community!

## Features

- Pre-configured mock data for popular python SDKs (coming soon).
- Easy-to-use interface for loading mocks from JSON files.
- Mock common SDK methods for integration testing.
- Apply and remove mocks dynamically during test execution.

## How It Works

The project uses a `MockManager` class to handle loading and applying mocks. Mocks are defined in JSON files, specifying the module, method, and return values, along with method signatures. You can load these mocks into your test suite to simulate the behavior of SDK calls.

### Example of a Mock Configuration

For example, this mock file (`os_mock_data.json`) can be used to mock common file system methods from the `os` module:

```json
{
  "mocked_modules": {
    "os": {
      "methods": {
        "listdir": {
          "return_value": ["file1.txt", "file2.txt", "folder1"],
          "signature": ["path"]
        },
        "remove": {
          "return_value": null,
          "signature": ["path"]
        }
      }
    }
  }
}
```

### Example Usage

You can use the `MockManager` to apply these mocks in your tests:

```python
from MockManager import MockManager

class TestFileSystem(unittest.TestCase):
    def setUp(self):
        self.mock_manager = MockManager('./mocks/os_mock_data.json')
        self.mock_manager.apply_mocks()

    def tearDown(self):
        self.mock_manager.stop_mocks()

    def test_listdir(self):
        files = os.listdir('/')
        self.assertEqual(files, ["file1.txt", "file2.txt", "folder1"])
```

## Future Mocks

We plan to expand the library to support a wide variety of SDKs. Here are some SDKs that are currently being considered for future mocks:

- **AWS SDK (boto3)**: Mock common services like S3, DynamoDB, and Lambda.
- **Google Cloud SDK**: Mock services like Cloud Storage, Pub/Sub, and Firestore.
- **Firebase SDK**: Mock Firebase Authentication, Firestore, and Cloud Functions.
- **Twilio SDK**: Mock messaging and voice API calls.
- **Stripe SDK**: Mock payments, subscriptions, and webhooks.
- **Slack SDK**: Mock API calls for chatbots and integrations.

If you'd like to contribute mocks for these or other SDKs, feel free to submit a pull request!

## Getting Started

### Prerequisites

- Python 3.x
- `unittest` for running tests

### Installation

Clone the repository:

```bash
git clone https://github.com/your-username/python-sdk-mocks.git
cd python-sdk-mocks
```

### Running Tests

You can run the tests using `unittest`:

```bash
python -m unittest discover -s tests
```

## Contributing

We welcome contributions to this project, especially during Hacktoberfest! Here are some ideas for contributions:

- Add new mock configurations for other SDKs.
- Improve existing mocks with additional method coverage.
- Write tests for new mock data.
- Add documentation for mock usage.

To contribute, please fork the repository, create a new branch, and submit a pull request. For more information, check out our [contributing guidelines](CONTRIBUTING.md).

### Contribution Guidelines

- Keep your contributions focused and concise.
- Ensure that all new mocks have corresponding test cases.
- Follow the Python [PEP 8](https://www.python.org/dev/peps/pep-0008/) coding style.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.