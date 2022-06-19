#!/bin/sh

echo "Enter the name of the file (i.e. my_video)"
read filename;
cd ~/Videos && ffmpeg -video_size 1920x1080 -framerate 30 -f x11grab -i :0.0 -f pulse -ac 2 -i default "$filename".mp4;
