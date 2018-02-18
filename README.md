# Flood Fill

Python floating point flood fill tool.

There are currently two flood fill algorithms implemented:  
* from_edges() - Loads all edge cells into a priority queue (returns lowest values first), starts at the minimum (edge) value, and iteratively searches all connected neighbors and adds equal or "higher" neighbors to the queue and fills "lower" sink neighbors.
* from_points() - Loads all cell values at the user specified outflow points into a priority queue (returns lowest values first), starts at the minimum outflow point, and iteratively searchs all connected neighbors and adds equal or "higher" neighbors to the queue and fills "lower" sink neighbors.

Both functions take a NumPy array as an input and return a filled NumPy array as output.  
The from_points() function has an additional parameter for defining the outflow cell locations.

## 4-way vs 8-way
Both functions have a "four_way" boolean argument that controls whether the algorithm searches the 4 (cross structuring element) or 8 (square structuring element) nearest cells.  The default value is False which will result in 8-way filling.

## Dependencies
* [NumPy](http://www.numpy.org/)  
* [pytest](http://doc.pytest.org/en/latest/) - Only needed to run the test suite

## Tests

The full test suite can be run using Pytest:

```
> python -m pytest
```

To get additional logging info, use the "-v" or "-s" tags:
```
python -m pytest -v -s
```
