#!/usr/bin/env python3
with open('/etc/apt/sources.list', 'r') as f:
    content = f.read()

# Fix 1: Change raspbian.raspberrypi.org to archive.raspbian.com
content = content.replace(
    "http://raspbian.raspberrypi.org/raspbian/",
    "http://legacy.raspbian.org/raspbian/"
)

# Fix 2: Comment out the Piper repository (it's offline)
content = content.replace(
    "deb http://updater.playpiper.com/repo stable non-free",
    "# Disabled - server offline\n# deb http://updater.playpiper.com/repo stable non-free"
)

with open('/etc/apt/sources.list', 'w') as f:
    f.write(content)
print('DONE')
