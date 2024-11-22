from argparse import ArgumentParser
import re
import json
from collections import Counter

def format_title(title):
    cleaned_title = re.sub(r"[^\w\s]", "", title).lower()
    words = cleaned_title.split()
    return words

def process(input_files, stopword_file):
    word_counts = {}
    for intput_file in input_files:
        word_counter = Counter()
        with open(intput_file, "r") as file:
            data = json.load(file)
            for post in data:
                title = post['data']['title']
                words = format_title(title)
                word_counter.update(words)
            if stopword_file:
                with open(stopword_file, "r") as file:
                    stop_words = json.load(file)
                    for stop_word in stop_words:
                        del word_counter[stop_word]
        word_counts[intput_file] = word_counter.most_common(10)
    return word_counts

def main():
    parser = ArgumentParser(description="Compute the top 10 frequent words from Reddit post titles.")
    parser.add_argument("input_files", nargs="+", help="The list of reddit json files to process.")
    parser.add_argument("-o", "--output_file", required=True, help="The name of the output file to store results in.")
    parser.add_argument("-s", "--stopword_file", default=None, help="The name of the stop words file to be used to remove stop words.")
    args = parser.parse_args()

    word_counts = process(args.input_files, args.stopword_file)
    with open(args.output_file, 'w') as file:
        json.dump(word_counts, file, indent=2)

    print(f"Top words have been saved to {args.output_file}")

if __name__ == "__main__":
    main()