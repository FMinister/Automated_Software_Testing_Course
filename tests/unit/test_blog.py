from unittest import TestCase
from blog import Blog


class BlogTest(TestCase):
    def test_create_blog(self):
        blog = Blog("Test", "Test Author")

        self.assertEqual("Test", blog.title)
        self.assertEqual("Test Author", blog.author)
        self.assertListEqual([], blog.posts)

    def test_repr(self):
        blog_1 = Blog("Test", "Test Author")
        blog_2 = Blog("My Day", "Rolf")

        self.assertEqual(blog_1.__repr__(), "Test by Test Author (0 posts)")
        self.assertEqual(blog_2.__repr__(), "My Day by Rolf (0 posts)")

    def test_repr_multiple_posts(self):
        blog_1 = Blog("Test", "Test Author")
        blog_1.posts = ["Test"]
        blog_2 = Blog("My Day", "Rolf")
        blog_2.posts = ["test", "another"]

        self.assertEqual(blog_1.__repr__(), "Test by Test Author (1 post)")
        self.assertEqual(blog_2.__repr__(), "My Day by Rolf (2 posts)")
