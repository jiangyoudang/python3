import argparse
import sys

parser = argparse.ArgumentParser(description='test description')
parser.add_argument('--dev', nargs='*', default='dev', choices=('dev', 'qa', 'prod'))

args = parser.parse_args()

print(sys.argv)
print(args.dev)