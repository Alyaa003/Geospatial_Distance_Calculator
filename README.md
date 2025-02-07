
# Geospatial Distance Calculator

A Python-based project to calculate the great-circle distance between two geographical locations using the Haversine formula.

## Overview

This project provides a simple way to calculate the distance between two geographical coordinates (latitude and longitude) on the Earth's surface. The Haversine formula is used to calculate the distance, taking into account the spherical shape of the Earth.

## Features

- Calculate the distance between two locations (Riyadh and Mecca, for example).
- Uses the Haversine formula for accurate distance measurement.
- Returns the distance in kilometers (or can be modified to other units).

## Requirements

- Python 3.x
- NumPy library

To install the required libraries, use the following:

```bash
pip install numpy
```

## How to Use

1. Clone or download this repository.
2. Run the Python script, which calculates the distance between two sets of coordinates.

```bash
python haversine_distance_calculator.py
```

You can modify the coordinates for different locations as needed.

## Code Explanation

1. **Coordinates**: The geographical coordinates of two locations (in this case, Riyadh and Mecca) are provided in arrays.
2. **Conversion**: The coordinates are converted from degrees to radians.
3. **Haversine Formula**: The formula is applied to calculate the great-circle distance based on the latitude and longitude differences.
4. **Output**: The distance is printed in kilometers.

## Example Output

```
The distance between Riyadh and Mecca is: 790.31 km
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
