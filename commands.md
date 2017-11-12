###Switch grub control
#####grub control arch linux
```
sudo grub-mkconfig -o /boot/grub/grub.cfg
sudo grub-install /dev/sda
```

#####grub contorl ubuntu
```
sudo update-grub
sudo grub-install /dev/sda
```

#####ubuntu change terminal emulator
```
sudo update-alternatives --config x-terminal-emulator
```


###Video/Audio Editing

#####strip audio from video
-an no audio, -vn no video
```
ffmpeg -i input.mp4 -acodec libmp3lame output.mp3
```

#####convert video to animated gif
```
ffmpeg -i capturedvideo.avi -vf scale=320:-1 -r 10 -f image2pipe -vcodec ppm - | convert -delay 5 -loop 0 - output.gif

```
#####convert mkv to mp4 single
```
ffmpeg -i FILENAME.mkv -vcodec copy -acodec copy FILENAME.mp4
```

#####convert mkv to mp4 in loop of current directory
```
for i in *mkv; do ffmpeg -i $i -vcodec copy -acodec copy $i.mp4; done
```

#####shrink video via bitrate
```
ffmpeg -i FILENAME.mkv -b:v 1000k -acodec copy FILENAME.mp4
```

#####shrink video via crf 0(highest quality) - 51(lowest quality)
```
ffmpeg -i FILENAME.mkv -vocdec libx264 -acodec copy -crf 30 FILENAME.mp4
```
    
#####Concatenate Videos
in file inputs.txt
```
file 'file1.mpg'
file 'file2.mpg;
```
```
ffmpeg -f concat -i inputs.txt -c copy output.mpg
```

#####current directory concatenate
```
ffmpeg -f concat -i <(for f in ./*.mp4; do echo "file '$PWD/$f'"; done) -c copy output.mp4
```

#####get video's video/audio info
```
mplayer -vo null -ao null -identify -frames 0 FILENAME.mp4
```

#####convert to mpeg, while cutting section out
#####-ss starting seconds, -t new video length in seconds
```
ffmpeg -i input.mp4 -vcodec mpeg1video -acodec copy -ss 61 -t 19 output.mpeg
```
#####without audio, create pygame video
```
ffmpeg -i input.mp4 -target ntsc-vcd -vcodec mpeg1video -an output.mpg
```
#####with audio, create pygame video
```
ffmpeg -i input.mp4 -vcodec mpeg1video -acodec libmp3lame -intra output.mpg
```
#####concatenate VOB files and convert to mp4 (crf 20 for better quality, 24 for worser but smaller)
```
ffmpeg -i concat:"VTS_01_1.VOB|VTS_01_2.VOB|VTS_01_3.VOB|VTS_01_4.VOB" -acodec libmp3lame -aq 100 -ac 2 -vcodec libx264 -crf 20 -threads 0 output.mp4
```
#####sync audio files
delay video by 3.84 seconds
```
ffmpeg.exe -i "movie.mp4" -itsoffset 3.84 -i "movie.mp4" -map 1:v -map 0:a -vcodec copy -acodec copy "movie-video-delayed.mp4"
```
delay audio by 3.84 seconds
```
ffmpeg.exe -i "movie.mp4" -itsoffset 3.84 -i "movie.mp4" -map 0:v -map 1:a -vcodec copy -acodec copy "movie-audio-delayed.mp4"

```
-itsoffset 3.84 -i "movie.mp4"
Offsets timestamps of all streams by 3.84 seconds in the input file that follows the option (movie.mp4).

-map 1:v -map 0:a
Takes video stream from the second (delayed) input and audio stream from the first input - both inputs may of course be the same file. add -3.84 for hastened section. 




####rename files in directory from .ARW to .tiff
rename 's/\.ARW$/\.tiff/' *.ARW
    
###Secure Copy

#####copy from server to local
```
sudo scp -P {src port} {src user}@{src IP}:{server src path} {local dest path}
sudo scp -P NUM USER@IP_ADDRESS:/home/metulburr/test.py /home/metulburr
```

