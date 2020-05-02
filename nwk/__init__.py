import os
import xmltodict

__author__ = "Marcus T Taylor"
__email__ = "taylormjm3121@gmail.com"
__version__ = "0.15"


def _read(read_file):
    path = os.path.abspath(__file__)
    location = path.replace(os.path.basename(path), "assets/{}.xml".format(read_file))
    try:
        with open(location) as xml:
            xml = xmltodict.parse(xml.read(), dict_constructor=dict)
    except FileNotFoundError:
        exit("Cannot locate file: '{}'.".format(location))
    else:
        return xml
