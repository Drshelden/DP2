#! python 3
import Eto.Forms as ef
import Eto.Drawing as ed
import rhinoscriptsyntax as rs
 
form = ef.Form()
form.Width = 300
form.Height = 200



label = ef.Label()
label.Text = "My Label Text"


layout = ef.DynamicLayout()
layout.Spacing = ed.Size(5, 5)
layout.Padding = ed.Padding(8)
layout.AddRow(label)

form.Content = layout
form.Show()

print("Form launched")
