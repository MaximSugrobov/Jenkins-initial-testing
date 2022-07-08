import re
import socket
import struct
import math
from itertools import combinations_with_replacement, combinations


def domain_name(url):
    split_url = url.split('/')
    if split_url[0] == 'http:' or split_url[0] == 'https:':
        full_name = split_url[2].split('.')
    else:
        full_name = split_url[0].split('.')
    if len(full_name) == 2:
        dom_name = full_name[0]
    elif len(full_name[0]) > len(full_name[1]):
        dom_name = full_name[0]
    else:
        dom_name = full_name[1]
    return dom_name
    # Регулярку я тоже отредактировал
    # return re.search(r'(https?://|www\.)?(\w{0,3}\.)?([a-z0-9-_]+)(\..+)?', url).group(3)


assert domain_name("http://google.com") == "google"
assert domain_name("http://google.co.jp") == "google"
assert domain_name("www.xakep.ru") == "xakep"
assert domain_name("https://youtube.com") == "youtube"
assert domain_name("http://www.zombie-bites.com") == "zombie-bites"
assert domain_name("http://ru.some-url.co.org") == "some-url"


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
    result = set()
    banana = 'banana'
    group_len = len(s) - len(banana)
    data = combinations(range(len(s)), group_len)
    for elem in data:
        s_list = list(s)
        for number in elem:
            s_list[number] = '-'
        str_temp = ''.join(s_list)
        if str_temp.replace('-', '') == banana:
            result.add(str_temp)
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


