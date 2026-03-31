#! python 3
import Eto.Forms as ef
import Eto.Drawing as ed
import rhinoscriptsyntax as rs



def onClick(sender, e):
    print("Color changed!")
    myEtoColor = myColor.Value
    form.Close()
    mySphere = rs.AddSphere((0,0,0), 5)
    rs.ObjectColor(mySphere, [myEtoColor.Rb, myEtoColor.Gb, myEtoColor.Bb])

 
form = ef.Dialog()
form.Width = 300
form.Height = 200



# label = ef.Label()
# label.Text = "My Label Text"

myColor = ef.ColorPicker()
myColor.Value = ed.Color.FromArgb(255, 0,0)


myButton = ef.Button()
myButton.Text = "OK"
myButton.Click += onClick


layout = ef.DynamicLayout()
layout.Spacing = ed.Size(5, 5)
layout.Padding = ed.Padding(8)
layout.AddRow(myColor)
layout.AddRow(myButton)

# form.Content = layout
form.Content = layout
form.ShowModal()

print("Form launched")
