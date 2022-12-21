"""Simple script that analyzes a few files and reports some word statistics from them"""
from pathlib import Path
import operator
import time
import json
import hashlib


def read_file_to_string(path: Path) -> str:
    """Given a path, read it to a string, that's it."""
    try:
        contents = path.read_text(encoding="utf-8")
    except FileNotFoundError:
        print(f"ERROR: The file {path} cannot be found.")
        return ""
    else:
        return contents


def calc_md5hash_of_string(input_str: str) -> str:
    """Calculate the MD5 hash of a given string"""
    return hashlib.md5(input_str.encode(encoding="utf-8")).hexdigest()


def calculate_word_statistics(path: Path) -> dict:
    """Given a file, calculate it's word statistics and return them as a dictionary"""
    contents = read_file_to_string(path)
    if contents == "":
        return {}

    stats = {}
    word_list = contents.split()
    word_set = set(word_list)
    stats["hash_md5"] = calc_md5hash_of_string(contents)
    stats["num_words"] = len(word_list)
    stats["unique_words"] = len(word_set)
    stats["word_counts"] = {}

    for word in word_set:
        stats["word_counts"][word] = word_list.count(word)

    sorted_word_counts = sorted(
        stats["word_counts"].items(), key=operator.itemgetter(1), reverse=True
    )
    stats["word_counts"] = sorted_word_counts
    return stats


def get_file_stats(path: Path) -> dict:
    """Get the stats for the given file, pull from cache first, if not cached, calculate them"""
    cache_filename = f"data/{path}.json"
    cache_path = Path(cache_filename)
    if cache_path.exists():
        file_stats = json.loads(cache_path.read_text(encoding="utf-8"))
        # Now make sure our file hash hasn't changed, if it has, then recompute
        new_file_hash = calc_md5hash_of_string(path.read_text(encoding="utf-8"))
        if ("hash_md5" not in file_stats) or (new_file_hash != file_stats["hash_md5"]):
            file_stats = calculate_word_statistics(path)
            cache_path.write_text(json.dumps(file_stats), encoding="utf-8")
    else:
        file_stats = calculate_word_statistics(path)
        cache_path.write_text(json.dumps(file_stats), encoding="utf-8")

    return file_stats


def report_word_statistics(path: Path):
    """Calculate useful statistics on the provided file
    and caches those statistics to a JSON file for easy retrieval.
    Things to improve: check the source file hash and recompute stats if necessary
    """
    start_time = time.time()
    num_top_words = 10
    file_stats = get_file_stats(path)

    print(f"Stats for {path}")
    print(f"\tTotal words : {file_stats['num_words']}")
    print(f"\tUnique words : {file_stats['unique_words']}")
    print(f"\tTop {num_top_words} used words are:")
    sorted_word_counts = file_stats["word_counts"]
    for iter_cnt in range(num_top_words):
        print(f"\t\t{sorted_word_counts[iter_cnt][0]}: {sorted_word_counts[iter_cnt][1]}")
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Execution time: {elapsed_time} seconds")


report_word_statistics(Path("chapter_10/partial_programs/exceptions/alice.txt"))
report_word_statistics(Path("chapter_10/partial_programs/exceptions/little_women.txt"))
report_word_statistics(Path("chapter_10/partial_programs/exceptions/moby_dick.txt"))
# report_word_statistics(Path("fake.txt"))
