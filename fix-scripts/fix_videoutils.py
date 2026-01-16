#!/usr/bin/env python3
with open('/usr/local/games/piper/src/legacy_engine/utils/videoUtils.py', 'r') as f:
    content = f.read()

# Fix 1: __start_video_process method
content = content.replace(
    "args = ['omxplayer', '--no-keys', video] + args",
    "args = ['omxplayer', '-o', 'local', '--no-keys', video] + args"
)

# Fix 2: playVideoCreation method (both occurrences)
content = content.replace(
    "['omxplayer', '--no-keys', video, '--vol'",
    "['omxplayer', '-o', 'local', '--no-keys', video, '--vol'"
)
content = content.replace(
    "['omxplayer', '--no-keys', '-n', '-1', video",
    "['omxplayer', '-o', 'local', '--no-keys', '-n', '-1', video"
)

# Fix 3: playMultipleVideos method
content = content.replace(
    "videosPath = 'omxplayer ' + currentVideoPath",
    "videosPath = 'omxplayer -o local ' + currentVideoPath"
)
content = content.replace(
    "videosPath + ' && ' + 'omxplayer '",
    "videosPath + ' && ' + 'omxplayer -o local '"
)

with open('/usr/local/games/piper/src/legacy_engine/utils/videoUtils.py', 'w') as f:
    f.write(content)
print('DONE')
