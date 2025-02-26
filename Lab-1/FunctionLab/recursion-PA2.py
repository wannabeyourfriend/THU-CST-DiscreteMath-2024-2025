def isPal(s):
    return s == s[::-1]


def koch(n):
    if n == 0:
        return "F"  # 0阶时直接画一条线
    else:
        # 递归生成 n-1 阶科赫曲线
        prev = koch(n - 1)
        # 组合生成 n 阶的绘制命令
        return prev + "L" + prev + "R" + prev + "L" + prev
    # 请不要修改下面的代码


def vowel(s):
    s = s.lower()
    yset = set()
    yset.add('a')
    yset.add('e')
    yset.add('i')
    yset.add('o')
    yset.add('u')
    if len(s) == 0:
        return 0
    else:
        if s[0] not in yset:
            return vowel(s[1:])
        else:
            return 1 + vowel(s[1:])
    # 请不要修改下面的代码


def squareSum(n):
    if n == 0:
        return 0
    else:
        return n * n + squareSum(n - 1)


def vonNeumann(n):
    if n == 0:
        return "{}"
    else:
        result = []
        for i in range(n):
            result.append(vonNeumann(i))
        return "{" + ", ".join(result) + "}"


def perm(s):
    if len(s) == 0:
        return {""}  # 使用集合以避免重复
    else:
        result = set()
        for i in range(len(s)):
            current_char = s[i]
            remaining_chars = s[:i] + s[i + 1:]
            for sub_permutation in perm(remaining_chars):
                result.add(current_char + sub_permutation)
        return sorted(list(result))


if __name__ == "__main__":
    for s in ['', 'abcdefgfedcba', 'I am the king of the world', 'Python', 'madam', 'Able was I ere I saw Elba']:
        print(isPal(s.lower()))
    print('*' * 20)
    for n in range(4):
        print(koch(n))
    print('*' * 20)
    for s in ['', 'abcdefgfedcba', 'I am the king of the world', 'Python', 'madam', 'Able was I ere I saw Elba']:
        print(vowel(s))
    print('*' * 20)
    for n in range(10):
        print(squareSum(n))
    print('*' * 20)
    for n in range(6):
        print(vonNeumann(n))

    ALPHABET = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for n in range(1, 5):
        print('*' * 20)
        string = ALPHABET[:n]
        print(perm(string))