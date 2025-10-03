import random
from typing import Any


class WRandom:
    """weighted random"""

    def __init__(self, choices: list[tuple[Any, int]]):
        self.num_choices = len(choices)
        self.items, weights = zip(*choices)
        total_weight = sum(weights)

        # normalize weights to scale with the number of choices
        scaled_probs = [w * self.num_choices / total_weight for w in weights]

        self.probability_table = [0.0] * self.num_choices
        self.alias_table = [0] * self.num_choices

        small = []  # indices of probabilities < 1
        large = []  # indices of probabilities >= 1

        for idx, prob in enumerate(scaled_probs):
            if prob < 1.0:
                small.append(idx)
            else:
                large.append(idx)

        while small and large:
            small_idx = small.pop()
            large_idx = large.pop()

            self.probability_table[small_idx] = scaled_probs[small_idx]
            self.alias_table[small_idx] = large_idx

            scaled_probs[large_idx] = scaled_probs[large_idx] - (
                1 - scaled_probs[small_idx]
            )
            if scaled_probs[large_idx] < 1.0:
                small.append(large_idx)
            else:
                large.append(large_idx)

        # handle leftover probabilities
        for leftover_idx in large + small:
            self.probability_table[leftover_idx] = 1.0
            self.alias_table[leftover_idx] = leftover_idx

    def choice(self) -> Any:
        # choose a random index and decide based on probability table
        idx = random.randint(0, self.num_choices - 1)
        if random.random() < self.probability_table[idx]:
            return self.items[idx]
        else:
            return self.items[self.alias_table[idx]]
