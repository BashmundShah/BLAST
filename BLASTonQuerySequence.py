import makeBlastDB as bdb
import pandas as pd
qdf=pd.DataFrame(columns=['Sequence','SeqName','Position','Kmer_Size'])
def createQueryDF(filename,k):
    file=open(filename)
    names=[]
    name=''
    sequence=''
    line=file.readline()
    while line:
        if(line[0]==">"):
            createQueryKmers(name,sequence,k)
            name=line[1:-1]
            names.append(name)
            sequence=''
        else:
            sequence+=line
        line=file.readline()
    createQueryKmers(name, sequence, k)
    file.close()
    return names

def createQueryKmers(name,sequence,k):
    sequence=sequence.replace('\n','')
    for position in range(0,len(sequence)-k+1):
        subsequence=sequence[position:position+k]
        qdf.loc[len(qdf)+1]=[subsequence,name,position,k]
if __name__ == '__main__':
    k=3
    queryFile="querySequence.txt"
    names=createQueryDF(queryFile,3)
    for chunk in pd.read_csv('Database.csv',chunksize=5000,index_col=0):
        db=chunk[chunk['SeqName']!=names[0]]
        qdf=pd.merge(qdf,db,on="Sequence")
    qdf=qdf.sort_values(['SeqName_y','Position_x'])
    qdf.to_csv('testresult.csv',index=0)
