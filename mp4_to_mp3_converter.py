import argparse
from moviepy.editor import *

def convert_to_mp3(mp4_file_path, output_mp3_path):
    try:
        video = VideoFileClip(mp4_file_path)
        video.audio.write_audiofile(output_mp3_path, codec='libmp3lame')
        print("Conversion successful!")
    except Exception as e:
        print("Error occurred during conversion:", str(e))

# Parse command-line arguments
parser = argparse.ArgumentParser(description='Convert MP4 to MP3.')
parser.add_argument('input_file', type=str, help='Path to input MP4 file')
parser.add_argument('output_file', type=str, help='Path to output MP3 file')
args = parser.parse_args()

# Convert MP4 to MP3
convert_to_mp3(args.input_file, args.output_file)

