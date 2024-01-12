import os
import subprocess
import shutil
#import test


def convertToMp4(videoList):
  
  mp4videos=[]
  input_folder = videoList[0]
  result_folder = "./out/mp4video/"
  
  if len(videoList[1])==1:
    if videoList[1][0].endswith('.mp4'):
      mp4videos.append(videoList[1][0])
      return [input_folder,mp4videos]

    file_path = input_folder
    output_file = f'{result_folder+videoList[1][0]}.mp4'
    subprocess.run(['ffmpeg', '-i', f'{file_path}', '-c:v', 'copy', output_file])
    mp4videos.append(output_file)
    print([result_folder,mp4videos])
    return [result_folder,mp4videos]
  
  else:
    for file in os.scandir(input_folder):
      if file.name.endswith('.mp4'):
        mp4videos.append(file.name)
        shutil.copy(file, result_folder)
      else:
        try:
          print(file.name)
          file_path = os.path.join(input_folder, file.name)
          output_file=f'{result_folder+os.path.splitext(file.name)[0]}.mp4'
          subprocess.run(['ffmpeg', '-i', f'{file_path}', '-c:v', 'copy', output_file])
          mp4videos.append(output_file)
        
        except OSError as e:
          print("Error:", e)
    print([result_folder,mp4videos])
    return [result_folder,mp4videos]
 
 