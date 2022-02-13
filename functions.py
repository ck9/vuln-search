from argparse import ArgumentParser

def get_option():
    argparser = ArgumentParser()
    argparser.add_argument('-q', '--querySearch',
                           action='store_true',
                           help='Search path & query.')
    return argparser.parse_args()