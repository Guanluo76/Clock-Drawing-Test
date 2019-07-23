from __future__ import absolute_import
import argparse


def CDT(image_filename_list):
    """
    Run the clock drawing test with given images and return the score.

    @param list image_filename_list: list of image filenames
    @return int score
    """
    from image_loader import ImageFetcher
    from experiment import Experiment

    # read in images
    for img_filename in image_filename_list:
        ImageFetcher().img_filename = img_filename

    # run the test and return the score
    return Experiment().score

def main():
    """
    Run the clock drawing test from command line.
    """
    # create cmd argument parser
    parser = argparse.ArgumentParser()

    # add cmd argument
    parser.add_argument('filename', type=str, nargs='*',
                        help='image filenames for each test step')

    # run and print the result
    print('Score: %d' % CDT(parser.parse_args().filename))


if __name__ == '__main__':
    main()

