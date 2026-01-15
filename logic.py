import yt_dlp
import os
import subprocess
import sys

def run_download(link, progress_func):

    save_path = os.path.join(os.path.expanduser("~"), "Videos")

    target_file = os.path.join(save_path, '%(title)s.%(ext)s')

    ydl_opts = {
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
        'outtmpl': target_file,
        'progress_hooks': [progress_func],
        'nocheckcertificate': True,
        'no_color': True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([link])

def update_yt_dlp():
    try:
        print("Starte Update von yt-dlp")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "yt-dlp"])
        return True

    except Exception as e:
        print(f"Update fehlgeschlagen: {e}")
        return False