#! python 3
import Eto.Forms as ef
 
form = ef.Form()
form.Width = 100
form.Height = 100

label = ef.Label()
label.Text = "My Label Text"

form.Content = label
form.Show()

print("Form launched")
