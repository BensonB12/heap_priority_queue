from typing import Dict, List
from subject import Subject


class Heap():
  def __init__(self):
    self.subjects: List[Subject] = [Subject(0, 0, 0)] # We will not be using index 1
    self.key_to_index: Dict[int, int] = {}

  def put(self, entry: Subject):
    if self.key_to_index.get(entry.key) is not None:
      index = self.key_to_index[entry.key]
      self.subjects[index] = entry # Need to sift/bubble
    self.subjects.append(entry) # Need to sift/bubble
    self.key_to_index[entry.key] = len(self.subjects) # Not always true
    
  def remove(self, key: int):
    if self.key_to_index.get(key) is None:
      return
    index = self.key_to_index[key]
    del self.subjects[index]
    # shift/bubble
    self.key_to_index.pop(key)
    
