def get_minimum_window(original: str, check: str) -> str:
    # WRITE YOUR BRILLIANT CODE HERE
    window, need = {}, {}
    l, r, valid = 0, 0, 0
    start, length = 0, len(original) + 1
    res = len(original) + 2
    ans = None
    for c in check:
        need[c] = need.get(c, 0) + 1
    while r < len(original):
        rChar = original[r]
        if rChar in need:
            window[rChar] = window.get(rChar, 0) + 1
            if window[rChar] == need[rChar]:
                valid += 1
            while valid == len(need):
                if length > r - l + 1:
                    ans = original[l:r + 1]
                    length = r - l + 1
                elif length == r - l + 1 and ans > original[l:r + 1]:
                    ans = original[l:r + 1]
                    length = r - l + 1
                lChar = original[l]
                if lChar in need:
                    if window[lChar] == need[lChar]:
                        valid -= 1
                    window[lChar] -= 1
                l += 1
        r += 1
    return "" if not ans else ans


if __name__ == '__main__':
    original = input()
    check = input()
    res = get_minimum_window(original, check)
    print(res)
