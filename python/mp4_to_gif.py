#!/home/alau/anaconda3/envs/sdc-lanes/bin/python
#
# Utility to use a clip of an input .mp4 video file to create a .gif image file.
#
# Usage: ./mp4_to_gif.py <input video filename> <start(sec)> <end(sec)> [<outfilename>]
#

from sys import argv
from moviepy.editor import VideoFileClip

##### Get values from command line #####
filename = argv[1]
begin = int(argv[2])
end = int(argv[3])
outfilename = argv[4]
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

outfile = f"./{name}.gif"

if outfilename:
  outname = outfilename
  trim = outfilename.find(".gif")
  if trim > -1:
    outname = outfilename[:trim]
  outfile = f"./{outname}.gif"
vclip.write_gif(outfile, fps=2)
#vclip.write_gif(f"./{name}.gif", fps=4, program='ffmpeg', loop=1, fuzz=1)
