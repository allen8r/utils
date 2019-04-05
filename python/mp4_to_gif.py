#!/home/alau/anaconda3/envs/sdc-lanes/bin/python
from sys import argv
from moviepy.editor import VideoFileClip

##### Get values from command line #####
name = argv[1]
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

vclip = VideoFileClip(f"./{name}.mp4").subclip(begin, end)
#vclip.write_gif(f"./{name}.gif", fps=3, program='imageio' loop=1, fuzz=0)
vclip.write_gif(f"./{name}.gif", fps=4, program='ffmpeg', loop=1, fuzz=0)



