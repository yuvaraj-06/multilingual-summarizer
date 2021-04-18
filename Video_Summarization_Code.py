from threading import Thread
import requests
global a,b
a=0
b=0
import base64
from moviepy.editor import *
url = "https://proxy.api.deepaffects.com/audio/generic/api/v1/async/asr"
#"https://webhook.site/9a465f54-10e2-44a7-b8d6-989c17c9bf50"
#
""""
audio_file_name=""##ENTER YOUR FILE PATH


clipA = VideoFileClip("apple.mp4")
clipB = VideoFileClip("apple.mp4")
clipC = VideoFileClip("apple.mp4")
clipD = VideoFileClip("apple.mp4")

import moviepy.editor as mp
def a():
    clip1 = clipA.subclip(62.4, 694)
    clip1.write_videofile("clip1.mp4")
    clipa = mp.VideoFileClip(r"clip1.mp4")
    clipa.audio.write_audiofile(r"mit1.wav")

def b():
    clip2 = clipB.subclip(694, 1414)
    clip2.write_videofile("clip2.mp4")
    clipb = mp.VideoFileClip(r"clip2.mp4")
    clipb.audio.write_audiofile(r"mit2.wav")
def c():
    clip3 = clipC.subclip(1414, 2134)
    clip3.write_videofile("clip3.mp4")
    clipc = mp.VideoFileClip(r"clip3.mp4")
    clipc.audio.write_audiofile(r"mit3.wav")
def d():
    clip4 = clipD.subclip(2134, 2854.8)
    clip4.write_videofile("clip4.mp4")
    clipd = mp.VideoFileClip(r"clip4.mp4")
    clipd.audio.write_audiofile(r"mit4.wav")
a1=Thread(target =a)
a2=Thread(target =b)
a3=Thread(target =c)
a4=Thread(target =d)
a1.start()
a2.start()
a3.start()
a4.start()
a1.join()
a2.join()
a3.join()
a4.join()
"""
#Test: Final11: sample rate 1411000, enableSpeakerDiarization": False,audioType": "meeting
#Test2: Final12: sample rate 1411000, enableSpeakerDiarization": False,audioType": "meeting, lang: eng-GB
#Test3: Final13: sample rate 44100, enableSpeakerDiarization": False,audioType": "meeting,lang: eng-GB (uk)
#Test4: Final14: sample rate 44100, enableSpeakerDiarization": False,audioType": "meeting,lang: eng-US

def one():
    querystring1 = {"apikey": "94e0kF5RyJWQpSwKl4WIdsjHIwjE8Q6m",
                    "webhook": "https://webhook.site/729fb752-49b8-4157-b7d8-c174be6ca8b2"}
    audio_file_name1 = "mit1.wav"
    with open(audio_file_name1, 'rb') as fin1:
        audio_content1 = fin1.read()

    payload1 = {"content":base64.b64encode(audio_content1).decode('utf-8'),"encoding": "WAV", "languageCode": "en-US", "sampleRate": 44100, "audioType": "meeting",
               "enableSpeakerDiarization": False, "enablePunctuation": True}

    #payload["content"] = base64.b64encode(audio_content1).decode('utf-8')
    headers = {
        'Content-Type': "application/json",
    }
    response = requests.post(url, json=payload1, headers=headers, params=querystring1)
    print(response.text)
def two():
    querystring2 = {"apikey": "Due2ogG7EZnO9SS94SDNlsycExyqBHCh","webhook": "https://webhook.site/9a465f54-10e2-44a7-b8d6-989c17c9bf50"}
    audio_file_name2 = "mit2.wav"
    with open(audio_file_name2, 'rb') as fin2:
        audio_content2 = fin2.read()

    payload2 = {"content": base64.b64encode(audio_content2).decode('utf-8'), "encoding": "WAV", "languageCode": "en-US",
                "sampleRate": 44100, "audioType": "meeting",
                "enableSpeakerDiarization": False, "enablePunctuation": True}

    #payload["content"] = base64.b64encode(audio_content2).decode('utf-8')
    headers = {
        'Content-Type': "application/json",
    }
    response = requests.post(url, json=payload2, headers=headers, params=querystring2)
    print(response.text)
