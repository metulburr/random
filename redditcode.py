
import argparse
#example:
#python3 test.py -i test.py -o testSPACED.py

parser = argparse.ArgumentParser(description='Reddit code post')
parser.add_argument('-i','--input', required=True, 
    help='file input')
parser.add_argument('-o','--output', required=True, 
    help='file output')
args = vars(parser.parse_args())

fin = open(args['input'])
lines = fin.readlines()
fin.close()

fout = open(args['output'], 'w')
for line in lines:
	fout.write((' ' * 4) + line)
fout.close()
