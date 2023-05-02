# dam_api_tools
This repository is a place to park various small scripts and tools that use the Heix DAM API.

All of these scripts are designed to be added to a users P4V application as a custom tool, or as shelf buttons in their respective DCCs. 
Further technical reading can be found [here](https://www.perforce.com/manuals/p4v/Content/P4V/advanced_options.custom.html).

---

## import_rm_tools.xml

#### Usage
This xml file can be used to import the P4V specific custom tools into your own P4V instance.
You will need to edit the script paths prior to import to replace the `YOUR_PATH` portion to reflect the script location on your specific machine.

---


## attach_preview.py

#### Usage

This script can be used from P4V to attach a given image to a selected workspace file as a preview. The user runs the tool with a current selection (single file) and will be prompted to provide the image path via dialog.

#### Arguments

`YOUR_PATH/p4v_custom_tools/p4v_custom_tools/attach_preview.py %f <image_filepath>`
1. Selected filepath from P4V interface
2. image_filepath to use (prompt)

---

## update_dam_preview_maya.py

#### Usage

Intended to be added as a custom Shelf button into Maya. When clicked while you have a Maya scene open within a P4 client workspace it will take a screenshot of your current viewport and attach it to your the current revision in Helix Core as a hex encoded value. This Value will then be visible in Helix DAM as a preview image.

#### Arguments

None. The current open scene name will be used.

---

## update_dam_preview_max.py


#### Usage
Intended to be run as a custom script in 3DSMax. When clicked while you have a 3DSMax scene open within a P4 client workspace it will take a screenshot of your current viewport and attach it to your the current revision in Helix Core as a hex encoded value. This value will then be visible in Helix DAM as a preview image.

#### Arguments

None. The current open scene name will be used.

---

## update_dam_preview_blender.py


#### Usage

Intended to be run as a custom script in Blender. When clicked while you have a Blender scene open within a P4 client workspace it will take a screenshot of your current viewport and attach it to your the current revision in Helix Core as a hex encoded value. This value will then be visible in Helix DAM as a preview image.

#### Arguments

None. The current open scene name will be used.

---

## update_dam_preview_vector.py


#### Usage

This script can be used from P4V to render a thumbnail and preview images for both EPS and SVG files. The user runs the tool with a current selection and the attributes will be attached to the current version in Helix Core to be displayed within HelixDAM.

To Note: This tool requires a few python libraries and dependencies to operate correctly.
Pillow, svglib, and ghostscript.

If working with windows, you may need to install the GhostScript executables as  pillow's eps implentation looks to your PATH env var for the executables.

#### Arguments

1. Selected filepath from P4V interface
