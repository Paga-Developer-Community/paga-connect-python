import os
import json
from unittest import TestCase

from paga_connect_client.paga_connect_client_core import PagaConnectCore


class TestPagaConnect(TestCase):

    def setUp(self):
        super(TestPagaConnect, self).setUp()
        self.scope = 'USER_DEPOSIT_FROM_CARD+MERCHANT_PAYMENT+USER_DETAILS_REQUEST'
        self.redirect_uri = 'http://localhost:9000/video/pagaconnect'
        self.user_data = 'FIRST_NAME+LAST_NAME+USERNAME+EMAIL+ACCOUNT_BALANCE'
        self.pagaConnect = PagaConnectCore('A3878DC1-F07D-48E7-AA59-8276C3C26647', 'Password1', True)
        self.authorization_code = 'VKSd11'

    def test_get_access_code(self):
        response = self.pagaConnect\
            .get_access_token(self.authorization_code,
                              self.redirect_uri, self.scope,
                              self.user_data)
        print(response)

        token_data = json.loads(response)
        access_token = token_data['access_token']
        print(access_token)

        self.assertIsNotNone(response, True)

    def test_make_payment(self):
        response = self.pagaConnect\
            .make_payment('9a7a753e-02dc-4c2b-b10f-1e358135ceac',
                          11, 200.0, 15, "xowqz", "NGN")

        print(response)

        self.assertIsNotNone(response, True)

    def test_money_transfer(self):
        response = self.pagaConnect.money_transfer('9a7a753e-02dc-4c2b-b10f-1e358135ceac',
                                                   'wee589926', 150.0, True, '08060075922')

        print(response)

        self.assertIsNotNone(response, True)

    def test_user_detail(self):
         response = self.pagaConnect.get_user_details('9a7a753e-02dc-4c2b-b10f-1e358135ceac')

         print(response)

         self.assertIsNotNone(response, True)



