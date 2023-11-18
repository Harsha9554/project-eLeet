def car_fleet_853(t, pos, spd):
    class car:
        def __init__(self, pos, spd):
            self.pos = pos
            self.spd = spd

        def __str__(self):
            return f"(p:{self.pos}, s:{self.spd})"

        def __repr__(self):
            return f"(p:{self.pos}, s:{self.spd})"

    def get_collision_point(c1, c2):
        # s0: 0-4, 4-2
        # s1: 4-4, 6-2
        # s2: 8-4, 8-2
        t = (c2.pos - c1.pos) / (c1.spd - c2.spd)
        return c1.pos + c1.spd * t

    def does_collide(c1, c2, t):
        if c1.spd <= c2.spd:
            return False
        else:
            if get_collision_point(c1, c2) <= t:
                return True
            return False

    n = len(pos)
    if n <= 1:
        return n

    sorted_cars = []
    stack = []

    for i, p in enumerate(pos):
        c = car(p, spd[i])
        sorted_cars.append(c)

    sorted_cars.sort(key=lambda c: c.pos)
    # print(sorted_cars)

    for c in sorted_cars:
        while stack and does_collide(stack[-1], c, t):
            stack.pop()
        stack.append(c)

    return len(stack)
