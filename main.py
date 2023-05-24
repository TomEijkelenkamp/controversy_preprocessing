import pandas as pd
import csv



def read_comments(comments):
    
    for idx_1, comment_list in enumerate(comments):
        print(f"Size in comment {idx_1}: {len(comment_list)}")
        for idx_2, comment in enumerate(comment_list):
            item = {'text': "", 'ups': 0, 'downs': 0, 'controversy': 0}
            print(f"Comment index {idx_1}-{idx_2}: {comment}")
            if 'body' in comment:
                item['text'] = comment['body']
                print(f"Body of comment: {comment['body']}")
            if 'ups' in comment:
                item['ups'] = comment['ups']
                print(f"Ups in comment: {comment['ups']}")
            if 'downs' in comment:
                item['downs'] = comment['downs']
                print(f"Downs in comment: {comment['downs']}")
            print("\n\n\n")
            if item['ups'] > 0 and item['downs'] > 0:
                if item['ups'] > item['downs']:
                    item['controversy'] = item['downs'] / item['ups']
                else:
                    item['controversy'] = item['ups'] / item['downs']
            write_csv(item)


def write_csv(new_data, field_names=['text', 'ups', 'downs', 'controversy'], filename='data.csv'):
    with open(filename,'a', encoding="utf-8") as csv_file:
        dict_object = csv.DictWriter(csv_file, fieldnames=field_names) 
        dict_object.writerow(new_data)


def read_post(post):
    if 'comments' in post:
        read_comments(post['comments'])
        

data = pd.read_json('threads.jsonl', orient="records", lines=True, chunksize=1000)
# print(data.shape)
for idx, post in enumerate(data):
    print(idx)
    read_post(post)