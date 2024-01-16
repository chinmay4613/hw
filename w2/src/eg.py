#!/usr/bin/env python3
"""
Unit testing file
"""
import copy
import random
import sys
import math
import traceback

import utils
from config import get_default_config
from sym import SYM
from num import NUM
from data import DATA

the = get_default_config()

def norm(mu=0, sd=1):
    R = random.random
    return mu + sd * math.sqrt(-2 * math.log(R())) * math.cos(2 * math.pi * R())

class EG:

    @staticmethod
    def test_all():
        failed_count = 0

        try:
            print("Start test_stats()")
            if not EG.test_stats():
                print("test_stats() failed")
                failed_count += 1
            else:
                print("test_stats() completed successfully")
        except Exception:
            print("test_stats() failed")
            print(traceback.format_exc())
            failed_count += 1

        print("\n\n")

        try:
            print("Start test_sym()")
            if not EG.test_sym():
                print("test_sym() failed")
                failed_count += 1
            else:
                print("test_sym() completed successfully")
        except Exception:
            print("test_sym() failed")
            print(traceback.format_exc())
            failed_count += 1

        print("\n\n")


        try:
            print("Start test_num()")
            if not EG.test_num():
                print("test_num() failed")
                failed_count += 1
            else:
                print("test_num() completed successfully")
        except Exception:
            print("test_num() failed")
            print(traceback.format_exc())
            failed_count += 1

        print("\n\n")


        try:
            print("Start test_csv()")
            if not EG.test_csv():
                print("test_csv() failed")
                failed_count += 1
            else:
                print("test_csv() completed successfully")
        except Exception:
            print("test_csv() failed")
            print(traceback.format_exc())
            failed_count += 1

        print("\n\n")


        """
        Unfinished testing case
        try:
            print("Start test_data()")
            if not EG.test_data():
                print("test_data() failed")
                failed_count += 1
            else:
                print("test_data() completed successfully")
        except Exception:
            print("test_data() failed")
            print(traceback.format_exc())
            failed_count += 1

        print("\n\n")
        """

        sys.exit(failed_count)


    @staticmethod
    def test_stats():
        # Store current config into cache
        b4 = copy.deepcopy(the)
        random.seed(the['seed'])

        # Testing part
        the.file = "../data/auto93.csv"

        data_obj = DATA(the.file)
        stats_result = data_obj.stats()
        formatted_result = utils.o(stats_result, 2)
        print(formatted_result)

        # Restore the original config
        the.update(b4)
        return formatted_result == "{.N: 398, Lbs-: 2970.42, Acc+: 15.57, Mpg+: 23.84}"
        # return formatted_result == "{.N: 398, Acc+: 15.57, Lbs-: 2970.42, Mpg+: 23.84}"

    @staticmethod
    def test_sym():
        # Store current config into cache
        b4 = copy.deepcopy(the)
        random.seed(the['seed'])

        # Testing part
        s = SYM()
        for x in [1, 1, 1, 1, 2, 2, 3]:
            s.add(x)
        mode, e = s.mid(), s.div()
        print(mode, e)

        # Restore the original config
        the.update(b4)

        return 1.37 < e < 1.38 and mode == 1


    @staticmethod
    def test_num():
        # Store current config into cache
        b4 = copy.deepcopy(the)
        random.seed(the['seed'])

        # Testing part
        e = NUM()
        for _ in range(1000):
            e.add(norm(10, 2))
        mu, sd = e.mid(), e.div()
        print(round(mu, 3), round(sd, 3))

        # Restore the original config
        the.update(b4)
        return 10 < mu < 10.2 and 2 < sd < 2.1


    @staticmethod
    def test_csv():
        # Store current config into cache
        b4 = copy.deepcopy(the)
        random.seed(the['seed'])
        the.file = "../data/auto93.csv"

        # Testing part
        n = 0
        for i, t in utils.csv(the.file):
            if i % 100 == 0:
                n += t[1]
                print(i, utils.o(t))

        # Restore the original config
        the.update(b4)
        return n == 492


    """
    function eg.data(     d,n)
      n=0
      d = DATA.new(the.file)
      for i, row in pairs(d.rows) do
        if i % 100 ==0 then n = n + #row.cells; l.oo(row.cells) end end
      l.oo(d.cols.x[1].cells)
      return n == 63 end
    """

    @staticmethod
    def test_data():
        # Store current config into cache
        b4 = copy.deepcopy(the)
        random.seed(the['seed'])

        # Testing part
        n = 0
        d = DATA(the.file)
        for i, row in enumerate(d.rows):
            if i % 100 == 0:
                n += len(row.cells)
                utils.oo(row.cells)

        utils.oo(d.cols.x[1].cells)

        # Restore the original config
        the.update(b4)
        return n == 63


if __name__ == '__main__':
    EG.test_all()
