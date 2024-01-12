# take a video as input or a list of videos
import os
from pathlib import Path
#from scripts import videotomp4 as vtm

def inputFiles():
  # Path to the file or folder
  folder_path = Path(input("/path/to/item:"))
  print("Path to the item: ", folder_path)

  # Check if the path is a directory (folder)
  videos=[]
  if os.path.isdir(folder_path):
      print(folder_path, "is a directory")
      for filename in os.listdir(folder_path):
          # Check if the current item is a file and has .txt extension
          if os.path.isfile(os.path.join(folder_path, filename)):
            # Do something with the file, e.g. print the filename
            #print("File: ", filename)
            videos.append(filename)
      #print(videos)
      return [folder_path,videos]

            #vtm.convertToMp4(filename)

  # Check if the path is a file
  elif os.path.isfile(folder_path):
      print(folder_path, "is a file")
      videos.append(os.path.basename(folder_path))
      print([os.path.dirname(folder_path),videos])
      return [folder_path,videos]
      #vtm.convertToMp4(folder_path)

  # If neither, then it is neither a file nor a directory
  else:
      print(folder_path, "is not a file or directory")
  

#inputFiles()

