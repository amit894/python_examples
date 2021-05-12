MAX=256

def longest_substring(string):
    longest_substring=""

    for i in range(len(string)):
        j=i
        string_count=[0]*256
        while(j<len(string)):
            string_count[ord(string[j])]+=1
            if single_occurence(string_count)==False:
                break
            j+=1
        temp=string[i:j]
        if len(temp)>len(longest_substring):
            longest_substring=temp
    return longest_substring


def single_occurence(arr):
    for i in arr:
        if i>1:
            return False
    return True

print(longest_substring("pwwkew"))
