#!/usr/bin/env python3
"""
Author : sudhanshu <sudhanshu@localhost>
Date   : 2020-11-09
Purpose: Say Hello
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Say Hello',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-n',
                        '--name',
                        help='Name to greet',
                        metavar='name',
                        type=str,
                        default='World')



    return parser.parse_args()

# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    name = args.name

    print('Hello, ' + name + '!')



# --------------------------------------------------
if __name__ == '__main__':
    main()
