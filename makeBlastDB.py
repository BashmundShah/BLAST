import os.path as path
k=7
def file_len(fname):
    i=0
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1
id=0
try:
    id=file_len("Database/Database_"+str(k)+".csv")
except IOError:
    id=0

def readFile(filename,k):
    if path.exists("Database/Database_"+str(k)+".csv") is False:
        database = open("Database/Database_" + str(k) + ".csv", mode='a')
        line = "ID,Sequence,SeqName,Position\n"
        database.write(line)
        database.close()
    queryFile = open(filename)
    line = queryFile.readline()
    name = ''
    sequence = ''
    i=1
    while line:
        if (line[0] == '>'):
            makeSubsets(name, sequence, k)
            name = line[1:-1]
            print("Sequence ",i," done...")
            i+=1
            sequence = ''
        else:
            sequence += line
        line = queryFile.readline()
    makeSubsets(name, sequence, k)
def makeSubsets(seqName,sequence,k):
    global id
    sequence=sequence.replace('\n','')
    database=open("Database/Database_"+str(k)+".csv",mode='a')
    for position in range(0,len(sequence)-k+1):
        subsequence=sequence[position:position+k]
        line=str(id)+','+subsequence+','+seqName+','+str(position+1)+'\n'
        database.write(line)
        id+=1
    database.close()

if __name__ == '__main__':
    filename= 'inputSequenceforDB.txt'
    readFile(filename,k)
    print("Database updated successfully")