#! python 3
import Rhino
import scriptcontext as sc
import Eto.Drawing as ed
import Eto.Forms as ef

def create_point_with_color(color):
    """Creates a point in the Rhino document with the specified color."""
    # Create a point at a default location (0, 0, 0)
    point = Rhino.Geometry.Point3d(0, 0, 0)
    
    # Add the point to the document
    point_id = sc.doc.Objects.AddPoint(point)
    
    # Set the object's color
    if point_id:
        obj = sc.doc.Objects.Find(point_id)
        if obj:
            obj.Attributes.ObjectColor = Rhino.Display.Color4f(color.R / 255.0, color.G / 255.0, color.B / 255.0).ToArgbColor()
            obj.Attributes.ColorSource = Rhino.DocObjects.ObjectColorSource.ColorFromObject
            obj.CommitChanges()
    
    # Redraw the Rhino viewport
    sc.doc.Views.Redraw()

class ColorPickerForm(ef.Dialog[bool]):
    def __init__(self):
        super().__init__()
        self.Title = "Color Picker Example"
        self.ClientSize = ed.Size(300, 100)
        self.Padding = ed.Padding(10)
        self.Resizable = False

        # Create a ColorPicker control
        self.color_picker = ef.ColorPicker()
        self.color_picker.ValueChanged += self.on_color_changed

        # Create a layout
        layout = ef.DynamicLayout()
        layout.Spacing = ed.Size(5, 5)
        layout.AddRow(self.color_picker)

        # Set the form content
        self.Content = layout

    def on_color_changed(self, sender, e):
        """Callback function when the color is changed."""
        selected_color = self.color_picker.Value
        create_point_with_color(selected_color)

# Show the form
form = ColorPickerForm()
form.ShowModal()
