from ytmusicapi import YTMusic
import re

def check_search_result(search_result, song):
    for result in search_result:
        if result['resultType'] == 'song' and result['title'] == song['title']:
            for artist in result['artists']:
                if artist['name'] in song['artist']:
                    return result['videoId']


def __main__ ():
    songlist_filepath = input('Audios list filepath: ')
    songlist = open(songlist_filepath, 'r').read()
    matches = re.finditer('(.*?)\n(.*?)\n([0-9]*?:[0-9]*?)\n', songlist, )
    songs = [{
        'artist': match.group(1),
        'title': match.group(2),
        'duration': match.group(3)
    } for index, match in enumerate(matches, start=1)]
    print('Found ' + str(len(songs)) + ' songs.')
    # ytm_headers_filepath = input('YTMusic headers filepath: ')
    # ytm_headers_raw = open(ytm_headers_filepath).read()
    ytm = YTMusic('ytmheaders.json')
    # ytm.setup(filepath='ytmheaders.json', headers_raw=ytm_headers_raw)
    playlist = ytm.create_playlist('Imported from VK', 'Contains songs automatically imported from VK')
    print('Created playlist with Id: ' + str(playlist))
    unfound = []
    found_count = 0
    for song in songs:
        query = song['artist'] + ' ' + song['title']
        try:
            search_result = ytm.search(query)
            videoId = check_search_result(search_result, song)
            if videoId:
                ytm.add_playlist_items(playlist, [videoId])
                print('Added ' + song['title'] + ' by ' + song['artist'])
                found_count += 1
            else:
                unfound.append(song)
        except:
            print('[!] Error searching for ' + query)
            unfound.append(song)
    print('Added ' + str(found_count) + ' of ' + str(len(songs)) + '. Exporting remaining to "unfound.txt"')
    unfound_list = ''.join([song['artist'] + ' - ' + song['title'] + '\n' for song in unfound])
    print(unfound_list)
    f = open('unfound.txt', 'w')
    f.write(unfound_list)
    f.close()


__main__()
