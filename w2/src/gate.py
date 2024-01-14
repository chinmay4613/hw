#!/usr/bin/env python3

import sys
import json
import argparse

DEFAULT_COHEN_SIZE = 0.35
DEFAULT_CSV_DATA_FILE_PATH = "../data/diabetes.csv"
DEFAULT_LOW_CLASS_FREQUENCY_KLUDGE = 1
DEFAULT_LOW_ATTRIBUTE_FREQUENCY_KLUDGE = 2
DEFALT_RANDOM_NUMBER_SEED = 31210


def get_stats():
    pass

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

    cohen_size = DEFAULT_COHEN_SIZE
    csv_file_name = DEFAULT_CSV_DATA_FILE_PATH
    low_class_frequency_kludge = DEFAULT_LOW_CLASS_FREQUENCY_KLUDGE
    low_attribute_frequency_kludge = DEFAULT_LOW_ATTRIBUTE_FREQUENCY_KLUDGE
    random_number_seed = DEFALT_RANDOM_NUMBER_SEED

    if args.cohen_size:
        cohen_size = args.cohen_size

    if args.csv_file_name:
        csv_file_name = args.csv_file_name

    if args.low_class_frequency_kludge:
        low_class_frequency_kludge = args.low_class_frequency_kludge

    if args.low_attribute_frequency_kludge:
        low_attribute_frequency_kludge = args.low_attribute_frequency_kludge
    
    if args.random_number_seed:
        random_number_seed = args.random_number_seed


    action = args.action

    if action == "stats":
        stats_result = get_stats()
        print(json.dumps(stats_result))
    else:
        pass

