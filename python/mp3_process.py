from mutagen.mp3 import MP3 
import mutagen.id3 
from mutagen.easyid3 import EasyID3 
#EasyID3.valid_keys["comment"]="COMM::'XXX'" 

#id3info = MP3("runaway.mp3", ID3=EasyID3) 
#for k, v in id3info.items(): 
#print k,v

audio=MP3("runaway.mp3")
print audio.info.length, audio.info.bitrate

audio2=EasyID3("runaway.mp3")
print audio2["performer"]

print EasyID3.valid_keys.keys()