def three():
    querystring3 = {"apikey": "zRTp8hBJQfKqYm5KVlSszM2puHVdw2y4","webhook": "https://webhook.site/06968693-ad08-4072-b428-be7c8cce6b4a"}

    audio_file_name3 = "mit3.wav"
    with open(audio_file_name3, 'rb') as fin3:
        audio_content3 = fin3.read()
    payload3 = {"content": base64.b64encode(audio_content3).decode('utf-8'), "encoding": "WAV", "languageCode": "en-US",
                "sampleRate": 44100, "audioType": "meeting",
                "enableSpeakerDiarization": False, "enablePunctuation": True}

    #payload["content"] = base64.b64encode(audio_content3).decode('utf-8')
    headers = {
        'Content-Type': "application/json",
    }
    response = requests.post(url, json=payload3, headers=headers, params=querystring3)
    print(response.text)
def four():
    querystring4 = {"apikey": "flAjWIPLD6uq9y1c9Cpdp5y9JGSfrHZA","webhook": "https://webhook.site/10a1676d-29b6-46b0-8809-5e91f72b8b97"}
    audio_file_name4 = "mit4.wav"
    with open(audio_file_name4,'rb') as fin4:
        audio_content4 = fin4.read()
    payload4 = {"content": base64.b64encode(audio_content4).decode('utf-8'), "encoding": "WAV", "languageCode": "en-US",
                "sampleRate": 44100, "audioType": "meeting",
                "enableSpeakerDiarization": False, "enablePunctuation": True}

    #payload["content"] = base64.b64encode(audio_content4).decode('utf-8')
    headers = {
        'Content-Type': "application/json",
    }
    response = requests.post(url, json=payload4, headers=headers, params=querystring4)
    print(response.text)
flag=False
print("started")
t1=Thread(target =one)
t2=Thread(target =two)
t3=Thread(target =three)
t4=Thread(target =four)
t1.start()
t2.start()
t3.start()
t4.start()
t1.join()
t2.join()
t3.join()
t4.join()
def run1():
    import webscrap
def run2():
   import webscrap2
def run3():
    import webscrap3
def run4():
    import webscrap4

