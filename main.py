from typing import List

busy = [
    {"start": "10:30", "stop": "10:50"},
    {"start": "18:40", "stop": "18:50"},
    {"start": "14:40", "stop": "15:50"},
    {"start": "16:40", "stop": "17:20"},
    {"start": "20:05", "stop": "20:20"},
]

start_work = "9:00"
end_work = "21:00"
windows_size = "00:30"


def time_to_minute(s: str) -> int:
    hours, minutes = s.split(":")
    return int(hours) * 60 + int(minutes)


def minute_to_time(i: int) -> str:
    hours = int(i / 60)
    minutes = i % 60
    return f"{hours}:{minutes if minutes >=9 else str(minutes)+'0'}"


def check_intersection(s1: list, s2: list) -> bool:
    new_min = max(s1[0], s2[0])
    new_max = min(s1[1], s2[1])
    return True if new_max >= new_min else False


def generate_slots(start: str, end: str, window_size: str) -> List[List[int]]:
    free_time = [
        windows
        for windows in range(time_to_minute(start), time_to_minute(end) + 1, time_to_minute(window_size))
    ]

    free_time_intervals = [[free_time[i - 1], free_time[i]] for i in range(1, len(free_time))]

    return free_time_intervals


def get_free_time(busy_time: List, start: str, end: str, window_size: str) -> list:
    free_time = []

    busy_time_simple = [
        [time_to_minute(busy_item["start"]), time_to_minute(busy_item["stop"])] for busy_item in busy_time
    ]
    all_slots = generate_slots(start=start, end=end, window_size=window_size)

    for free_time_item in all_slots:
        flg_free = True
        for busy_time_simple_item in busy_time_simple:
            if check_intersection(busy_time_simple_item, free_time_item):
                flg_free = False

        if flg_free:
            free_time.append(free_time_item)

    free_time_format = [
        {"start": minute_to_time(f[0]), "stop": minute_to_time(f[1])} for f in free_time if len(free_time) > 0
    ]
    return free_time_format


def main():
    print(get_free_time(busy_time=busy, start=start_work, end=end_work, window_size=windows_size))


if __name__ == "__main__":
    main()
