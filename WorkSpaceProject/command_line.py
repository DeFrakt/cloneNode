#Import modules
import argparse
import fileinput
from functions import *

#Create Command Line arguments, file & ID to be cloned
parser = argparse.ArgumentParser()
parser.add_argument("--file", "-f", type=str,  required=True, help='JSON file to import')
parser.add_argument('integers', metavar='N', type=int,help='Entity ID to be copied')
args = parser.parse_args()

#Open JSON file
with open(args.file) as file:
    #Save Master Dictionary
    master_entity = add_entity(file.read())
    #Save ID 
    id_clone = args.integers
    #Command Line 
    print("Entity ID to be cloned")
    print("*"*40)
    print(args.integers,"\n")

#ID key for links
link_key = {'key': [],'found_links': []}
#gather entity ID if cloned
cloned = []  