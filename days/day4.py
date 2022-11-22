from Day import Day
import hashlib

# Create Day Object & Get Input
day = Day(4, 'The Ideal Stocking Stuffer')
input = day.input

# Function to Calculate Hash Solution
def get_hashes(key, zeroes):
    n = 1
    prefix = zeroes * '0'

    while True:
        s = key + str(n)
        h = hashlib.md5(s.encode()).hexdigest()[:zeroes]
        if h == prefix:
            return n
        n += 1
