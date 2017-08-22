# Flood Fill

Pure Python float point flood fill algorithm.  

There are currently two flood fill algorithms implemented:  
* fast_fill() - Loads all edge cells into a priority queue (returns lowest values first), starts at the minimum (edge) value, and iteratively searchs all connected neighbors and adds equal or "higher" neighbors to the queue and fills "lower" sink neighbors.
* slow_fill() - Initially sets all values to the maximum value of the image and then uses the SciPy ndimage.grey_erosion() function to morphologically erode the image down to the input image.  Sink values will be filled since they cannot be eroded down to an edge cell.

Both functions take a NumPy array as an input and return a filled NumPy array as output.  
Both functions have a "four_way" boolean argument that controls whether the algorithm searches the 4 (cross structuring element) or 8 (square structuring element) nearest cells.  The default value is False which will result in 8-way filling.

This code was modified from this post/example:  
    http://arcgisandpython.blogspot.com/2012/01/python-flood-fill-algorithm.html

## Dependencies
NumPy  
SciPy ndimage (optional)

## Tests

The full test suite can be run using Pytest:

```
> python -m pytest
```

To get additional logging info, use the "-v" or "-s" tags:
```
python -m pytest -v -s
```
