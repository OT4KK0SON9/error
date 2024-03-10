apt update && apt upgrade
pkg install git
pkg install python
git clone https://github.com/error
cd error
mkdir music
mv -f music.mp3 music
apt install mpv
cd
cd error/music/
mpv music.mp3
clear
cd error
ls
