import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-j","--js",dest="js_file", help="tweet.js file inside the archive folder", metavar="FILE")
    args = parser.parse_args()


    if args.js_file is None:
        print("No argument. Enter argument -h or --help for more information")
        exit(1)

