from argparse import ArgumentParser
import re
import json
from collections import Counter
import math
import time

def format_title(title):
    cleaned_title = re.sub(r"[^\w\s]", "", title).lower()
    words = cleaned_title.split()
    return words

def compute_idf(input_files, all_terms):
    idf = {}
    start_time = time.time()
    total_docs = len(input_files)
    for term in all_terms:
        containing_docs = 0
        for input_file in input_files:
            with open(input_file, "r") as file:
                data = json.load(file)
                for post in data:
                    title = post['data']['title']
                    words = format_title(title)
                    if term in words:
                        containing_docs += 1
                        break
        idf[term] = math.log(total_docs / (containing_docs))
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Elapsed time for idf: {elapsed_time} seconds")
    return idf

def compute_tf_idf(tf, idf):
    tf_idf = {}
    start_time = time.time()
    for document, counter in tf.items():
        tf_idf[document] = {}
        for term, count in counter.items():
            tf_idf[document][term] = count * idf[term]
        sorted_terms = sorted(tf_idf[document].items(), key=lambda item : item[1], reverse=True)
        tf_idf[document] = dict(sorted_terms[:10])
    end_time = time.time()
    elapsed_time  = end_time - start_time
    print(f"Elapsed time for tf_idf: {elapsed_time} seconds")
    return tf_idf

def process(input_files, stopword_file):
    start_time = time.time()
    word_counts = {}
    all_terms = set()
    for intput_file in input_files:
        word_counter = Counter()
        with open(intput_file, "r") as file:
            data = json.load(file)
            for post in data:
                title = post['data']['title']
                words = format_title(title)
                for word in words:
                    all_terms.add(word)
                word_counter.update(words)
            if stopword_file:
                with open(stopword_file, "r") as file:
                    stop_words = json.load(file)
                    for stop_word in stop_words:
                        if stop_word in word_counter:
                            del word_counter[stop_word]
        word_counts[intput_file] = word_counter
    if stopword_file:
        for stop_word in stop_words:
            all_terms.discard(stop_word)
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Elapsed time for processing: {elapsed_time} seconds")
    idf = compute_idf(input_files, all_terms=all_terms)
    tf_idf = compute_tf_idf(tf=word_counts, idf=idf)
    return tf_idf

def main():
    parser = ArgumentParser(description="Compute the words with top 10 tfidf scores from Reddit post titles.")
    parser.add_argument("input_files", nargs="+", help="The list of reddit json files to process.")
    parser.add_argument("-o", "--output_file", required=True, help="The name of the output file to store results in.")
    parser.add_argument("-s", "--stopword_file", default=None, help="The name of the stop words file to be used to remove stop words.")
    args = parser.parse_args()

    tf_idf = process(args.input_files, args.stopword_file)
    with open(args.output_file, 'w') as file:
        json.dump(tf_idf, file, indent=2)

    print(f"Words with top tf-idf scores have been saved to {args.output_file}")

if __name__ == "__main__":
    main()