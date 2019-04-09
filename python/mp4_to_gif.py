#!/home/alau/anaconda3/envs/sdc-lanes/bin/python
#
# Usage: ./video-capture.py <filename> <start(sec)> <end(sec)>
#

from sys import argv
from moviepy.editor import VideoFileClip

##### Get values from command line #####
filename = argv[1]
begin = int(argv[2])
end = int(argv[3])
########################################


########################################
# == VideoFileClip API =================
########################################
#
# VideoFileClip.write_gif(
#   filename, 
#   fps=None,
#   program='imageio',
#   opt='nq',
#   fuzz=1,
#   verbose=True,
#   loop=0,
#   dispose=False,
#   colors=None,
#   tempfiles=False)
#
#########################################

filename_parts = filename.split('.')
ext = filename_parts[-1]
name = "".join(filename_parts[:-1])

if ext != 'mp4':
  print(f'\n>>EXIT: {filename} is not a .mp4 file.\nOnly .mp4 video files can be used as input.')
  raise SystemExit

vclip = VideoFileClip(f"./{filename}").subclip(begin, end)
#vclip.write_gif(f"./{name}.gif", fps=3, program='imageio' loop=1, fuzz=0)
vclip.write_gif(f"./{name}.gif", fps=4, program='ffmpeg', loop=1, fuzz=1)