import os
os.environ["IMAGEIO_FFMPEG_EXE"] = "\Users\167818\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\LocalCache\local-packages\Python311\site-packages\ffmpeg"
from moviepy.editor import VideoFileClip
videoClip = VideoFileClip("4CH.mp4")
videoClip.write_gif("4CH.gif")
