# How to save a pose as the rest pose in Blender

Tested on Blender 2.93.

1. Move to animation frame 0
1. Select Armature
1. Always check orient rig.
1. Rig skeleton in "Rig On the Fly" Blender addon
1. Select left hand and click IK no pole
1. Select the right hand and click IK no pole
1. Pose your skeleton to t-pose
1. Animation key the entire skeleton
1. Go to object mode
1. For each mesh weighted by the skeleton
    1. Go to the mesh object properties
    1. Go to armature Modifier
    1. Save armature as a shape key
1. Select the skeleton
1. Go to pose mode
1. Select all
1. Apply pose as rest pose
1. Select all
1. Clear transforms
1. Select all
1. Animation key the entire skeleton
1. Go to object mode
1. For each blend shape in each mesh weighted by the skeleton
    1. Go to object data properties
    1. Move new shape key called "Armature" below the bottom. (First slot)
    1. Move "Armature" down one slot to the slot after the first slot.
    2. Duplicate as many times as there are blend shapes
    3. Set each blend to 1.0 strength
    1. Delete the each of the extra blend shapes
4. Select Armature
5. Bake rig on the fly skeleton
6. Cleanup Recursive Unused Datablocks
7. Done

## License

MIT License

Copyright (c) 2021 V-Sekai

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
