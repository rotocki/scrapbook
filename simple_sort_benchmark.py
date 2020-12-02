from random import randint
from timeit import default_timer


def is_sorted(elements):
    for idx in range(len(elements) - 1):
        x, y = elements[idx], elements[idx + 1]
        if x > y:
            return False
    return True


def measure_sort_time(sort_function, elements):
    start_timer = default_timer()
    sorted_elements = sort_function(elements)
    elapsed_time = default_timer() - start_timer
    return elapsed_time, sorted_elements


def check_sort(sort_function, elements):
    elapsed_time, sorted_elements = measure_sort_time(sort_function, elements)

    if not is_sorted(sorted_elements):
        raise Exception(
            "{} did not properly sort {}. Returned result: {}"
            .format(sort_function.__name__, elements, sorted_elements)
        )
    
    print("{} finished sorting in {:.6f}s"
          .format(sort_function.__name__, elapsed_time))


def standard_sort(elements):
    return sorted(elements)


def no_sort(elements):
    return elements


def random_sequence(length):
    return [randint(-length, length) for _ in range(length)]


def main():
    assert is_sorted([]) == True
    assert is_sorted([1]) == True
    assert is_sorted([1, 2, 3]) == True
    assert is_sorted([2, 1]) == False
    assert is_sorted([1, 3, 2]) == False
    assert is_sorted([3, 2, 1]) == False

    check_sort(standard_sort, [3, 2, 1])
    sequence = random_sequence(1000000)
    print("first 10 items of random sequence: {}".format(sequence[:10]))
    check_sort(standard_sort, sequence)

    # This line will fail to return a sorted result!
    check_sort(no_sort, [1, 2, 3, 5, 4])


if __name__ == '__main__':
    main()
