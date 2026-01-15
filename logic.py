import yt_dlp
import os

def run_download(link, progress_func):

    save_path = os.path.join(os.path.expanduser("~"), "Videos")

    target_file = os.path.join(save_path, '%(title)s.%(ext)s')

    ydl_opts = {
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
        'outtmpl': '%(title)s.%(ext)s',
        'progress_hooks': [progress_func],
        'nocheckcertificate': True,
        'no_color': True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([link])