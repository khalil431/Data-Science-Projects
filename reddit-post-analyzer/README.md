# Reddit Data Analyzer  

A Python-based toolset for scraping Reddit posts, processing text data, and analyzing word frequencies using both a naive technique and TF-IDF implemented from scratch. This project is designed to extract insights from subreddit post titles by creating wordlists and calculating term importance.  

---

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [License](#license)

## Installation
Step-by-step instructions on how to get the development environment running.

1. **Clone the Repository**
	- Clone the project repository from GitHub:
		- **Usage example:**
		```bash
		git clone https://github.com/khalil431/Data-Science-Projects.git
		```
	- Alternatively, download the repository ZIP file and extract it.

## Usage

1. **Fetch Subreddit Data**
	- Use `collect_jsons.py` to scrape posts from subreddits and save them to JSON files. This script scrapes posts from r/mcgill, r/montreal, r/programming, r/marvel, r/mylittlepony, and r/3Dprinting by default.
		- **Usage example:**
		```bash
		python scripts/collect_jsons.py
		```

2. **Build Frequency Wordlists**
	- Use `build_naive_frequent_word_list.py` to compute the top 10 most frequent words from the post titles. This script uses the naive algorithm by computing word frequencies for each subreddit. The help commands for `build_naive_frequent_word_list.py` is available through the --help flag. Including the stopword json file is optional. Make sure `collect_jsons.py` has been rune before as the reddit json files are required for this step to run properly.
		- **Usage example:**
		```bash
		python src/build_naive_frequent_word_list.py mcgill.json montreal.json programming.json marvel.json mylittlepony.json 3Dprinting.json -o naive_wordlist.json -s stopwords/stop_words_english.json
		```

3. **Build TF-IDF Wordlists**
	- Use `build_tfidf_word_list.py` to compute the words with top 10 tf-idf scores from Reddit post titles. This script calculates the tf-idf scores from scratch. The help commands for `build_tfidf_word_list.py` is available through the --help flag. Including the stopword json file is optional. Make sure `collect_jsons.py` has been rune before as the reddit json files are required for this step to run properly.
		- **Usage example:**
		```bash
		python src/build_tfidf_word_list.py mcgill.json montreal.json programming.json marvel.json mylittlepony.json 3Dprinting.json -o tfidf_wordlist.json -s stopwords/stop_words_english.json
		```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

