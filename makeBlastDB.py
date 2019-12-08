def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1
id=file_len("Database.csv")
def readFile(filename,k):
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
    database=open("Database.csv",mode='a')
    for position in range(0,len(sequence)-k+1):
        subsequence=sequence[position:position+k]
        line=str(id)+','+subsequence+','+seqName+','+str(position)+','+str(k)+'\n'
        database.write(line)
        id+=1
    database.close()

if __name__ == '__main__':
    k=int(input("Enter the size of K-mer:"))
    filename='TEST Seq.txt'
    readFile(filename,k)
    print("Database updated successfully")