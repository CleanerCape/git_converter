from pathlib import Path
from moviepy.editor import VideoFileClip

cwd = Path(".")
files = cwd.glob("*.mp4")
file_names = []

for file in files:
    file_name = str(file)
    file_names.append(file_name)

for file_name in file_names:
    videoClip = VideoFileClip(file_name)
    videoClip.write_gif(file_name[:-4] + ".gif",fps=videoClip.fps,program="ffmpeg")