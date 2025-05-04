import unittest
from music_playlist_system import Song, PodcastEpisode

class TestSong(unittest.TestCase):
    def setUp(self):
        self.song = Song("Bohemian Rhapsody", "Queen", 5.92, "Rock")
    
    def test_song_creation(self):
        self.assertEqual(self.song.title, "Bohemian Rhapsody")
        self.assertEqual(self.song.artist, "Queen")
        self.assertAlmostEqual(self.song.duration, 5.92)
        self.assertEqual(self.song.genre, "Rock")
    
    def test_song_display(self):
        expected = "Bohemian Rhapsody by Queen (5.92 min) - Rock"
        self.assertEqual(self.song.display(), expected)

class TestPodcastEpisode(unittest.TestCase):
    def setUp(self):
        self.podcast = PodcastEpisode("AI Today", "Lex Fridman", 120.0, "Artificial Intelligence")
    
    def test_podcast_creation(self):
        self.assertEqual(self.podcast.title, "AI Today")
        self.assertEqual(self.podcast.host, "Lex Fridman")
        self.assertAlmostEqual(self.podcast.duration, 120.0)
        self.assertEqual(self.podcast.topic, "Artificial Intelligence")
    
    def test_podcast_display(self):
        expected = "AI Today hosted by Lex Fridman (120.0 min) - Artificial Intelligence"
        self.assertEqual(self.podcast.display(), expected)

if __name__ == "__main__":
    unittest.main()