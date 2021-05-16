def longest_substring(string):
    max_len=0
    last_idx={}
    start_idx=0
    for i in range(len(string)):
        if string[i] in last_idx:
            start_idx=max(start_idx,last_idx[string[i]]+1)
        max_len=max(max_len,i-start_idx+1)
        last_idx[string[i]]=i

    return max_len
