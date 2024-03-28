class Segtree:
    def __init__(self, lb, rb):
        self.lb = lb
        self.rb = rb
        self.s = 0
        self.l = None
        self.r = None

        if lb != rb:
            t = (lb + rb) // 2
            self.l = Segtree(lb, t)
            self.r = Segtree(t, rb)

    def copy(self):
        if self.l:
            self.l = Segtree(self.l.lb, self.l.rb)
            self.r = Segtree(self.r.lb, self.r.rb)

    def add(self, k, x):
        self.copy()
        self.s += x
        if self.l:
            if k < self.l.rb:
                self.l.add(k, x)
            else:
                self.r.add(k, x)

    def sum(self, lq, rq):
        if lq <= self.lb and self.rb <= rq:
            return self.s
        if max(self.lb, lq) >= min(self.rb, rq):
            return 0
        return self.l.sum(lq, rq) + self.r.sum(lq, rq)


roots = []
roots.append(Segtree(0, 2))

# def add(k, x, v):
#     root = Segtree(roots[v].lb, roots[v].rb)
#     root.add(k, x)
#     roots.append(root)