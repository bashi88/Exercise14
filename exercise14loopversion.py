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

####################################################################
## Create Geometry of interest point polygon etc

## Creating 2 points
pthome = ogr.Geometry(ogr.wkbPoint)
ptbeach = ogr.Geometry(ogr.wkbPoint)

## SetPoint(self, int point, double x, double y, double z = 0)
pthome.SetPoint(0, 174.585736, -36.094600)
ptbeach.SetPoint(0, 174.591133, -36.095310)


#########################################################################
## Create output types of interest - shp,kml

##set inputs and parameters
Drivers = ["ESRI Shapefile", "KML"]
Mangawhai = "Mangawhai"
outputtypes = [ "Exercise14.shp","Exercise14.kml"]
i = 0

##build filebuilder function with iterating loop
def geofilebuilder(Driverslist,layer, outputnamesandextentions):
    for i in len(range(Drivers)):
        ## Creating the file driver
        driverName = Driverslist[i]
        drv = ogr.GetDriverByName( driverName )
        if drv is None:
            print "%s driver not available.\n" % driverName
        else:
            print "%s driver IS available.\n" % driverName

        ## Creating the file
        fn = outputnamesandextentions[i]
        layername = layer
        ds = drv.CreateDataSource(fn)
        print ds.GetRefCount()

        ## Creating Layer
        layer = ds.CreateLayer(layername, spatialReference, ogr.wkbPoint)
        print(layer.GetExtent())

        ## Defining features
        layerDefinition = layer.GetLayerDefn()
        featurea = ogr.Feature(layerDefinition)
        featureb = ogr.Feature(layerDefinition)

        ## Adding points to the features
        featurea.SetGeometry(pthome)
        featureb.SetGeometry(ptbeach)

        ## Storing features in a layer
        layer.CreateFeature(featurea)
        layer.CreateFeature(featureb)

        print Driverslist[i] + "file made"
        ds.Destroy()

    print "all files made"

geofilebuilder(Drivers, Mangawhai, outputtypes)


add output to QGIS
fn = Filetypes[i]
layername = Mangawhai
qgis.utils.iface.addVectorLayer(fn, layername, "ogr")
                 


