class DT:
    def __init__(self, max_depth, min_entropy, min_elem):
        self.max_depth = max_depth
        self.min_entropy = min_entropy
        self.min_elem = min_elem
        self.root = node()