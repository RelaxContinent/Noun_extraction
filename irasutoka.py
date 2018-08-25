import subprocess as sp
import sys
sys.path.append("c:/users/tiger/appdata/local/programs/python/python36-32/lib/site-packages")


def mymecab(str):
    a=sp.Popen(["mecab","-E  """],shell=True,stdin=sp.PIPE,stdout=sp.PIPE)
    a.stdin.write(str.encode("sjis"))
    a.stdin.close()
    a.wait()
    return(a.stdout.read().decode("sjis"))

def writing_data():
    word_list={}
    str=input()
    separate_topic=mymecab(str).split("\n")
    for i in separate_topic:
        if(i!='  '):
            if (i.split("\t")[1].split(",")[1] == "一般"):
                if(i.split("\t")[1].split(",")[0]=="名詞"):
                    if(i.split("\t")[0] in word_list):
                        word_list[i.split("\t")[0]] += 1
                    else:
                        word_list[i.split("\t")[0]]=1
                    #print(i.split("\t")[0])
    return word_list
while(True):
    print(writing_data())
