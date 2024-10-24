import json
from unittest.mock import patch

# MockManager class to manage loading and applying mocks from JSON data
class MockManager:
    def __init__(self, json_file=None):
        self.mocks = {}
        self.patches = []
        if json_file:
            self.load_from_json(json_file)

    def load_from_json(self, json_file):
        """Load mock configuration from a JSON file."""
        with open(json_file, 'r') as file:
            self.mocks = json.load(file)

    def apply_mocks(self):
        """Apply mocks based on the configuration."""
        for module_name, module_details in self.mocks.get("mocked_modules", {}).items():
            for method_name, method_data in module_details["methods"].items():
                self.apply_specific_mock(module_name, method_name, method_data)

    def apply_specific_mock(self, module_name, method, mock_data):
        """Helper function to apply mock for specific methods."""
        def mock_response(*args, **kwargs):
            return mock_data["return_value"]

        # Patch the method in the target module (e.g., os)
        p = patch(f"{module_name}.{method}", new=mock_response)
        p.start()
        self.patches.append(p)

    def stop_mocks(self):
        """Stop all active patches."""
        for p in self.patches:
            p.stop()
