from django.test import TestCase
from .models import BlogPost, Comments
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date


class TestBlogPostModel(TestCase):
    """
    Unit tests for blogpost model
    """
    @classmethod
    def setUpTestData(cls):
        test_user = User.objects.create_user(
            username='testuser', password='testpassword1'
        )
        BlogPost.objects.create(
            created_by=test_user,
            description="This is a test",
            title="This is a test blogpost title",
            body='This is a test blogpost body',
            category='Football',
        )

    def test_description_max_chars(self):
        """
        Tests description max characters is 200
        """
        test_post = BlogPost.objects.get(id=1)
        max_length = test_post._meta.get_field('description').max_length
        self.assertEqual(max_length, 200)

    def test_title_max_chars(self):
        """
        Tests title max characters is 50
        """
        test_post = BlogPost.objects.get(id=1)
        max_length = test_post._meta.get_field('title').max_length
        self.assertEqual(max_length, 50)

    def test_category_choices(self):
        """Tests the category choices"""
        test_post = BlogPost.objects.get(id=1)
        choices = dict(test_post._meta.get_field('category').choices)
        self.assertEqual(choices, {
            'Football': 'Football',
            'GAA': 'GAA',
            'Rugby': 'Rugby',
            'Other': 'Other',
        })

    def test_absolute_url(self):
        """
        Tests the absolute url reverses to home page
        """
        test_post = BlogPost.objects.get(id=1)
        self.assertEqual(test_post.get_absolute_url(), reverse('home'))

    def test__str__(self):
        """
        Tests the string method returns correct data in correct format
        """
        test_post = BlogPost.objects.get(id=1)
        test_string = (
            f"Blog post by {test_post.created_by} on {test_post.date_created}"
        )
        self.assertEqual(str(test_post), test_string)


class TestCommentModel(TestCase):
    """
    Unit Tests for comments model
    """
    def setUp(self):
        """
        Creates valid comment database entry
        """
        # Needed for created_by id non null constraint
        test_user = User.objects.create_user(
            username='testuser2', password='testpassword1'
        )
        self.user = User.objects.create_user(
            username='testuser', password='testpassword')
        # Same blogpost entry as Test Blogpost model used here
        self.blog_post = BlogPost.objects.create(
            created_by=test_user,
            description="This is a test",
            title="This is a test blogpost title",
            body='This is a test blogpost body',
            category='Football',
        )

    def test_comment_is_valid(self):
        """
        Tests that asserted values are valid
        """
        comment = Comments.objects.create(
            post=self.blog_post,
            comment='This is a test comment.',
            user=self.user,
        )
        self.assertEqual(comment.post, self.blog_post)
        self.assertEqual(comment.comment, 'This is a test comment.')
        self.assertEqual(comment.user, self.user)

    def test_comment__str__(self):
        """
        Tests __str__ method returns correct value
        """
        comment = Comments.objects.create(
            post=self.blog_post,
            comment='This is a test comment.',
            user=self.user,
        )
        self.assertEqual(
            str(comment), f"Comment by {self.user} on {comment.time}"
            )
