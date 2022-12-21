import os 
import json 
import yaml 
import argparse 
from task2 import * 
 
 
def process_data(data): 
    for i in data: 
        a = i.get('a') 
        b = i.get('b', i.get('a')) 
        operation = i.get('operation') 
 
        if "/" in a: 
            num_a = int(a.split("/")[0]) 
            den_a = int(a.split("/")[-1]) 
        else: 
            num_a = int(a) 
            den_a = 1 
 
        if "/" in b: 
            num_b = int(b.split("/")[0]) 
            den_b = int(b.split("/")[-1]) 
        else: 
            num_b = int(b)
            den_b = 1

        rnum_1 = RationalNumber(num=num_a, den=den_a)
        rnum_2 = RationalNumber(num=num_b, den=den_b)

        for j in operation:
            if j == '*':
                print(repr (rnum_1), "*", repr(rnum_2), "=", repr(rnum_1 * rnum_2))
            if j == '/':
                print(repr (rnum_1), "/", repr(rnum_2), "=", repr(rnum_1 / rnum_2))
            if j == '+':
                print(repr (rnum_1), "+", repr(rnum_2), "=", repr(rnum_1 + rnum_2))
            if j == '-':
                print(repr (rnum_1), "-", repr(rnum_2), "=", repr(rnum_1 - rnum_2))

if __name__ == '__main__': 
    parser = argparse.ArgumentParser() 
    parser.add_argument('-f', '--filename', type=str, help='json or yaml file for task') 
    args = parser.parse_args() 
 
if not args.filename: 
    raise Exception('need filename') 

name, ext = os.path.splitext(args.filename) 
if ext == '.json': 
    loader = json.load 
elif ext == '.yaml': 
    loader = yaml.load 
else: 
    raise Exception('wrong file type') 
 
with open(args.filename, "r") as read_file: 
    data = loader(read_file) 
process_data(data)