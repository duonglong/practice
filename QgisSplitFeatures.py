from osgeo import ogr

SHAPE_FILE = "/Users/longdt/Sabah Forestry Department/Training Data 2/strata8.shp"
shapefile = ogr.Open(SHAPE_FILE)
layer = shapefile.GetLayer(0)

for i in range(layer.GetFeatureCount()):
    feature = layer.GetFeature(i)
    name = feature.GetField("NAME")
    geometry = feature.GetGeometryRef()
    print i, name, geometry.GetGeometryName()
layer = iface.activeLayer()
QgsVectorFileWriter.writeAsVectorFormat( layer, 'H:/temp/' + layer.name() + ".shp", "utf-8", layer.crs(), "ESRI Shapefile", 1)
