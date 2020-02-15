import csv
import io
import functools


def to_csv(l: list):
    if len(l):
        fields = list(l[0].keys())
    else:
        fields = []
    f = io.StringIO()
    writer = csv.DictWriter(f, fieldnames=fields)
    writer.writeheader()
    for data in l:
        writer.writerow(data)
    return f.getvalue()

def flatten(l: list):
    final_l = []
    for i in l:
        if isinstance(i, (list, tuple)):
            final_l.extend(flatten(i))
        else:
            final_l.append(i)
    return final_l

def substract(l: list, l2: list, remove_duplicate: bool =True):
    final_l = []
    for i in l:
        if i not in l2:
            final_l.append(i)
        else:
            if not remove_duplicate:
                l2.remove(i)
    return final_l

def unique(l: list):
    return list(set(l))