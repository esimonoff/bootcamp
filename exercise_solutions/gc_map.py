def gc_map(seq, block_size, gc_thresh):
    """Take sequence, split it into blocks of a certain size, and determine GC
    content in each block. Function returns a string with blocks above a
    certain GC threshold in upper-case and blocks below that threshold in
    lower-case.
    """

    # Initialize empty list of blocks
    blocks = []

    # Initialize largest number of full blocks to test for GC content
    block_number = len(seq) // block_size

    # Initialize counter for block index
    block_index = 0

    # Create a list of block strings
    for i in range(0, (block_number * block_size), block_size):
        if block_index <= block_number:
            blocks.insert(block_index, str((seq[i:i+block_size])))
            block_index += 1

    # Initialize lists for saving GC content of each block
    gc_blocks_list = [0] * block_number
    gc_counter = [0] * block_number

    # Scan through each block and calculate GC content
    for i in range(len((blocks))):
        for base in blocks[i]:
            if base in 'GCgc':
                gc_counter[i] += 1
        gc_blocks_list[i] = gc_counter[i] / block_size

    # Create and populate a list for storing locations of blocks with GC values
    # above a certain threshold
    gc_bool = [0] * block_number
    for i, gc_content in enumerate(gc_blocks_list):
        if gc_content > gc_thresh:
            gc_bool[i] = 1
        else:
            gc_bool[i] = 0

    # For GC values that tested above a certain threshold, make the appropriate
    # block upper-case. For all other values, make block lower-case.
    for i, bool in enumerate(gc_bool):
        if bool == 1:
            blocks[i] = blocks[i].upper()
        if bool == 0:
            blocks[i] = blocks[i].lower()

    return ''.join(blocks)
