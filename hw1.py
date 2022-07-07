import re
import socket
import struct
import math
from itertools import product, combinations_with_replacement


def domain_name(url):
    return re.search(r'(//|www\.)([^www\.]\D+?)\..*$', url).group(2)


assert domain_name("http://google.com") == "google"
assert domain_name("http://google.co.jp") == "google"
assert domain_name("www.xakep.ru") == "xakep"
assert domain_name("https://youtube.com") == "youtube"


def int32_to_ip(int32):
    return socket.inet_ntoa(struct.pack("!I", int32))


assert int32_to_ip(2154959208) == "128.114.17.104"
assert int32_to_ip(0) == "0.0.0.0"
assert int32_to_ip(2149583361) == "128.32.10.1"


def zeros(n):
    prime_factor = 1
    number_of_zeros = 0
    while n >= prime_factor:
        prime_factor *= 5
        number_of_zeros += n // prime_factor
    return number_of_zeros


assert zeros(0) == 0
assert zeros(6) == 1
assert zeros(30) == 7


def bananas(s):
    temp_list = []
    data = product('ban-', repeat=len(s))
    for elem in data:
        str_elem = ''.join(elem)
        temp_list.append(str_elem)
    result = set([word for word in temp_list if word.replace('-', '') == 'banana'
                  and all(symbol == '-' or symbol == s[idx] for idx, symbol in enumerate(word))])
    return result


assert bananas("banann") == set()
assert bananas("banana") == {"banana"}
assert bananas("bbananana") == {"b-an--ana", "-banana--", "-b--anana", "b-a--nana", "-banan--a",
                     "b-ana--na", "b---anana", "-bana--na", "-ba--nana", "b-anan--a",
                     "-ban--ana", "b-anana--"}
assert bananas("bananaaa") == {"banan-a-", "banana--", "banan--a"}
assert bananas("bananana") == {"ban--ana", "ba--nana", "bana--na", "b--anana", "banana--", "banan--a"}


def count_find_num(primesL, limit):
    n = len(primesL)
    min_n = min(primesL)
    while (limit / math.prod(primesL)) // min_n >= 1:
        n += 1
        min_n += min_n
    ans = []
    for n in range(len(primesL), n + 1):
        a = combinations_with_replacement(primesL, n)
        for elem in a:
            if all(num in elem for num in primesL):
                if math.prod(elem) <= limit:
                    ans.append(math.prod(elem))
    result = [len(ans), max(ans)] if ans != [] else []
    return result


primesL = [2, 3]
limit = 200
assert count_find_num(primesL, limit) == [13, 192]

primesL = [2, 5]
limit = 200
assert count_find_num(primesL, limit) == [8, 200]

primesL = [2, 3, 5]
limit = 500
assert count_find_num(primesL, limit) == [12, 480]

primesL = [2, 3, 5]
limit = 1000
assert count_find_num(primesL, limit) == [19, 960]

primesL = [2, 3, 47]
limit = 200
assert count_find_num(primesL, limit) == []


