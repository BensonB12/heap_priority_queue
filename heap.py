from typing import List

from subject import Subject


class Heap:
    def __init__(self):
        self.subjects: List[Subject] = [None]  # We will not be using index 0
        self.key_to_index: Dict[int, int] = {}

    def put(self, entry: Subject):
        if self.key_to_index.get(entry.key) is not None:
            index = self.key_to_index[entry.key]
            self.subjects[index] = entry
            self._sift_up(index)
            self._sift_down(index)
        else:
            self.subjects.append(entry)
            index = len(self.subjects) - 1
            self.key_to_index[entry.key] = index
            self._sift_up(index)

    def remove(self, key: int):
        if self.key_to_index.get(key) is None:
            return
        index = self.key_to_index[key]

        if index == len(self.subjects) - 1:
            self.subjects.pop()
        else:
            last_entry = self.subjects.pop()
            self.subjects[index] = last_entry
            self.key_to_index[last_entry.key] = index
            self._sift_up(index)
            self._sift_down(index)

        del self.key_to_index[key]

    def get(self, key: int):
        if key not in self.key_to_index:
            return None
        return self.subjects[self.key_to_index[key]]

    def get_next(self):
        if len(self.subjects) > 1:
            return self.subjects[1]
        return None

    def initialize(self, entries: List[Subject]):
        self.subjects = [None] + entries
        self.key_to_index = {entry.key: i + 1 for i, entry in enumerate(entries)}
        for i in range(len(self.subjects) // 2, 0, -1):
            self._sift_down(i)

    def get_all(self):
        return self.subjects[1:]

    def _swap(self, parent, child):
        self.subjects[parent], self.subjects[child] = (
            self.subjects[child],
            self.subjects[parent],
        )
        self.key_to_index[self.subjects[parent].key] = parent
        self.key_to_index[self.subjects[child].key] = child

    def _sift_down(self, index):
        while 2 * index < len(self.subjects):
            left = 2 * index
            right = left + 1
            smallest = left
            if (
                right < len(self.subjects)
                and self.subjects[right].priority < self.subjects[left].priority
            ):
                smallest = right
            if self.subjects[smallest].priority < self.subjects[index].priority:
                self._swap(index, smallest)
                index = smallest
            else:
                break

    def _sift_up(self, index):
        while index > 1:
            parent_index = index // 2
            if self.subjects[index].priority < self.subjects[parent_index].priority:
                self._swap(index, parent_index)
                index = parent_index
            else:
                break
