
def licenseKeyFormatting(S, K):
    """
    :type S: str
    :type K: int
    :rtype: str
    """
    def chunks(l, n):
        for i in range(0, len(l), n):
            yield l[i:i+n]
    s = S[::-1].upper().replace('-', '')   
    print(list(chunks(s, K)))
    return '-'.join(list(chunks(s, K)))[::-1]
l
S = "5F3Z-2e-9-w"
K = 4
print(S[::-1])
print(licenseKeyFormatting(S, K))
