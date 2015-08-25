import unittest

from quickbooks.objects.customer import Customer


class CustomerTests(unittest.TestCase):
    def test_unicode(self):
        customer = Customer()
        customer.DisplayName = "test"

        self.assertEquals(unicode(customer), "test")

    def test_to_ref(self):
        customer = Customer()
        customer.DisplayName = "test"
        customer.Id  = 100

        ref = customer.to_ref()

        self.assertEquals(ref.name, "test")
        self.assertEquals(ref.type, "Customer")
        self.assertEquals(ref.value, 100)