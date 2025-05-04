import unittest
from music_playlist_system import PlaylistManager, Playlist

class TestPlaylistManager(unittest.TestCase):
    def setUp(self):
        # Clear any existing state
        self.manager = PlaylistManager()
        for playlist in self.manager.list_playlists():
            self.manager.delete_playlist(playlist)
    
    def test_singleton_pattern(self):
        manager2 = PlaylistManager()
        self.assertIs(self.manager, manager2)
    
    def test_create_playlist(self):
        playlist = self.manager.create_playlist("New Playlist")
        self.assertEqual(playlist.name, "New Playlist")
        self.assertIsNotNone(self.manager.get_playlist("New Playlist"))
    
    def test_create_duplicate_playlist(self):
        self.manager.create_playlist("Unique Playlist")
        with self.assertRaises(ValueError):
            self.manager.create_playlist("Unique Playlist")
    
    def test_get_playlist(self):
        self.manager.create_playlist("Test Get")
        playlist = self.manager.get_playlist("Test Get")
        self.assertIsInstance(playlist, Playlist)
        self.assertEqual(playlist.name, "Test Get")
    
    def test_get_nonexistent_playlist(self):
        self.assertIsNone(self.manager.get_playlist("Nonexistent"))
    
    def test_delete_playlist(self):
        self.manager.create_playlist("To Delete")
        self.manager.delete_playlist("To Delete")
        self.assertIsNone(self.manager.get_playlist("To Delete"))
    
    def test_list_playlists(self):
        self.manager.create_playlist("List Test 1")
        self.manager.create_playlist("List Test 2")
        playlists = self.manager.list_playlists()
        self.assertEqual(len(playlists), 2)
        self.assertIn("List Test 1", playlists)
        self.assertIn("List Test 2", playlists)

if __name__ == "__main__":
    unittest.main()