# -*- encoding: utf-8 -*-
#
#  reader.py
#
#  Copyright 2017 Cody Schindler <cschindler@anasysinstruments.com>
#
#  This program is the property of Anasys Instruments, and may not be
#  redistributed or modified without explict permission of the author.

import anasysdoc

def main():
    # f = anasysdoc.read('./test/test data/Z Noise Cover Off.axz')
    f = anasysdoc.read('./test/test data/TappingModeimage.axz')

    hms = []
    for key, hm in f.HeightMaps.items():
        hm.show()
    # print(dir(f))
    # print(dir(f.HeightMaps['Height 1'].Tags))
    # print(f.HeightMaps['Height 1'].Tags.Tag)
    # print(f['HeightMaps'])
        # hm.savefig()
    # r = anasys_file.read('./test/test data/TappingModeimage3.axz')
    # r = anasys_file.read('./test/test data/TappingModeimage.axx')
    # r = anasys_file.read('./test/test data/TappingModeimage.axd')
    # print(r)

if __name__ == '__main__':
    # import argparse
    main()
