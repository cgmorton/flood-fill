import numpy as np
# import pytest

import fill


def test_fast_fill_8way():
    print('Testing fast_fill() 8-way')
    data = np.array([
        [1.0, 1.0, 1.0, 1.0, 1.0],
        [1.0, 0.5, 1.0, 1.0, 1.0],
        [1.0, 1.0, 0.6, 1.0, 1.0],
        [1.0, 0.7, 1.0, 1.0, 1.0],
        [1.0, 0.8, 1.0, 1.0, 1.0]])
    expected = np.array([
        [1.0, 1.0, 1.0, 1.0, 1.0],
        [1.0, 0.8, 1.0, 1.0, 1.0],
        [1.0, 1.0, 0.8, 1.0, 1.0],
        [1.0, 0.8, 1.0, 1.0, 1.0],
        [1.0, 0.8, 1.0, 1.0, 1.0]])
    np.testing.assert_array_equal(
        fill.fast_fill(data, four_way=False), expected)


def test_fast_fill_4way():
    print('Testing fast_fill() 4-way')
    data = np.array([
        [1.0, 1.0, 1.0, 1.0, 1.0],
        [1.0, 0.5, 1.0, 1.0, 1.0],
        [1.0, 1.0, 0.6, 1.0, 1.0],
        [1.0, 0.7, 1.0, 1.0, 1.0],
        [1.0, 0.8, 1.0, 1.0, 1.0]])
    expected = np.array([
        [1.0, 1.0, 1.0, 1.0, 1.0],
        [1.0, 1.0, 1.0, 1.0, 1.0],
        [1.0, 1.0, 1.0, 1.0, 1.0],
        [1.0, 0.8, 1.0, 1.0, 1.0],
        [1.0, 0.8, 1.0, 1.0, 1.0]])
    np.testing.assert_array_equal(
        fill.fast_fill(data, four_way=True), expected)


# def test_slow_fill_8way():
#     print('Testing slow_fill() 8-way')
#     data = np.array([
#         [1.0, 1.0, 1.0, 1.0, 1.0],
#         [1.0, 0.5, 1.0, 1.0, 1.0],
#         [1.0, 1.0, 0.6, 1.0, 1.0],
#         [1.0, 0.7, 1.0, 1.0, 1.0],
#         [1.0, 0.8, 1.0, 1.0, 1.0]])
#     expected = np.array([
#         [1.0, 1.0, 1.0, 1.0, 1.0],
#         [1.0, 0.8, 1.0, 1.0, 1.0],
#         [1.0, 1.0, 0.8, 1.0, 1.0],
#         [1.0, 0.8, 1.0, 1.0, 1.0],
#         [1.0, 0.8, 1.0, 1.0, 1.0]])
#     np.testing.assert_array_equal(
#         fill.slow_fill(data, four_way=False), expected)


# def test_slow_fill_4way():
#     print('Testing slow_fill() 4-way')
#     data = np.array([
#         [1.0, 1.0, 1.0, 1.0, 1.0],
#         [1.0, 0.5, 1.0, 1.0, 1.0],
#         [1.0, 1.0, 0.6, 1.0, 1.0],
#         [1.0, 0.7, 1.0, 1.0, 1.0],
#         [1.0, 0.8, 1.0, 1.0, 1.0]])
#     expected = np.array([
#         [1.0, 1.0, 1.0, 1.0, 1.0],
#         [1.0, 1.0, 1.0, 1.0, 1.0],
#         [1.0, 1.0, 1.0, 1.0, 1.0],
#         [1.0, 0.8, 1.0, 1.0, 1.0],
#         [1.0, 0.8, 1.0, 1.0, 1.0]])
#     np.testing.assert_array_equal(
#         fill.slow_fill(data, four_way=True), expected)


def test_np_binary_erosion_8way():
    print('Testing np_binary_erosion() 8-way')
    structure = np.array([[1, 1, 1], [1, 1, 1], [1, 1, 1]]).astype(np.bool)

    data = np.array([
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 0],
        [1, 1, 1, 0, 0],
        [0, 1, 1, 1, 1],
        [1, 1, 1, 1, 1]])
    expected = np.array([
        [0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]])
    np.testing.assert_array_equal(
        fill.np_binary_erosion(data, structure), expected)


def test_np_binary_erosion_4way():
    print('Testing np_binary_erosion() 4-way')
    # Cross structuring element
    structure = np.array([[0, 1, 0], [1, 1, 1], [0, 1, 0]]).astype(np.bool)

    data = np.array([
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 0],
        [1, 1, 1, 0, 0],
        [0, 1, 1, 1, 1],
        [1, 1, 1, 1, 1]])
    expected = np.array([
        [0, 0, 0, 0, 0],
        [0, 1, 1, 0, 0],
        [0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0]])
    np.testing.assert_array_equal(
        fill.np_binary_erosion(data, structure), expected)
