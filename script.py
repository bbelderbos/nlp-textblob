from collections import namedtuple
from operator import attrgetter
import sys

from textblob import TextBlob

Comment = namedtuple("Comment", "text polarity subjectivity")


def get_sentiments(file):
    with open(file) as f:
        for line in f.readlines():
            yield TextBlob(line.strip())


def main(file, sort_key="polarity"):
    blobs = get_sentiments(file)
    scores = []
    for blob in blobs:
        sent = blob.sentiment
        scores.append(
            Comment(blob, sent.polarity, sent.subjectivity)
        )
    scores.sort(key=attrgetter(sort_key))
    return scores


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} reviews.txt")
        sys.exit(1)

    reviews = sys.argv[1]
    scores = main(reviews)

    print("polarity | subjectivity | text")
    print("-" * 50)
    for row in scores:
        polarity = round(row.polarity, 3)
        subjectivity = round(row.subjectivity, 3)
        print(f"{polarity:<8} | {subjectivity:<12} | {row.text}")
