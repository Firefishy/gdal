import sys
# import osgeo.utils.esri2wkt as a convenience to use as a script
from osgeo.utils.esri2wkt import *  # noqa
from osgeo.utils.esri2wkt import main
from osgeo.gdal import deprecation_warn


deprecation_warn('esri2wkt', 'utils')
sys.exit(main(sys.argv))
