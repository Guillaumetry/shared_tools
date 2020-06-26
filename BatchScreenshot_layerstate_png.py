#wrote by guev

import rhinoscriptsyntax as rs
import Rhino
import scriptcontext as sc
import System.Drawing
import os

def Capture (filePath,width,height):
    RhinoDocument = Rhino.RhinoDoc.ActiveDoc
    view = Rhino.RhinoDoc.ActiveDoc.Views.ActiveView
    viewcapture = Rhino.Display.ViewCapture()
    viewcapture.TransparentBackground = True
    viewcapture.Width = width
    viewcapture.Height = height
    #size = System.Drawing.Size(width,height)
    capture = viewcapture.CaptureToBitmap(view)
    capture.Save(filePath)

def main ():
    
    #snapshots = sc.doc.Snapshots.Names
    layerstates = sc.doc.NamedLayerStates.Names
    namedviews = sc.doc.NamedViews
    
    view_count = 0

    PIXwidth = rs.GetInteger("Width [px] = ",1600)
    PIXheight = rs.GetInteger("Height [px] = ",900)
    
    folder = rs.BrowseForFolder(message="Select destination folder") 

    for view in namedviews:
    
        namedviews.Restore(view_count,sc.doc.Views.ActiveView.ActiveViewport)
        view_count += 1
        for state in layerstates:
            imagename = (str(state) + "_" + view.Name + ".png")
            imagepath = folder + "\\" + imagename
            Rhino.RhinoApp.RunScript("-_Layerstatemanager _Restore \"" + state + "\" _Enter _Enter", False)
            Capture (imagepath,PIXwidth,PIXheight)
            
    rs.MessageBox("All images were added to " + folder,0,"Congrats")

if( __name__ == "__main__" ):
    main()
