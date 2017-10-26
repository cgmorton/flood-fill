# Flood Fill

Pure Python floating point flood fill algorithm.  

There are currently two flood fill algorithms implemented:  
* flood_fill() - Loads all edge cells into a priority queue (returns lowest values first), starts at the minimum (edge) value, and iteratively searchs all connected neighbors and adds equal or "higher" neighbors to the queue and fills "lower" sink neighbors.
* outflow_fill() - Loads all cell values at the user specified outflow points into a priority queue (returns lowest values first), starts at the minimum outflow point, and iteratively searchs all connected neighbors and adds equal or "higher" neighbors to the queue and fills "lower" sink neighbors.

Both functions take a NumPy array as an input and return a filled NumPy array as output.  
The outflow_fill() function has an additional parameter for defining the outflow cell locations.
Both functions have a "four_way" boolean argument that controls whether the algorithm searches the 4 (cross structuring element) or 8 (square structuring element) nearest cells.  The default value is False which will result in 8-way filling.

This code was modified from this post/example:  
    http://arcgisandpython.blogspot.com/2012/01/python-flood-fill-algorithm.html

## Dependencies
* [NumPy](http://www.numpy.org/)  
* [pytest](http://doc.pytest.org/en/latest/) - Only needed to run the test suite

## Python 2
The code is currently setup for Python 2.7, but it would be very easy to modify for Python 3X.  The only change that needs to be made is to convert the "xrange" calls to "range".  Python 3 could also be supported using the [future](http://python-future.org/) or [six](https://pythonhosted.org/six/) modules.

## Tests

The full test suite can be run using Pytest:

```
> python -m pytest
```

To get additional logging info, use the "-v" or "-s" tags:
```
python -m pytest -v -s
```
