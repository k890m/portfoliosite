# # tests/test_app.py

# import unittest
# import os
# os.environ['TESTING'] = 'true'

# from app import app

# class AppTestCase(unittest.TestCase):
#     def setUp(self):
#         self.client = app.test_client()

#     def test_home(self):
#         response = self.client.get("/")
#         assert response.status_code == 200
#         html = response.get_data(as_text=True)
#         assert "<title>MLH Fellow</title>" in html
#         # TODO Add more tests relating to the home page

#     def test_timeline(self):
#         response = self.client.get("/api/timeline_post")
#         assert response.status_code == 200
#         assert response.is_json
#         json = response.get_json()
#         assert "timeline_posts" in json
#         assert len(json["timeline_posts"]) == 0
#         # TODO Add more tests relating to the /api/timeline_post GET and POST apis
#         # TODO Add more tests relating to the timeline page

# # def test_malformed_timeline_post(self):
# #     # POST request missing name
# #     response = self.client.post("/api/timeline_post", data={"email": "john@example.com", "content": "Hello world, I'm John!"})
# #     assert response.status_code == 400
# #     html = response.get_data(as_text=True)
# #     assert "Invalid name" in html

# #     # POST request with empty content
# #     response = self.client.post("/api/timeline_post", data={"name": "John Doe", "email": "john@example.com", "content": ""})
# #     assert response.status_code == 400
# #     html = response.get_data(as_text=True)
# #     assert "Invalid content" in html

# #     # POST request with malformed email
# #     response = self.client.post("/api/timeline_post", data={"name": "John Doe", "email": "not-an-email", "content": "Hello world, I'm John!"})
# #     assert response.status_code == 400
# #     html = response.get_data(as_text=True)
# #     assert "Invalid email" in html

# # tests/test_app.py
# tests/test_app.py

import unittest
import os
os.environ['TESTING'] = 'true'

from app import app

class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_home(self):
        response = self.client.get("/")
        assert response.status_code == 200
        html = response.get_data(as_text=True)
        assert "<title>MLH Fellow</title>" in html
        # Additional tests for the home page
        assert "Welcome to the MLH Fellow program" in html
        assert "<h1>Home Page</h1>" in html

    def test_timeline(self):
        response = self.client.get("/api/timeline_post")
        assert response.status_code == 200
        assert response.is_json
        json = response.get_json()
        print(json)  # Debug statement
        assert "timeline_posts" in json
        assert len(json["timeline_posts"]) == 0
        # Additional tests for the timeline page
        response = self.client.post("/api/timeline_post", data={"name": "Alice", "email": "alice@example.com", "content": "This is a test post."})
        assert response.status_code == 200
        json = response.get_json()
        print(json)  # Debug statement
        assert "timeline_posts" in json
        assert len(json["timeline_posts"]) == 1
        assert json["timeline_posts"][0]["name"] == "Alice"
        assert json["timeline_posts"][0]["email"] == "alice@example.com"
        assert json["timeline_posts"][0]["content"] == "This is a test post."

    def test_malformed_timeline_post(self):
        # POST request missing name
        response = self.client.post("/api/timeline_post", data={"email": "john@example.com", "content": "Hello world, I'm John!"})
        assert response.status_code == 400
        html = response.get_data(as_text=True)
        assert "Invalid name" in html

        # POST request with empty content
        response = self.client.post("/api/timeline_post", data={"name": "John Doe", "email": "john@example.com", "content": ""})
        assert response.status_code == 400
        html = response.get_data(as_text=True)
        assert "Invalid content" in html

        # POST request with malformed email
        response = self.client.post("/api/timeline_post", data={"name": "John Doe", "email": "not-an-email", "content": "Hello world, I'm John!"})
        assert response.status_code == 400
        html = response.get_data(as_text=True)
        assert "Invalid email" in html

if __name__ == '__main__':
    unittest.main()
