from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from .models import Conversation, Message
from rest_framework.test import APITestCase

class ConversationAPITestCase(APITestCase):
    def setUp(self) -> None:
        self.user = User.objects.create_user(username='testuser', email='test1@gmail.com', password='123')
        self.conversation = Conversation.objects.create(user=self.user, )
        self.conversation_second = Conversation.objects.create(user=self.user, )
        self.conversation_third = Conversation.objects.create(user=self.user, )
        self.conversation_forth = Conversation.objects.create(user=self.user, )
        self.conversation_fifth = Conversation.objects.create(user=self.user, )
        self.url = reverse('get_conversation', kwargs={'id': self.conversation.id})

    def test_get_conversation(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['id'], self.conversation.id)
        self.assertEqual(response.data['user'], self.conversation.user.id)

    def test_list_conversation(self):
        response = self.client.get(reverse('list_conversation'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 5)
        self.assertEqual(len(response.data['results']), 1)

    def test_pagination_list_conversation(self):
        response_first_page = self.client.get(reverse('list_conversation'))
        response_second_page = self.client.get(reverse('list_conversation'), {'page': 2})
        # response_second_page = self.client.get(reverse(response_first_page.data['next']))
        self.assertEqual(response_first_page.status_code, status.HTTP_200_OK)
        self.assertEqual(response_second_page.status_code, status.HTTP_200_OK)

        self.assertEqual(len(response_first_page.data['results']), 1)
        self.assertEqual(len(response_second_page.data['results']), 1)

        self.assertEqual(response_first_page.data['previous'], None)
        self.assertNotEqual(response_first_page.data['next'], None)
        self.assertNotEqual(response_second_page.data['next'], None)

        self.assertNotEqual(
            response_first_page.data['results'][0]['id'],
            response_second_page.data['results'][0]['id']
        )

    def test_get_conversation_not_exist(self):
        response = self.client.get(reverse('get_conversation', kwargs={'id': 1000}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data, "conversation not exist")


