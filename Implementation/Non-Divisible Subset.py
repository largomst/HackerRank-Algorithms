n, k = list(map(lambda x: int(x), input().strip().split(' ')))
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

result = set()

# S is a set that the sun of any two element in it is not evenly divisible by k

def CanDicisibleByThree(arr, k):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if (arr[i] + a[j]) % k == 0:
                return True
    return False


def GetSubs(father, size):
    all_subs = []
    excludes = set()
    for i in father:
        sub = set()
        sub.add(i)
        if len(sub) == size:
            all_subs.append(sub)
        else:
            excludes.add(i)
            new_father = father.difference(excludes)
            _sub = GetSubs(new_father, size - 1)
            for s in _sub:
                all_subs.append(sub.union(s))
    return all_subs

def GetSubAll(father):
    all_subs = []
    for size in range(1.len(father)+1):
        all_subs.append(GetSubs(father),size)
    
    return all_subs

def main(arr):
    result = []
    all_subs = GetSubAll(arr)
    for subs in all_subs:
        for sub in subs:
            if(not CanDicisibleByThree(sub)):

        