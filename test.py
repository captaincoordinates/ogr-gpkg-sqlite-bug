from osgeo.ogr import Open, UseExceptions
from re import sub as re_sub


UseExceptions()

def read_layer_extent(src_path: str) -> None:
    datasource = Open(src_path)
    layer = datasource.GetLayerByIndex(0)
    sql = "SELECT ogr_layer_Extent('{layer_name}')".format(layer_name=re_sub("'", "''", layer.GetName()))
    extents = datasource.ExecuteSQL(sql, dialect="SQLite")
    print(f"Extents: {extents.GetFeatureCount()}")


from argparse import ArgumentParser
parser = ArgumentParser()
parser.add_argument(
    "src_path",
    type=str,
)
args = parser.parse_args()

read_layer_extent(src_path=args.src_path)
