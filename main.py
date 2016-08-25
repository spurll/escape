#!/usr/bin/env python3

# Written by Gem Newman. This work is licensed under a Creative Commons
# Attribution-ShareAlike 4.0 International License.


from argparse import ArgumentParser

from escape.controller import main


def console_main():
    parser = ArgumentParser(description='Procedurally generated escape rooms.')
    parser.add_argument(
        'seed', help='Optional seed to use to generate the escape room.'
    )
    args = parser.parse_args()

    main(args.seed)


if __name__ == '__main__':
    console_main()
