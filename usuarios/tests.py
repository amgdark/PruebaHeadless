from django.test import TestCase


class TestUsuario(TestCase):
	def test_suma(self):
		import time
		time.sleep(5)
		self.assertEquals(1 + 1, 2)
