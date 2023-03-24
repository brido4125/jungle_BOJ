def longest_subarray(ary, Q):
    start = 0
    end = 0
    curr_sum = ary[0]
    max_len = 0

    while end < len(ary):
        if curr_sum <= Q:
            curr_len = end - start + 1
            max_len = max(max_len, curr_len)
            end += 1
            if end < len(ary):
                curr_sum += ary[end]
        else:
            curr_sum -= ary[start]
            start += 1

    return max_len
