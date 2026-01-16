#!/usr/bin/env python3
with open('/usr/local/games/piper/src/legacy_engine/utils/soundUtils.py', 'r') as f:
    content = f.read()
content = content.replace("['omxplayer',  sound, '--vol'", "['omxplayer', '-o', 'local', sound, '--vol'")
with open('/usr/local/games/piper/src/legacy_engine/utils/soundUtils.py', 'w') as f:
    f.write(content)
print('DONE')
