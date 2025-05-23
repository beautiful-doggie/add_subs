import os 
ffmpeg_dir = r"C:\Users\luzihan\Desktop\youtube_translate\ffmpeg-master-latest-win64-gpl-shared\bin"
os.environ["PATH"] = ffmpeg_dir + os.pathsep + os.environ["PATH"]
import ffmpeg 


def add_subtitles_to_video(video_path, srt_path, output_path):
    ffmpeg.input(video_path).output(output_path, vf=f"subtitles='{srt_path}'").run(cmd=r"C:\Users\luzihan\Desktop\youtube_translate\ffmpeg-master-latest-win64-gpl-shared\bin\ffmpeg.exe")


if __name__=="__main__":
    # video_dir="videos"
    # srt_dir="srt"
    # output_dir="output_videos"
    # os.makedirs(output_dir,exist_ok=True)

    # for filename in os.listdir(video_dir):
    #     base_name=os.path.splitext(filename)[0]
    #     video_path=os.path.join(video_dir,filename)
    #     srt_path=os.path.join(srt_dir,base_name+".srt")
    #     output_path=os.path.join(output_dir,base_name+"_with_subs.mp4")
        
    #     add_subtitles_to_video(video_path,srt_path,output_path)





    video_path=r"videos\ceshi.mp4"
    output_path=r"output_videos\ceshi_with_subs.mp4"
    srt_path = r"ceshi.srt"
    add_subtitles_to_video(video_path,srt_path,output_path)
