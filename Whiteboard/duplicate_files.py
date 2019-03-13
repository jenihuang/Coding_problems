from collections import defaultdict
import os


def list_all_files(filepath):

    if not os.path.isdir(filepath):
        return [filepath]
    else:
        result = []
        for child in os.lstdir(filepath):
            result.append(list_all_files(child))
        return result


def find_duplicates(filepath):
    files = list_all_files(filepath)
    duplicate_count = defaultdict(list)

    for file in files:
        chars = hash(file)
        duplicate_count[chars].append(file)

    # for value in duplicate_count.items():
    #     if len(value) > 1:
    #         duplicates.append(value)

    return [value for value in duplicate_count.items() if len(value) > 1]
