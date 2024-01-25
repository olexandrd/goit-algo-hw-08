import heapq


def calculate_length(fragment_list: list) -> int:
    heapq.heapify(fragment_list)
    costs = list()

    while len(fragment_list) > 1:
        shortest_1 = heapq.heappop(fragment_list)
        shortest_2 = heapq.heappop(fragment_list)
        cost = shortest_1 + shortest_2
        costs.append(cost)
        heapq.heappush(fragment_list, cost)
    return costs


def main():
    lst = [4, 6, 12, 3, 5]
    connection_costs = calculate_length(lst)
    print(
        f"Connection order:\n" + " => ".join([str(order) for order in connection_costs])
    )
    print("Total costs:", sum(connection_costs))


if __name__ == "__main__":
    main()
