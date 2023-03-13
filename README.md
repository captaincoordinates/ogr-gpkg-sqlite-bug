# OGR GeoPackage SQLite bug

This repo demonstrates a bug in OGR. The `ogr_layer_Extent` function is not available for a geopackage data source.

## To Test
- `docker build -t captaincoordinates/ogr_gpkg_sqlite_bug .`
- `docker run --rm captaincoordinates/ogr_gpkg_sqlite_bug python -m test /data/shp/poly_4326.shp` (succeeds)
- `docker run --rm captaincoordinates/ogr_gpkg_sqlite_bug python -m test /data/gpkg/poly_4326.gpkg` (fails)
