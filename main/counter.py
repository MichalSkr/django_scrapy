from collections import Counter
import re
from stop_words import get_stop_words


def count(post_content):
    word_count = {}
    stop_words = get_stop_words('english') + get_stop_words('polish')
    for post in post_content:
        words = [re.search(r'\w+', el).group() for el in post.split()]
        words = [word for word in words if word.lower() not in stop_words and len(word) > 1]
        counter = Counter(list(filter(None, words)))
        # Add words and values to dictionary or update the count for already added words
        for key, value in counter.items():
            if key in word_count:
                word_count[key] += value
            else:
                word_count[key] = value

    # "Sorts" the dict by values, returning tuples and puts it back into a dict with only top 10 words
    sorted_by_value = dict(sorted(word_count.items(), key=lambda kv: kv[1], reverse=True)[:10])
    return sorted_by_value
