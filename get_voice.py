import os 
ffmpeg_dir = r"C:\Users\luzihan\Desktop\youtube_translate\ffmpeg-master-latest-win64-gpl-shared\bin"
os.environ["PATH"] = ffmpeg_dir + os.pathsep + os.environ["PATH"]
import ffmpeg

def extract_audio(video_path,audio_path):
   
    ffmpeg.input(video_path).output(audio_path,ac=1,ar=16000).overwrite_output().run()
   
 
    return audio_path 

if __name__ == "__main__":
     video_dir="videos"
     audio_dir="audio"
     for filename in os.listdir(video_dir):
          video_path=os.path.join(video_dir,filename)
          audio_filename=os.path.splitext(filename)[0]+".wav"
          audio_path=os.path.join(audio_dir,audio_filename)
     if not os.path.exists(audio_path):
          extract_audio(video_path,audio_path)

    