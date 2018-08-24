import subprocess as sp
import sys
sys.path.append("mecabのパス")


def mymecab(str):
    a=sp.Popen(["mecab","-E  """],shell=True,stdin=sp.PIPE,stdout=sp.PIPE)
    a.stdin.write(str.encode("sjis"))
    a.stdin.close()
    a.wait()
    return(a.stdout.read().decode("sjis"))

def writing_data():
    str=input()
    separate_topic=mymecab(str).split("\n")
    for i in separate_topic:
        if(i!='  '):
            if (i.split("\t")[1].split(",")[1] == "一般"):
                if(i.split("\t")[1].split(",")[0]=="名詞"):
                    print(i.split("\t")[0])
while(True):
    writing_data()
