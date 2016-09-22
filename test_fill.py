import numpy as np
import pytest

import fill

def test_fast_fill01():
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

def test_fast_fill02():
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

def test_slow_fill01():
    print('Testing slow_fill() 8-way')
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
        fill.slow_fill(data, four_way=False), expected)

def test_slow_fill02():
    print('Testing slow_fill() 4-way')
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
        fill.slow_fill(data, four_way=True), expected)