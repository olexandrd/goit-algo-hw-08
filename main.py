import heapq


def calculate_length(fragment_list: list) -> int:
    heapq.heapify(fragment_list)
    while len(fragment_list) > 1:
        heapq.heappush(
            fragment_list, heapq.heappop(fragment_list) + heapq.heappop(fragment_list)
        )
    return heapq.heappop(fragment_list)


def main():
    lst = [4, 6, 12, 3, 5]
    print(calculate_length(lst))


if __name__ == "__main__":
    main()
