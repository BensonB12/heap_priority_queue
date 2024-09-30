from subject import Subject
from heap import Heap


def test_put_get():
    heap = Heap()
    heap.put(Subject(1, "a", 5))
    heap.put(Subject(2, "b", 2))
    assert heap.get(1).value == "a"
    assert heap.get(2).priority == 2


def test_get_next():
    heap = Heap()
    heap.put(Subject(1, "a", 5))
    heap.put(Subject(2, "b", 2))
    assert heap.get_next().value == "b"  # Min priority at the root


def test_remove():
    heap = Heap()
    heap.put(Subject(1, "a", 5))
    heap.put(Subject(2, "b", 2))
    heap.remove(2)
    assert heap.get_next().key == 1


def test_initialize():
    heap = Heap()
    entries = [Subject(1, "a", 5), Subject(2, "b", 2), Subject(3, "c", 3)]
    heap.initialize(entries)
    assert heap.get_next().key == 2  # Min priority at the root


def test_get_all():
    heap = Heap()
    heap.put(Subject(1, "a", 5))
    heap.put(Subject(2, "b", 2))
    heap.put(Subject(3, "c", 3))
    all_entries = heap.get_all()
    assert len(all_entries) == 3
