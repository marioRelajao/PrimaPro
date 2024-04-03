# Spotify Playlist Updater

## Overview

This Python script allows you to update a Spotify playlist with songs by specified artists using the Spotipy library.

## Prerequisites

Before using this script, ensure you have the following:

- Python installed
- A Spotify account.
- Register your application on the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/applications) to obtain your client ID and client secret.
- Set up a Spotify playlist and obtain its ID.

## Installation

1. Clone this repo.

    ```
    git clone https://github.com/marioRelajao/PrimaPro.git
    ```

2. Install Spotipy.

    ```
    pip install spotipy
    ```

## Usage

1. Replace the secrets by creating  `config.py`and adding your Spotify username, playlist ID, client ID, and client secret.
2. Edit the `artists` list in the script with the names of the artists whose songs you want to add to the playlist.
3. Run the script.

    ```
    python primavera.py
    ```

## Notes

- The script adds the first song found for each artist in the `artists` list to the specified playlist.
- Ensure the playlist is set to public/private and set the scope acordingly.
- For security reasons, ensure you don't expose your client ID, client secret, or any other sensitive information publicly.


Sure, here's a TODO list you can include in your README.md:

## TODO

- [ ] Implement error handling for cases such as invalid artist names or failed API requests.
- [ ] Add support for adding more than one song per artist to the playlist.
- [ ] Improve user interaction by adding command-line arguments for specifying artists and playlist details.
## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
