from nose.tools import eq_
from rest_framework import status
from rest_framework.test import APITestCase


class CurrenciesTestCase(APITestCase):
    def setUp(self):
        self.valid_request_data =  {
            "init_date": "2020-02-02",
            "end_date":"2020-02-10",
            "currency": "SP68257"
        }
        self.invalid_request_data = {
            "init_date": "2020-02-02",
            "end_date":"2020-02-10",
            "currency": "AAAAAAAA,AAAAAAAA,AAAAAAAA,AAAAAAA"
        }

    def test_get_currency_data_ok(self):
        response = self.client.post('/currencies/', self.valid_request_data)
        eq_(response.status_code, status.HTTP_200_OK)

    def test_get_currency_data_invalid(self):
        response = self.client.post('/currencies/', self.invalid_request_data)
        eq_(response.status_code, status.HTTP_400_BAD_REQUEST)

