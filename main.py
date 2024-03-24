class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list

    def __iter__(self):
        # print('Цикл начинается')
        self.counter = 0
        self.new = []
        self.list1 = iter(self.list_of_list[self.counter])
        # print(23, self.list1)
        return self

    def __next__(self):
        try:
            item = next(self.list1)
            # print(item)
        except StopIteration:
            if self.counter == len(self.list_of_list) - 1:
                raise StopIteration
            self.counter += 1
            self.list1 = iter(self.list_of_list[self.counter])
            item = next(self.list1)
            # print(item)
        return item


def test_1():
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):
        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()
