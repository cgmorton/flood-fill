import numpy as np
# import pytest

import fill


def test_np_binary_erosion_8way():
    print('Testing np_binary_erosion() 8-way')
    structure = np.array([[1, 1, 1], [1, 1, 1], [1, 1, 1]]).astype(np.bool)

    data = np.array([
        [1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 0, 1],
        [1, 1, 1, 0, 0, 1],
        [0, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1]])
    expected = np.array([
        [0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0]])
    np.testing.assert_array_equal(
        fill.np_binary_erosion(data, structure), expected)


def test_np_binary_erosion_4way():
    print('Testing np_binary_erosion() 4-way')
    # Cross structuring element
    structure = np.array([[0, 1, 0], [1, 1, 1], [0, 1, 0]]).astype(np.bool)

    data = np.array([
        [1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 0, 1],
        [1, 1, 1, 0, 0, 1],
        [0, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1]])
    expected = np.array([
        [0, 0, 0, 0, 0, 0],
        [0, 1, 1, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0]])
    np.testing.assert_array_equal(
        fill.np_binary_erosion(data, structure), expected)


def test_flood_fill_8way():
    print('Testing flood_fill() 8-way')
    data = np.array([
        [1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
        [1.0, 0.5, 1.0, 1.0, 1.0, 0.9],
        [1.0, 1.0, 0.6, 1.0, 1.0, 1.0],
        [1.0, 0.7, 1.0, 1.0, 1.0, 1.0],
        [1.0, 0.8, 1.0, 1.0, 1.0, 1.0]])
    expected = np.array([
        [1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
        [1.0, 0.8, 1.0, 1.0, 1.0, 0.9],
        [1.0, 1.0, 0.8, 1.0, 1.0, 1.0],
        [1.0, 0.8, 1.0, 1.0, 1.0, 1.0],
        [1.0, 0.8, 1.0, 1.0, 1.0, 1.0]])
    np.testing.assert_array_equal(
        fill.flood_fill(data, four_way=False), expected)


def test_flood_fill_4way():
    print('Testing flood_fill() 4-way')
    data = np.array([
        [1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
        [1.0, 0.5, 1.0, 1.0, 1.0, 0.9],
        [1.0, 1.0, 0.6, 1.0, 1.0, 1.0],
        [1.0, 0.7, 1.0, 1.0, 1.0, 1.0],
        [1.0, 0.8, 1.0, 1.0, 1.0, 1.0]])
    expected = np.array([
        [1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
        [1.0, 1.0, 1.0, 1.0, 1.0, 0.9],
        [1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
        [1.0, 0.8, 1.0, 1.0, 1.0, 1.0],
        [1.0, 0.8, 1.0, 1.0, 1.0, 1.0]])
    np.testing.assert_array_equal(
        fill.flood_fill(data, four_way=True), expected)


def test_outflow_fill_8way():
    print('Testing outflow_fill() 8-way')
    data = np.array([
        [1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
        [1.0, 0.1, 1.0, 1.0, 1.0, 1.0],
        [0.1, 0.6, 0.2, 0.3, 1.0, 1.0],
        [0.2, 0.7, 0.3, 0.4, 0.1, 1.0],
        [1.0, 0.8, 0.4, 1.0, 1.0, 1.0],
        [1.0, 1.0, 0.2, 1.0, 1.0, 1.0]])
    expected = np.array([
        [1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
        [1.0, 0.3, 1.0, 1.0, 1.0, 1.0],
        [0.3, 0.6, 0.3, 0.3, 1.0, 1.0],
        [0.3, 0.7, 0.3, 0.4, 0.1, 1.0],
        [1.0, 0.8, 0.4, 1.0, 1.0, 1.0],
        [1.0, 1.0, 0.4, 1.0, 1.0, 1.0]])
    outflow_pts = [[3, 4]]
    np.testing.assert_array_equal(fill.outflow_fill(
        data, outflow_pts, four_way=False), expected)


def test_outflow_fill_4way():
    print('Testing outflow_fill() 4-way')
    data = np.array([
        [1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
        [1.0, 0.1, 1.0, 1.0, 1.0, 1.0],
        [0.1, 0.6, 0.2, 0.3, 1.0, 1.0],
        [0.2, 0.7, 0.3, 0.4, 0.1, 1.0],
        [1.0, 0.8, 0.4, 1.0, 1.0, 1.0],
        [1.0, 1.0, 0.2, 1.0, 1.0, 1.0]])
    expected = np.array([
        [1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
        [1.0, 0.6, 1.0, 1.0, 1.0, 1.0],
        [0.6, 0.6, 0.4, 0.4, 1.0, 1.0],
        [0.6, 0.7, 0.4, 0.4, 0.1, 1.0],
        [1.0, 0.8, 0.4, 1.0, 1.0, 1.0],
        [1.0, 1.0, 0.4, 1.0, 1.0, 1.0]])
    outflow_pts = [[3, 4]]
    np.testing.assert_array_equal(fill.outflow_fill(
        data, outflow_pts, four_way=True), expected)


def test_outflow_fill_8way_nodata():
    print('Testing outflow_fill() 8-way')
    data = np.array([
        [1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
        [1.0, 0.1, 1.0, 1.0, 1.0, 1.0],
        [0.1, 0.6, 0.2, 0.3, 1.0, 1.0],
        [0.2, 0.7, 0.3, 0.4, 0.1, 1.0],
        [1.0, 0.8, 0.4, 1.0, 1.0, 1.0],
        [1.0, 1.0, 0.2, 1.0, 1.0, 1.0]])
    mask = np.array([
        [0, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 1, 0],
        [0, 1, 1, 1, 1, 0],
        [0, 1, 1, 1, 1, 0],
        [0, 1, 1, 1, 1, 0],
        [0, 1, 1, 1, 1, 0]]).astype(np.bool)
    expected = np.array([
        [1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
        [1.0, 0.3, 1.0, 1.0, 1.0, 1.0],
        [0.1, 0.6, 0.3, 0.3, 1.0, 1.0],
        [0.2, 0.7, 0.3, 0.4, 0.1, 1.0],
        [1.0, 0.8, 0.4, 1.0, 1.0, 1.0],
        [1.0, 1.0, 0.4, 1.0, 1.0, 1.0]])
    outflow_pts = [[3, 4]]

    # Set inactive cells to nan before filling
    # Mask array must be a boolean type for this to work correctly
    data_mod = np.copy(data)
    data_mod[~mask] = np.nan
    output = fill.outflow_fill(data, outflow_pts, four_way=False)
    # Reset inactive cells to their original value after filling
    output[~mask] = data[~mask]
    print(output)
    print(expected)

    np.testing.assert_array_equal(output, expected)
