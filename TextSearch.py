import timeit
import pandas as pd


def knuth_morris_pratt_search(text, pattern):
    def compute_lps(pattern):
        lps = [0] * len(pattern)
        length = 0
        i = 1
        while i < len(pattern):
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1
        return lps

    M = len(pattern)
    N = len(text)
    lps = compute_lps(pattern)
    i = j = 0
    while i < N:
        if pattern[j] == text[i]:
            i += 1
            j += 1
        elif j != 0:
            j = lps[j - 1]
        else:
            i += 1
        if j == M:
            return i - j
    return -1


def boyer_moore_search(text, pattern):
    def build_shift_table(pattern):
        table = {}
        length = len(pattern)
        for index, char in enumerate(pattern[:-1]):
            table[char] = length - index - 1
        table.setdefault(pattern[-1], length)
        return table

    shift_table = build_shift_table(pattern)
    i = 0

    while i <= len(text) - len(pattern):
        j = len(pattern) - 1
        while j >= 0 and text[i + j] == pattern[j]:
            j -= 1
        if j < 0:
            return i
        i += shift_table.get(text[i + len(pattern) - 1], len(pattern))
    return -1


def rabin_karp_search(text, pattern):
    def polynomial_hash(s, base=256, modulus=101):
        n = len(s)
        hash_value = 0
        for i, char in enumerate(s):
            power_of_base = pow(base, n - i - 1) % modulus
            hash_value = (hash_value + ord(char) * power_of_base) % modulus
        return hash_value

    pattern_length = len(pattern)
    text_length = len(text)
    base = 256
    modulus = 101
    pattern_hash = polynomial_hash(pattern, base, modulus)
    current_slice_hash = polynomial_hash(text[:pattern_length], base, modulus)
    h_multiplier = pow(base, pattern_length - 1) % modulus
    for i in range(text_length - pattern_length + 1):
        if pattern_hash == current_slice_hash:
            if text[i : i + pattern_length] == pattern:
                return i
        if i < text_length - pattern_length:
            current_slice_hash = (
                current_slice_hash - ord(text[i]) * h_multiplier
            ) % modulus
            current_slice_hash = (
                current_slice_hash * base + ord(text[i + pattern_length])
            ) % modulus
            if current_slice_hash < 0:
                current_slice_hash += modulus
    return -1


def main():
    files = {"Text_1": "data/стаття1.txt", "Text_2": "data/стаття2.txt"}
    patterns = {
        "valid": "наступні",
        "non-valid": "абабагаламага",
        "semi-valid": "наступні_",
    }
    functions = {
        "Boyer-Moore": boyer_moore_search,
        "Knuth-Morris-Pratt": knuth_morris_pratt_search,
        "Rabin-Karp": rabin_karp_search,
    }

    txt = {}
    for tn, fn in files.items():
        with open(fn, "r", encoding="cp1251") as f:
            txt[tn] = f.read()

    for fn, f in functions.items():
        for tn in txt:
            for pn, p in patterns.items():
                t = timeit.timeit(lambda: f(txt[tn], p), number=100)
                print(f"{fn:<18} ( {tn}, pattern {pn:<10} ) t = {t:6f}")


if __name__ == "__main__":
    main()