r1=Thread(target =run1)
r2=Thread(target =run2)
r3=Thread(target =run3)
r4=Thread(target =run4)
r1.start()
r2.start()
r3.start()
r4.start()
r1.join()
r2.join()
r3.join()
r4.join()
def sum():
    import wikipedia
    from fuzzywuzzy import process
    from fuzzywuzzy import fuzz
    import copy
    import numpy as np
    def superImportant(topic):

        content = wikipedia.summary(topic)
        pageObj = wikipedia.WikipediaPage(topic)

        hyperLinks1 = []
        nonhyperLinks = content.split()
        for words2 in pageObj.links:
            if words2 in content:
                hyperLinks1.append(words2)

        contentWords = list(set(copy.deepcopy(hyperLinks1) + nonhyperLinks))

        fails = 0

        for words in hyperLinks1:
            try:
                content = wikipedia.summary(words)
                pageObj = wikipedia.WikipediaPage(words)
                count = 0
                for words2 in pageObj.links:
                    if words2 in content:
                        contentWords.append(words2)
                        count += 1
                    if count >= 1 * len(hyperLinks1):
                        break
            except:
                fails += 1

        contentWords = set((" ".join(contentWords)).split())
        return contentWords


    def changePriorities(dic, mapWords):
        frequencies = []
        for k, v in dic.items():
            frequencies.append(v)
        X = copy.deepcopy(np.percentile(np.array(frequencies), 95))

        misMatches = 0
        for words in mapWords:
            if words in dic.keys():
                dic[words] = X
            elif words.lower() in dic.keys():
                dic[words.lower()] = X
            else:
                misMatches += 1

        return dic, misMatches


    # JUST RUN THIS CELL

    import copy
    import nltk
    import numpy as np
    import string
    from sklearn.feature_extraction.text import CountVectorizer
    from nltk.corpus import stopwords
    from fuzzywuzzy import process
    from fuzzywuzzy import fuzz
    from scipy import stats
    import matplotlib.pyplot as plt
    nltk.download('wordnet')
    nltk.download('stopwords')
    def chunk(sourceFile, wordsPerLine=None, endLineAt=None):
        fi = open(sourceFile, "r+")
        text = fi.read()
        text = text.replace("\n", "")

        if wordsPerLine != None:
            text = text.split()
            for words in range(1, len(text) + 1):
                if words % 3 == 0:
                    text[words - 1] = text[words - 1] + "\n"
            fi.seek(0)
            fi.write(" ".join(text))
        if endLineAt != None:

            for words in endLineAt:
                text = text.split(words)
                text = "\n".join(text)

            fi.seek(0)
            fi.write(text)

        fi.close()
        return


    def getKey(D, val):
        for key, value in D.items():
            if val == value:
                return key
        return -1


    def completeFiltering(singleStringTxt, multiLineTxt, limitOnFreq, limitOnDataW=10000):
        wholeText = singleStringTxt
        cleansed = wholeText.split()[:limitOnDataW]
        table = str.maketrans("", "", string.punctuation)
        cleansed = [w.translate(table) for w in cleansed]
        patched = " ".join(cleansed)
        cleansed = patched.split()
        cleansed = [words for words in cleansed if not words.lower() in stopwords.words()]

        cleansedTxt = " ".join(cleansed)

        wholeText = [cleansedTxt]
        lineWiseText = multiLineTxt

        # list of text documents
        # create the transform
        vectorizer1 = CountVectorizer()
        vectorizer2 = CountVectorizer()
        # tokenize and build vocab
        vectorizer1.fit(wholeText)
        vectorizer2.fit(lineWiseText)

        # summarize
        wToInd1 = vectorizer1.vocabulary_
        wToInd2 = vectorizer2.vocabulary_
        # encode document
        vector1 = vectorizer1.transform(wholeText)
        vector2 = vectorizer2.transform(lineWiseText)
        # summarize encoded vector
        v1 = vector1.toarray()
        v2 = vector2.toarray()

        finalCount = np.sum(v1, axis=0, keepdims=False)

        countDict1 = dict()

        countDict2 = dict()
        priorities2 = dict()
        for ind in range(len(finalCount)):
            if finalCount[ind] >= limitOnFreq:
                countDict1[getKey(wToInd1, ind)] = finalCount[ind]

        for lines in range(v2.shape[0]):
            countDict = dict()
            for ind in range(v2.shape[1]):
                if v2[lines][ind] >= limitOnFreq:
                    countDict[getKey(wToInd2, ind)] = v2[lines][ind]

            priorities = sorted(countDict, key=countDict.get, reverse=True)

            countDict2[str(lines + 1)] = countDict
            priorities2[str(lines + 1)] = priorities

        contentWords = superImportant("Apple Inc")
        countDict1, misMatch = changePriorities(countDict1, contentWords)
        print("These many got mismatched : ", misMatch)

        priorities1 = sorted(countDict1, key=countDict1.get, reverse=True)

        return priorities1, priorities2, countDict1, countDict2


    def fuzzyWayCondense(fileSource, priorities1, priorities2, prioritiesMap1, prioritiesMap2, limitOnLines=3,
                         limitOnDataL=100, method="Frequency", printLineScores=False):
        if method == "Frequency":
            priorities = priorities1
            prioritiesMap = prioritiesMap1
        elif method == "TF-IDF":
            priorities = priorities1
            prioritiesMap = prioritiesMap1
            prioritiesMapext = prioritiesMap2
            includeTFIDF = np.zeros((limitOnDataL, len(priorities)))
        fi = open(fileSource, "r")
        include = np.zeros((limitOnDataL, len(priorities)))

        wholeLines = fi.readlines()[:limitOnDataL]
        maintain = dict()

        for lines in range(1, limitOnDataL + 1):
            maintain[str(lines)] = []

        fi.close()

        for words in priorities:
            options = process.extract(words, wholeLines, limit=limitOnDataL)
            for line, score in options:

                if (words in line.split()) and method == "Frequency":
                    maintain[str(wholeLines.index(line) + 1)].append(words)
                    include[wholeLines.index(line)][priorities.index(words)] = score * prioritiesMap[words]
                elif (words in line.split()) and method == "TF-IDF":
                    maintain[str(wholeLines.index(line) + 1)].append(words)
                    includeTFIDF[wholeLines.index(line)][priorities.index(words)] = \
                    prioritiesMapext[str(wholeLines.index(line) + 1)][words] * prioritiesMap[words]
        if method == "TF-IDF":

            includeTFIDF = list(np.sum(includeTFIDF, axis=0))

            for words in priorities:
                options = process.extract(words, wholeLines, limit=limitOnDataL)
                for line, score in options:

                    if (words in line.split()):
                        include[wholeLines.index(line)][priorities.index(words)] = score * includeTFIDF[
                            priorities.index(words)]

        for lines in range(1, limitOnDataL + 1):
            maintain[str(lines)] = set(maintain[str(lines)])

        include = list(np.sum(include, axis=1))
        includeTemp = np.array(copy.deepcopy(include))

        if printLineScores == True:
            print("\nThe Scores of the Sentences from 1 to", limitOnDataL, " are as follows \n", include)
            print("\nThe Key Words Per Line for all the lines are : \n", maintain)

        condensedLines = []
        condensedLinesIndices = []
        if limitOnLines != "NormSTDPick":
            includeTemp = (np.sort(includeTemp))[::-1]
            for i in range(limitOnLines):
                condensedLines.append(wholeLines[include.index(includeTemp[i])])
                condensedLinesIndices.append(include.index(includeTemp[i]) + 1)
                include[include.index(includeTemp[i])] = -1
        else:
            includeTemp = np.array([(value >= np.percentile(includeTemp, 50)) for value in includeTemp]).astype(int)
            includeTemp = np.reshape(np.argwhere(includeTemp), (-1,)) + 1
            condensedLines = [wholeLines[i - 1] for i in includeTemp]
            condensedLinesIndices = includeTemp

        condensedText = " ".join(condensedLines)

        return condensedText, condensedLines, condensedLinesIndices


    import json

    T1path = "final1.txt"  # "/content/drive/My Drive/transcript1"
    T2path = "final2.txt"  # "/content/drive/My Drive/transcript2"
    T3path = "final3.txt"  # "/content/drive/My Drive/transcript3"
    T4path = "final4.txt"  # "/content/drive/My Drive/transcript4"
    Tpath = "1.txt"  # "/content/drive/My Drive/entireTranscript.txt"

    transcript = ""
    tpt1 = open(T1path, "r")
    T1 = tpt1.read()
    T1dict = eval(T1)
    tpt1.close()

    tpt2 = open(T2path, "r")
    T2 = tpt2.read()
    T2dict = eval(T2)
    tpt2.close()

    tpt3 = open(T3path, "r")
    T3 = tpt3.read()
    T3dict = eval(T3)
    # T3dict = json.loads(T3dict.decode("utf-8"))
    tpt3.close()

    tpt4 = open(T4path, "r")
    T4 = tpt4.read()
    T4dict = eval(T4)
    # T4dict = json.loads(T4dict.decode("utf-8"))
    tpt4.close()

    transcript += T1dict["response"]["transcript"]
    transcript += T2dict["response"]["transcript"]
    transcript += T3dict["response"]["transcript"]
    transcript += T4dict["response"]["transcript"]

    tpt = open(Tpath, "w")
    tpt.write(transcript)
    tpt.close()

    # tpt  = open(Tpath,"r")
    Tdicts = [T1dict, T2dict, T3dict, T4dict]
    # print(tpt.read())

    # RUN THIS CELL WITH SPECIFIED PATH TO LOAD ALL THE TEXT FILE AS STRING INTO "wholeText" AND TEXT FILE AS LINES INTO "lineWiseText"

    # path = "/content/drive/My Drive/TedTranscript.txt" #Path of the file from the drive
    path = Tpath  # "/content/drive/My Drive/entireTranscript.txt"

    chunk(path, endLineAt=[".", "?"])

    fi = open(path, "r")
    wholeText = fi.read()
    fi.seek(0)
    totalWords = len((fi.read()).split())
    fi.seek(0)
    totalLines = len(fi.readlines())
    fi.seek(0)
    lineWiseText = fi.readlines()
    fi.close()

    # print("Total Lines present in the Source File is : ", totalLines)
    # print("Total Words present in the source File is : ", totalWords)

    # "completeFiltering" func takes "wholeText", "lineWiseText", "limitOnFreq" (let this be unchanged), "limitOnDataW" (this equals the "totalWords" in above cell)
    # "completeFiltering" func returns priorities1,2 and countDict1,2 which are used more for internal purposes so I'm hiding these outputs
    priorities1, priorities2, countDict1, countDict2 = completeFiltering(wholeText, lineWiseText, limitOnFreq=1,
                                                                         limitOnDataW=totalWords)

    # print("\nTop Prior Words of 10K Words data : ", priorities1)
    # print("\nTop Prior Words of every Line data : ", priorities2)

    # "fuzzyWayCondense" func takes "path", "priorities1,2", "countDict1,2", "limitOnLines" (this is can be anything <= "totalLines"), "limitonDataL"(this equals the "totalLines" in above cell), "method" (let it be unchanged), "printLineScores"(let it be False setting it to True just prints scores which are of no use to u)
    # "fuzzyWayCondense" func returns "condensedText"(optional use to u), "condensedLines"(optional use to u just gives list of line strings) ,"condensedLinesIndices1(u might need this)"
    condensedText, condensedLines, condensedLinesIndices1 = fuzzyWayCondense(path, priorities1, priorities2, countDict1,
                                                                             countDict2, limitOnLines="NormSTDPick",
                                                                             limitOnDataL=totalLines, method="TF-IDF",
                                                                             printLineScores=False)
    print("\nThis is the TF-IDF Way : \n")
    print("\nThe Original Lines which made thorugh the filtering process  are the line numbers : \n",
          condensedLinesIndices1)
    # print("\nOverall the condensed Text : \n", condensedText)

    # "fuzzyWayCondense" func takes "path", "priorities1,2", "countDict1,2", "limitOnLines" (this is can be anything <= "totalLines"), "limitonDataL"(this equals the "totalLines" in above cell), "method" (let it be unchanged), "printLineScores"(let it be False setting it to True just prints scores which are of no use to u)
    # "fuzzyWayCondense" func returns "condensedText"(optional use to u), "condensedLines"(optional use to u just gives list of line strings) ,"condensedLinesIndices2(u might need this)"
    # condensedText, condensedLines, condensedLinesIndices2 = fuzzyWayCondense(path,priorities1, priorities2,countDict1, countDict2, limitOnLines="NormSTDPick", limitOnDataL = totalLines, method = "Frequency", printLineScores=False)
    # print("\nThis is the Frequency Way : \n")
    # print("\nThe Original Lines which made thorugh the filtering process  are the line numbers : \n", condensedLinesIndices2)
    # print("\nOverall the condensed Text : \n", condensedText)

    # "finalSet" gives union of results of both methods
    # finalSet =  set(condensedLinesIndices1).union(set(condensedLinesIndices2))
    finalSet = set(condensedLinesIndices1)
    print("\nConsider these lines as Important : ", finalSet)
    print("\nPercentage of Condensation of initial Text is : {:.4f}%".format(
        ((totalLines - len(finalSet)) / totalLines) * 100))

    Jsonpath = "2.txt"  # "/content/drive/My Drive/entireJasonObj.txt"

    correction = 0
    for transcripts in range(4):
        for times in Tdicts[transcripts]["response"]["words"]:
            times["start"] = times["start"] + correction
            times["end"] = times["end"] + correction
            mark = times["end"]

        correction = mark

    jsonObjs = {"response": dict()}
    jsonObjs["response"]["words"] = T1dict["response"]["words"] + T2dict["response"]["words"] + T3dict["response"][
        "words"] + T4dict["response"]["words"]
    jsonObjs = str(jsonObjs)
    json = open(Jsonpath, "w")
    json.write(jsonObjs)
    json.close()

    pathr = Jsonpath  # "/content/drive/My Drive/tedxtJasonObject" # PATH TO THE TEXT FILE CONTAINING JASON OBJECT (DICTIONARY OF REQUEST ID, RESPONSE, TIMESTAMPS OF WORDS ....)
    fi = open(pathr, "r")
    fullDataDict = eval(fi.read())


    def convert(seconds):
        seconds = seconds % (24 * 3600)
        hour = seconds // 3600
        seconds %= 3600
        minutes = seconds // 60
        seconds %= 60

        return "%d:%02d:%02d" % (hour, minutes, seconds)


    wholeWords = wholeText.split()
    wholeLines = lineWiseText
    prevWordsCount = dict()
    wds = 0
    for sen in wholeLines:
        prevWordsCount[str(wholeLines.index(sen) + 1)] = wds
        wds += len(sen.split())

    timeStamps = dict()

    for line in finalSet:

        try:
            startInd = prevWordsCount[str(line)]
            endInd = prevWordsCount[str(line + 1)] - 1
            # USE "convert" if u need the output time stamps to be in HH:MM:SS if not remove "convert"
            timeRange = (
            fullDataDict["response"]["words"][startInd]["start"], fullDataDict["response"]["words"][endInd]["end"])
            timeStamps[int(line)] = timeRange
            count = 1
        except:
            print("")

    c = 0
    Stamps = []
    for line in sorted(timeStamps):
        c += 1
        Stamps.append(timeStamps[line])
    print(Stamps)
    V = []
    clip = VideoFileClip("apple.mp4")
    for t in range(0, len(Stamps)):
        a = Stamps[t][0]
        b = Stamps[t][1]
        clipx = clip.subclip(a, b)
        V.append(clipx)
    # x concatinating both the clips
    final = concatenate_videoclips(V)
    final.write_videofile("apple.avi",codec='rawvideo')