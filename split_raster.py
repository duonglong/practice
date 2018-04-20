#!/usr/bin/python
# __author__ = 'trananhdung'

import fiona
import subprocess
import os
import sys
from scipy.misc import imsave
from skimage import io
import json

help_string = """
Tool for split raster (geotiff) by shape
Usage:
    $ ./split_raster.py [path_to_tiff] [path_to_shape] [output_directory]
"""


def run(tif_file, shp_file, output):
    """

    :param tif_file: string - path to tiff file
    :param shp_file: string - path to shape file
    :param output: string - path to out-directory
    :return: True
    """
    assert tif_file and shp_file and output, "You need to fully pass all arguments."
    tiff_coordinates = {}
    with fiona.open(shp_file) as source:
        meta = source.meta

        for f in source:
            out_name = (f['properties']['strata2014'] + '.' + str(f['properties']['id'])).replace(' ', '_')
            outfile = os.path.join(output, "%s.shp" % out_name)

            with fiona.open(outfile, 'w', **meta) as sink:
                sink.write(f)
            sub_tif = os.path.join(output, out_name + '.tif')

            subprocess.call(['gdalwarp', '-dstalpha', '-cutline', outfile, '-crop_to_cutline',
                             tif_file, sub_tif])

            # Generate png
            # generate_png_mask(sub_tif)
            tiff_coordinates[f['properties']['id']] = {
                "latitude": None,
                "longitude": None,
                "coordinates": f['geometry']['coordinates']
            }
    if tiff_coordinates:
        save_to_json(output + "/" + tif_file.split("/")[-1].replace(".tif", ".json"), tiff_coordinates)
    return True


def save_to_json(output, data):
    """

    :param data: dict - json data
    :return:
    """
    with open(output, 'w') as outfile:
        json.dump(data, outfile)


def generate_png_mask(tiff_path):
    """
    Create png file which has the same shape as tiff file's shape with transparent color
    :param tiff_path: string - path to tiff file
    :return:
    """
    color = (255, 255, 0)

    def convert_to_color(data):
        print("converting...")
        for i in range(0, len(data)):
            for j in range(0, len(data[i])):
                if data[i][j][3] != 0:
                    data[i][j][0], data[i][j][1], data[i][j][2] = color
                    data[i][j][3] = 100  # Leave Alpha band
        print("done.")
        return data

    tiff = io.imread(tiff_path)
    png = convert_to_color(tiff)
    # Save to file
    png_out_path = "/".join(tiff_path.split("/")[:-1]) + "/png/"
    # if not os.path.exists(png_out_path):
    #     os.makedirs(png_out_path)
    imsave(png_out_path, png, format='png')
    return png_out_path


def main(*args):
    print(args)
    try:
        _, tiff, shape, dest = args
        run(tif_file=tiff, shp_file=shape, output=dest)
        exit(0)
    except:
        print(help_string)
        exit(0)


if __name__ == '__main__':
    main(*sys.argv)
