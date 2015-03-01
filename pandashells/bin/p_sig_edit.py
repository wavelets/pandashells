#! /usr/bin/env python

# standard library imports
import argparse

from pandashells.lib import arg_lib, io_lib, outlier_lib


def main():
    msg = "Perform recursive sigma editing on columns of a dataframe. "
    msg += "Recursively NaNs out values greater than sigma_thresh standard "
    msg += "deviations away from sample mean."

    # read command line arguments
    parser = argparse.ArgumentParser(description=msg)

    arg_lib.add_args(parser, 'io_in', 'io_out', 'example')

    parser.add_argument("-t", "--sigma_thresh", help="Sigma threshold",
                        nargs=1, required=True, type=float)
    parser.add_argument("-c", "--cols", required=True,
                        help="Column(s) to sigma-edit", nargs="+")
    parser.add_argument("--max_iter", help="Max number of recursions",
                        nargs=1, type=int, default=[20])

    # parse arguments
    args = parser.parse_args()

    # get the input dataframe
    df = io_lib.df_from_input(args)
    df = outlier_lib.sigma_edit_dataframe(
        args.sigma_thresh[0], args.cols, df, max_iter=args.max_iter[0])

    # write dataframe to output
    io_lib.df_to_output(args, df)

if __name__ == '__main__':  # pragma: no cover
    main()
