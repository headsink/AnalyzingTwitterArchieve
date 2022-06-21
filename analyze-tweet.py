import argparse

if __name__ == 'main':
    parser = argparse.ArgumentParser()
    parser.add_argument("-j","--js",dest="js_file", help="tweet.js file inside the archive folder", metavar="FILE")
    args = parser.parse_args()

    