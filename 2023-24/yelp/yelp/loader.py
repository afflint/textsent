import json
import pandas as pd


def load_sample():
    sample_file = '/Users/flint/Data/yelp/data/yelp_sample.json'
    with open(sample_file, 'r') as infile:
        yelp = json.load(infile)
    return yelp

def stars(data: list):
    for review in data:
        if pd.notnull(review['stars']) and pd.notnull(review['content']):
            yield review['content'], review['stars']
            
def categories(data: list, flat: bool = True):
    for review in data:
        if pd.notnull(review['content']):
            if flat:
                for category in review['categories']:
                    yield review['content'], category
            else:
                yield review['content'], review['categories']