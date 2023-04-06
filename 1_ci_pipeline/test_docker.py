import unittest
import subprocess

class FlaskAppTests(unittest.TestCase):
    def test_flask_app_runs(self):
        # Run the Flask app container in detached mode
        subprocess.run(["docker", "run", "-d", "-p", "8000:5000", "app"])

        # Check if the Flask app is running by making a request to the endpoint
        response = subprocess.run(["curl", "http://localhost:8000/users"], capture_output=True, text=True)
        self.assertIn("Lara Croft", response.stdout)
        self.assertIn("Mario", response.stdout)
        self.assertIn("Gordon Freeman", response.stdout)

if __name__ == '__main__':
    unittest.main()