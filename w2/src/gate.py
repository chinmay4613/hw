#!/usr/bin/env python3

import sys
import json
import argparse
from config import get_default_config

from data import DATA

the = None

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--cohen', dest="cohen_size", help="small effect size")
    parser.add_argument('-f', '--file', dest="csv_file_name", help="csv data file name")
    parser.add_argument('-k', '--k', dest="low_class_frequency_kludge", help="low class frequency kludge")
    parser.add_argument('-m', '--m', dest="low_attribute_frequency_kludge", help="low attribute frequency kludge")
    parser.add_argument('-s', '--seed', dest="random_number_seed", help="random number seed")
    parser.add_argument('-t', '--todo', dest="action", help="start up action")

    args = parser.parse_args()

    if not args.action:
        parser.print_help()
        sys.exit(0)

    the = get_default_config()

    if args.cohen_size:
        the.cohen = args.cohen_size

    if args.csv_file_name:
        the.file = args.csv_file_name

    if args.low_class_frequency_kludge:
        the.k = args.low_class_frequency_kludge

    if args.low_attribute_frequency_kludge:
        the.m = args.low_attribute_frequency_kludge
    
    if args.random_number_seed:
        the.seed = args.random_number_seed

    if args.action:
        the.todo = args.action

    action = args.action

    if action == "stats":
        data_obj = DATA(the.file)
        stats_result = data_obj.stats()
        print(json.dumps(stats_result))
    else:
        pass
