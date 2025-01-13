import argparse
from pytube import YouTube
from moviepy.editor import *

def download_video(url, output_path):
    try:
        yt = YouTube(url)
        yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').first().download(output_path)
        print("Download successful!")
    except Exception as e:
        print("Error occurred during download:", str(e))

def convert_to_mp3(input_path, output_path):
    try:
        video = VideoFileClip(input_path)
        video.audio.write_audiofile(output_path, codec='libmp3lame')
        print("Conversion to MP3 successful!")
    except Exception as e:
        print("Error occurred during conversion to MP3:", str(e))

# Parse command-line arguments
parser = argparse.ArgumentParser(description='Download YouTube video and convert to MP3 or MP4.')
parser.add_argument('url', type=str, help='YouTube video URL')
parser.add_argument('--format', choices=['mp3', 'mp4'], default='mp4', help='Output format (default: mp4)')
parser.add_argument('--output', type=str, default='output', help='Output file name without extension (default: output)')
args = parser.parse_args()

# Download YouTube video
download_video(args.url, args.output + '.mp4')

# Convert to chosen format
if args.format == 'mp3':
    convert_to_mp3(args.output + '.mp4', args.output + '.mp3')
    print("Conversion completed. MP3 file saved as", args.output + '.mp3')
else:
    import os
    os.rename(args.output + '.mp4', args.output + '.mp4')
    print("Download completed. MP4 file saved as", args.output + '.mp4')

