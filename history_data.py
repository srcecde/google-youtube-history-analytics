"""
-*- coding: utf-8 -*-
========================
Python Google-YouTube History Analytics
========================

Developed by: Chirag Rathod (Srce Cde)
Email: chiragr83@gmail.com

========================
"""

import pandas as pd
import collections
from collections import defaultdict
import datetime
import csv
import argparse
import json
import os


def YouTubeData():
    data_dic = defaultdict(list)
    try:
        os.chdir('history')
        read_data = pd.read_html('search-history.html')
    except:
        exit('\033[91m'+'No data/directory found for YouTube history or \nsearch-history.html file not found'+'\033[0m')

    y = []

    for i in read_data[0][1]:
        y.append(i[:4])

    for i, j in zip(y, read_data[0][0]):
        data_dic[i].append(j)

    del data_dic['Time']

    count_data = {i: collections.Counter(j).most_common() for i, j in data_dic.items()}

    os.chdir('..')
    hist_file = open('YouTube_Search_History.csv', 'w')
    hist_write = csv.writer(hist_file)

    for i, j in sorted(count_data.items(), reverse=True):
        hist_write.writerow([i])

        for k in j:
            x = ' :'.join(map(str, k))
            hist_write.writerow(x.split(":"))

    hist_file.close()

# ****************************************
    try:
        os.chdir('history')

        with open('watch-history.json', 'r') as f:
            fr = f.read()
            xj = json.loads(fr)
    except:
        exit('\033[91m'+'No data/directory found for YouTube history or \nwatch-history.json file not found'+'\033[0m')

    os.chdir('..')
    watch_file = open('YouTube_Watch_History.csv', 'w')
    watch_write = csv.writer(watch_file)

    for i in xj:
        s = i['snippet']['title']
        a = i['snippet']['publishedAt']
        p = i['snippet']['position']

        watch_write.writerow(['Title :', s])
        watch_write.writerow(['Time :', a])
        watch_write.writerow(['Position :', p])
        watch_write.writerow(" ")

        # print("Title : {}".format(s))
        # print("Time : {}".format(a))
        # print("Position : {}".format(p))
        # print("\n")

    watch_file.close()


# **************************************************


def GoogleSearchData():
    data_dic = defaultdict(list)
    try:
        os.chdir('Searches')
    except:
        exit('\033[91m'+'No data/directory found for Google Search'+'\033[0m')

    list_dir = os.listdir()

    for i in list_dir:
        with open(i, 'r') as f:
            fr = f.read()
            json_data = json.loads(fr)
            event_data = json_data['event']
        q_time = []
        for j in event_data:
            q = j['query']['id']
            qt = j['query']['query_text']

            for k in q:
                gtime = int(k['timestamp_usec']) / 1000000
                str_time = datetime.datetime.fromtimestamp(gtime).strftime('%Y-%B')
                data_dic[str_time].append(qt)
            q_time.append(str_time)

    c = {i: collections.Counter(j).most_common() for i, j in data_dic.items()}

    os.chdir('..')
    s_hist = open('google_search_data.csv', 'w')
    s_hist_write = csv.writer(s_hist)

    for i, j in sorted(c.items(), reverse=True):
        s_hist_write.writerow(" ")
        s_hist_write.writerow([i])
        s_hist_write.writerow(" ")

        for k in j:
            x = ' : '.join(map(str, k))
            s_hist_write.writerow(x.split(" : "))


def main():

    parser = argparse.ArgumentParser()

    parser.add_argument('--y', help='calls YouTube data history parser')
    parser.add_argument('--g', help='calls Google search data history parser')

    args = parser.parse_args()

    if args.y:
        YouTubeData()

    if args.g:
        GoogleSearchData()

    if not args.y or args.g:
        YouTubeData()
        GoogleSearchData()


if __name__ == '__main__':
    main()
