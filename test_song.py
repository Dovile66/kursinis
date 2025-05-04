import unittest
from main import Song

class TestSong(unittest.TestCase):
    def test_create_song(self):
        song = Song("Bohemian Rhapsody", "Queen", "5:55")
        self.assertEqual(song.get_title(), "Bohemian Rhapsody")
        self.assertEqual(song.get_artist(), "Queen")
        self.assertEqual(song.get_duration(), "5:55")
        with self.assertRaises(ValueError):
            Song("", "Queen", "5:55")
        with self.assertRaises(ValueError):
            Song("Bohemian Rhapsody", "", "5:55")
        with self.assertRaises(ValueError):
            Song("Bohemian Rhapsody", "Queen", "")

    def test_song_equality(self):
        song1 = Song("Bohemian Rhapsody", "Queen", "5:55")
        song2 = Song("Bohemian Rhapsody", "Queen", "5:55")
        song3 = Song("Stairway to Heaven", "Led Zeppelin", "8:00")
        self.assertEqual(song1, song2)
        self.assertNotEqual(song1, song3)
        self.assertNotEqual(song1, "not a song")

    def test_song_string_representation(self):
        song = Song("Bohemian Rhapsody", "Queen", "5:55")
        self.assertEqual(str(song), "Bohemian Rhapsody - Queen (5:55)")

if __name__ == '__main__':
    unittest.main()