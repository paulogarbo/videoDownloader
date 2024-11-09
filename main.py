from yt_dlp import YoutubeDL

def download_highest_resolution(url):
    ydl_opts = {
        'format': 'bestvideo[ext=mp4][height<=1080]+bestaudio[ext=m4a]/best[ext=mp4][height<=1080]',
        # Preferência para MP4 e qualidade até 1080p
        'outtmpl': 'C:\\Users\\garba\\Videos\\%(title)s.%(ext)s',  # Local e nome do arquivo de saída
        'merge_output_format': 'mp4'  # Formato final do arquivo se precisar juntar vídeo e áudio
    }
    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

if __name__ == '__main__':
    VIDEO_URL = 'https://www.youtube.com/watch?v=zEcehthgR5s&ab_channel=FelipeRocha%E2%80%A2FullStackClub'
    download_highest_resolution(VIDEO_URL)
