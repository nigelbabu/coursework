#!/usr/bin/python3


def main():
    # A dict to hold song data
    song_data = {}
    # Open the file using `with` so it's closed automatically
    with open('lab4.abc') as f:
        for line in f:
            # Find the index
            if line.startswith('X:'):
                song_data['index'] = line.split(':', 1)[1].strip()
            # Find the title
            if line.startswith('T:'):
                if song_data.get('title') is None:
                    song_data['title'] = line.split(':', 1)[1].strip()
            # Find the time signature 
            if line.startswith('M:'):
                song_data['time_sig'] = line.split(':', 1)[1].strip()
            # Find the key signature
            if line.startswith('K:'):
                song_data['key_sig'] = line.split(':', 1)[1].strip()
            if song_data.get('key_sig') is not None:
                # 195 ... Road to Lisdoonvarna, The ... Time sig: C| ... Key sig: D ...J
                print(f"{song_data['index']} ... {song_data['title']}",
                      f" ... Time sig: {song_data['time_sig']} ... ",
                      f"Key sig: {song_data['key_sig']} ... ")
                song_data = {}



if __name__ == '__main__':
    main()
