from argparse import ArgumentParser

parser=ArgumentParser()

parser.add_argument('--output','-o', required=True,help='Output filename')
parser.add_argument('--text','-t', required=True,help='Text to be saved on the outputfile')

args=parser.parse_args()

with open(args.output,'w') as f:
    f.write(args.text+'\n')

print(f'Write text successful to file {args.output}')