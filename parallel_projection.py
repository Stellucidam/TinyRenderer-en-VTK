
import vtk

treader = vtk.vtkJPEGReader()
treader.SetFileName('obj/african_head_diffuse.jpg')

texture = vtk.vtkTexture()
texture.SetInputConnection(treader.GetOutputPort())

reader = vtk.vtkOBJReader()
reader.SetFileName('obj/african_head.obj')

mapper = vtk.vtkPolyDataMapper()
mapper.SetInputConnection(reader.GetOutputPort())

actor = vtk.vtkActor()
actor.SetMapper(mapper)
actor.SetTexture(texture)
actor.GetProperty().SetInterpolationToGouraud()

cam = vtk.vtkCamera()
cam.SetFocalPoint(0,0,0)
cam.SetPosition(0,0,1)
cam.SetViewUp(0,1,0)
cam.ParallelProjectionOn()
cam.SetParallelScale(1.2)

ren = vtk.vtkRenderer()
ren.AddActor(actor)
ren.SetBackground(0.1, 0.1, 0.1)
ren.SetActiveCamera(cam)

renWin = vtk.vtkRenderWindow()
renWin.AddRenderer(ren)
renWin.SetSize(800,800)

iren = vtk.vtkRenderWindowInteractor()
iren.SetRenderWindow(renWin)

style = vtk.vtkInteractorStyleTrackballCamera()
iren.SetInteractorStyle(style)

iren.Start()
