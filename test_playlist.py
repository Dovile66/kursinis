import unittest
from music_playlist_system import Playlist, Song, PodcastEpisode

class TestPlaylist(unittest.TestCase):
    def setUp(self):
        self.playlist = Playlist("Test Playlist")
        self.song = Song("Test Song", "Test Artist", 3.5, "Test Genre")
        self.podcast = PodcastEpisode("Test Podcast", "Test Host", 60.0, "Test Topic")
    
    def test_initial_state(self):
        self.assertEqual(self.playlist.name, "Test Playlist")
        self.assertEqual(len(self.playlist), 0)
    
    def test_add_items(self):
        self.playlist.add_item(self.song)
        self.assertEqual(len(self.playlist), 1)
        
        self.playlist.add_item(self.podcast)
        self.assertEqual(len(self.playlist), 2)
    
    def test_remove_items(self):
        self.playlist.add_item(self.song)
        self.playlist.add_item(self.podcast)
        
        self.playlist.remove_item(0)
        self.assertEqual(len(self.playlist), 1)
        
        self.playlist.remove_item(0)
        self.assertEqual(len(self.playlist), 0)
    
    def test_remove_invalid_index(self):
        with self.assertRaises(IndexError):
            self.playlist.remove_item(0)  # Empty playlist
        
        self.playlist.add_item(self.song)
        with self.assertRaises(IndexError):
            self.playlist.remove_item(1)  # Index out of range
    
    def test_total_duration(self):
        self.playlist.add_item(self.song)
        self.playlist.add_item(self.podcast)
        expected = 3.5 + 60.0
        self.assertAlmostEqual(self.playlist.total_duration(), expected)
    
    def test_display_method(self):
        # This mainly tests that display doesn't crash
        self.playlist.add_item(self.song)
        self.playlist.display()  # Just verify no exceptions

if __name__ == "__main__":
    unittest.main()