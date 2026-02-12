from functools import lru_cache

@lru_cache(None)
def x(a, b):
    # Ackermann function: recursive computation with base cases and caching
    # Base case: when b=0, return a+1
    # Recursive case: computes nested function calls or reduces parameters
    return a + 1 if b == 0 else x(a - 1, x(a, b - 1)) if a > 0 else x(1, b - 1)

def y(n):
    # Gray code conversion: XOR with right-shifted version to produce reflected binary code
    # Mask to 32-bit unsigned integer to maintain consistent bit width
    return (n ^ (n >> 1)) & 0xffffffff

def z(s):
    r = 0
    for i, c in enumerate(s):
        # Transform character using Gray code based on Ackermann function result
        # XOR accumulates the encoded values
        r ^= y(ord(c) + x(i % 2, ord(c) % 3))
        # Rotate left by 5 bits: shift left 5, OR with bits shifted out on right
        # Mask to keep result in 32-bit range
        r = ((r << 5) | (r >> 27)) & 0xffffffff
    return r

def main():
    import sys
    data = sys.stdin.read().strip()
    print(hex(z(data)))

if __name__ == "__main__":
    main()
