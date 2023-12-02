import unittest

from chapter5.queue_full_capacity_exception import QueueFullCapacityException
from chapter5.simulate_Queue import Queue


class MyTestCase(unittest.TestCase):
    def test_if_queue_is_empty(self):
        queue = Queue(5)
        self.assertTrue(queue.is_empty())

    def test_that_queue_is_not_empty(self):
        queue = Queue(5)
        queue.add(5)
        self.assertFalse(queue.is_empty())

    def test_that_i_can_add_two_and_remove_one(self):
        queue = Queue(5)
        queue.add(54)
        queue.add(65)
        self.assertEquals(54, queue.remove())

    def test_that_i_can_add_two_elements_if_i_remove_three_its_throw_an_exception(self):
        queue = Queue(5)
        queue.add(54)
        queue.add(65)
        queue.remove()
        queue.remove()
        with self.assertRaises(QueueFullCapacityException) as ex:
            queue.remove()

    def test_that_i_can_add_two_elements_if_i_peek_i_get_the_first_element(self):
        queue = Queue(5)
        queue.add(54)
        queue.add(65)
        self.assertEquals(54, queue.peek())

    def test_that_when_the_queue_is_full_i_cant_add_to_it(self):
        queue = Queue(5)
        queue.add(54)
        queue.add(65)
        queue.add(65)
        queue.add(65)
        queue.add(65)
        with self.assertRaises(QueueFullCapacityException) as ex:
            queue.add(23)



if __name__ == '__main__':
    unittest.main()
