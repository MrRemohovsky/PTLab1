# -*- coding: utf-8 -*-
import argparse
import os
import sys

from TopStudentsCounter import TopStudentsCounter
from CalcRating import CalcRating
from TextDataReader import TextDataReader
from YamlDataReader import YamlDataReader


DATA_MAP = {
    '.txt': {
        'reader': TextDataReader,
        'calc': CalcRating,
        'text': 'Rating:'
    },
    '.yaml': {
        'reader': YamlDataReader,
        'calc': TopStudentsCounter,
        'text': 'Top students count with scores of 90 or above in all subjects:'
    }
}


def get_path_from_arguments(args) -> str:
    parser = argparse.ArgumentParser(description="Path to datafile")
    parser.add_argument("-p", dest="path", type=str, required=True,
                        help="Path to datafile")
    args = parser.parse_args(args)
    return args.path


def main():
    path = get_path_from_arguments(sys.argv[1:])
    ext = os.path.splitext(path)[1].lower()

    if ext in (".yaml", ".yml") and ext != '.yaml':
        data_map = DATA_MAP['.yaml']
    else:
        data_map = DATA_MAP[ext]

    try:
        reader, calc = data_map['reader'], data_map['calc']
    except KeyError:
        raise Exception(f"Unsupported file type: {ext}")

    students = reader().read(path)
    print("Students:")
    for student, grades in students.items():
        print(f"{student}:")
        for subject, score in grades:
            print(f"  {subject}: {score}")

    calc_data = calc(students).calc()
    print(data_map['text'], calc_data)


if __name__ == "__main__":
    main()
