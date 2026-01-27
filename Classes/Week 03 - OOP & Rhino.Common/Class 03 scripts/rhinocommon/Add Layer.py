#! python3

import rhinoscriptsyntax as rs
import scriptcontext as sc
import math

import System
import System.Collections.Generic
import Rhino

layer_name = "New Layer 02"


layer_index = sc.doc.Layers.Find(layer_name, True)
if layer_index>=0:
    print("A layer with the name", layer_name, "already exists.")
    #return Rhino.Commands.Result.Cancel

# Add a new layer to the document
layer_index = sc.doc.Layers.Add(layer_name, System.Drawing.Color.Black)
if layer_index<0:
    print( "Unable to add", layer_name, "layer.")
   #return Rhino.Commands.Result.Failure
else: print("Layer: ", layer_name, "added!")

#return Rhino.Commands.Result.Success