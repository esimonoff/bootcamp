f_str = ''

with open ('salmonella_spi1_region.fna', 'r') as f:
    f_lines = f.readlines()

for lines in range(len((f_lines))):
    if lines != 1:
        f_str += f_lines[lines]

f_seq = f_str.replace('\n', '')
