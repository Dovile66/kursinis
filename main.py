# music_playlist_system.py
import json
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List, Dict, Optional


# Abstraction and Inheritance
class MusicItem(ABC):
    """Abstract base class for all music items"""
    @abstractmethod
    def display(self) -> str:
        pass


@dataclass
class Song(MusicItem):
    """Concrete class representing a song"""
    title: str
    artist: str
    duration: float  # in minutes
    genre: str

    def display(self) -> str:
        return f"{self.title} by {self.artist} ({self.duration} min) - {self.genre}"


# Polymorphism
@dataclass
class PodcastEpisode(MusicItem):
    """Concrete class representing a podcast episode"""
    title: str
    host: str
    duration: float  # in minutes
    topic: str

    def display(self) -> str:
        return f"{self.title} hosted by {self.host} ({self.duration} min) - {self.topic}"


# Composition
class Playlist:
    """Playlist class that composes MusicItem objects"""
    def __init__(self, name: str):
        self.name = name
        self._items: List[MusicItem] = []

    def add_item(self, item: MusicItem) -> None:
        """Add a music item to the playlist"""
        self._items.append(item)

    def remove_item(self, index: int) -> None:
        """Remove a music item by index"""
        if 0 <= index < len(self._items):
            self._items.pop(index)

    def display(self) -> None:
        """Display all items in the playlist"""
        print(f"\nPlaylist: {self.name}")
        print("-" * 40)
        for i, item in enumerate(self._items, 1):
            print(f"{i}. {item.display()}")
        print(f"Total duration: {self.total_duration():.2f} minutes\n")

    def total_duration(self) -> float:
        """Calculate total duration of playlist"""
        return sum(item.duration for item in self._items)

    def __len__(self) -> int:
        return len(self._items)


# Singleton Pattern
class PlaylistManager:
    """Singleton class to manage all playlists"""
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._playlists: Dict[str, Playlist] = {}
        return cls._instance

    def create_playlist(self, name: str) -> Playlist:
        """Create a new playlist"""
        if name in self._playlists:
            raise ValueError("Playlist with this name already exists")
        self._playlists[name] = Playlist(name)
        return self._playlists[name]

    def get_playlist(self, name: str) -> Optional[Playlist]:
        """Get an existing playlist by name"""
        return self._playlists.get(name)

    def delete_playlist(self, name: str) -> None:
        """Delete a playlist by name"""
        if name in self._playlists:
            del self._playlists[name]

    def list_playlists(self) -> List[str]:
        """List all playlist names"""
        return list(self._playlists.keys())


# File I/O Operations
class PlaylistIO:
    """Handles importing and exporting playlists to JSON files"""
    @staticmethod
    def export_to_json(playlist: Playlist, filename: str) -> None:
        """Export playlist to JSON file"""
        data = {
            "name": playlist.name,
            "items": [
                {
                    "type": "song" if isinstance(item, Song) else "podcast",
                    "title": item.title,
                    "artist_or_host": item.artist if isinstance(item, Song) else item.host,
                    "duration": item.duration,
                    "genre_or_topic": item.genre if isinstance(item, Song) else item.topic
                }
                for item in playlist._items
            ]
        }
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)

    @staticmethod
    def import_from_json(filename: str) -> Playlist:
        """Import playlist from JSON file"""
        with open(filename) as f:
            data = json.load(f)
        
        playlist = Playlist(data["name"])
        for item_data in data["items"]:
            if item_data["type"] == "song":
                item = Song(
                    title=item_data["title"],
                    artist=item_data["artist_or_host"],
                    duration=item_data["duration"],
                    genre=item_data["genre_or_topic"]
                )
            else:
                item = PodcastEpisode(
                    title=item_data["title"],
                    host=item_data["artist_or_host"],
                    duration=item_data["duration"],
                    topic=item_data["genre_or_topic"]
                )
            playlist.add_item(item)
        return playlist


if __name__ == "__main__":
    # Demo usage
    manager = PlaylistManager()
    
    # Create playlists
    rock_playlist = manager.create_playlist("Rock Classics")
    podcast_playlist = manager.create_playlist("Tech Podcasts")
    
    # Add songs
    rock_playlist.add_item(Song("Bohemian Rhapsody", "Queen", 5.92, "Rock"))
    rock_playlist.add_item(Song("Stairway to Heaven", "Led Zeppelin", 8.02, "Rock"))
    
    # Add podcasts
    podcast_playlist.add_item(PodcastEpisode("AI Today", "Lex Fridman", 120.0, "Artificial Intelligence"))
    podcast_playlist.add_item(PodcastEpisode("Future of Tech", "Joe Rogan", 90.5, "Technology"))
    
    # Display playlists
    rock_playlist.display()
    podcast_playlist.display()
    
    # Export one playlist
    PlaylistIO.export_to_json(rock_playlist, "rock_classics.json")