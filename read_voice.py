import whisper 
import os 
ffmpeg_dir = r"C:\Users\luzihan\Desktop\youtube_translate\ffmpeg-master-latest-win64-gpl-shared\bin"
os.environ["PATH"] = ffmpeg_dir + os.pathsep + os.environ["PATH"]
import datetime
import srt 



def transcribe_audio(audio_path):
    model = whisper.load_model("base")  # 可选 tiny, base, small, medium, large
    result = model.transcribe(audio_path)
    return result["segments"]

# 转换为 SRT 格式
def convert_to_srt(segments):
    subs = []
    for i, seg in enumerate(segments):
        start = datetime.timedelta(seconds=(seg["start"]))
        end = datetime.timedelta(seconds=(seg["end"]))
        subs.append(srt.Subtitle(index=i+1, start=start, end=end, content=seg["text"]))
    return subs

# from googletrans import Translator
import time 
import requests
import hashlib 
import random
from dotenv import load_dotenv
load_dotenv()
APP_ID =  os.getenv("BAIDU_APP_ID")
APP_KEY = os.getenv("BAIDU_APP_KEY")
def baidu_translate(text, from_lang='en', to_lang='zh'):
    endpoint = 'https://fanyi-api.baidu.com/api/trans/vip/translate'
    salt = str(random.randint(32768, 65536))
    sign = hashlib.md5((APP_ID + text + salt + APP_KEY).encode('utf-8')).hexdigest()

    params = {
        'q': text,
        'from': from_lang,
        'to': to_lang,
        'appid': APP_ID,
        'salt': salt,
        'sign': sign
    }

    try:
        response = requests.get(endpoint, params=params, timeout=5)
        result = response.json()
        if "trans_result" in result:
            return result['trans_result'][0]['dst']
        else:
            print("翻译失败：", result)
            return text  # 保留原文
    except Exception as e:
        print("请求错误：", e)
        return text
def translate_subtitles(subs):
    for sub in subs:
        original_text = sub.content.strip()
        translated = baidu_translate(original_text)
        sub.content = translated
    return subs

import srt 

def save_srt(subs, output_path):
    srt_data = srt.compose(subs)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(srt_data)

#test 

if __name__=="__main__":
    audio_dir="audio"
    srt_dir="srt"
    
    for filename in os.listdir(audio_dir):
        audio_path=os.path.join(audio_dir,filename)
    
        srt_name=os.path.splitext(filename)[0]+".srt"
        srt_path=os.path.join(srt_dir,srt_name)
        if os.path.exists(srt_path):
            continue 

        segments=transcribe_audio(audio_path)
        sub0=convert_to_srt(segments)
        sub1=translate_subtitles(sub0)      
        save_srt(sub1,srt_path)
    # segments=transcribe_audio(audio_path)
    # sub0=convert_to_srt(segments)
    # sub1=translate_subtitles(sub0)
    # srt_path = "subtitles.srt"
    # save_srt(sub1,srt_path)

  
