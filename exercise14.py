#set working directory
import os
os.chdir('/home/user/data/Exercise14')
print os.getcwd()

#import ogr
from osgeo import ogr

## Create 1st point geometry
#beach = "POINT (-36543.08 1743528.24)"  
#ptbeach = ogr.CreateGeometryFromWkt(beach)
#print(ptbeach)
#
## Create 2nd point geometry
#home = "POINT ( -36540.56 174358.65)"  
#pthome = ogr.CreateGeometryFromWkt(home)
#print(pthome)

from osgeo import osr
##  spatial reference
spatialReference = osr.SpatialReference()
spatialReference.ImportFromEPSG(4326)  # from EPSG - Lat/long

## Loading osgeo
try:
  from osgeo import ogr, osr
  print 'Import of ogr and osr from osgeo worked.  Hurray!\n'
except:
  print 'Import of ogr and osr from osgeo failed\n\n'

## Is the ESRI Shapefile driver available?
driverName = "ESRI Shapefile"
drv = ogr.GetDriverByName( driverName )
if drv is None:
    print "%s driver not available.\n" % driverName
else:
    print  "%s driver IS available.\n" % driverName

## choose your own name
## make sure this layer does not exist in your 'data' folder
fn = "Exercise14.shp"
layername = "Mangawhai"

## Create shape file
ds = drv.CreateDataSource(fn)
print ds.GetRefCount()

## Create Layer
Mangawhai = ds.CreateLayer(layername, spatialReference, ogr.wkbPoint)
## Now check your data folder and you will see that the file has been created!
## From now on it is not possible anymore to CreateDataSource with the same name
## in your workdirectory untill your remove the name.shp name.shx and name.dbf file.
print(Mangawhai.GetExtent())

# Create a point
pthome = ogr.Geometry(ogr.wkbPoint)
ptbeach = ogr.Geometry(ogr.wkbPoint)
#
### SetPoint(self, int point, double x, double y, double z = 0)
pthome.SetPoint(0,-36.094600,174.585736)  
ptbeach.SetPoint(0,-36.095310,174.591133)

## Back to the pyramid, we still have no Feature
## Feature is defined from properties of the layer:e.g:

layerDefinition = Mangawhai.GetLayerDefn()
featureh = ogr.Feature(layerDefinition)
featureb = ogr.Feature(layerDefinition)

### Lets add the points to the feature
featureh.SetGeometry(pthome)
featureb.SetGeometry(ptbeach)

## Lets store the feature in a layer
Mangawhai.CreateFeature(featureh)
Mangawhai.CreateFeature(featureb)

qgis.utils.iface.addVectorLayer(fn, layername, "ogr") 

print 'shp file made'

print "create KML file"

driverName2 = "KML"
drv2 = ogr.GetDriverByName( driverName2 )
if drv2 is None:
    print "%s driver not available.\n" % driverName2
else:
    print  "%s driver IS available.\n" % driverName2

## choose your own name
## make sure this layer does not exist in your 'data' folder
fn1 = "Exercise14kml.kml"
layername1 = "Mangawhaikml"

## Create shape file
ds1 = drv2.CreateDataSource(fn1)
print ds1.GetRefCount()

Mangawhaikml = ds1.CreateLayer(layername1, spatialReference, ogr.wkbPoint)

layerDefinition = Mangawhaikml.GetLayerDefn()
featurekmlh = ogr.Feature(layerDefinition)
featurekmlb = ogr.Feature(layerDefinition)

### Lets add the points to the feature
featurekmlh.SetGeometry(pthome)
featurekmlb.SetGeometry(ptbeach)

## Lets store the feature in a layer
Mangawhaikml.CreateFeature(featurekmlh)
Mangawhaikml.CreateFeature(featurekmlb)

qgis.utils.iface.addVectorLayer(fn1, layername1, "ogr") 

print 'kml file made'



## Saving the file, but OGR doesn't have a Save() option
## The shapefile is updated with all object structure 
## when the script finished of when it is destroyed, 
# if necessay SyncToDisk() maybe used

ds.Destroy()
ds1.Destroy()
## below the output is shown of the above Python script that is run in the terminal



