from datetime import date

from django.test import TestCase
from django.urls import reverse

from .models import Member


class MemberManagementTests(TestCase):
    def setUp(self):
        self.member = Member.objects.create(
            firstname='Jane',
            lastname='Doe',
            phone=1234567890,
            joined_date=date(2024, 1, 1),
        )

    def test_update_member_updates_date_with_form_fields(self):
        response = self.client.post(reverse('home'), {
            'fname': 'Jane',
            'lname': 'Doe',
            'phone_num': '9998887777',
            'joined_date': '2025-05-05',
            'action': 'update',
        })

        self.assertEqual(response.status_code, 302)
        self.member.refresh_from_db()
        self.assertEqual(self.member.phone, 9998887777)
        self.assertEqual(self.member.joined_date, date(2025, 5, 5))

    def test_delete_member_removes_member_by_name(self):
        response = self.client.post(reverse('home'), {
            'fname': 'Jane',
            'lname': 'Doe',
            'action': 'delete',
        })

        self.assertEqual(response.status_code, 302)
        self.assertFalse(Member.objects.filter(id=self.member.id).exists())
