import requests
import time

link = input("https://www.tiktok.com/@imy0i/video/6995525769904639259")

while True:
  time.sleep(1)
  requests.get(link)
