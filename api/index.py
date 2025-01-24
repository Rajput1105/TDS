# api/index.py
import json
from urllib.parse import parse_qs, urlparse
from http.server import BaseHTTPRequestHandler

# Load student marks from file
with open("q-vercel-python.json", "r") as file:
    student_data = json.load(file)

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Parse query parameters
        query_params = parse_qs(urlparse(self.path).query)
        names = query_params.get("name", [])  # Extract name parameters

        # Fetch marks for requested names
        response_data = {name: next((s["marks"] for s in student_data if s["name"] == name), None) for name in names}

        # Send response
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(response_data).encode('utf-8'))
