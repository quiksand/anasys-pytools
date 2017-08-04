# -*- encoding: utf-8 -*-
#
#  reader.py
#
#  Copyright 2017 Cody Schindler <cschindler@anasysinstruments.com>
#
#  This program is the property of Anasys Instruments, and may not be
#  redistributed or modified without explict permission of the author.

debug = True                         #debug flag
pr = False                           #flag for printing todo()s to console
import xml.etree.ElementTree as ET   #for parsing XML
import gzip                          #for unzipping .axz files
if debug:
    import inspect                   #debugging module
import os

class AnasysFile():
    """Object for holding all data in a file generated by Analysis Studio"""
    def __init__(self, f_name):
        #set tag attributes as named python attributes
        # for key, val in src_root.items():
        #     setattr(self, key, val)
        # for neighbor in src_root.iter():
        #     if neighbor.attrib:
        #         print(neighbor.attrib)
        doc_root = self.read(f_name)
        self.data = self.convert_tags(doc_root)
        print(self.data)
    #     print(dir(self))
    # def __repr__(self):
    #     for d in dir(self):
    #         print(d)

    def convert_tags(self, element):
        """Iterates through element tree object and converts to python dicts"""
        todo("verify dict is really the best data structure for this")
        todo("add code to move attributes into children")
        todo("make it so tags aren't overwritten")
        new_obj = {}
        if list(element) == []:
            #element has no children - return either text or {}
            if element.text:
                return element.text
            else:
                return {}
        else:
            #element has children - loop through and recurse on each
            for child in element:
                new_obj[child.tag] = self.convert_tags(child)
            return new_obj

        #ALTERNATE METHOD OF OBJECTIFYING XML
        # def etree_to_dict(self, t):
        #     d = {t.tag : map(etree_to_dict, list(t))}
        #     d.update(('@' + k, v) for k, v in t.attrib.iteritems())
        #     d['text'] = t.text
        #     return d
        #
        # tree = etree.parse("some_file.xml")
        # etree_to_dict(tree.getroot())

    def get_extension(self, f_path):
        """Returns the extension of a file, given the file path"""
        ext = os.path.splitext(f_path)[1][1:].lower()
        return ext

    def check_path(self, f_path):
        """Checks for errors with file existance and type"""
        todo("Throw an error and exit for two edge cases")
        if not os.path.isfile(f_path):
            print("Error: File path does not exist")
            todo("Throw an error and exit")
        if not (f_path.lower().endswith(".axz") or f_path.lower().endswith(".axd")):
            print("Error: File type must be .axz or .axd")
            todo("Throw an error and exit")

    def read(self, f_name):
        """Main function for reading in data from axz or axd files and returns a python object"""
        todo("make this a wrapper func for AnasysFile class creation and move relevant funcs inside class def")
        #get complete file path
        f_path = os.path.abspath(f_name)
        #check that file is kosher
        self.check_path(f_path)
        #get the file extension
        ext = self.get_extension(f_path)
        #get the xml data from axz or axd
        if ext == 'axz':
            f_xml = self.open_axz(f_path)
        else:
            f_xml = self.open_axd(f_path)
        root = f_xml.root
        return root

    def strip_namespace(self, f_data):
        """strips annoying xmlns data that elementTree auto-prepends to all element tags"""
        for _, el in f_data:
            el.tag = el.tag.split('}', 1)[1] #strip namespaces from tags
        return f_data

    def open_axd(self, f_path):
        """Opens an axd file and returns its content as an ElementTree object"""
        f_data = ET.iterparse(f_path)
        f_data = self.strip_namespace(f_data)
        return f_data #returns an ET.iterparse object

    def open_axz(self, f_path):
        """Opens an axz file and returns its content as an ElementTree object"""
        with gzip.open(f_path) as f:
            f_data = ET.iterparse(f)
            f_data = self.strip_namespace(f_data)
        return f_data #returns an ET.iterparse object

def read(f):
    clear_msgs()
    AnasysFile(f)
def clear_msgs():
    with open('messages.txt', "w") as f:
        f.write("")

def todo(message="Do something!"):
    """For debug only- creates console notes with line numbers"""
    def get_line_number():
        return inspect.currentframe().f_back.f_back.f_lineno
    def get_calling_function_name():
        return inspect.getframeinfo(inspect.currentframe().f_back.f_back).function
    if debug:
        complete_message = "TODO ({:4d}): {:.15}() - {}".format(get_line_number(), get_calling_function_name(), message)
        if pr:
            print(complete_message)
        with open("messages.txt", "a") as f1:
            f1.write(complete_message)
    else:
        pass
