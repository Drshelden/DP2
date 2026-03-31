#! python 3
import Eto.Forms as ef
import Eto.Drawing as ed

def buttonClick(sender, e):
    a = 5
    print(sender.Text)
    form.Close()

def sliderChanged(sender, e):
    print(sender.Value)
 
form = ef.Form()
form.Width = 100
form.Height = 200

stack_layout = ef.StackLayout()
stack_layout.Spacing = 8
stack_layout.Padding = ed.Padding(8)


label = ef.Label()
label.Text = "My Label Text"

slider = ef.Slider()
slider.MaxValue = 10
slider.MinValue = 0
slider.Value = 3
slider.ValueChanged += sliderChanged
slider.ValueChanged += buttonClick

button = ef.Button()
button.Text = "OK"
button.Click += buttonClick

stack_layout.Items.Add(ef.StackLayoutItem(label))
stack_layout.Items.Add(ef.StackLayoutItem(slider))
stack_layout.Items.Add(ef.StackLayoutItem(button))

form.Content = stack_layout
form.Show()

print("Form launched")
