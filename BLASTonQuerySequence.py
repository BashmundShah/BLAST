import pandas as pd

qdf = pd.DataFrame(columns=['Sequence', 'SeqName', 'Position', 'Kmer_Size'])
id = 1


def processDataframe(df):
    output = pd.DataFrame(columns=['S.no', 'QuerySeqID', '#ofMatchingKmers', 'startPosX',
                                   'endPosX', 'TotalLenX', 'DatabaseSeqID', 'startPosY',
                                   'EndPosY', 'TotalLenY'])
    n = len(df)
    print(qdf)
    nKmers = 1
    startPos_x = -1
    lastPos_x = 0
    startPos_y = -1
    lastPos_y = 0
    for i in range(1, n):
        if (startPos_x < 0) & (startPos_y < 0):
            startPos_x = df['Position_x'].iloc[i - 1]
            startPos_y = df['Position_y'].iloc[i - 1]
        if (df['Position_x'].iloc[i] == df['Position_x'].iloc[i - 1] + 1) and (
                df['Position_y'].iloc[i] == df['Position_y'].iloc[i - 1] + 1):
            nKmers += 1
        else:
            lastPos_x = df['Position_x'].iloc[i - 1] + k - 1
            lastPos_y = df['Position_y'].iloc[i - 1] + k - 1
            global id
            output.loc[len(output) + 1] = [id, df['SeqName_x'].iloc[i - 1], nKmers, startPos_x, lastPos_x,
                                           nKmers + k - 1, df['SeqName_y'].iloc[i - 1], startPos_y,
                                           lastPos_y, nKmers + k - 1]
            id += 1
            startPos_x = df['Position_x'].iloc[i]
            startPos_y = df['Position_y'].iloc[i]
            lastPos_x = 0
            lastPos_y = 0
            nKmers = 1
            if(i==n-1):
                lastPos_x = df['Position_x'].iloc[i] + k - 1
                lastPos_y = df['Position_y'].iloc[i] + k - 1
                output.loc[len(output) + 1] = [id, df['SeqName_x'].iloc[i], nKmers, startPos_x, lastPos_x,
                                               nKmers + k - 1, df['SeqName_y'].iloc[i], startPos_y,
                                               lastPos_y, nKmers + k - 1]
    output.to_csv('OutputFiles\outputFile_'+str(k)+'.csv', index=0)


def createQueryDF(filename, k):
    file = open(filename)
    names = []
    name = ''
    sequence = ''
    line = file.readline()
    while line:
        if (line[0] == ">"):
            createQueryKmers(name, sequence, k)
            name = line[1:-1]
            names.append(name)
            sequence = ''
        else:
            sequence += line
        line = file.readline()
    createQueryKmers(name, sequence, k)
    file.close()
    return names


def createQueryKmers(name, sequence, k):
    sequence = sequence.replace('\n', '')
    for position in range(0, len(sequence) - k + 1):
        subsequence = sequence[position:position + k]
        qdf.loc[len(qdf) + 1] = [subsequence, name, position+1, k]


if __name__ == '__main__':
    k = 4
    queryFile = "querySequence.txt"
    names = createQueryDF(queryFile, k)
    for chunk in pd.read_csv("Database/Database_" + str(k) + ".csv", chunksize=5000, index_col=0):
        db = chunk[chunk['SeqName'] != names[0]]
        qdf = pd.merge(qdf, db, on=['Sequence'])
        qdf = qdf.sort_values(['SeqName_x', 'SeqName_y'])
        processDataframe(qdf)
