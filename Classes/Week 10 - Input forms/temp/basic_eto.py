import scriptcontext as sc
import json
import os

from Rhino.UI import RhinoEtoApp

import Eto.Forms as ef
import Eto.Drawing as ed


class SumSlidersDialog(ef.Dialog):
	def __init__(self):
		super(SumSlidersDialog, self).__init__()
		self.Title = "Two Sliders Sum"
		self.Padding = ed.Padding(12)
		self.Resizable = False
		self._is_updating = False

		self.slider_1 = ef.Slider()
		self.slider_1.MinValue = 1
		self.slider_1.MaxValue = 10
		self.slider_1.Value = 1
		self.slider_1.ValueChanged += self.on_slider_changed

		self.value_1_text = ef.TextBox()
		self.value_1_text.Width = 40
		self.value_1_text.Text = str(self.slider_1.Value)
		self.value_1_text.TextChanged += self.on_value_1_text_changed

		self.slider_2 = ef.Slider()
		self.slider_2.MinValue = 1
		self.slider_2.MaxValue = 10
		self.slider_2.Value = 1
		self.slider_2.ValueChanged += self.on_slider_changed

		self.value_2_text = ef.TextBox()
		self.value_2_text.Width = 40
		self.value_2_text.Text = str(self.slider_2.Value)
		self.value_2_text.TextChanged += self.on_value_2_text_changed

		self.sum_text = ef.TextBox()
		self.sum_text.ReadOnly = True

		self.file_path_text = ef.TextBox()
		self.file_path_text.ReadOnly = True
		self.file_path_text.Width = 260

		self.browse_button = ef.Button(Text="Select File")
		self.browse_button.Click += self.on_select_file_click

		self.save_button = ef.Button(Text="Save Slider Values")
		self.save_button.Click += self.on_save_file_click

		layout = ef.DynamicLayout()
		layout.Spacing = ed.Size(8, 8)
		layout.AddRow(ef.Label(Text="Slider 1 (1-10):"))
		layout.AddRow(self.slider_1, self.value_1_text)
		layout.AddRow(ef.Label(Text="Slider 2 (1-10):"))
		layout.AddRow(self.slider_2, self.value_2_text)
		layout.AddRow(ef.Label(Text="Sum:"), self.sum_text)
		layout.AddRow(ef.Label(Text="JSON File:"), self.file_path_text, self.browse_button)
		layout.AddRow(None, self.save_button)

		self.Content = layout
		self.update_sum()

	def on_slider_changed(self, sender, e):
		if self._is_updating:
			return

		self._is_updating = True
		self.value_1_text.Text = str(self.slider_1.Value)
		self.value_2_text.Text = str(self.slider_2.Value)
		self._is_updating = False
		self.update_sum()

	def on_value_1_text_changed(self, sender, e):
		if self._is_updating:
			return

		value = self._parse_slider_value(self.value_1_text.Text, self.slider_1.Value)
		self._is_updating = True
		self.slider_1.Value = value
		self.value_1_text.Text = str(value)
		self._is_updating = False
		self.update_sum()

	def on_value_2_text_changed(self, sender, e):
		if self._is_updating:
			return

		value = self._parse_slider_value(self.value_2_text.Text, self.slider_2.Value)
		self._is_updating = True
		self.slider_2.Value = value
		self.value_2_text.Text = str(value)
		self._is_updating = False
		self.update_sum()

	def _parse_slider_value(self, text, fallback):
		try:
			value = int(text)
		except (TypeError, ValueError):
			return fallback

		if value < 1:
			return 1
		if value > 10:
			return 10
		return value

	def update_sum(self):
		total = self.slider_1.Value + self.slider_2.Value
		self.sum_text.Text = str(total)

	def on_select_file_click(self, sender, e):
		dialog = ef.OpenFileDialog()
		dialog.Title = "Select JSON File"
		dialog.Filters.Add(ef.FileFilter("JSON Files", ".json"))

		if dialog.ShowDialog(self) != ef.DialogResult.Ok:
			return

		path = dialog.FileName
		self.file_path_text.Text = path
		self.load_slider_values(path)

	def on_save_file_click(self, sender, e):
		name_dialog = FileNamePromptDialog("slider_values.json")
		name_dialog.ShowModal(self)
		if not name_dialog.Accepted:
			return

		file_name = (name_dialog.FileName or "").strip()
		if not file_name:
			ef.MessageBox.Show(self, "Please enter a file name.", "Save Error")
			return

		if not file_name.lower().endswith(".json"):
			file_name += ".json"

		base_path = (self.file_path_text.Text or "").strip()
		if base_path:
			directory = os.path.dirname(base_path)
		else:
			directory = os.getcwd()

		path = os.path.join(directory, file_name)
		self.file_path_text.Text = path
		self.save_slider_values(path)

	def load_slider_values(self, path):
		try:
			with open(path, "r") as file_obj:
				data = json.load(file_obj)
		except Exception as ex:
			ef.MessageBox.Show(self, "Could not read file:\n{0}".format(ex), "Load Error")
			return

		if not isinstance(data, dict):
			ef.MessageBox.Show(self, "File must contain a JSON dictionary.", "Load Error")
			return

		value_1 = self._parse_slider_value(data.get("slider_1"), self.slider_1.Value)
		value_2 = self._parse_slider_value(data.get("slider_2"), self.slider_2.Value)

		self._is_updating = True
		self.slider_1.Value = value_1
		self.slider_2.Value = value_2
		self.value_1_text.Text = str(value_1)
		self.value_2_text.Text = str(value_2)
		self._is_updating = False
		self.update_sum()

	def save_slider_values(self, path):
		data = {
			"slider_1": int(self.slider_1.Value),
			"slider_2": int(self.slider_2.Value),
		}

		try:
			with open(path, "w") as file_obj:
				json.dump(data, file_obj, indent=2)
		except Exception as ex:
			ef.MessageBox.Show(self, "Could not save file:\n{0}".format(ex), "Save Error")
			return

		ef.MessageBox.Show(self, "Saved slider values to:\n{0}".format(path), "Saved")


class FileNamePromptDialog(ef.Dialog):
	def __init__(self, default_name):
		super(FileNamePromptDialog, self).__init__()
		self.Title = "New File Name"
		self.Padding = ed.Padding(12)
		self.Resizable = False
		self.Accepted = False
		self.FileName = default_name

		self.name_text = ef.TextBox()
		self.name_text.Text = default_name
		self.name_text.Width = 260

		ok_button = ef.Button(Text="OK")
		ok_button.Click += self.on_ok_click

		cancel_button = ef.Button(Text="Cancel")
		cancel_button.Click += self.on_cancel_click

		self.DefaultButton = ok_button
		self.AbortButton = cancel_button

		layout = ef.DynamicLayout()
		layout.Spacing = ed.Size(8, 8)
		layout.AddRow(ef.Label(Text="Enter file name:"))
		layout.AddRow(self.name_text)
		layout.AddRow(None, ok_button, cancel_button)
		self.Content = layout

	def on_ok_click(self, sender, e):
		self.Accepted = True
		self.FileName = self.name_text.Text
		self.Close()

	def on_cancel_click(self, sender, e):
		self.Accepted = False
		self.Close()


def main():
	parent = RhinoEtoApp.MainWindowForDocument(sc.doc)
	dialog = SumSlidersDialog()
	dialog.ShowModal(parent)


if __name__ == "__main__":
	main()