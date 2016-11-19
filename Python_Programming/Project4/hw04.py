#Homework 04 - CS2021

def every_other(s):
    """Mutates a linked list so that all the odd-indiced elements are removed
    (using 0-based indexing).

    >>> s = Link(1, Link(2, Link(3, Link(4))))
    >>> every_other(s)
    >>> s
    Link(1, Link(3))
    >>> odd_length = Link(5, Link(3, Link(1)))
    >>> every_other(odd_length)
    >>> odd_length
    Link(5, Link(1))
    >>> singleton = Link(4)
    >>> every_other(singleton)
    >>> singleton
    Link(4)
    """
    # Tracker will help traverse the linked list by pointing
    # to the next node in the list
    tracker = s.rest
    for i in range(1, len(s)):
        if tracker is Link.empty:
            break

        if i % 2 != 0:
            # Increment i by 2 to keep indices correct after removing
            # a node.
            i += 2
            if i == len(s) - 1:
                # Only difference here than below is that if this is the
                # last node in the list, make tracker.rest = ()
                tracker.first = tracker.rest.first
                tracker.rest = ()
                tracker = tracker.rest
            else:
                # Node at i's .first becomes node at (i + 1)'s .first
                tracker.first = tracker.rest.first
                # Node at i's .rest becomes node at (i + 1)'s .rest
                tracker.rest = tracker.rest.rest
                # Tracker points to next node
                tracker = tracker.rest
        else:
            tracker = tracker.rest



def has_cycle(s):
    """Return whether Link s contains a cycle.

    >>> s = Link(1, Link(2, Link(3)))
    >>> s.rest.rest.rest = s
    >>> has_cycle(s)
    True
    >>> t = Link(1, Link(2, Link(3)))
    >>> has_cycle(t)
    False
    """
    # List to keep track of Link objects visited.
    nodes_visited = []
    nodes_visited.append(s)

    # tracker helps us traverse linked list.
    tracker = s.rest

    # Iterate through linked list until end is found or
    # cycle is found.
    while tracker is not Link.empty:
        if tracker in nodes_visited:
            return True
        else:
            nodes_visited.append(tracker)
            tracker = tracker.rest

    return False


def has_cycle_constant(s):
    """Return whether Link s contains a cycle.

    >>> s = Link(1, Link(2, Link(3)))
    >>> s.rest.rest.rest = s
    >>> has_cycle_constant(s)
    True
    >>> t = Link(1, Link(2, Link(3)))
    >>> has_cycle_constant(t)
    False
    """
    # pointer1 will keep track of one node at a time.
    # pointer2 will traverse whole list and check if
    # it points to the same node as pointer 1.
    pointer1 = s
    pointer2 = s.rest

    # Loop will stop when either pointer1 is Link.empty
    # (i.e. no cycle found), or when pointer1 points to the same
    # node as pointer 2.
    while pointer1 != Link.empty or pointer2 != Link.empty:
        if pointer1 is pointer2:
            return True

        if pointer2 is Link.empty:
            return False
        else:
            pointer2 = pointer2.rest.rest
            pointer1 = pointer1.rest


##############################
# Linked List implementation #
##############################

class Link:

    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __len__(self):
        return 1 + len(self.rest)

    def __repr__(self):
        if self.rest is not Link.empty:
            rest_str = ', ' + repr(self.rest)
        else:
            rest_str = ''
        return 'Link({0}{1})'.format(repr(self.first), rest_str)

    def __contains__(self, value):
        if self.first == value:
            return True

        pointer = self.rest
        while pointer != Link.empty:
            if pointer.first == value:
                return True
            else:
                pointer = pointer.rest

  
    def __iadd__(self, other):
        pointer = self
        while pointer is not Link.empty:
            if pointer.first is Link.empty:
                return other

            pointer = pointer.rest
            if pointer.rest is Link.empty:
                pointer.rest = other
                return self


class ScaleIterator:
    """An iterator the scales elements of the iterable s by a number k.

    >>> s = ScaleIterator([1, 5, 2], 5)
    >>> list(s)
    [5, 25, 10]

    >>> m = ScaleIterator(naturals(), 2)
    >>> [next(m) for _ in range(5)]
    [2, 4, 6, 8, 10]
    """
    def __init__(self, s, k):
        self.s = iter(s)
        self.k = k

    def __iter__(self):
        return self

    def __next__(self):
        try:
            item = next(self.s) * self.k
            return item
        except IndexError:
            raise StopIteration




def scale(s, k):
    """Yield elements of the iterable s scaled by a number k.

    >>> s = scale([1, 5, 2], 5)
    >>> type(s)
    <class 'generator'>
    >>> list(s)
    [5, 25, 10]

    >>> m = scale(naturals(), 2)
    >>> [next(m) for _ in range(5)]
    [2, 4, 6, 8, 10]
    """
    s_iter = iter(s)
    while True:
        yield next(s_iter) * k



def merge(s0, s1):
    """Yield the elements of strictly increasing iterables s0 and s1, removing
    repeats. Assume that s0 and s1 have no repeats. You can also assume that s0
    and s1 represent infinite sequences.

    >>> twos = scale(naturals(), 2)
    >>> threes = scale(naturals(), 3)
    >>> m = merge(twos, threes)
    >>> type(m)
    <class 'generator'>
    >>> [next(m) for _ in range(10)]
    [2, 3, 4, 6, 8, 9, 10, 12, 14, 15]
    """
    i0, i1 = iter(s0), iter(s1)
    e0, e1 = next(i0), next(i1)

    list_of_yielded = []


    while True:
        if e0 in list_of_yielded:
            while e0 in list_of_yielded:
                e0 = next(i0)

        if e1 in list_of_yielded:
            while e1 in list_of_yielded:
                e1 = next(i1)

        if e0 == e1:
            yield e0
            list_of_yielded.append(e0)
            e0, e1 = next(i0), next(i1)
        elif e0 < e1:
            yield e0
            yield e1
            list_of_yielded.append(e0)
            list_of_yielded.append(e1)
            e0, e1 = next(i0), next(i1)
        else:
            yield e1
            yield e0
            list_of_yielded.append(e1)
            list_of_yielded.append(e0)
            e0, e1 = next(i0), next(i1)



def make_s():
    """A generator function that yields all positive integers with only factors
    2, 3, and 5.

    >>> s = make_s()
    >>> type(s)
    <class 'generator'>
    >>> [next(s) for _ in range(20)]
    [1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, 16, 18, 20, 24, 25, 27, 30, 32, 36]
    """
    s = naturals()
    s2 = scale(s, 2)
    s3 = scale(s, 3)
    s5 = scale(s, 5)

    s_and_s2 = merge(s, s2)
    s3_and_s5 = merge(s3, s5)
    all_s = merge(s_and_s2, s3_and_s5)
    while True:
        return all_s


def naturals():
    """A generator function that yields the infinite sequence of natural
    numbers, starting at 1. 

    >>> m = naturals()
    >>> type(m)
    <class 'generator'>
    >>> [next(m) for _ in range(10)]
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    """
    i = 1
    while True:
        yield i
        i += 1
