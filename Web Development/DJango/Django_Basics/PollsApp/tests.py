from django.test import TestCase
from .models import Question
from django.utils import timezone
from django.shortcuts import reverse
import datetime

# Create your tests here.
class PublicationTests(TestCase):
    def test_question_was_published_recently(self):
        """
          this test if the was_created_recently method will return False when tested with past Questions
        """
        present_date = timezone.now()
        recent_question = Question(question = "test", created_at=present_date)
        self.assertIs(recent_question.was_created_recently(), True)
    
    def test_question_was_published_in_future(self):
        """
        this checks if the was_created_recently method will return True or False if it was given dates that are in the future
        """
        future_date = timezone.now() + datetime.timedelta(days=1)
        future_question = Question(created_at = future_date)
        self.assertIs(future_question.was_created_recently(), False)
    
    def test_question_was_published_in_the_past(self):
        """
        this test if the was_created_recently method will return False when tested with past Questions
        """
        past_date = timezone.now() - datetime.timedelta(days=1, seconds=1)
        past_question = Question(question="test", created_at=past_date)
        self.assertIs(past_question.was_created_recently(), False)

def create_question(question_text, days):
    """ 
    this function creates data inside our test table
    """
    date = timezone.now() + datetime.timedelta(days=days)
    Question.objects.create(question=question_text, created_at=date)
    

# Creating Tests for our Views
class ViewTests(TestCase):
    def test_no_question(self):
        """
        this checks if the questions are returned when probed for questions
        """
        response = self.client.get("/polls/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls are available")
        self.assertQuerySetEqual(response.context["question_list"], [])

    
    def test_past_question(self):
        """
        This method tests if the view returns questions that are published in the past 
        """
        create_question("test question", -30)
        response = self.client.get("/polls/")
        self.assertEqual(response.status_code, 200)
        self.assertQuerySetEqual(response.context['question_list'], ["<Question: test question>"])
        
