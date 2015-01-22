# Team: ZeaPol
# Team Members: Roeland de Koning / Barbara Sienkiewicz
# Date: 23/01/2015
# Exercise 14


## Setting working directory
import os
os.chdir('/home/user/data/Exercise14')
print os.getcwd()

## Importing ogr and osr
from osgeo import ogr
from osgeo import osr

## Spatial reference: http://spatialreference.org/ref/epsg/wgs-84/
spatialReference = osr.SpatialReference()
spatialReference.ImportFromEPSG(4326)

## Loading osgeo
try:
  from osgeo import ogr, osr
  print 'Import of ogr and osr from osgeo worked. Hurray!\n'
except:
  print 'Import of ogr and osr from osgeo failed\n\n'

#########################################################################
## Creating a driver for Shapefile
driverName = "ESRI Shapefile"
drv = ogr.GetDriverByName( driverName )
if drv is None:
    print "%s driver not available.\n" % driverName
else:
    print  "%s driver IS available.\n" % driverName

## Creating shape file
fn = "Exercise14.shp"
layername = "Mangawhai"
ds = drv.CreateDataSource(fn)
print ds.GetRefCount()

## Creating Layer
Mangawhai = ds.CreateLayer(layername, spatialReference, ogr.wkbPoint)
print(Mangawhai.GetExtent())

## Creating 2 points
pthome = ogr.Geometry(ogr.wkbPoint)
ptbeach = ogr.Geometry(ogr.wkbPoint)

## SetPoint(self, int point, double x, double y, double z = 0)
pthome.SetPoint(0, 174.585736, -36.094600)  
ptbeach.SetPoint(0, 174.591133, -36.095310)

## Defining features
layerDefinition = Mangawhai.GetLayerDefn()
featureh = ogr.Feature(layerDefinition)
featureb = ogr.Feature(layerDefinition)

## Adding points to the features
featureh.SetGeometry(pthome)
featureb.SetGeometry(ptbeach)

## Storing features in a layer
Mangawhai.CreateFeature(featureh)
Mangawhai.CreateFeature(featureb)
qgis.utils.iface.addVectorLayer(fn, layername, "ogr") 
print "shp file made"

########################################################################

## Creating a driver for kml
driverName2 = "KML"
drv2 = ogr.GetDriverByName( driverName2 )
if drv2 is None:
    print "%s driver not available.\n" % driverName2
else:
    print  "%s driver IS available.\n" % driverName2

## Creating kml file
fn1 = "Exercise14kml.kml"
layername1 = "Mangawhaikml"
ds1 = drv2.CreateDataSource(fn1)
print ds1.GetRefCount()

## Creating Layer
Mangawhaikml = ds1.CreateLayer(layername1, spatialReference, ogr.wkbPoint)

## Defining features
layerDefinition = Mangawhaikml.GetLayerDefn() 
featurekmlh = ogr.Feature(layerDefinition)
featurekmlb = ogr.Feature(layerDefinition)

### Adding points to the features
featurekmlh.SetGeometry(pthome)
featurekmlb.SetGeometry(ptbeach)

## Storing features in a layer
Mangawhaikml.CreateFeature(featurekmlh)
Mangawhaikml.CreateFeature(featurekmlb)
qgis.utils.iface.addVectorLayer(fn1, layername1, "ogr") 
print "kml file made"

ds.Destroy()
ds1.Destroy()
