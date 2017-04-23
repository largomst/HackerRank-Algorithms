def solution(table, K):
    count = 0
    while K >= min(table):
        m = min(table)
        table.remove(m)
        K -= m
        count += 1
    return count


if __name__ == '__main__':
    N, K = input().strip().split(" ")
    N, K = int(N), int(K)
    price = [int(a) for a in input().strip().split(" ")]
    print(solution(price, K))
