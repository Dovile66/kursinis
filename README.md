# Music Streaming Playlist System Report

## 1. Introduction

### a. What is your application?

This application is a Python-based Music Streaming Playlist System. It allows users to manage their music by creating playlists, adding songs, and organizing them. The system is designed with an object-oriented approach, making it extensible and maintainable. It includes features for handling users, songs, and playlists, and also provides functionality for importing and exporting playlist data from/to CSV files.

### b. How to run the program?

1.  **Prerequisites:**
    * Python 3.x installed.
    * (Optional) A virtual environment manager like `venv` is recommended to isolate project dependencies.

2.  **Installation:**
    * No specific installation steps are needed as the application is a collection of Python files.  Ensure that all files (`main.py`, `test_song.py`, `test_playlist.py`, `test_user.py`, `test_file_handling.py`, and `song_list.txt`) are in the same directory.

3.  **Running the program:**
    * Open a terminal or command prompt.
    * Navigate to the directory containing the Python files.
    * Run the main script:
        ```bash
        python main.py
        ```
    * The program will execute the main function, which includes:
        * Loading initial songs from `song_list.txt`.
        * Creating example users and playlists.
        * Adding songs to playlists.
        * Demonstrating song playback.
        * Demonstrating playlist export and import.
        * Running the unit tests.

### c. How to use the program?

The program is primarily a library of classes and functions that can be used to build a music player or similar application.  Here's how the core components can be used:

* **Classes:**
    * `Song`: Represents a song with title, artist, and duration.  Create song objects using:
        ```python
        song = Song("Song Title", "Artist Name", "3:45")
        ```
    * `Playlist`: Represents a collection of songs.  Create playlist objects, add/remove songs, and get lists of songs:
        ```python
        playlist = Playlist("My Playlist")
        playlist.add_song(song)
        playlist.remove_song(song)
        songs = playlist.get_songs()
        ```
    * `User` (abstract), `FreeUser`, `PremiumUser`:  Represent users of the system.  `FreeUser` and `PremiumUser` inherit from `User` and have different song playing behavior.  Create user objects and manage their playlists:
        ```python
        free_user = FreeUser("user123")
        premium_user = PremiumUser("user456")
        playlist = free_user.create_playlist("My Playlist")
        ```
* **Functions:**
    * `import_songs(filepath)`:  Imports songs from a CSV file into a list of `Song` objects.
    * `export_playlist(playlist, filepath)`:  Exports a `Playlist` object to a CSV file.
    * `load_initial_songs(filepath)`: Loads song titles from a text file.

See the `if __name__ == "__main__":` block in `main.py` for example usage.

## 2. Body / Analysis

### a. Explain how the program covers (implements) functional requirements

The program implements the following functional requirements:

* **Object-Oriented Design:** The system is built using OOP principles:
    * **Abstraction:** The `PlaylistItem` and `User` abstract classes define common interfaces.
    * **Encapsulation:** Classes like `Song` and `Playlist` encapsulate their data using private attributes and provide controlled access through methods.
    * **Inheritance:** `FreeUser` and `PremiumUser` inherit from `User`, allowing for specialized user behavior.
    * **Polymorphism:** The `play_song()` method is implemented differently in `FreeUser` and `PremiumUser`.
* **Data Structures:** The program uses lists (`List`) to store collections of songs within playlists and playlists within users.
* **File Handling:**
    * The `import_songs()` and `export_playlist()` functions handle importing and exporting data from/to CSV files.
    * The `load_initial_songs()` function reads initial song data from a text file (`song_list.txt`).
* **Decorator Pattern:** The `log_song_play` decorator adds logging functionality to the `play_song()` methods of user classes.
* **Unit Testing:** The system includes a comprehensive set of unit tests using the `unittest` framework.  The tests are separated into individual files:
    * `test_song.py`: Tests the `Song` class.
    * `test_playlist.py`: Tests the `Playlist` class.
    * `test_user.py`: Tests the `User`, `FreeUser`, and `PremiumUser` classes.
    * `test_file_handling.py`: Tests the file handling functions.

## 3. Results and Summary

### a. See "Results" functional requirement

The program successfully implements the core features of a music streaming playlist system.  It provides a structured way to manage songs, playlists, and users, and includes file handling and unit testing.  The unit tests ensure the reliability of the code.

### b. See "Conclusions" functional requirement

The application provides a good foundation for a more complex music streaming application.  The object-oriented design makes it relatively easy to add new features or modify existing ones.  The inclusion of unit tests ensures that the core functionality remains stable as the application evolves.

### c. How it would be possible to extend your application?

Here are some ways the application could be extended:

* **Implement a user interface:** Add a graphical user interface (GUI) or a command-line interface (CLI) to make the application interactive.
* **Implement actual song playing:** Integrate a music player library (e.g., `pygame`) to enable actual playback of audio files.
* **Add more user features:** Implement user authentication, profiles, and the ability to follow other users.
* **Implement more playlist features:** Add features like playlist sharing, collaborative playlists, and playlist genres.
* **Add search functionality:** Allow users to search for songs and playlists.
* **Implement data persistence:** Use a database (e.g., SQLite, PostgreSQL) to store user, song, and playlist data persistently.
* **Implement streaming:** Support streaming music from online sources.
* **Enhance error handling:** Implement more robust error handling and input validation.
