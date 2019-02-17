from django.test import TestCase
from eventex.subscriptions.admin import SubscritionModelAdmin, Subscription, admin
from unittest.mock import Mock


class SubscriptionModelAdminTest(TestCase):
    def setUp(self):
        Subscription.objects.create(name='Henrique Bastos',
                                    cpf='12345678901',
                                    email='henrique@bastos.net',
                                    phone='21-996186180')
        self.model_admin = SubscritionModelAdmin(Subscription, admin.site)

    def test_has_action(self):
        """Action mark_as_paid should be installed"""
        self.assertIn('mark_as_paid', self.model_admin.actions)

    def test_mark_all(self):
        """It should mark all selected subscriptions as paid"""
        self.call_actions()
        self.assertEqual(1, Subscription.objects.filter(paid=True).count())


    def test_message(self):
        """It should send a message to the user"""
        mock = self.call_actions()
        mock.assert_called_once_with(None, '1 inscrição foi marcada como paga.')

    def call_actions(self):
        queryset = Subscription.objects.all()

        mock = Mock()
        old_message_user = SubscritionModelAdmin.message_user
        SubscritionModelAdmin.message_user = mock

        self.model_admin.mark_as_paid(None, queryset)

        SubscritionModelAdmin.message_user = old_message_user

        return mock
