#!/usr/bin/env python3
"""Print index, title, time signature, and key signature from an abc file

Sample output of the following form:
    195 ... Road to Lisdoonvarna, The ... Time sig: C| ... Key sig: D ...
    196 ... Jenny's Wedding ... Time sig: C| ... Key sig: D ...
    197 ... Dark Girl in Blue, The ... Time sig: C| ... Key sig: D ...
    198 ... Knotted Cord, The ... Time sig: C| ... Key sig: Ador ...

"""
from pygame import mixer
import time



def play_music(file_name='/home/nigel/coursework/cmpu1026/killavil_fancy.mp3'):
    """Play music for 30 seconds
    """
    mixer.init()
    mixer.music.load(file_name)
    mixer.music.set_volume(0.7)
    mixer.music.play()
    time.sleep(10)
    mixer.music.fadeout(500)


def clean(line):
    """
    Clean a given line so it has only the output required.

    Split by `:` once and then take the second half and remove the \n
    """
    return line.split(':', 1)[1].strip()


def main():
    """
    Main function that holds most of the logic for the program
    """
    # A dict to hold song data
    song_data = {}
    # Open the file using `with` so it's closed automatically
    with open('lab4.abc') as abcfile:
        for line in abcfile:
            # Find the index
            if line.startswith('X:'):
                song_data['index'] = clean(line)
            # Find the title, only use the first item that starts with T:
            if line.startswith('T:') and song_data.get('title') is None:
                song_data['title'] = clean(line)
            # Find the time signature
            if line.startswith('M:'):
                song_data['time_sig'] = clean(line)
            # Find the key signature and print everything because this should be
            # a complete record
            if line.startswith('K:'):
                song_data['key_sig'] = clean(line)
                print(f"{song_data['index']} ... {song_data['title']}",
                      f" ... Time sig: {song_data['time_sig']} ... ",
                      f"Key sig: {song_data['key_sig']} ... ")
                # Reset the song data to an empty dict
                song_data = {}
    play_music()



if __name__ == '__main__':
    main()
