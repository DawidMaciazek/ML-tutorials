import matplotlib
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import matplotlib.dates as mdates

import numpy as np

import time

PATTERN_AVE_LENGTH = 11

date, bid, ask = np.loadtxt('data/GBPUSD1d.txt', unpack=True,
                            delimiter=',',
                            converters={0:mdates.strpdate2num('%Y%m%d%H%M%S')})

ave_line = ((bid+ask)*0.5)

pattern_arr = []
performance_arr = []
pattern_for_rec = [None]*10

def percent_change(start_point, current_point):
    return 100.0*(current_point - start_point)/abs(start_point)

def pattern_storage():
    start_time = time.time()

    x = len(ave_line)

    points_number = 10
    pattern = [None]*points_number

    for y in xrange(PATTERN_AVE_LENGTH,x):
        for i in reversed(range(points_number)):
            pattern[i] = percent_change(ave_line[y-10], ave_line[y-i])

        outcome_range = ave_line[y+20:y+30]
        current_point = ave_line[y]

        try:
            if outcome_average:
                outcome_average = np.average(outcome_range)
            else:
                outcome_average = 0.0
        except Exception, e:
            print str(e)
            outcome_average = 0.0

        outcome_future = percent_change(current_point, outcome_average)

        pattern_arr.append(pattern[:])
        performance_arr.append(outcome_future)

    end_time = time.time() - start_time
    print("Total storage time: {}s".format(end_time))


def load_raw_fx():
   #                            converters={0:mdates.strpdate2num('%Y%m%d%H%M%S')})

    fig = plt.figure(figsize=(10,7))
    ax1 = plt.subplot2grid((40,40), (0,0), rowspan=40, colspan=0)

    ax1.plot(date, bid)
    ax1.plot(date, ask)
    plt.gca().get_yaxis().get_major_formatter().set_useOffset(False)

    ax1.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m-%d %H:%M:%S"))
    for label in ax1.xaxis.get_ticklabels():
        label.set_rotation(45)

    ax1_2 = ax1.twinx()
    ax1_2.fill_between(date, 0, (ask-bid), facecolor='g', alpha=.3)

    plt.subplots_adjust(bottom=.23)

    plt.grid(True)
    plt.show()


def current_pattern():
    for i, j in zip(range(10), range(-10,0)):
        pattern_for_rec[i] = percent_change(ave_line[-11], ave_line[j])

    print pattern_for_rec

def pattern_recognition():
    sim = np.empty(10, dtype=float)
    print "start"
    for each_pattern in pattern_arr:
        for i in range(10):
            sim[i] = 100.0 - abs(percent_change(each_pattern[i], pattern_for_rec[i]))
        how_sim = np.average(sim)

        if how_sim > 70.0:
            pattern_index = pattern_arr.index(each_pattern)
            print "==========================="
            print pattern_for_rec
            print each_pattern
            print 'prediceted outcome: {}'.format(performance_arr[pattern_index])
            print "==========================="
    print "END"


pattern_storage()
current_pattern()
pattern_recognition()

