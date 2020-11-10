#!/usr/bin/env python3
"""
Author : sudhanshu <sudhanshu@localhost>
Date   : 2020-11-10
Purpose: Crows's Nest -- choose the correct article 
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Crows's Nest -- choose the correct article",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('word',
                        metavar='word',
                        help='A word')

    parser.add_argument('-s',
                        '--starboard',
                        help='For starboard side',
                        action='store_true')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    flag = args.starboard
    boatSide = 'starboard' if flag else 'larboard'
    word = args.word
    char = word[0].lower()
    vowels = 'aeiou'
    article = 'an' if char in vowels else 'a'
    if (word[0].isupper()) :
        article = article.capitalize() 
    line = 'Ahoy, Captain, '+article+' '+word+' off the larboard bow!'
    line2 = 'Ahoy, Captain, {} {} off the larboard bow!'.format(article, word)
    line3 = f'Ahoy, Captain, {article} {word} off the {boatSide} bow!'
    print(line3)


# --------------------------------------------------
if __name__ == '__main__':
    main()
