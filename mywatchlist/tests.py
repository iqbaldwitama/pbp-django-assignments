from django.test import TestCase, Client

# Create your tests here.
class TestViews(TestCase):

    def test_show_html(self):         
        self.client = Client()
        response = self.client.get('/mywatchlist/html/')
        self.assertEqual(response.status_code,200)
    
    def test_show_xml(self):         
        self.client = Client()
        response = self.client.get('/mywatchlist/xml/')
        self.assertEqual(response.status_code,200)
    
    def test_show_json(self):         
        self.client = Client()
        response = self.client.get('/mywatchlist/json/')
        self.assertEqual(response.status_code,200)