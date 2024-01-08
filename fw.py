#!/usr/bin/env python3

import json
import argparse
import os,sys

def readjson():
    with open(args.json,'r',encoding='utf-8') as file:
        jsonconfig = json.load(file)
    return jsonconfig

if __name__ == "__main__":
    mypath="/home/next/ITS3/eudaq/user/ITS3/misc/myscripts/"
    parser = argparse.ArgumentParser(description="APTS readout",formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('--json','-j',help='Json file to initialize',default=mypath+"daq.json")
    args=parser.parse_args()

    jsonconfig = readjson()
    print(jsonconfig['ALPIDE_DAQ'])

    for key.val in jsonconfig['ALPIDE_DAQ'].items():
        print(val)
