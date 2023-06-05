from typing import List

import pytest

from dsa_and_algorithms.001_linear_data_structures.001_arrays_and_strings import (
    are_anagrams,
    arrays_are_equal,
    find_all_anagrams,
    find_duplicates,
    no_repeated_chars,
    print_back_and_forth,
    print_diagonals,
    print_spiral,
    print_substrings,
    remove_even,
    reverse_array,
    smallest_substring,
    strings_are_opposite,
    subarray_sums,
    two_sum,
    zig_zag,
)


@pytest.mark.parametrize(
    "input_array,expected",
    [[1, 2, 3, 4, 5], [5, 4, 3, 2, 1]],
)
def test_reverse_array(input_array: List[int], expected: List[int]) -> None:
    assert reverse_array(input_array) == expected
    
@pytest.mark.parametrize(
    "input_string,expected",
    ["iloveinterviewprep", "ioenevepe"],
)
def test_remove_even(input_string: str, expected: str) -> None:
    assert remove_even(input_string) == expected
    
@pytest.mark.parametrize(
    "input_string,num_rows,expected",
    ["PAYPALISHIRING", 3,"PAHNAPLSIIGYIR"],
)
def test_zig_zag(input_string: str, num_rows: int, expected: str) -> None:
    assert zig_zag(input_string, num_rows) == expected
    
@pytest.mark.parametrize(
    "input_array,expected",
    [
        [
            [1, 2, 3, 4, 5],
            [6, 7, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 17, 18, 19, 20]
        ],
        [1, 2, 3, 4, 5, 10, 9, 8, 7, 6, 11, 12, 13, 14, 15, 20, 19, 18, 17, 16]
    ],
)
def test_print_back_and_forth(input_array: List[List[int]], expected: List[int]) -> None:
    assert print_back_and_forth(input_array) == expected

@pytest.mark.parametrize(
    "input_array,expected",
    [
        [
            [1, 2, 3, 4, 5],
            [6, 7, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 17, 18, 19, 20]
        ],
        [1, 2, 3, 4, 5, 10, 15, 20, 19, 18, 17, 16, 11, 6, 7, 8, 9, 14, 13, 12]
    ],
)
def test_print_spiral(input_array: List[List[int]], expected: List[int]) -> None:
    assert print_spiral(input_array) == expected

@pytest.mark.parametrize(
    "input_array,expected",
    [
        [
            [1, 2, 3, 4, 5],
            [6, 7, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 17, 18, 19, 20]
        ],
        [1, 2, 6, 11, 7, 3, 4, 8, 12, 16, 17, 13, 9, 5, 10, 14, 18, 19, 15, 20]
    ],
)
def test_print_diagonals(input_array: List[List[int]], expected: List[int]) -> None:
    assert print_diagonals(input_array) == expected

@pytest.mark.parametrize(
    "input_string,expected",
    ["abc", ["a", "ab", "abc", "b", "bc", "c"]],
)
def test_print_substrings(input_string: str, expected: List[str]) -> None:
    assert print_substrings(input_string) == expected

@pytest.mark.parametrize(
    "input_array,expected",
    [[1, 2, 3, 2], 2],
)
def test_find_duplicates(input_array: List[int], expected: int) -> None:
    assert find_duplicates(input_array) == expected

@pytest.mark.parametrize(
    "input_array,target,expected",
    [[1, 2, 3, 4, 5, 3], 5, [[1, 4], [2, 3]]],
)
def test_two_sum(input_array: List[int], target: int, expected: List[List[int]]) -> None:
    assert two_sum(input_array, target) == expected
    
@pytest.mark.parametrize(
    "input_array_1,input_array_2,expected",
    [[[1, 2, 3], [1, 2, 3], True], [[3, 2, 1], [1, 2, 3], False]],
)
def test_arrays_are_equal(input_array_1: List[int], input_array_2: List[int], expected: boo;) -> None:
    assert arrays_are_equal(input_array_1, input_array_2) == expected

@pytest.mark.parametrize(
    "input_string_1,input_string_2,expected",
    [["abcd", "dcba", True], ["abc", "dbc", False]],
)
def test_strings_are_opposite(input_string_1: str, input_string_2: str, expected: bool) -> None:
    assert strings_are_opposite(input_string_1, input_string_2) == expected

@pytest.mark.parametrize(
    "input_string_1,input_string_2,expected",
    [["abcd", "dcba", True], ["abc", "bac", True], ["abc", "dbc", False]],
)
def test_are_anagrams(input_string_1: str, input_string_2: str, expected: bool) -> None:
    assert are_anagrams(input_string_1, input_string_2) == expected

@pytest.mark.parametrize(
    "input_array,k,expected",
    [[1, 2, 3, 4, 5], 3, [6, 9, 12]],
)
def test_subarray_sums(input_array: List[int], k: int, expected: List[int]) -> None:
    assert subarray_sums(input_array, k) == expected
    
@pytest.mark.parametrize(
    "input_string,expected",
    ["abcdbaba", 4],
)
def test_no_repeated_chars(input_string: str, expected: int) -> None:
    assert no_repeated_chars(input_string, num_rows) == expected

@pytest.mark.parametrize(
    "input_string_1,input_string_2,expected",
    ["abcbcba", "abc", [0, 4]],
)
def test_find_all_anagrams(input_string_1: str, input_string_2: str, expected: List[int]) -> None:
    assert find_all_anagrams(input_string_1, input_string_2) == expected

@pytest.mark.parametrize(
    "input_string_1,input_string_2,expected",
    ["aabbccdd", "abc", "abbc"],
)
def test_smallest_substring(input_string_1: str, input_string_2: str, expected: str) -> None:
    assert smallest_substring(input_string, num_rows) == expected
