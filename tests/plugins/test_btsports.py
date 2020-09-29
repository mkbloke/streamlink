import unittest

from streamlink.plugins.btsports import BTSports


class TestPluginBTSports(unittest.TestCase):
    def test_can_handle_url(self):
        should_match = [
            "https://sport.bt.com/btsportsplayer/football-match-1",
            "https://sport.bt.com/ss/Satellite/btsportsplayer/football-match-1",
            "https://bt.com/sport/watch/live-now/bt-sport-1",
            "https://www.bt.com/sport/watch/live-now/bt-sport-1",
            "https://bt.com/sport/watch/live-now/bt-sport-espn",
            "https://www.bt.com/sport/watch/live-now/bt-sport-espn",
            "https://bt.com/sport/watch/video/clips/2020/september/diamond-de-klerk-is-a-hero-for-us",
            "https://www.bt.com/sport/watch/video/clips/2020/september/diamond-de-klerk-is-a-hero-for-us",
            "https://bt.com/sport/watch/video/clips/2020/september/motogp-highlights-grand-prix-of-catalunya",
            "https://www.bt.com/sport/watch/video/clips/2020/september/motogp-highlights-grand-prix-of-catalunya",
        ]
        for url in should_match:
            self.assertTrue(BTSports.can_handle_url(url))

    def test_can_handle_url_negative(self):
        should_not_match = [
            "http://www.bt.com/",
            "http://bt.com/",
            "http://www.tvcatchup.com/",
            "http://www.youtube.com/",
        ]
        for url in should_not_match:
            self.assertFalse(BTSports.can_handle_url(url))
