# fromvktoytm

Adds your VK audios to YouTube Music.

### Input format

The only supported input for now is raw copied list of tracks in the following format in a text file:
```
Track title (track title)
Devil In My Veins (artist name)
3:58 (duration)

Glass Animals
The Other Side Of Paradise
5:20

A Tribe Called Quest
Jazz (We've Got)
4:10

...
```
### YouTube Music authentication

The app uses [this unofficial API](https://github.com/sigma67/ytmusicapi) to communicate with YouTube Music. 
Follow [this](https://github.com/sigma67/ytmusicapi/blob/master/docs/source/setup.rst#copy-authentication-headers) this instructions to copy your authentication headers
and then provide them in a text file the first time you use the app. A new file called `ytmheaders.json` will be created and then used.
