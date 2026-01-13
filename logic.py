import yt_dlp

def run_download(link, progress_func):
    ydl_opts = {
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
        'outtmpl': '%(title)s.%(ext)s',
        'progress_hooks': [progress_func],
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([link])