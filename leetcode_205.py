def isIsomorphic(s: str, t: str) -> bool:
    return [*map(s.index, s)] == [*map(t.index, t)]

if __name__ == '__main__':
    print(isIsomorphic("egg", "add"))