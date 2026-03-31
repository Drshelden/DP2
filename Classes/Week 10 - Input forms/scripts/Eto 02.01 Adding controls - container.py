#! python 3
import scriptcontext as sc
 
import Rhino
from Rhino.UI import RhinoEtoApp, EtoExtensions
import Eto.Forms as ef
import Eto.Drawing as ed
 
form = ef.Form()
form.Width = 300
form.Height = 200

stack_layout = ef.StackLayout()
stack_layout.Spacing = 8
stack_layout.Padding = ed.Padding(8)
 
button_one = ef.Button()
button_one.Text = "One"
button_two = ef.Button()
button_two.Text = "Two"
button_three = ef.Button()
button_three.Text = "Three"
 
stack_layout.Items.Add(ef.StackLayoutItem(button_one))
stack_layout.Items.Add(ef.StackLayoutItem(button_two))
stack_layout.Items.Add(ef.StackLayoutItem(button_three))


form.Content = stack_layout

form.Show()

print("Form launched")
