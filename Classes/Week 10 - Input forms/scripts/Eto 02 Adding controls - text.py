#! python 3
import Eto.Forms as ef
 
form = ef.Form()
form.Width = 300
form.Height = 200


label = ef.Label()
label.Text = "A Label"

form.Content = label

form.Show()

print("Form launched")
