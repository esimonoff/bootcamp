def reverse_complement(seq, material='DNA'):
    """Take `seq` and return its complement"""

    # Initialize rev_seq to lowercase seq
    rev_seq = seq.lower()

    # Create the reverse complement from the reverse sequence
    rev_seq = rev_seq.replace('a','T')
    rev_seq = rev_seq.replace('t','A')
    rev_seq = rev_seq.replace('c','G')
    rev_seq = rev_seq.replace('g','C')

    return rev_seq[::-1]
