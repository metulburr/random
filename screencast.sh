#arch linux
ffmpeg -f alsa -ac 1 -i plughw:0,0 -f x11grab -r 24 -s hd1080 -i :0.0 -qscale 0 NEW.mkv

ffmpeg -f alsa -ac 2 -i plughw:0,0 -f x11grab -r 100 -s 1920x1080 -i :0.0 -acodec pcm_s16le -vol 768 -vcodec libx264 -preset ultrafast -threads 5 output.mkv


#ubuntu
#capture video of entire desktop
ffmpeg -f alsa -ac 2 -i plughw:0,0 -f x11grab -r 100 -s 1920x1080 -i :0.0 -acodec pcm_s16le -vcodec libx264 -preset ultrafast -threads 5 archinstall4.mkv


#capture video of top-left desktop only
ffmpeg -f alsa -ac 2 -ab 128k -i pulse -f x11grab -s 800x600 -r 30 -i :0.0+10,20 -acodec libmp3lame -vcodec mpeg4 -vtag xvid /home/metulburr/capturedvideo.avi


