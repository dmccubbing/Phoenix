#---------------------------------------------------------------------------
# Name:        etg/htmlcell.py
# Author:      Robin Dunn
#
# Created:     27-Oct-2012
# Copyright:   (c) 2012 by Total Control Software
# License:     wxWindows License
#---------------------------------------------------------------------------

import etgtools
import etgtools.tweaker_tools as tools

PACKAGE   = "wx"   
MODULE    = "_html"
NAME      = "htmlcell"   # Base name of the file to generate to for this script
DOCSTRING = ""

# The classes and/or the basename of the Doxygen XML files to be processed by
# this script. 
ITEMS  = [ "wxHtmlSelection",
           "wxHtmlRenderingState",
           "wxHtmlRenderingStyle",
           "wxHtmlRenderingInfo",
           "wxHtmlCell",
           "wxHtmlContainerCell",
           "wxHtmlLinkInfo",
           "wxHtmlColourCell",
           "wxHtmlWidgetCell",
           ]    
    
#---------------------------------------------------------------------------

def run():
    # Parse the XML file(s) building a collection of Extractor objects
    module = etgtools.ModuleDef(PACKAGE, MODULE, NAME, DOCSTRING)
    etgtools.parseDoxyXML(module, ITEMS)
    
    #-----------------------------------------------------------------
    # Tweak the parsed meta objects in the module object as needed for
    # customizing the generated code and docstrings.
    
    
    
    c = module.find('wxHtmlCell')
    assert isinstance(c, etgtools.ClassDef)
    c.addPrivateCopyCtor()
    
    c.find('SetNext.cell').transfer = True
    c.find('AdjustPagebreak.pagebreak').inOut = True
    
    
    #-----------------------------------------------------------------
    tools.doCommonTweaks(module)
    tools.runGenerators(module)
    
    
#---------------------------------------------------------------------------
if __name__ == '__main__':
    run()
