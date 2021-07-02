def subString(s, n):
    # Stores the total
    # count of substrings
    hash = {0: 1}
    pre = 0
    count = 0

    # Traverse the string S
    for i in s:

        # Flip the ord(i)-97 bits in pre
        pre ^= (1 << ord(i) - 97)

        # Increment the count by hash[pre]
        count += hash.get(pre, 1)

        # Increment count of pre in hash
        hash[pre] = hash.get(pre, 1) + 1

    # Return the total count obtained
    return count


def uniq_substring(test):
    lista = []
    [lista.append(test[i:i+k+1]) for i in range(len(test)) for k in
     range(len(test)-i) if test[i:i+k+1] not in lista and
     test[i:i+k+1][::-1] not in lista]
    print(lista)


# Driver Code

S = "aabb"
N = len(S)
print(subString(S, N))
