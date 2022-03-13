import random
from queue import Queue
import unittest


class AnimalShelter:
    '''
    3.6 Animal Shelter: An animal shelter, which holds only dogs and cats, operates on a strictly
    "first in, first out" basis. People must adopt either the "oldest" (based on arrival time)
    of all animals at the shelter, or they can select whether they would prefer a dog or a cat
    (and will receive the oldest animal of that type). They cannot select which specific animal
    they would like. Create the data structures to maintain this system and implement operations
    such as enqueue, dequeueAny, dequeueDog, and dequeueCat.You may use the built-in LinkedList data structure.
    '''
    def __init__(self):
        self._dogs = Queue()
        self._cats = Queue()
        self._seq = 0

    def enqueue(self, animal, is_dog):
        if is_dog:
            queue = self._dogs
        else:
            queue = self._cats

        queue.enqueue([self._seq, animal])
        self._seq += 1

    def dequeue_any(self):
        if self._dogs.is_empty() and self._cats.is_empty():
            return None

        if self._dogs.is_empty():
            _, animal = self._cats.dequeue()

            return animal

        if self._cats.is_empty():
            _, animal = self._dogs.dequeue()

            return animal

        dog_seq, dog = self._dogs.peek()
        cat_seq, cat = self._cats.peek()

        if dog_seq < cat_seq:
            _, animal = self._dogs.dequeue()
        else:
            _, animal = self._cats.dequeue()

        return animal

    def dequeue_dog(self):
        if self._dogs.is_empty():
            return None

        _, animal = self._dogs.dequeue()

        return animal

    def dequeue_cat(self):
        if self._cats.is_empty():
            return None

        _, animal = self._cats.dequeue()

        return animal


class AnimalShelterTest(unittest.TestCase):
    def test_dequeue_any(self):
        animals = [random.randint(0, 1) for _ in range(10)]

        shelter = AnimalShelter()

        for i, is_dog in enumerate(animals):
            shelter.enqueue(i, is_dog)

        for i in range(len(animals)):
            animal = shelter.dequeue_any()
            self.assertEqual(i, animal)

    def test_dequeue_dog_or_cat(self):
        animals = [random.randint(0, 1) for _ in range(10)]

        shelter = AnimalShelter()

        for i, is_dog in enumerate(animals):
            shelter.enqueue(i, is_dog)

        for i, is_dog in enumerate(animals):
            if is_dog:
                animal = shelter.dequeue_dog()
            else:
                animal = shelter.dequeue_cat()

            self.assertEqual(i, animal)


if __name__ == '__main__':
    unittest.main()
