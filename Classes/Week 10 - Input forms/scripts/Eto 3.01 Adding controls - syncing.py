#! python3
 
# Imports
import Rhino
import scriptcontext
import System
import Rhino.UI
import Eto.Drawing as drawing
import Eto.Forms as forms

minVal = 0
maxVal = 500

# SampleEtoRoomNumber dialog class
class SampleEtoDialog(forms.Dialog[bool]):
 
    # Dialog box Class initializer
    def __init__(self):
        super().__init__()
        # Initialize dialog box
        self.Title = 'Something else'
        self.Padding = drawing.Padding(5)
        self.Resizable = False

        self.Label_01 = forms.Label()
        self.Label_01.Text = "Enter text"

        self.Label_02 = forms.Label()
        self.Label_02.Text = str(minVal)

        self.Label_03 = forms.Label()
        self.Label_03.Text = str(maxVal)
      
        #---------------- Text Box ------------------
        self.TextBox_01 = forms.TextBox()
        self.TextBox_01.Text = "" 
        self.TextBox_01.TextChanged += self.OnTextChanged
    
        #---------------- SLIDER ------------------
        self.Slider_01 = forms.Slider()
        self.Slider_01.MinValue = minVal
        self.Slider_01.MaxValue = maxVal
        self.Slider_01.ValueChanged += self.OnSliderChanged


        # Create the default button
        self.OKButton = forms.Button()
        self.OKButton.Text ='OK'
        self.OKButton.Click += self.OnOKButtonClick

        # Create the default button
        self.CancelButton = forms.Button()
        self.CancelButton.Text ='Cancel'
        self.CancelButton.Click += self.OnCancelButtonClick
 
        # Create a table layout and add all the controls
        layout = forms.DynamicLayout()
        layout.Spacing = drawing.Size(5, 5)
        layout.AddRow(self.Label_01, self.TextBox_01, self.Label_02, self.Slider_01, self.Label_03)
        layout.AddRow(self.OKButton, self.CancelButton)
 
        # Set the dialog content
        self.Content = layout
 
    # Start of the class functions
 
    # Close button click handler
    def OnOKButtonClick(self, sender, e):
        if self.TextBox_01.Text == "":
            self.Close(False)
        else:
            self.Close(True)
    
    def OnTextChanged(self, sender, e):
        if (self.TextBox_01.Text !=""):
            self.Textself.Slider_01.Value = int(self.TextBox_01.Text)
        else: 
            self.Textself.Slider_01.Value = 0

    def OnSliderChanged(self, sender, e):
        self.TextBox_01.Text = str(self.Slider_01.Value)

  # Cancel button click handler
    def OnCancelButtonClick(self, sender, e):
        self.Close(False)

    def GetText(self):
        return self.TextBox_01.Text

    ## End of Dialog Class ##
 

dialog = SampleEtoDialog();
rc = dialog.ShowModal(Rhino.UI.RhinoEtoApp.MainWindow)
if (rc):
    print("The user entered: " ,  dialog.GetText()) #Print the Room Number from the dialog control
else:
    print("Nothing entered")