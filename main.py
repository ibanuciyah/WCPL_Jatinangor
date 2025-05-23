from img_scrapper import img_scraper
import cv2
import csv
from datetime import datetime, timedelta

date=datetime.now()+timedelta(days=1)
date=date.strftime("%Y%m%d")
time_list=[1,4,7,10,13,16,19,22]

for time in time_list:
    print(date,time)
    url = f"http://nimbus.meteo.itb.ac.id/weather/model/wrf_new/cy00/d02/rainuv10/wrf-00-rainuv10-{date}_{time:02d}.png"
    img_scraper(url)

    takhujan=[(0, 0, 0)]
    low=[(0, 255, 255), (0, 230, 255), (0, 206, 255), (0, 181, 255), (0, 156, 255), (0, 131, 255), (0, 107, 255), (0, 82, 255)]
    medium=[(0, 57, 255), (0, 46, 235)]
    high=[(0, 39, 207), (0, 32, 180)] 
    vhigh=[(0, 26, 153), (0, 19, 126), (0, 12, 99), (0, 5, 71)]


    x,y=350,248
    # Load image
    img = cv2.imread("hasil.png")

    b,g,r= img[y,x]
    print(r,g,b)
    if (r,g,b) in low:
        current_rain=[date,time,0,1,0,0,0]
    elif (r,g,b) in medium:
        current_rain=[date,time,0,0,1,0,0]
    elif (r,g,b) in high:
        current_rain=[date,time,0,0,0,1,0]
    elif (r,g,b) in vhigh:
        current_rain=[date,time,0,0,0,0,1]
    else:
        current_rain=[date,time,1,0,0,0,0]

    with open("hasil.csv", "a", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(current_rain)