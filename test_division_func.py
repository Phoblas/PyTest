from cmath import inf

import pytest
import sys

#  DICT OPERATIONS


def add_pair_to_dict(dictionary, new_key, new_value):
    dictionary[new_key] = new_value
    return dictionary


def get_value(dictionary, key):
    return dictionary[key]


#   DICT CHECK OPERATIONS


def get_type_key(dictionary):
    if len(dictionary) == 0:
        return None
    return type((dictionary.keys()))


def get_type_value(dictionary):
    if len(dictionary) == 0:
        return None
    return type((dictionary.values()))


@pytest.mark.parametrize("dict_before, key,  value, dict_after", [({0: 1, 1: 2}, 3, 4, {0: 1, 1: 2, 3: 4}),
                                                                  ({"s1": 1, "s2": 2}, "s3", 3, {"s1": 1, "s2": 2, "s3": 3}),
                                                                  ({1: "s", 2 : "s"}, 3, "s", {1: "s", 2: "s", 3: "s"}),
                                                                  ({}, 1, 3, {1: 3})])
def test_good_case(dict_before, key, value, dict_after):
    assert add_pair_to_dict(dict_before, key, value) == dict_after


def test_receive_bad_type_key():
    if type("str") is get_type_key({1: 3}):
        with pytest.raises(TypeError):
            add_pair_to_dict({1: 3}, "str", 4)


def test_receive_bad_type_value():
    if type("str") is get_type_value({1: 3}):
        with pytest.raises(TypeError):
            add_pair_to_dict({1: 3}, 4, "str")


def test_receive_not_allow_key():
    key = "search_tag"
    dictionary = {1: 3}
    if "key" not in dictionary.keys():
        with pytest.raises(KeyError):
            get_value(dictionary, key)

#   TUPLE OPERATIONS

def func2(item2):
    return tuple(item2)

#   TUPLE OPERATIONS CHECK

@pytest.mark.parametrize("item2, answer", [(("apple", "banana", "cherry"), ("apple", "banana", "cherry")),
                                          ((1, 5, 7, 9, 3), (1, 5, 7, 9, 3)),
                                          ((True, False, False), (True, False, False))])
def test_tuple_simple_values(item2, answer):
    assert func2(item2) == answer

@pytest.mark.parametrize("item2, answer", [((123, 543, 53), 0),
                                          (("apple", "banana"), 0.5)])
def test_tuple_assertion_error(item2, answer):
    try:
        assert func2(item2) == answer
    except AssertionError:
        pass