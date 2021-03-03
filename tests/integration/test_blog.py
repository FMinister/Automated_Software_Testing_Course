from unittest import TestCase
from blog import Blog


class BlogTest(TestCase):
    def test_create_post_in_blog(self):
        blog_1 = Blog("Test", "Test Author")
        blog_1.create_post("Test Title", "Test Content")

        self.assertEqual(len(blog_1.posts), 1)
        self.assertEqual(blog_1.posts[0].title, "Test Title")
        self.assertEqual(blog_1.posts[0].content, "Test Content")

    def test_json_no_posts(self):
        blog_1 = Blog("Test", "Test Author")

        expected = {"title": "Test", "author": "Test Author", "posts": []}

        self.assertDictEqual(expected, blog_1.json())

    def test_json(self):
        blog_1 = Blog("Test", "Test Author")
        blog_1.create_post("Test Title", "Test Content")

        expected = {
            "title": "Test",
            "author": "Test Author",
            "posts": [{"title": "Test Title", "content": "Test Content"}],
        }

        self.assertDictEqual(expected, blog_1.json())
