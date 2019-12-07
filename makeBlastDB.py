id=1
def makeSubsets(seqName,sequence,k):
    global id
    sequence=sequence.replace('\n','')
    database=open("Database.csv",mode='a')
    for position in range(0,len(sequence)-k+1):
        subsequence=sequence[position:position+k]
        line=str(id)+','+subsequence+','+seqName+','+str(position)+','+str(k)+'\n'
        database.write(line)
        id+=1
    database.close()

if __name__ == '__main__':
    k=3
    filename='TEST Seq.txt'
    queryFile = open(filename)
    line=queryFile.readline()
    name=''
    sequence=''
    while line:
        if(line[0]=='>'):
            makeSubsets(name,sequence,k)
            name=line[1:-1]
            sequence=''
        else:
            sequence+=line
        line=queryFile.readline()
    makeSubsets(name, sequence, k)
    print("Database updated successfully")