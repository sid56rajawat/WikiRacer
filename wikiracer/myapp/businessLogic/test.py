import unittest
from getLinks import *

class TestWikipediaLinks(unittest.TestCase):

    def test_make_wikipedia_url(self):
        self.assertEqual(make_wikipedia_url("Python"), "https://en.wikipedia.org/wiki/Python")

    def test_anchors_extractor(self):
        content = b'<html><body><a href="/wiki/Python">Python</a><a href="/wiki/Java">Java</a></body></html>'
        anchors = anchors_extractor(content)
        self.assertEqual(len(anchors), 2)
        self.assertEqual(anchors[0]['href'], '/wiki/Python')
        self.assertEqual(anchors[0].text, 'Python')
        self.assertEqual(anchors[1]['href'], '/wiki/Java')
        self.assertEqual(anchors[1].text, 'Java')

    def test_is_valid_link(self):
        self.assertTrue(is_valid_link('/wiki/Python'))
        self.assertFalse(is_valid_link('/wiki/Python:Language'))
        self.assertFalse(is_valid_link('/wiki/Python#Introduction'))
        self.assertFalse(is_valid_link('https://en.wikipedia.org/wiki/Python'))

    def test_get_links(self):
        link_names = get_link_names("Python")
        self.assertGreater(len(link_names), 0)
        self.assertLessEqual(len(link_names), 100)
        

