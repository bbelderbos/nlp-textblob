import sys

from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer


def get_sentiments(file):
    with open(file) as f:
        for line in f.readlines():
            yield TextBlob(line.strip(), analyzer=NaiveBayesAnalyzer)


def main(file):
    blobs = get_sentiments(file)
    for blob in blobs:
        print(blob)


if __name__ == "__main__":
    if len(sys.argv) == 2:
        reviews = sys.argv[1]
        main(reviews)
    else:
        print(f"Usage: {sys.argv[0]} reviews.txt")
