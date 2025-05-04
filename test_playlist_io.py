import unittest
import os
import json
from music_playlist_system import PlaylistIO, Playlist, Song, PodcastEpisode

class TestPlaylistIO(unittest.TestCase):
    def setUp(self):
        self.test_filename = "test_playlist.json"
        self.playlist = Playlist("Test IO Playlist")
        self.playlist.add_item(Song("IO Song", "IO Artist", 4.2, "IO Genre"))
        self.playlist.add_item(PodcastEpisode("IO Podcast", "IO Host", 45.0, "IO Topic"))
        
        if os.path.exists(self.test_filename):
            os.remove(self.test_filename)
    
    def tearDown(self):
        if os.path.exists(self.test_filename):
            os.remove(self.test_filename)
    
    def test_export_to_json(self):
        PlaylistIO.export_to_json(self.playlist, self.test_filename)
        
        self.assertTrue(os.path.exists(self.test_filename))
        
        with open(self.test_filename) as f:
            data = json.load(f)
        
        self.assertEqual(data["name"], "Test IO Playlist")
        self.assertEqual(len(data["items"]), 2)
        self.assertEqual(data["items"][0]["title"], "IO Song")
        self.assertEqual(data["items"][1]["title"], "IO Podcast")
    
    def test_import_from_json(self):
        # First export to create test file
        PlaylistIO.export_to_json(self.playlist, self.test_filename)
        
        imported = PlaylistIO.import_from_json(self.test_filename)
        
        self.assertEqual(imported.name, "Test IO Playlist")
        self.assertEqual(len(imported), 2)
        
        # Verify first item is song
        first_item = imported._items[0]
        self.assertIsInstance(first_item, Song)
        self.assertEqual(first_item.title, "IO Song")
        
        # Verify second item is podcast
        second_item = imported._items[1]
        self.assertIsInstance(second_item, PodcastEpisode)
        self.assertEqual(second_item.title, "IO Podcast")
    
    def test_import_nonexistent_file(self):
        with self.assertRaises(FileNotFoundError):
            PlaylistIO.import_from_json("nonexistent_file.json")

if __name__ == "__main__":
    unittest.main()