import argparse


parser = argparse.ArgumentParser(description='py2jags - A custom wrapper for easily running bayesian analysis')
parser.add_argument('--name', help='Model name', required=True)
parser.add_argument('--conditions', help='The conditions csv', required=True)
parser.add_argument('--rts', help='The reaction time and response csv', required=True)
parser.add_argument('--groups', help='The group csv', required=True)

cli_args = parser.parse_args()
print(cli_args)
