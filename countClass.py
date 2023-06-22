import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-p','--path',type=str)
args = parser.parse_args()

path = args.path

file_lst = os.listdir(path)

fileCount=0

walking = 0
crouch = 0
lying = 0
text=[]
nullfile=[]
# for filename in file_lst:
#    with open("./guardian/labels/train/img_129.txt", 'r') as f:
#       print("./guardian/labels/train/img_129.txt")
#       for i in f.readline().split('\n'):
#         text.append(i)
#         print("시작:",text)
#         break
for filename in file_lst:
    with open(path+"/"+filename, 'r') as f:
        fileCount+=1
        print(filename)
        for i in f.readlines():
            text.append(list(map(float, i.rstrip().split(" "))))
        for i in range(len(text)):
            if text == []:
                nullfile.append(filename)
                continue
            elif int(text[i][0]) == 1:
                crouch+=1
            elif int(text[i][0]) == 2:
                lying+=1
            elif int(text[i][0]) == 0:
                walking+=1
        text=[]
            
print("walking: ",walking)
print("crouch: ", crouch)
print("lying: ", lying)
print("sum: ", walking+crouch+lying)
print("fileCount: ", fileCount)
print("누락된 파일 이름:", nullfile)
# if text == []:
            #     continue
            # elif int(text[0]) == 1:
            #     crouch+=1
            # elif int(text[0]) == 2:
            #     lying+=1
            # elif int(text[0]) == 0:
            #     walking+=1