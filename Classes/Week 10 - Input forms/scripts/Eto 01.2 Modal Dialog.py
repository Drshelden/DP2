#! python 3
import Eto.Forms as ef

dialog = ef.Dialog()
dialog.Width = 100
dialog.Height = 100
dialog.ShowModal() # <-- Code execution stops here

print("Code returned")
