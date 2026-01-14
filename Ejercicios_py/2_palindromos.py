def isPanlindrome(inputStr: str) -> bool:
    return inputStr == inputStr[::-1]

print(isPanlindrome("aabaa"))
print(isPanlindrome("abac"))
print(isPanlindrome("salas"))