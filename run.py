#! blender --background --python .\blend_export.py

# The MIT License (MIT)

# Copyright (c) 2016 Godot Engine

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

"""
Automates the regeneration of various export formats from golden blend files.

Note: In environments that do not support shebang execution, Blender may be
invoked from the command line with the arguments from the first line of this
script (see run_tests.bat).
"""

import bpy
import posixpath
import shutil
import os

directories = ["characters"]
export_types = ["gltf"]
for export_type in export_types:
    shutil.rmtree(export_type, ignore_errors=True)
    posixpath.os.mkdir(export_type, mode=0o777)
for directory in directories:
    for filename in os.listdir(directory):
        if not filename.endswith(".blend"):
            continue
        for export_type in export_types:
            bpy.ops.wm.open_mainfile(filepath=os.path.join(directory, filename))
            basename = filename.rsplit(".blend", 1)[0]
            export_path = os.path.normpath(os.path.join(directory, os.pardir, export_type, basename + "." + export_type))
            if export_type == "gltf":
                bpy.ops.export_scene.gltf(
                    filepath=export_path,
                    export_format='GLB',
                    export_copyright="Creative Commons Attribution 4.0 International Public License 2021 V-Sekai and 2019 MIT License Wonder Unit",
                )
            elif export_type == "fbx":
                bpy.ops.export_scene.fbx(filepath=export_path)
            elif export_type == "obj":
                bpy.ops.export_scene.obj(filepath=export_path)
            elif export_type == "dae":
                bpy.ops.wm.collada_export(filepath=export_path)
