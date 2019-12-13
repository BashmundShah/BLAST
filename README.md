# BLAST
A scaled down version of Basic Local Alignment Search Tool.
MakeBlastDB script requires 2 inputs 'k:size of k-mer' and 'input sequence file'.
Its output is a database file numbered by the k-mer size

BLASTonQuerySequence takes two inputs as well i.e. kmersize and query sequence.
It should be ensured that the database file for the given kmer size exists already.
It returns an output file that shows the matching subsequences between query sequences and database sequences.
