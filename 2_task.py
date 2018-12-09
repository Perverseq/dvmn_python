import collections
import json

SALES = [
    "Электрический чайник",
    "Тостер",
    "Фен для волос",
    "Фен для волос",
    "Тостер",
    "Тостер",
]


def get_stats_from_file():
    with open('./sales_log.json') as stats_file:
        content = stats_file.read()
        data = json.loads(content)
        statistics = collections.Counter(data)
    return statistics


def print_stats(statistics):
    for name, cost in statistics.most_common():
        print(f"{name} - {cost}")


def main():
    print_stats(get_stats_from_file())


if __name__ == "__main__":
    main()
