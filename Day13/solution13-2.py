from math import gcd, isclose
import math

class EgcdResult:
    def __init__(self, g, r, s):
        self.g = g
        self.r = r
        self.s = s

def egcd(a, b):
    """Extended Euclidean Algorithm."""
    old_r, r = a, b
    old_s, s = 1, 0
    old_t, t = 0, 1

    while r != 0:
        q = old_r // r
        old_r, r = r, old_r - q * r
        old_s, s = s, old_s - q * s
        old_t, t = t, old_t - q * t

    return EgcdResult(old_r, old_s, old_t)

class SQ:
    def __init__(self, p, q):
        self.p = p
        self.q = q  # p + q * t

def find(a, b, c):
    """Solve the equation a * x + b * y = c."""
    result = egcd(a, b)
    g, s, _ = result.g, result.r, result.s
    rc = c % b

    if rc % g != 0:
        return None

    p0 = s * (rc // g)
    q0 = b // g

    while p0 < 0:
        p0 += q0
    if p0 > q0:
        p0 %= q0

    assert (c - a * p0) % b == 0
    assert (c - a * (p0 + q0)) % b == 0

    return SQ(p0, q0)

def combine(a, b):
    """Combine two SQ equations."""
    g = egcd(a.q, b.q).g

    if a.p % g != b.p % g:
        return None

    p0 = a.p
    while p0 % b.q != b.p:
        p0 += a.q

    q0 = (a.q // g) * b.q

    assert p0 % a.q == a.p
    assert p0 % b.q == b.p

    return SQ(p0, q0)

def main():
    OFFSET = 10**13
    sum_cost = 0

    with open("Day13/input.txt", "r") as file:
        parts = file.read().strip().split("\n\n")

    for part in parts:
        lines = part.split("\n")
        ax, ay = map(int, lines[0].replace("Button A: X+", "").replace("Y+", "").split(", "))
        bx, by = map(int, lines[1].replace("Button B: X+", "").replace("Y+", "").split(", "))
        px, py = map(lambda x: int(x) + OFFSET, lines[2].replace("Prize: X=", "").replace("Y=", "").split(", "))

        sx = find(ax, bx, px)
        if sx is None:
            continue

        sy = find(ay, by, py)
        if sy is None:
            continue

        sc = combine(sx, sy)
        if sc is None:
            continue

        best = float('inf')

        def test(a):
            nonlocal best
            rx = px - ax * a
            ry = py - ay * a

            if rx < 0 or ry < 0:
                return False

            b = rx // bx

            if rx == b * bx and ry == b * by:
                cost = 3 * a + b
                if cost < best:
                    best = cost
            return True

        a = sc.p
        rx = px - ax * sc.p
        ry = py - ay * sc.p

        assert rx % bx == 0
        assert ry % by == 0

        xb = rx // bx
        yb = ry // by

        dxb = ax * sc.q // bx
        dyb = ay * sc.q // by

        if xb == yb:
            print("!! Found on the first try (never happened for me)")
            test(a)
            if dxb == dyb:
                print("!!! Multiple solutions")
                test(a + (rx // ax) // sc.q * sc.q)
        elif dxb != dyb and (math.copysign(1, xb - yb) == math.copysign(1, dxb - dyb)):
            d = abs(xb - yb)
            dd = abs(dxb - dyb)
            if d % dd == 0:
                test(a + (d // dd) * sc.q)

        if best < float('inf'):
            sum_cost += best

    print(sum_cost)

if __name__ == "__main__":
    main()
