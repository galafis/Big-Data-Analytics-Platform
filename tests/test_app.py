'''
Unit tests for the Big-Data-Analytics-Platform Flask application.
Author: Gabriel Demetrios Lafis
'''

import unittest
import json
import os
import sys

# Add the project root to the Python path to allow for module imports
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.app import app

class TestApp(unittest.TestCase):

    def setUp(self):
        """Set up the test client and other test variables."""
        self.app = app.test_client()
        self.app.testing = True

    def test_index_route(self):
        """Test the main index route, which should return the web interface."""
        response = self.app.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Big Data Analytics Platform", response.data)
        self.assertIn(b"Welcome to the Platform", response.data)

    def test_status_route(self):
        """Test the API status endpoint."""
        response = self.app.get("/api/status")
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data.decode("utf-8"))
        self.assertEqual(data["status"], "running")
        self.assertEqual(data["version"], "1.0.0")
        self.assertTrue("timestamp" in data)

    def test_process_data_route_success(self):
        """Test the data processing endpoint with valid data."""
        test_data = {"key": "value", "id": 123}
        response = self.app.post("/api/process",
                                 data=json.dumps(test_data),
                                 content_type="application/json")
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data.decode("utf-8"))
        self.assertEqual(data["status"], "success")
        self.assertEqual(data["received_data"], test_data)

    def test_process_data_route_no_data(self):
        """Test the data processing endpoint with no data."""
        response = self.app.post("/api/process",
                                 content_type="application/json")
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data.decode("utf-8"))
        self.assertEqual(data["error"], "No data provided")

    def test_analytics_route(self):
        """Test the analytics endpoint, which runs an R script."""
        response = self.app.get("/api/analytics")
        # This test's success depends on whether R is installed in the environment.
        # We will check for either a success (200) or a server error (500).
        self.assertIn(response.status_code, [200, 500])
        data = json.loads(response.data.decode("utf-8"))
        if response.status_code == 200:
            self.assertEqual(data["status"], "success")
            self.assertIsInstance(data["analytics_output"], list)
            self.assertIn("Analytics Report:", data["analytics_output"][0])
        else:
            self.assertEqual(data["status"], "error")
            self.assertIn(data["message"], ["R script failed", "R analytics script not found"])

    def test_upload_route_no_file(self):
        """Test the file upload endpoint without a file."""
        response = self.app.post("/api/upload")
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data.decode("utf-8"))
        self.assertEqual(data["error"], "No file part")

if __name__ == "__main__":
    unittest.main()

