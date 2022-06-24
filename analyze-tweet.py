import argparse
import json
import os

def load_tweet_from_js_file(js_file):
    data = ""
    with open(js_file,'r') as theDoc:
        for theline in theDoc:
            theline = theline.replace('window.YTD.tweet.part0 = ', '')
            data+=theline
        tweets = json.loads(data)
    return tweets


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-j", "--js", dest="js_file",
                        help="tweet.js file inside the archive folder", metavar="FILE")
    args = parser.parse_args()

    if args.js_file is None:
        print("No argument. Enter argument -h or --help for more information")
        exit()
    else:
        tweets = load_tweet_from_js_file(args.js_file)
