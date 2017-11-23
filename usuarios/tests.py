from django.test import TestCase



class TestHeadLess(TestCase):

	def test_suma(self):
		self.assertEquals( 1 + 1, 2)
