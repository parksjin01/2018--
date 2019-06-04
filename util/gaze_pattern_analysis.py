import json

fixation = []
saccade = []
regression = []

filelist = ["p432-hassanieh.pdf2.json",
            "p432-hassanieh.pdf3.json",
            "p432-hassanieh.pdf4.json",
            "p432-hassanieh.pdf5.json",
            "p432-hassanieh.pdf6.json",
            "p432-hassanieh.pdf7.json"]

for fname in filelist:
    with open(fname, 'rt') as f:
        data = json.loads(f.read())

    for idx in range(len(data["start"])):
        fixation.append(int(data["end"][idx]) - int(data["start"][idx]))

    for idx in range(len(data["start"]) - 1):
        try:
            if int(data["class"][idx + 1]) >= int(data["class"][idx]):
                saccade.append((int(data["class"][idx + 1]) - int(data["class"][idx])))
                # regression.append(0)
            else:
                regression.append((int(data["class"][idx]) - int(data["class"][idx + 1])))
                # saccade.append(0)
        except:
            print int(data["start"][idx + 1]), int(data["end"][idx])

print fixation
print saccade
print regression

##################################### K-mean & Graph #####################################

import matplotlib.pyplot as plt
import operator

def fixation_CDF(fixation):
    plt.clf()
    fixation_class = {50:0, 100:0, 150:0, 200:0, 250:0, 300:0, 350:0, 400:0, 500:0, 600:0, 700:0, 800:0, 900:0, 1000:0}
    for fix in fixation:
        for idx in range(len(fixation_class.keys())):
            if fixation_class.keys()[idx] > fix:
                fixation_class[fixation_class.keys()[idx]] += 1
    print len(fixation)
    print fixation_class
    for k in fixation_class.keys():
        fixation_class[k] /= float(len(fixation))

    fixation_class = sorted(fixation_class.items(), key=operator.itemgetter(0))

    key = [0]
    value = [0]

    for k, v in fixation_class:
        key.append(k)
        value.append(v)

    plt.axvline(300, color="r", linestyle="--")
    plt.plot(key, value, label="fixation duration")
    plt.xlabel("duration")
    plt.ylabel("CDF")
    plt.title("Fixation duration CDF")
    plt.grid(True)
    plt.savefig("graph/fixation_cdf")

def fixation_graph(fixation):
    plt.clf()
    plt.axhline(300, color='r', linestyle='--')
    plt.plot(range(len(fixation)), fixation, label="fixation")
    plt.xlabel("reading time")
    plt.ylabel("Fixation")
    plt.savefig("graph/fixation")

def saccade_CDF(saccade):
    plt.clf()
    saccade_class = {3:0, 5:0, 7:0, 9:0, 11:0, 13:0, 15:0, 17:0, 19:0, 21:0, 23:0, 25:0, 27:0, 29:0}
    for fix in saccade:
        for idx in range(len(saccade_class.keys())):
            if saccade_class.keys()[idx] > fix:
                saccade_class[saccade_class.keys()[idx]] += 1
    print len(saccade)
    print saccade_class
    for k in saccade_class.keys():
        saccade_class[k] /= float(len(saccade))

    saccade_class = sorted(saccade_class.items(), key=operator.itemgetter(0))

    key = [0]
    value = [0]

    for k, v in saccade_class:
        key.append(k)
        value.append(v)

    plt.axvline(13, color="r", linestyle="--")
    plt.plot(key, value, label="saccade duration")
    plt.xlabel("duration")
    plt.ylabel("CDF")
    plt.title("Saccade CDF")
    plt.grid(True)
    plt.savefig("graph/saccade_cdf")
    
def saccade_graph(saccade):
    plt.clf()
    plt.axhline(13, color='r', linestyle='--')
    plt.plot(range(len(saccade)), saccade, label="saccade")
    plt.xlabel("reading time")
    plt.ylabel("Saccade CDF")
    plt.savefig("graph/saccade")
    
def regression_CDF(regression):
    plt.clf()
    regression_class = {3:0, 5:0, 7:0, 9:0, 11:0, 13:0, 15:0, 17:0, 19:0, 21:0, 23:0, 25:0, 27:0, 29:0}
    for fix in regression:
        for idx in range(len(regression_class.keys())):
            if regression_class.keys()[idx] > fix:
                regression_class[regression_class.keys()[idx]] += 1
    print len(regression)
    print regression_class
    for k in regression_class.keys():
        regression_class[k] /= float(len(regression))

    regression_class = sorted(regression_class.items(), key=operator.itemgetter(0))

    key = [0]
    value = [0]

    for k, v in regression_class:
        key.append(k)
        value.append(v)

    plt.axvline(13, color="r", linestyle="--")
    plt.plot(key, value, label="regression duration")
    plt.xlabel("duration")
    plt.ylabel("CDF")
    plt.title("Regression CDF")
    plt.grid(True)
    plt.savefig("graph/regression_cdf")

def regression_graph(regression):
    plt.clf()
    plt.plot(range(len(regression)), regression, label="regression")
    plt.xlabel("reading time")
    plt.ylabel("Regression")
    plt.savefig("graph/regression")

fixation_CDF(fixation)
fixation_graph(fixation)
saccade_CDF(saccade)
saccade_graph(saccade)
regression_CDF(regression)
regression_graph(regression)

print len(fixation)
print data["class"]
print sum(fixation)/len(fixation)
print sum(saccade)/len(saccade)
print sum(regression)/len(regression)
print sum(regression)/float(sum(saccade) + sum(regression))
print (sum(saccade) + sum(regression))/(len(saccade) + len(regression))