import unittest


class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


class LruCache:
    '''
    16.25 LRU Cache: Design and build a "least recently used" cache, 
    which evicts the least recently used item. The cache should map 
    from keys to values (allowing you to insert and retrieve a value 
    associated with a particular key) and be initialized with a max size. 
    When it is full, it should evict the least recently used item.
    '''

    def __init__(self, max_size):
        self._max_size = max_size
        self._cache = {}

        self._key_to_node = {}
        self._head = None
        self._tail = None

    def put(self, key, value):
        if len(self._cache) == self._max_size:
            # remove least recently used key
            lru_key = self._head.value
            self._head = self._head.next
            self._head.prev = None
            del self._key_to_node[lru_key]

            del self._cache[lru_key]

        self._cache[key] = value

        # track new key
        node = Node(key)

        if self._head is None:
            self._head = node
            self._tail = node
        else:
            self._tail.next = node
            node.prev = self._tail
            self._tail = node

        self._key_to_node[key] = node

    def get(self, key):
        value = self._cache[key]

        # move key to the end of the list
        node = self._key_to_node[key]

        if node != self._tail:
            # no need to move tail node
            if node == self._head:
                self._head = self._head.next
                self._head.prev = None
            else:
                node.prev.next = node.next
                node.next.prev = node.prev

            self._tail.next = node
            node.prev = self._tail
            node.next = None
            self._tail = node

        return value


class LruCacheTest(unittest.TestCase):
    def test_lru_cache(self):
        cache = LruCache(5)
        cache.put('a', 1)
        cache.put('b', 2)
        cache.put('c', 3)
        cache.put('d', 4)
        cache.put('e', 5)

        self.assertEqual(1, cache.get('a'))
        self.assertEqual(1, cache.get('a'))
        self.assertEqual(3, cache.get('c'))
        self.assertEqual(2, cache.get('b'))

        cache.put('f', 6)
        self.assertEqual(6, cache.get('f'))

        with self.assertRaises(KeyError):
            cache.get('d')


if __name__ == '__main__':
    unittest.main()
