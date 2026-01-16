#!/usr/bin/env python3
with open('/etc/apt/sources.list', 'r') as f:
    content = f.read()

# Fix: Use legacy.raspbian.org for archived Buster release
content = content.replace(
    "http://archive.raspbian.com/raspbian/",
    "http://legacy.raspbian.org/raspbian/"
)

with open('/etc/apt/sources.list', 'w') as f:
    f.write(content)
print('DONE')
