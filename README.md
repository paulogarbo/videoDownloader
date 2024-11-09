# YouTube Video Downloader

Este projeto é um simples downloader de vídeos do YouTube, desenvolvido em Python utilizando a biblioteca `yt-dlp`. Ele baixa vídeos em alta resolução diretamente no formato `.mp4`, com qualidade até 1080p (ou a melhor disponível abaixo de 1080p).

## Pré-requisitos

1. **Python 3.6+** - Certifique-se de ter o Python instalado. [Baixe aqui](https://www.python.org/downloads/).
2. **yt-dlp** - Uma biblioteca para fazer o download de vídeos do YouTube. Instale com o comando:

    ```bash
    pip install yt-dlp
    ```
   
3. **FFmpeg** - `yt-dlp` usa o FFmpeg para combinar vídeo e áudio em arquivos separados. [Instale o FFmpeg](https://ffmpeg.org/download.html) e certifique-se de adicioná-lo ao PATH do sistema.
- [Tutorial](https://www.wikihow.com/Install-FFmpeg-on-Windows)

## Instalação

1. Clone este repositório:

    ```bash
    git clone https://github.com/paulogarbo/videoDownloader.git
    cd youtube-video-downloader
    ```

## Como Usar

1. Substitua a URL do vídeo no código com o link do vídeo do YouTube que deseja baixar.
2. Execute o script:

    ```bash
    python downloader.py
    ```

### Exemplo de Uso

```python
from yt_dlp import YoutubeDL

def download_highest_resolution(url):
    ydl_opts = {
        'format': 'bestvideo[ext=mp4][height<=1080]+bestaudio[ext=m4a]/best[ext=mp4][height<=1080]',
        'outtmpl': 'C:\\Users\\seu_usuario\\Videos\\%(title)s.%(ext)s',
        'merge_output_format': 'mp4'
    }
    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

if __name__ == '__main__':
    VIDEO_URL = 'https://www.youtube.com/watch?v=seu_video_id'
    download_highest_resolution(VIDEO_URL)
