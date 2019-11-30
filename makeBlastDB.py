import re
def readfile(filename,k):
    file=open(filename)
    text=file.read()
    text=text.split(">")
    text.remove('')
    for x in text:
        seqName,sequence=x.split("\n",maxsplit=1)
        print(seqName,sequence)
        makeSubsets(seqName,sequence,k)

def makeSubsets(seqName,sequence,k):
    for position in range(0,len(sequence)-k+1):
        print(seqName,sequence[position:position+k],position)
if __name__ == '__main__':
    k=5
    filename='basic test seq.txt'
    readfile(filename,k)