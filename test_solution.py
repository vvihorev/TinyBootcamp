import os
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('solution_file')
args = parser.parse_args()
solution = args.solution_file

# os.system(f"black problems/{solution}.py")
os.system(f"pytest problems/{solution}.py")
os.system(f"flake8 problems/{solution}.py")
