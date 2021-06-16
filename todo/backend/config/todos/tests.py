from datetime import timedelta
from django.test import TestCase
from .models import Todo

class TodoModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Todo.objects.create(title='Finish Chapter 2', body='Continue to slowly work through chapter two of the API book while learning new concepts, best practices, etc.')

    def test_title_content(self):
        todo = Todo.objects.get(id=1)
        expected_object_name = f'{todo.title}'
        self.assertEqual(expected_object_name, 'Finish Chapter 2')

    def test_body_content(self):
        todo = Todo.objects.get(id=1)
        expected_object_name = f'{todo.body}'
        self.assertEqual(expected_object_name, 'Continue to slowly work through chapter two of the API book while learning new concepts, best practices, etc.')

    