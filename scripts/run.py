
from gaffophone.classes import Gaffophone
import argparse


def main(args):
    gf = Gaffophone(args)
    gf.run()




if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-b", default="body.mkd", dest="body_template")
    parser.add_argument("-t", default="title.mkd", dest="title_template")
    parser.add_argument("-s", default="submission.mkd", dest="submission_template")
    args = parser.parse_args()
    main(args)
