import csv
import itertools
import random

from threading import Thread
from urllib import urlretrieve

THREADS = 10
TOTAL = 10000
URLS = []

def urls():
    with open("../images_2016_08/train/images.csv") as fh:
        reader = csv.reader(fh, delimiter=",")
        for row in reader:
            # o_image = row[2]
            z_image = row[-1]
            if z_image.strip() != "":
                yield z_image




def main():
    for _ in range(THREADS):
        t = Agent()
        t.start()


class Agent(Thread):
    def __init__(self):
        Thread.__init__(self)

    def run(self):
        downloaded = 0
        while downloaded < TOTAL/THREADS:
            url = URLS.next()
            try:
                fname = url.split("/")[-1].split(".jpg")[0]
                urlretrieve(url, filename="random_sample/%s.jpg" % fname)
            except:
                continue
            downloaded += 1
            print url




URLS = urls()
main()
