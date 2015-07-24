#! /usr/bin/env python

# standard library imports
import os
import sys  # noqa
import argparse

import pandashells


def main():
    # create a dict of data-set names and corresponding files
    package_dir = os.path.dirname(os.path.realpath(pandashells.__file__))
    sample_data_dir = os.path.realpath(os.path.join(package_dir, 'example_data'))

    f_dict = {}
    for f in os.listdir(sample_data_dir):
        f_dict[f.replace('.csv', '')] = os.path.join(sample_data_dir, f)

    # populate the arg parser with current configuration
    msg = "Print sample data set to stdout"
    parser = argparse.ArgumentParser(description=msg)

    parser.add_argument(
        '-d', '--dataset', nargs=1, type=str,
        dest='dataset', choices=sorted(f_dict.keys()), required=True,
        help='The name of the sample dataset')

    # parse arguments
    args = parser.parse_args()

    # print contents of data file to output
    f_name = f_dict[args.dataset[0]]
    with open(f_name) as in_file:
        try:
            # line by line avoids weird sys.excepthook bug on pipe to head
            for line in in_file:
                print line.strip()
        except IOError:
            pass


if __name__ == '__main__':  # pragma: no cover
    main()
