checkClass = {}
checkVid_wrt = {}
tagStream={}
sendInfo={}
getCount={}
isSend=0

def addTagStream(key):
    global tagStream
    tagStream[key] = True
    #print("tagStream!!!!!!:",tagStream)

def setCheckClass(key, value, countDetect):
    global checkClass
    global getCount
    checkClass[key] = value
    getCount[key] = countDetect
    # print(key," cehckClassKey!!!!!!!!!!!!!!!:",checkClass[key])
def getCheckClass(key):
    # print(key,"GetCheckClass 체크 : ", checkClass.get(key))
    return checkClass.get(key)

def getCountClass(key):
    return getCount.get(key)

def setCheckVid_wrt(key, value):
    global checkVid_wrt
    checkVid_wrt[key] = value

def getCheckVid_wrt(key):
    return checkVid_wrt.get(key)

def setTagStream(key, value):
    global tagStream
    # print("TRUE OR FALSE : ", value)
    tagStream[key] = value

def getTagStream(key):
    print("tagStream :",tagStream)
    return tagStream.get(key)

def setIsSend(check, key, cam_name):
    global isSend
    global sendInfo
    isSend = check
    sendInfo[key] = [check, cam_name]

def getIsSend():
    return isSend