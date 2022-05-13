from  pytube import YouTube
import math

#link="https://www.youtube.com/watch?v=Vi9Y9AL13Rc" 
link=input("Enter link: ")
video=YouTube(link)

print("Video Title: ", video.title)
print("Video Author: ", video.author)
video_min=math.trunc(video.length /60)
video_sec=video.length%60
print("Video length: ", video_min, " mins and ",video_sec, " secs")
print("Video Rating: ", video.views)
print("Video Publish date: ", video.publish_date)

user_choice=input("Would you like to download the video Y/N? ")
if user_choice.upper()=='Y':
  user_choice=input("Would you like highest or lowest resolution H/L? ")
  if user_choice.upper()=="L":
    my_video=video.streams.first()
    my_video.download()
    print("Video has been downloaded")
  elif user_choice.upper()=="H":
    my_video=video.streams.get_highest_resolution()
    my_video.download()
    print("Video has been downloaded")
  else:
    print("Invalid input")
else:
  print("Video will not be downloaded")