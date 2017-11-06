# coding=utf-8
from rest_framework.test import APITestCase
from rest_framework.reverse import reverse
from rest_framework import status
from django_dynamic_fixture import G

from .models import Company


class CasesApi(APITestCase):
    def test_company_list(self):
        company1 = G(Company)
        data = self.client.get(reverse('company-list')).data['results']
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]['id'], company1.id)
        self.assertEqual(data[0]['name'], company1.name)
        self.assertEqual(data[0]['email'], company1.email)
        self.assertEqual(data[0]['address'], company1.address)
        G(Company)
        data = self.client.get(reverse('company-list')).data['results']
        self.assertEqual(len(data), 2)

    def test_create_company(self):
        data = {
            'name': 'Company 1',
            'email': 'aaa@aaa.com',
            'phone': '+79995555555',
            'address': 'asd asd'
        }
        resp = self.client.post(reverse('company-list'), data, format='json')
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)
        company1 = Company.objects.get()
        self.assertEqual(company1.name, data['name'])
        self.assertEqual(company1.email, data['email'])
        self.assertEqual(company1.phone, data['phone'])
        self.assertEqual(company1.address, data['address'])

    def test_change_company(self):
        company1 = G(Company)
        data = {
            'name': 'Company 1',
            'email': 'aaa@aaa.com',
            'phone': '+79995555555',
            'address': 'asd asd'
        }
        resp = self.client.put(reverse('company-detail', kwargs={'pk': company1.pk}), data, format='json')
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        company1.refresh_from_db()
        self.assertEqual(company1.name, data['name'])
        self.assertEqual(company1.email, data['email'])
        self.assertEqual(company1.phone, data['phone'])
        self.assertEqual(company1.address, data['address'])
