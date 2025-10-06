import shutil
import os
from datetime import datetime
import glob

def create_backup_zip():
    os.makedirs("data/backups", exist_ok=True)
    filename = f"data/backups/backup_{datetime.now().strftime('%Y%m%d_%H%M')}.zip"
    shutil.make_archive(filename.replace(".zip", ""), 'zip', "data")
    return filename

def rotate_backups(max_backups):
    backups = sorted(glob.glob("data/backups/*.zip"), key=os.path.getmtime, reverse=True)
    for b in backups[max_backups:]:
        os.remove(b)
