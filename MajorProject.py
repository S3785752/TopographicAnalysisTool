# --------- #
# SECTION 1 #
# --------- #

# ---------------------- #
# for the user to define #
# ---------------------- #

contFilePath = 'C:/Users/1143c/Downloads/FloodAnalysis/Contours/EL_CONTOUR.shp' # file location of your contour shape file

rasterOutputPath = 'C:/Users/1143c/Downloads/FloodAnalysis/Raster/ElevRaster.tif' # output file location of the raster elevation file 

ElevRastStats = 'C:/Users/1143c/Downloads/FloodAnalysis/Raster/ElevRasterStats.html' # output file location of elevation raster statistics
ElevRasterClassified = 'C:/Users/1143c/Downloads/FloodAnalysis/Raster/ElevRasterClassified.tif' # output file location of reclassified raster

classificationRulesElev = 'C:/Users/1143c/Downloads/FloodAnalysis/Rules/rulesElev.txt' # file location of your rules txt file for the elevation raster
classificationRulesAsp = 'C:/Users/1143c/Downloads/FloodAnalysis/Rules/rulesAsp.txt' # file location of your rules txt file for the aspect raster

aspectOutputPath = 'C:/Users/1143c/Downloads/FloodAnalysis/Aspect/AspectRaster.tif' # output file location for aspect raster
aspectClassified = 'C:/Users/1143c/Downloads/FloodAnalysis/Aspect/AspectRasterClassified.tif' # output file location for classified aspect raster

ElevationRasterStyle = 'C:/Users/1143c/Downloads/FloodAnalysis/Styles/ElevationColourRamp.qml' # file location for the supplied elevation raster colour ramp 
AspectRasterStyle = 'C:/Users/1143c/Downloads/FloodAnalysis/Styles/AspectColourRamp.qml' # file location for the supplied aspect raster colour ramp 

ShadedRelief = 'C:/Users/1143c/Downloads/FloodAnalysis/Raster/ShadedRelief.tif'

rasterPixelSize = 0.0001 # choose required raster resolution

createReclassedRaster = False # choose if you want elevation raster to be reclasses
createAspect = True # choose if you want an aspect raster
createReclassedAspect = True # choose if you want aspect raster to be reclassed
createShadedRelief = True # choose if you want shaded relief raster

# import statements   

import processing
import qgis.core
import qgis.analysis

# insert contour into interface

contLayer = iface.addVectorLayer(contFilePath, '' , "ogr")

# define the required values for interpolation tool

layer = iface.activeLayer() # select EL_CONTOUR layer
LayerExtent = layer.extent() # extract extent of EL_CONTOUR
print(LayerExtent) # check if correctly retrieved

contFilePathInter = contFilePath + '::~::0::~::3::~::0' # modified filepath to integrate with interpolation tool 

# perform vector to raster conversion
    
Raster = processing.run("qgis:tininterpolation", { 'EXTENT' : LayerExtent,
                                          'INTERPOLATION_DATA' : contFilePathInter, 
                                          'METHOD' : 0,
                                          'OUTPUT' : rasterOutputPath, 
                                          'PIXEL_SIZE' : rasterPixelSize })

# insert ElevRaster into interface

RasterLayer = iface.addRasterLayer(rasterOutputPath, "ElevRaster", "gdal")

# retrieve ElevRaster cell statistics 

output = processing.run("qgis:rasterlayerstatistics", { 'INPUT' : rasterOutputPath,
                                                        'BAND' : 1,
                                                        'OUTPUT_HTML_FILE' : ElevRastStats }) # output now records the statistics generated

print(output) # display stats

maximum = output.get('MAX')
minimum = output.get('MIN')

print('the following are the min and max values')
print(maximum)
print(minimum)

# -------------------------------------------------------------------------- #
# before entering section 2 of the code, please record the max and min       #
# values and use these values in the classification tool to define the       #
# classes copy and paste the classes in the classificationRulesElev txt file #
# -------------------------------------------------------------------------- #

# --------- #
# SECTION 2 #
# --------- #

# reclassify elevation by desired height

if createReclassedRaster is True:
    processing.run("grass7:r.reclass", { 'GRASS_RASTER_FORMAT_META' : '',
                                        'GRASS_RASTER_FORMAT_OPT' : '',
                                        'GRASS_REGION_CELLSIZE_PARAMETER' : 0,
                                        'GRASS_REGION_PARAMETER' : None,
                                        'input' : rasterOutputPath,
                                        'output' : ElevRasterClassified,
                                        'rules' : classificationRulesElev,
                                        'txtrules' : '' })

if createReclassedRaster is True:
    RasterLayerReclassed = iface.addRasterLayer(ElevRasterClassified, "ElevRasterClassified", "gdal") 
    
# set elevation raster style (colour ramp)

if createReclassedRaster is True:
    processing.run("native:setlayerstyle", { 'INPUT' : ElevRasterClassified,
                                            'STYLE' : ElevationRasterStyle })

# calculate the aspect

if createAspect is True:
    processing.run("gdal:aspect", { 'BAND' : 1, 
                                   'COMPUTE_EDGES' : False, 
                                   'EXTRA' : '', 
                                   'INPUT' : rasterOutputPath, 
                                   'OPTIONS' : '', 
                                   'OUTPUT' : aspectOutputPath, 
                                   'TRIG_ANGLE' : True, 
                                   'ZERO_FLAT' : True, 
                                   'ZEVENBERGEN' : False})

if createAspect is True:
    AspectRasterLayer = iface.addRasterLayer(aspectOutputPath, "AspectRaster", "gdal") 

# reclassify aspect

if createReclassedAspect is True:
    processing.run("grass7:r.reclass", { 'GRASS_RASTER_FORMAT_META' : '',
                                        'GRASS_RASTER_FORMAT_OPT' : '',
                                        'GRASS_REGION_CELLSIZE_PARAMETER' : 0,
                                        'GRASS_REGION_PARAMETER' : None,
                                        'input' : aspectOutputPath,
                                        'output' : aspectClassified,
                                        'rules' : classificationRulesAsp,
                                        'txtrules' : '' })

if createReclassedAspect is True:
    AspectRasterLayerReclassed = iface.addRasterLayer(aspectClassified, "AspectRasterReclassed", "gdal") 

# set aspect raster style (colour ramp)

if createReclassedAspect is True:
    processing.run("native:setlayerstyle", { 'INPUT' : aspectClassified,
                                            'STYLE' : AspectRasterStyle })
# shaded relief calculation

if createShadedRelief is True:
    processing.run("grass7:r.relief", { 'GRASS_RASTER_FORMAT_META' : '', 
                                       'GRASS_RASTER_FORMAT_OPT' : '', 
                                       'GRASS_REGION_CELLSIZE_PARAMETER' : 0, 
                                       'GRASS_REGION_PARAMETER' : None, 
                                       'altitude' : 30, 
                                       'azimuth' : 270, 
                                       'input' : rasterOutputPath, 
                                       'output' : ShadedRelief, 
                                       'scale' : 1, 
                                       'units' : 0, 
                                       'zscale' : 1 })

if createShadedRelief is True:
    ShadedReliefLayer = iface.addRasterLayer(ShadedRelief, "shadedReliefLayer", "gdal") 



























































