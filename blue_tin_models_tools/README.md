# Guidelines

## Characters

The objective of Shot Generator is to keep the setup of a shot extremely simple. Therefore, the characters are designed with the silhouette of the character in mind - a shape that upon quick glance, you can tell:
  * Gender
  * Age
  * Body type
  * Height
  * Pose

### The Models

Female and Male bone proportions and body shape are different so they needed to be their own models. Additionally, adult and youth bone proportions and body shape are different so they needed to be their own models. [ Male, Female ] x [ Adult, Youth] = 4 models.

We accomplished this by creating 4 main models: 
  * Female - Adult
  * Female - Youth
  * Male - Adult
  * Male - Youth

<img src="https://user-images.githubusercontent.com/441117/50731218-9b1b4680-112c-11e9-844f-e950ba16b6ec.png">

### Morph targets (Blend Shapes)

Body type is accomplished through morph targets. Morph targets or Blend Shapes are modifications to existing geometry. They have the same exact vertices, they are just in different locations. So you can easily mix/blend between 1 or more morph targets to get interesting model shapes. We decided on 4 prototypical body shapes: 

  * Mesomorph (Medium Build) [default] <br><img src="https://user-images.githubusercontent.com/441117/50731145-7bcfe980-112b-11e9-86c5-2157ef20b45f.png" width=500>
  * Ectomorph (Skinny)<br><img src="https://user-images.githubusercontent.com/441117/50731176-fc8ee580-112b-11e9-9102-a83692533551.png" width=500>
  * Muscular<br><img src="https://user-images.githubusercontent.com/441117/50731184-221bef00-112c-11e9-915f-b7f086ee2ba6.png" width=500>
  * Obese<br><img src="https://user-images.githubusercontent.com/441117/50731190-3eb82700-112c-11e9-9978-9b349252ba2c.png" width=500>

By blending a combination, you can make many body shapes: 
  * Skinny athletic person (Ectomorph: 0.7, Muscular: 0.4)<br><img src="https://user-images.githubusercontent.com/441117/50731203-6f985c00-112c-11e9-96e8-4a84655810d9.png" width=500>
  * Stocky person (Obese: 0.5, Muscular: 0.5)<br><img src="https://user-images.githubusercontent.com/441117/50731207-74f5a680-112c-11e9-8428-4b7f3ff38261.png" width=500>

### Armature (Skeleton Structure)

The mesh of the model is rigged/skinned mostly by Mixamo's online tool. We use their standard 65 bone Standard Skeleton, which includes individual fingers. The bone names are named like: mixamorig:LeftUpLeg

<img src="https://user-images.githubusercontent.com/441117/50726908-49999a00-10e1-11e9-8bbc-71aefa5df0ac.png" width="300">

### Scale (Height)

1 3D Unit = 1 Meter = 3.28084 Feet = 1.09361 Yards

Even though a 3D unit is arbitrary, the world has loosely agreed that this is the preferred conversion. 

Shot Generator automatically scales the models to normalize them. However the scales for the standard model heights are:

  * Male - Adult: 1.8 (5'11")
  * Female - Adult: 1.625 (5'4")
  * Female - Youth: 1.6 (5'3")
  * Male - Youth: 1.6 (5'3")

Height is controlled by scaling the armature/skeleton to the appropriate height. The only exception is that the head bone does not scale. As people are taller and shorter, their heads are roughly the same size. It is true that skulls vary in size. The scale of the head can be overridden. 

### Pose

Posing is done in the engine. This is by rotating bones, and saving a preset of all the bone rotations. There are no limitations on how you can rotate bones. Go crazy.

### UV / Texture

There is one material and one texture. It's adjacent to the model in the textures folder.

## Custom Character Models

The main reason why we are releasing these models open source is so people can make their own models or customize the existing models.

Making a new model should be fairly simple.

What you don't need: 

  * You don't even need a rigged skeleton. (It will work without - of course you can't pose it)
  * You don't need a standard skeleton. (You can pose any bones. So you could have a rigged dog.)
  * You don't need blend shapes / morph targets.
  * You can have any blend shapes you want (It will load them in dynamically)

What you need:

  * A model with a mesh
  * A single material with a single texture

So some custom examples:

  * A character downloaded off the internet with no rig and you don't need to pose it
  * A dog - Who's a good boy?<br>  <img src="https://user-images.githubusercontent.com/441117/50732776-b5b2e700-114f-11e9-8877-d4b160e30389.png" width="300">
  * A snake
  * A monster
  * A person with very specific morph targets
  * A very specific model with lots of detail
  * A model based on one of these models you slightly edited

## Checklist

Substance .sbsar is a file format used by Substance Designer, a node-based texturing tool for creating materials.

MaterialX is an open standard for transfer of rich material and look-development content between applications and renderers.

1. Use Blender blend files from 2.93 LTS.
1. Export Blend file:
    1. All images are stored outside of the blend file.
    1. Do not have LOD in the name.
    1. Do not store LODs in the Blend file.
    1. Do not store glTF2s or other formats other than `.blend` in the repo.
