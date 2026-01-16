#!/usr/bin/env python3
with open('/usr/local/games/piper/src/media/player.py', 'r') as f:
    content = f.read()

# Fix: VideoPlayer.__init__ - add -o local to omxplayer args
content = content.replace(
    "self._video_player_args = ['omxplayer', '--no-keys']",
    "self._video_player_args = ['omxplayer', '-o', 'local', '--no-keys']"
)

with open('/usr/local/games/piper/src/media/player.py', 'w') as f:
    f.write(content)
print('DONE')
