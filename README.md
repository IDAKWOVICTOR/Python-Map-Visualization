# Python-Map-Visualization

This Python script uses the `geopandas` library to create a visual representation of Nigeria's states based on a provided shapefile. The script includes the following features:

- **Import Libraries:**
  - `geopandas` for working with geospatial data.
  - `pandas` for data manipulation.
  - `matplotlib.pyplot` for plotting.

- **Read Shapefile:**
  - Reads a shapefile containing Nigeria's state boundaries and creates a GeoDataFrame (`shape`) to store the spatial data.

- **Plotting the Map:**
  - Sets up a plot (`ax`) using the state boundaries and visualizes the spatial data.
  - Colors each state based on its size (`Shape_Area`) using the 'RdBu' color map.
  - Displays a legend indicating the range of state sizes.

- **Styling the Plot:**
  - Removes axis labels and spines to create a cleaner map.

- **Labeling States:**
  - Labels each state with its name (`ADM1_EN`) at the centroid using the GeoDataFrame's geometry.

- **Title and Display:**
  - Adds a title to the map.
  - Displays the map using `plt.show()`.

## How to Use

1. Install the required libraries using:
   ```bash
   pip install geopandas pandas matplotlib
