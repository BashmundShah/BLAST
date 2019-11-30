import pandas as pd

df = pd.DataFrame(columns=['Sequence', 'SeqName', 'Position', 'Kmer_Size'])

def readfile(filename,k):
    file=open(filename)
    text=file.read()
    text=text.split(">")
    text.remove('')
    i=1
    for x in text:
        seqName,sequence=x.split("\n",maxsplit=1)
        sequence=sequence.replace('\n','')
        print(i,sequence)
        i+=1
        makeSubsets(seqName,sequence,k)

def makeSubsets(seqName,sequence,k):
    for position in range(0,len(sequence)-k+1):
        subsequence=sequence[position:position+k]
        df.loc[len(df)+1]=[subsequence,seqName,position,k]
if __name__ == '__main__':
    k=7
    filename='TEST Seq.txt'
    readfile(filename,k)
    print(df)