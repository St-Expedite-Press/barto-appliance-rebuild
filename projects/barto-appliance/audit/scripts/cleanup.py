"""
cleanup.py
Removes timestamp-named screenshots (keeping only descriptively-named ones)
and fixes stale references in docs.
"""
import os, re, glob

DESIGNS_SHOTS = os.path.join(os.path.dirname(__file__), '..', 'designs', 'screenshots')

def clean_timestamp_shots():
    """Delete raw timestamp screenshot files, keep named ones."""
    removed = 0
    for f in os.listdir(DESIGNS_SHOTS):
        if re.match(r'screenshot_localhost_\d{4}', f):
            os.remove(os.path.join(DESIGNS_SHOTS, f))
            removed += 1
    print(f'  Removed {removed} timestamp screenshot files')

if __name__ == '__main__':
    print('Cleaning up...')
    if os.path.isdir(DESIGNS_SHOTS):
        clean_timestamp_shots()
    print('Done.')