#####while SSH'd into server, copy from local to server
```
sudo scp -P {src port} {src user}@{src IP}:{home src path} {server dest path}
sudo scp -P NUM USER@IP_ADDRESS:/home/metulburr/test.py /home/metulburr
```
    
    
###Screencasting

####arch
```
ffmpeg -f alsa -ac 1 -i plughw:0,0 -f x11grab -r 24 -s hd1080 -i :0.0 -qscale 0 NEW.mkv
ffmpeg -f alsa -ac 2 -i plughw:0,0 -f x11grab -r 100 -s 1920x1080 -i :0.0 -acodec pcm_s16le -vol 768 -vcodec libx264 -preset ultrafast -threads 5 output.mkv
```

####ubuntu
#####capture video of entire desktop
```
ffmpeg -f alsa -ac 2 -i plughw:0,0 -f x11grab -r 100 -s 1920x1080 -i :0.0 -acodec pcm_s16le -vcodec libx264 -preset ultrafast -threads 5 archinstall4.mkv

#####capture video of entire desktop without sound
ffmpeg -f x11grab -r 50 -s 1920x1080 -i :0.0 -acodec pcm_s16le -vcodec libx264 -preset ultrafast -threads 5 captured.mkv
```
#####capture video of top-left desktop only
```
ffmpeg -f alsa -ac 2 -ab 128k -i pulse -f x11grab -s 800x600 -r 30 -i :0.0+10,20 -acodec libmp3lame -vcodec mpeg4 -vtag xvid /home/metulburr/capturedvideo.avi
```
#####capture window
run desired window to get windo info on it
```
xwininfo
```
will output something like
```
metulburr@ubuntu:~$ xwininfo
...

  Absolute upper-left X:  0
  Absolute upper-left Y:  680
  Relative upper-left X:  0
  Relative upper-left Y:  0
  Width: 600
  Height: 400
...
```
then pass these to ffmpeg in the form of
-s 600x400 -i :0.0+0,680
to get the total of
```
ffmpeg -f x11grab -r 50 -s 600x400 -i :0.0+0,680 -acodec pcm_s16le -vcodec libx264 -preset ultrafast -threads 5 captured.mkv
```




#####IRC Commands
```
/nick USERNAME
/msg nickserv identify <password>

/msg chanserv info #channelname
/msg chanserv register #channelname

/msg chanserv recover #channelname
/mode #channelname -i (get rid of invite only)
/mode #channelname -m (get rid of muted users)
```


###tmux 
#####leave/join tmux with session running
```
tmux detach/attach
```

####pair two sessions
#####create a session
```
tmux -S /tmp/pair
sudo chmod 777 /tmp/pair
```
#####join a session
(joiner must have permissions in directory tmux created in if somewhere else)
```
tmux -S /tmp/pair attach  
```


###grep
#####recursively search files for a string
-r recursive, -i ignore_case, -l list_filename, -H show_filename, -n show line numers
```
grep -ril "\bword\b" .

```


###sed
#####replace in file text of all occurances
s is used to replace the found expression "foo" with "bar"
g stands for "global", meaning to do this for the whole line. If you leave off the g and "foo" appears twice on the same line, only the first "foo" is changed to "bar".
-i option is used to edit in place on filename.
-e option indicates a command to run.
```
sed -i -e 's/foo/bar/g' filename
```

###DBus
#####start/stop torrents on ktorrent
```
qdbus org.ktorrent.ktorrent /core startAll
qdbus org.ktorrent.ktorrent /core stopAll
qdbus org.ktorrent.ktorrent /KTorrent startAll
qdbus org.ktorrent.ktorrent /MainApplication quit
qdbus org.ktorrent.ktorrent
```
#####crontab line to start ktorrent at x time, export required
```
10 2 * * * export DISPLAY=:0 && ktorrent
```


#####remove bad ppas ubuntu
```
ls /etc/apt/sources.list.d
sudo rm -i /etc/apt/sources.list.d/<PPA_NAME>
```
