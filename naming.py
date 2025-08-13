from dataclasses import dataclass

@dataclass
class Names:
    # public tokens (opaque handles you can pass around)
    op: str; od: str; Op: str; Od: str   # downstream (lower) & upstream (upper)

class IndexRegistry:
    def __init__(self, n: int, step: int = 0):
        self.n = n
        self.step = step
        # raw base names without step
        self._base = [Names(f"op{i}", f"od{i}", f"Op{i}", f"Od{i}") for i in range(n)]

    def rails(self, i: int) -> Names:
        return self._base[i]

    def with_step(self, ind: str) -> str:
        # only add a step suffix to lowercase 'current' ends; uppercase stays stable
        if ind and ind[0].islower():  # op*, od*
            return f"{ind}_s{self.step}"
        return ind  # Op*, Od* remain as declared

    def advance(self):
        self.step += 1

    # convenience groups
    def upstream_inputs(self):
        return [x for i in range(self.n) for x in (self._base[i].Op, self._base[i].Od)]

    def downstream_outputs(self):
        return [x for i in range(self.n) for x in (self._base[i].op, self._base[i].od)]

