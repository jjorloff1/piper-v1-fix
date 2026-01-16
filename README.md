# Piper Computer Kit V1 Fixes

Fixes applied to a Piper Computer Kit V1 running upgraded software (v2.8.2) from a newer SD card.

**Raspberry Pi IP:** 192.168.1.122
**SSH Login:** `ssh pi@192.168.1.122` (password: piper)

---

## Fix 1: Audio Output (3.5mm Jack)

### Problem
The upgraded Piper software assumed HDMI audio (for newer kits with built-in speakers). On V1 kits with a separate 3.5mm audio jack, loading a level would mute the audio.

### Root Cause
In `soundUtils.py`, the command `amixer cset numid=3 1` was intended to select analog output on older Raspberry Pi OS. On newer OS versions, `numid=3` is the Master Volume control, so this command was setting volume to 1 (essentially muting).

Additionally, `omxplayer` calls throughout the codebase didn't specify `-o local` to force audio through the 3.5mm jack.

### Files Modified
| File | Change |
|------|--------|
| `/usr/local/games/piper/src/legacy_engine/utils/soundUtils.py` | Commented out `amixer cset numid=3 1`, added `-o local` to omxplayer |
| `/usr/local/games/piper/src/legacy_engine/utils/videoUtils.py` | Added `-o local` to all omxplayer calls (5 places) |
| `/usr/local/games/piper/src/media/player.py` | Added `-o local` to video player args |

### Backups
- `soundUtils.py.backup`
- `videoUtils.py.backup`
- `player.py.backup`

### To Restore (if needed)
```bash
ssh pi@192.168.1.122
sudo cp /usr/local/games/piper/src/legacy_engine/utils/soundUtils.py.backup /usr/local/games/piper/src/legacy_engine/utils/soundUtils.py
sudo cp /usr/local/games/piper/src/legacy_engine/utils/videoUtils.py.backup /usr/local/games/piper/src/legacy_engine/utils/videoUtils.py
sudo cp /usr/local/games/piper/src/media/player.py.backup /usr/local/games/piper/src/media/player.py
```

---

## Fix 2: Apt Package Manager

### Problem
`sudo apt install` was failing with 404 errors.

### Root Cause
1. Raspbian Buster repositories moved from `raspbian.raspberrypi.org` to `legacy.raspbian.org`
2. Piper's update server (`updater.playpiper.com`) is offline/discontinued

### Files Modified
| File | Change |
|------|--------|
| `/etc/apt/sources.list` | Changed repo URL to `legacy.raspbian.org`, commented out dead Piper repo |

### New sources.list Content
```
deb http://legacy.raspbian.org/raspbian/ buster main contrib non-free rpi
# Uncomment line below then 'apt-get update' to enable 'apt-get source'
#deb-src http://legacy.raspbian.org/raspbian/ buster main contrib non-free rpi
# Disabled - server offline
# deb http://updater.playpiper.com/repo stable non-free
```

### Backup
- `/etc/apt/sources.list.backup`

### To Restore (if needed)
```bash
ssh pi@192.168.1.122
sudo cp /etc/apt/sources.list.backup /etc/apt/sources.list
sudo apt update
```

---

## Additional: Installed Go Game

Installed GNU Go board game for playing Weichi/Go:

```bash
sudo apt install gnugo cgoban
```

- **gnugo**: The AI engine (computer opponent)
- **cgoban**: The graphical interface

Desktop shortcut created at `/home/pi/Desktop/cgoban.desktop`

To configure gnugo in cgoban: Set the Go Modem program path to `/usr/games/gnugo --mode gtp`

---

## Fix Scripts

The Python scripts used to apply these fixes are saved in `fix-scripts/`:

| Script | Purpose |
|--------|---------|
| `fix_soundutils.py` | Adds `-o local` to omxplayer in soundUtils.py |
| `fix_videoutils.py` | Adds `-o local` to omxplayer in videoUtils.py |
| `fix_player.py` | Adds `-o local` to omxplayer in player.py |
| `fix_apt_sources.py` | Comments out dead Piper repo |
| `fix_apt_sources2.py` | Changes Raspbian URL to legacy.raspbian.org |

To re-run a fix script:
```bash
scp fix-scripts/fix_soundutils.py pi@192.168.1.122:/tmp/
ssh pi@192.168.1.122 "sudo python3 /tmp/fix_soundutils.py"
```

---

## Notes

- Piper software version: 2.8.2-d1 (highest compatible with V1 kit)
- Raspberry Pi OS: Buster (Debian 10)
- The Piper update server is discontinued; future updates would come as SD card images from playpiper.com

## Support Resources

- Piper V1 Support: https://www.playpiper.com/pages/getsupport-pc01
- Piper Contact: hi@playpiper.com
