
.. _material_editor:

=================
Material Editor
=================

.. seealso::

        Here you can find the section dedicated to video tutorials, it may be useful to you: :ref:`vt_material_editor`

The material editor is a very important panel, and it takes many different forms depending on the type of material applied
**Nexus** / **Simple PBR** Explained here: :ref:`me_material_nexus_type`


Example Material Editor Nexus with 4 Modules for painting:

.. image:: _static/_images/material_editor/material_editor_nexus_four_modules.webp
    :align: center
    :width: 800
    :alt: Material Editor Nexus Four Modules

|

From this panel you can also access painting and many other features!

------------------------------------------------------------------------------------------------------------------------

.. _me_material_nexus_type:

Material Nexus type
====================


If you are in Nexus mode, or have applied materials that support nexus modules, The panel looks like this:

**This is the classic Nexus panel of Texture-based materials**

.. image:: _static/_images/material_editor/material_editor_before_add_module.jpg
    :align: center
    :width: 400
    :alt: Material Editor Before Add Module

|

Here an example of the Blender node tree with an Extreme PBR Nexus material containing 2 modules and 2 Fx Layers (related to the modules)

.. image:: _static/_images/material_editor/nexus_nodes_system.webp
    :align: center
    :width: 800
    :alt: Nexus Nodes System

Don't worry, everything is managed through the Extreme PBR panel as shown in the previous photo to this one!

------------------------------------------------------------------------------------------------------------------------

.. _add_module:

Add Module
----------

.. image:: _static/_images/material_editor/add_module_example_01.png
    :align: center
    :width: 800
    :alt: Add Module Example 01

|

With this button you can add up to a maximum of 4 modules, which will allow you to paint :ref:`texture_paint` them on
the object you are working on.

.. note::
    In order to add a module, rely on the :ref:`material_browser` in fact you will add exactly what you have in the preview,
    or you can add via :ref:`shader_maker`

    Add Module will not work with Non Nexus type materials!

------------------------------------------------------------------------------------------------------------------------

.. _module_material_panel:

Module Material Panel
-----------------------


.. _show_hide_group:

Show / Hide Group
******************

This button allows you to hide or show all the properties of a group (Nexus Module), it is useful if you are using the
FX Module, it makes the workspace cleaner and allows you to focus only on what you are doing.

.. image:: _static/_images/material_editor/me_show_hide_group_01.png
    :align: center
    :width: 400
    :alt: Material Editor Show Hide Group


------------------------------------------------------------------------------------------------------------------------

.. _search_module:

Search Module
**************

.. note::
      Useful only if there are 2 or more modules present in the material.


This button opens a search menu, which allows you to replace / move the modules present in the material.
As soon as you select a module, the module from where you are starting will be replaced with the one you have chosen and vice versa.

.. image:: _static/_images/material_editor/me_search_module.png
    :align: center
    :width: 400
    :alt: Material Editor Search Module


------------------------------------------------------------------------------------------------------------------------

.. _module_name:

Module Name (Group Name)
*************************

From here you can view and also change the name of the group (Nexus Module) you are using.

.. image:: _static/_images/material_editor/me_module_name.png
    :align: center
    :width: 600
    :alt: Module Name

------------------------------------------------------------------------------------------------------------------------

.. _replace_module:

Replace Module
***************


The Replace Module button allows you to replace the module you are using by loading another module, in accordance with the preview
of the :ref:`material_browser` you have chosen.

.. image:: _static/_images/material_editor/me_replace_module.png
    :align: center
    :width: 400
    :alt: Replace Module


------------------------------------------------------------------------------------------------------------------------

Remove Module
**************

This button appears only if there are 2 or more Nexus Modules, so it will allow you to remove the underlying module.

.. image:: _static/_images/material_editor/me_remove_module.webp
    :align: center
    :width: 600
    :alt: Remove Module


------------------------------------------------------------------------------------------------------------------------

.. _module_clip_texture:

Clip Texture
*************

.. image:: _static/_images/material_editor/me_clip_texture_button.webp
    :align: center
    :width: 600
    :alt: Clip Texture

|


This button allows you to clip the texture, clip texture means that the texture will not be repeated, but will only be once,
so, the object will have only one texture, without repetitions, no seamless.

**Example of a texture clipped:**

.. image:: _static/_images/material_editor/me_clip_texture_example.webp
    :align: center
    :width: 800
    :alt: Clip Texture Example


------------------------------------------------------------------------------------------------------------------------

.. _module_reset_values:

Reset Values
**************

The Reset Values Button allows you to reset the properties of the module you are using to the default values.

.. image:: _static/_images/material_editor/me_reset_values.png
    :align: center
    :width: 600
    :alt: Reset Values

------------------------------------------------------------------------------------------------------------------------

.. _module_info:

Info
*****

The Info button allows you to view the information of the module you are using, for example the name of the author etc.

.. image:: _static/_images/material_editor/me_info.png
    :align: center
    :width: 600
    :alt: Info

|

.. note::
        Not all modules necessarily have the info button, it depends on who created them, sometimes it is not present, but usually
        this information is in the :ref:`info_and_tag` menu

------------------------------------------------------------------------------------------------------------------------

.. _module_tips:

Tips
*****

This button allows you to view or hide the hint next to each slider of the module you are using.
so by pressing the hint buttons, you will see a window appear with a description of the parameter you are using.


.. image:: _static/_images/material_editor/me_tips.png
    :align: center
    :width: 600
    :alt: Tips


------------------------------------------------------------------------------------------------------------------------

.. _texture_manager_button:

Texture Manager Button
************************

The texture manager buttons allows you to access the :ref:`texture_manager_panel` and manage the textures you are using in your material.
note well, texture manager is explained here: :ref:`texture_manager_panel`

When you find these buttons next to the sliders, it means that these sliders are linked to a texture, and therefore
you can manage the texture through the texture manager.

.. image:: _static/_images/material_editor/me_texture_manager_button.png
    :align: center
    :width: 800
    :alt: Texture Manager Button

|

.. note::
        If no texture is linked to that property, the button will not have the texture icon, but an **import** icon

------------------------------------------------------------------------------------------------------------------------

.. _diffuse_color:

Diffuse Color
**************

This color box allows you to choose a color to apply to the diffuse texture, in case there is no texture, this takes the place of the texture as a solid color.

.. note::
        This color works in accordance with the :ref:`colorize_strength`

.. image:: _static/_images/material_editor/me_diffuse_color.png
    :align: center
    :width: 800
    :alt: Diffuse Color

------------------------------------------------------------------------------------------------------------------------

.. _color_lab_button:

Color Lab Button
*****************


Color Lab Button gives you access to the popup panel for color management, you can find a detailed explanation
here: :ref:`color_lab`


.. image:: _static/_images/material_editor/color_lab_button.jpg
    :align: center
    :width: 800
    :alt: Color Lab Button


------------------------------------------------------------------------------------------------------------------------

.. _colorize_strength:

Colorize Strength
******************

This slider allows you to adjust the strength of the color you have chosen in the :ref:`diffuse_color` box.


.. image:: _static/_images/material_editor/me_colorize_strength.webp
    :align: center
    :width: 400
    :alt: Colorize Strength

|

This slider was created so that a value up to 0.5 will colorize the material, so the color will not replace the texture,
but it will overlap it, while a value greater than 0.5 will replace the texture with the chosen color up to the value 1.0
which is the maximum colorization value, so it will be as if you had no texture, but only the chosen color, this
always keeping the other maps like the specular, the normal etc.


------------------------------------------------------------------------------------------------------------------------

Colorize Sample
****************

By activating this button, 2 new sliders will appear, the first allows you to choose the color to be sampled, the second
is the **Tolerance** which allows you to choose how much the sampled color must be similar to the original color to be
replaced.

So in accordance with these settings, now the colorization will only color the parts that have the color similar to that.

.. image:: _static/_images/material_editor/me_colorize_sample.webp
    :align: center
    :width: 800
    :alt: Colorize Sample


------------------------------------------------------------------------------------------------------------------------

.. _me_emission:

Emission
********

.. note::
        In **Cycles Render** the Emission also acts as lighting, in **Eevee** no, in **Eevee** it is only a visual effect.

.. image:: _static/_images/material_editor/me_emission.webp
    :align: center
    :width: 400
    :alt: Emission

|

This slider is used to set the Emissivity of the material, there are some materials that have a dedicated emissivity map
type **Facade** where the emissivity maps are on the windows, so if you adjust these sliders with that type of
material, you will have your emission on the areas where there is the emissivity map, while if there is no emissivity map, then
this slider will work as general emissivity of the material, the whole material will be emitting.

------------------------------------------------------------------------------------------------------------------------

.. _me_transparent:

Transparent
************

.. image:: _static/_images/material_editor/me_transparent_and_ops.webp
    :align: center
    :width: 400
    :alt: Transparent and Ops

|

Transparent slider is used to set the transparency of the material, if a transparency map is present, then this slider
will only adjust certain areas of the material, while if it is not present, then it will adjust the general transparency of the material,
the whole material in this case will be transparent according to the set value.

Note, in **Eevee render** and only in **Eevee render** transparency is handled differently, so you will have to use
the button next to the slider (Transparent Mode button) to choose how to handle transparency, you can choose between these settings:


**This material use a transparency map:**

.. image:: _static/_images/material_editor/metal_walkway_002.png
    :align: center
    :width: 400
    :alt: Metal Walkway 002

|

.. _me_transparent_mode:

Transparent Mode
#################

This button actually manages the **Blend Mode** and **Shadow Mode** of the material

.. image:: _static/_images/material_editor/blend_mode_shadow_mode.webp
    :align: center
    :width: 400
    :alt: Blend Mode Shadow Mode

|

Is BLEND blends every pixel between material and transparency, Is HASHED performs the blend in a noisy fashion (faster),
Is CLIP sets as transparent only pixels under a threshold value (useful for texture controlled transparency).

Settings only for Eevee Render:

- **Is Opaque:** Blend Mode: Opaque, Shadow Mode: Opaque

.. image:: _static/_images/material_editor/mp_is_opaque.jpg
    :align: center
    :width: 800
    :alt: Is Opaque

|

- **Is Blend:** Blend Mode: Alpha Blend, Shadow Mode: Alpha Ashed

.. image:: _static/_images/material_editor/mp_is_blend.jpg
    :align: center
    :width: 800
    :alt: Is Blend

|

- **Is Hashed** Blend Mode: Alpha Hashed, Shadow Mode: Alpha Hashed (The best, but requires more rendering samples to get a good result)

.. image:: _static/_images/material_editor/mp_is_hashed.jpg
    :align: center
    :width: 800
    :alt: Is Hashed

|

- **Is Clip** Blend Mode: Alpha Clip, Shadow Mode: Alpha Clip

.. image:: _static/_images/material_editor/mp_is_clip.jpg
    :align: center
    :width: 800
    :alt: Is Clip




------------------------------------------------------------------------------------------------------------------------

Subsurface/Radius
******************

.. image:: _static/_images/material_editor/me_subsurface_radius.webp
    :align: center
    :width: 400
    :alt: Subsurface

|

These values allow you to adjust the Subsurface Scattering of the material.
Subsurface Scattering is the ability of a material to let light pass through it, but not transparently,
but in a diffuse way, as if the light were diffused inside the material, this is very useful for materials
like skin, leaves, ears, rubber, plastic, etc.

**Example of Subsurface Scattering:**

.. image:: _static/_images/material_editor/subsurface_suzanne.jpg
    :align: center
    :width: 400
    :alt: Subsurface Example


------------------------------------------------------------------------------------------------------------------------

Ambient Occlusion
******************

.. image:: _static/_images/material_editor/me_ambient_occlusion.webp
    :align: center
    :width: 400
    :alt: Ambient Occlusion

|

This slider allows you to adjust the Ambient Occlusion of the material, if an Ambient Occlusion map is present.

This allows you to further simulate the ambient occlusion through its map. This is useful in Eevee, where
the calculation of the ambient occlusion is quite approximate, this slider will give a touch of realism in addition to the material.

If you are in Cycles Render, in some cases it can be useful.

------------------------------------------------------------------------------------------------------------------------

Metallic
*********

.. image:: _static/_images/material_editor/me_metallic.webp
    :align: center
    :width: 400
    :alt: Metallic

|

This slider allows you to adjust the Metallic of the material, if a Metallic map is present, if it is not present
then this slider will adjust the general metallic of the material, the whole material in this case will be metallic
depending on the set value, a metallic value of 1.0 and a Roughness of 0.0, will render the material as a
shiny metal, while a metallic value of 0.0 and a Roughness of 1.0 will render the material as a non-metallic material

.. image:: _static/_images/material_editor/metal_004.png
    :align: center
    :width: 400
    :alt: Metallic Example


.. hint::
        On a completely black material, setting the Metallic will have no effect, as the black color
        does not reflect light, so no effect will be seen, to see the effect of the Metallic, it is necessary
        set a color other than black, even if it is a very dark color, in this way you will see the effect of the Metallic.
        In short, everything except total black 😊

------------------------------------------------------------------------------------------------------------------------

Specular/Tint
**************

.. image:: _static/_images/material_editor/me_specular_tint.webp
    :align: center
    :width: 400
    :alt: Specular Tint

|

This 2 properties work in symbiosis:


.. _me_specular:

Specular
#########

This slider adjusts the specular of the material, if a specular map is present, then this slider will only adjust
some areas of the material, while if it is not present, then it will adjust the general specular of the material.


Specular Tint
##############

Mix between white and the base color in order to tint the specular highlights.

**Example between Specular tint at 0.0 and 1.0, on the left 0.0, on the right 1.0**

.. image:: _static/_images/material_editor/specular_tint_example.webp
    :align: center
    :width: 800
    :alt: Specular Tint Example

------------------------------------------------------------------------------------------------------------------------

.. _me_roughness:

Roughness
**********

.. image:: _static/_images/material_editor/me_roughness.webp
    :align: center
    :width: 400
    :alt: Roughness

|

This slider allows you to adjust the Roughness of the material, if a Roughness map is present, then this slider will only adjust
some areas of the material, while if it is not present, then it will adjust the general roughness of the material.


**Example, on the left the roughness is at 0.0 on the right at 1.0:**

.. image:: _static/_images/material_editor/me_roughness_zero_to_max.webp
    :align: center
    :width: 800
    :alt: Roughness Zero To Max

------------------------------------------------------------------------------------------------------------------------

Sheen / Sheen Tint
*******************

.. image:: _static/_images/material_editor/me_sheen_and_tint.webp
    :align: center
    :width: 400
    :alt: Sheen and Tint

|

These 2 properties work in symbiosis:

Sheen
#######

The sheen is a soft velvet-like reflection that appears in the areas where the light is reflected, value 0.0 means no sheen,
while value 1.0 means maximum sheen.

Sheen Tint
###########

Mix between white and the base color in order to tint the sheen. Value 0.0 means no tint, while value 1.0 means maximum tint.

**Sheen Example:**
First image, **Sheen 0.0** **Sheen Tint 0.0**, Second image **Sheen 1.0** **Sheen Tint 0.0**, Third image **Sheen 1.0** **Sheen Tint 1.0**

.. image:: _static/_images/material_editor/me_sheen_tint_example.webp
    :align: center
    :width: 800
    :alt: Sheen Example

------------------------------------------------------------------------------------------------------------------------

Clearcoat / Roughness
**********************

.. image:: _static/_images/material_editor/me_clearcoat_and_roughness.webp
    :align: center
    :width: 400
    :alt: Clearcoat and Roughness

|

Clearcoat
##########

The clearcoat is a layer of varnish that is applied to the material, it is a layer that is applied on top of the material,
this is similar to the clearcoat of a car.

Clearcoat Roughness
###################

In accordance with the clearcoat, this slider allows you to adjust the roughness of the clearcoat.

**Example, First Image Clearcoat 0.0, Second Image Clearcoat 1.0 and Roughness 0.0, Third Image Clearcoat 1.0 and Roughness 0.25**

.. image:: _static/_images/material_editor/me_clearcoat_example.webp
    :align: center
    :width: 800
    :alt: Clearcoat Example


------------------------------------------------------------------------------------------------------------------------

Transmission
*************

.. image:: _static/_images/material_editor/me_transmission_section.webp
    :align: center
    :width: 400
    :alt: Transmission

|

The transmission is the ability of a material to let light pass through it, this is very useful for materials
like glass, water etc.

This property works in symbiosis with the **IOR** and **Transmission Roughness** properties

The value of the transmission is a value between 0.0 and 1.0, where 0.0 means no transmission, while 1.0
means maximum transmission (To simulate a normal glass it will have 1.0 of transmission)

Ray Tracer Button
##################

The button Raytracer, activate or deactivate, the Screen Space Refractions (For the Glass). Eevee only, in Cycles, this is not necessary,
in Eevee Render it is really necessary to activate it if you want to get a realistic result even if not perfect.

This button activates or deactivates the **Screen Space Refractions** in the material properties and deactivates the property
**Subsurface Translucent** if it is active, otherwise they will go into contrast (This is only necessary for the
Eevee rendering engine, it is not necessary in Cycles)

IOR
#####

The IOR is the index of refraction, it is a value that is used to calculate the refraction of the material.
For example the IOR of the glass is 1.45, the IOR of the water is 1.33, the IOR of the diamond is 2.42 etc...

Transmission Roughness
########################

This slider allows you to adjust the roughness of the transmission. The transmission Roughness will make the material
more or less transparent, the higher the value, the less transparent the material will be, the lower the value, the more transparent
the material will be.

------------------------------------------------------------------------------------------------------------------------

Normal
*******

.. image:: _static/_images/material_editor/me_normal.webp
    :align: center
    :width: 400
    :alt: Normal

|

The normal map (Only if present) allows you to add details to the material this is very useful for simulating details
like reliefs, scratches, etc ... A value equal to 0.0 means no normal map.

Here is an example, on the left the value is 0.0, on the right the value is 1.0

.. image:: _static/_images/material_editor/me_normal_example.webp
    :align: center
    :width: 800
    :alt: Normal Example

------------------------------------------------------------------------------------------------------------------------

Bump / Distance
****************

.. image:: _static/_images/material_editor/me_bump_and_distance.webp
    :align: center
    :width: 400
    :alt: Bump and Distance

|

.. note::
        In Blender at the moment the Bump map has a small resolution limitation, so if you zoom in very close to the object
        you will notice that the Bump map is a bit pixelated, this is a limitation of Blender at the moment.

These 2 properties work in symbiosis:


Bump
#####

The bump map (Only if present) allows you to add details to the material this is very useful for simulating details
like reliefs, scratches, etc ... A value equal to 0.0 means no bump map.

Bump Distance
################

This slider allows you to adjust the distance of the bump map, the higher the value, the more the bump map will be visible,
the lower the value, the less the bump map will be visible.


Here an example, on the left the value of the Bump is 0.0 (Consequently the distance has no effect, on the right the value of the Bump is 0.20 and the distance is 1.0

.. image:: _static/_images/material_editor/me_bump_distance_example.webp
    :align: center
    :width: 800
    :alt: Bump Distance Example

|

.. note::
        The Bump Map, unlike the normal map, is less detailed, as the map is in Black and White, but it creates an effect
        of greater relief than the normal map.

------------------------------------------------------------------------------------------------------------------------

.. _me_vector_location:

Locations XYZ
**************

.. image:: _static/_images/material_editor/me_locations_xyz.webp
    :align: center
    :width: 400
    :alt: Locations XYZ

|

These 3 sliders **LX** **LY** **LZ** allow you to adjust the location of the texture, this is useful if you want to move
the position of the texture on the object.

.. note::
        The **Location Z** property will only work if the mapping type is set to **Box**, **Sphere** or **Tube**
        To access these properties refer to this paragraph: :ref:`mapping_editor_panel` and here: :ref:`mapping_editor_button`


.. attention::
        If you are using the displacement Modifier, these sliders will not move the Displacement effect, to move the
        displacement effect together with the texture, you have to use the **Mapping Editor** described here: :ref:`mapping_editor_panel`
        and here: :ref:`mapping_editor_button`
        because these sliders will not move the UV mapping. If you are using the Displacement **Microdisplacement**
        then these sliders will also work to move the displacement effect, but only in **Cycles Render** mode


------------------------------------------------------------------------------------------------------------------------

.. _me_vector_rotation:

Rotation XYZ
**************

.. image:: _static/_images/material_editor/me_rotation_xyz.webp
    :align: center
    :width: 400
    :alt: Rotation XYZ

|

These 3 sliders **RX** **RY** **RZ** allow you to adjust the rotation of the texture, this is useful if you want to rotate
the position of the texture on the object.

.. note::
        The **Rotation Z** property will only work if the mapping type is set to **Box**, **Sphere** or **Tube**
        To access these properties refer to this paragraph: :ref:`mapping_editor_panel` and here: :ref:`mapping_editor_button`

.. attention::
        If you are using the displacement Modifier, these sliders will not rotate the Displacement effect, to rotate the
        displacement effect together with the texture, you have to use the **Mapping Editor** described here: :ref:`mapping_editor_panel`
        and here: :ref:`mapping_editor_button`
        because these sliders will not rotate the UV mapping. If you are using the Displacement **Microdisplacement**
        then these sliders will also work to rotate the displacement effect, but only in **Cycles Render** mode


------------------------------------------------------------------------------------------------------------------------

.. _me_vector_scale:

Scale XYZ
**********

.. image:: _static/_images/material_editor/me_scale_xyz.webp
    :align: center
    :width: 400
    :alt: Scale XYZ

|

These 3 sliders **SX** **SY** **SZ** allow you to adjust the scale of the texture, this is useful if you want to scale
the position of the texture on the object.

.. note::
        The **Scale Z** property will only work if the mapping type is set to **Box**, **Sphere** or **Tube**
        To access these properties refer to this paragraph: :ref:`mapping_editor_panel` and here: :ref:`mapping_editor_button`

.. attention::
        If you are using the displacement Modifier, these sliders will not scale the Displacement effect, to scale the
        displacement effect together with the texture, you have to use the **Mapping Editor** described here: :ref:`mapping_editor_panel`
        and here: :ref:`mapping_editor_button`
        because these sliders will not scale the UV mapping. If you are using the Displacement **Microdisplacement**
        then these sliders will also work to scale the displacement effect, but only in **Cycles Render** mode

------------------------------------------------------------------------------------------------------------------------

.. _me_vector_scale_uniform:

Scale Uniform
**************

.. image:: _static/_images/material_editor/me_scale_uniform.webp
    :align: center
    :width: 400
    :alt: Scale Uniform

|

This slider allows you to scale the texture uniformly, this is useful if you want to scale the texture uniformly.

.. attention::
        If you are using the displacement Modifier, this slider will not scale the Displacement effect, to scale the
        displacement effect together with the texture, you have to use the **Mapping Editor** described here: :ref:`mapping_editor_panel`
        and here: :ref:`mapping_editor_button`
        because this slider will not scale the UV mapping. If you are using the Displacement **Microdisplacement**
        then this slider will also work to scale the displacement effect, but only in **Cycles Render** mode


------------------------------------------------------------------------------------------------------------------------

World Coordinate
*****************

.. image:: _static/_images/material_editor/me_world_coordinate.webp
    :align: center
    :width: 400
    :alt: World Coordinate

|

The World Coordinate button, if active, allows you to use the coordinates of the world, otherwise it uses the coordinates of the object,
if you move the object once the button is activated, you will see that the texture will move together with the object when you move the object.
from its position.

------------------------------------------------------------------------------------------------------------------------

Random Location
****************

.. image:: _static/_images/material_editor/me_random_location.webp
    :align: center
    :width: 400
    :alt: Random Location

|

The random location allows you to move the texture randomly, provided that the objects to which this is applied
material in which the Random is activated, are separate objects, otherwise it will not work.

Here is an example of a scene with a fence with random location active, followed by an example with random location disabled:

.. image:: _static/_images/material_editor/random_location_example_on.webp
    :align: center
    :width: 800
    :alt: Random Location Example On


.. image:: _static/_images/material_editor/random_location_example_off.webp
    :align: center
    :width: 800
    :alt: Random Location Example Off



------------------------------------------------------------------------------------------------------------------------

.. _add_fx_layer:

Add Fx Layer
-------------

.. image:: _static/_images/material_editor/me_add_fx_layer.webp
    :align: center
    :width: 400
    :alt: Add Fx Layer

|

This Button, in accordance with the material preview present in the :ref:`material_browser` allows you to add an effect
to the material. This is explained well in this chapter: :ref:`fx_layer`

By adding an Fx Layer, the addon takes the selected material and analyzes it to understand which map to use as a Mask,
so the selection order is this:

    1. **mask**
    2. **imperfections**
    3. **roughness**
    4. **specular**
    5. **occlusion**
    6. **displace**
    7. **metal**
    8. **diffuse**
    9. **alpha**

So, in order, the addon as soon as it finds a map of those listed above, uses it as a mask to decide where to apply the effect,
and where not, in fact the first maps are all in black and white, white indicates where to apply the effect, black where not to apply it,
using the shades of these maps, we get an Fx Layer. You can also disable the mask map at a later time.


------------------------------------------------------------------------------------------------------------------------

Adjust Node Tree
-----------------

.. image:: _static/_images/material_editor/me_adjust_node_tree.webp
    :align: center
    :width: 400
    :alt: Adjust Node Tree

|

Adjust Node Tree button, if the nodes of Extreme PBR Nexus have been disconnected (For example due to an error, or an involuntary manipulation)
allows you to reconnect all Nexus nodes, and realigns them so that they have a correct order.


Here is an extreme example, before and after:

.. |Before| image:: _static/_images/material_editor/me_module_unconnected.jpg
    :width: 100%

.. |After| image:: _static/_images/material_editor/me_module_reconnected.jpg
    :width: 100%

+-------------------+
| |Before|          |
+-------------------+
| |After|           |
+-------------------+



.. _fx_layer:

Fx Layer
---------

.. note::
        In order to add the Fx Layer you will have to use the **Add Fx** button described here: :ref:`add_fx_layer`


The Fx Layer allows you to add **Above** the material (Module) you are using, an effect, such as
a **Fingerprints** effect or a **Dust** effect or a **Scratches** effect etc ...

To add an Fx Layers, make sure you have applied the material with the **Nexus** option, as the materials applied
with the **Simple PBR** mode do not support Fx Layers.


**An example, wood material, without Fx Layer**

.. image:: _static/_images/fx_layer/fx_plane_no_fx_example.webp
    :align: center
    :width: 100%
    :alt: Fx Plane No Fx Example

**An example, wood material, with Fx Layer Colored**

.. image:: _static/_images/fx_layer/fx_plane_fingerprint_white_example.webp
    :align: center
    :width: 100%
    :alt: Fx Plane Fingerprint White Example

**An example, wood material, with Fx Layer Normal and Roughness**

.. image:: _static/_images/fx_layer/fx_plane_fingerprint_normal_example.webp
    :align: center
    :width: 100%
    :alt: Fx Plane Fingerprint Normal Example

|

.. note::
        All Texture-based materials can become Fx Layers, the Fx Layer in fact uses the maps present in any material
        of the Extreme PBR library, so you have a wide choice. For example you can also apply an FX layer of another wood to the material,
        this will use the maps of the other wood in addition to the underlying material

------------------------------------------------------------------------------------------------------------------------

Fx Layer Panel
----------------


Here is how an Fx Layer panel looks inside the material editor, in fact, once added, it will be
underneath the corresponding material panel (Nexus Module), you can also add 2 Fx Layers if you want, but
it is not recommended to exaggerate with the Fx Layers, as they could slow down the rendering, in addition at the moment, Blender
supports a maximum of 24 Textures per material, so using the Fx Layers, you could exceed this limit, and make it become
the material unusable in Blender.




.. image:: _static/_images/fx_layer/fx_layer_panel_01.webp
    :align: center
    :width: 400
    :alt: Fx Layer Panel 01

------------------------------------------------------------------------------------------------------------------------


Fx Layer same tools
********************


Most references are the same as the material panel, so I won't repeat them, but I leave the reference to the material panel
because they have the same functions:

**Left: Fx Layer, Right: Module**

.. image:: _static/_images/material_editor/fx_layer_same_tools.webp
    :align: center
    :width: 600
    :alt: Fx Layer Same Tools

|


- **Show / Hide Group:** :ref:`show_hide_group`
- **Search Module/Fx:** :ref:`search_module`
- **Module/Fx Name:** :ref:`module_name`
- **Replace Module/Fx:** :ref:`replace_module`


Remove Fx Layer
****************

In addition to removing the Fx Layer, just press the **Remove Fx Layer** button here:

.. image:: _static/_images/fx_layer/fr_layer_remove_button.webp
    :align: center
    :width: 400
    :alt: Fx Layer Remove Button

|

**Clip Texture:** :ref:`module_clip_texture`


------------------------------------------------------------------------------------------------------------------------

.. _fx_dynamic_mask:

Dynamic Mask
*************

.. image:: _static/_images/material_editor/fx_dynamic_mask_section.webp
    :align: center
    :width: 400
    :alt: Dynamic Mask Section

|

By this area you can manage the Fx Layer in 5 modes:


**Choose Mask Selector**

.. image:: _static/_images/material_editor/fx_choose_mask_selector.webp
    :align: center
    :width: 600
    :alt: Fx Choose Mask Selector

------------------------------------------------------------------------------------------------------------------------

Dynamic Mask Paint Mode
########################

This is the default setting once you apply an Fx Layer, in this mode you can paint
where you want the Fx Layer to be visible on the material.

.. important::
        If you intend to use the same material with the same Fx Layer on multiple objects with different shapes,
        you will have to make the material unique, because the painting mask will not work on objects with different shapes.


Paint Tools
############

.. image:: _static/_images/material_editor/fx_paint_tools_button.webp
    :align: center
    :width: 400
    :alt: Fx Paint Tools

|

Paint Tools Button gives you access to the **Paint Tools** popup panel explained in this chapter: :ref:`paint_tools_panel`

------------------------------------------------------------------------------------------------------------------------

Paint Un-Paint
################

.. image:: _static/_images/material_editor/fx_paint_unpaint.webp
    :align: center
    :width: 400
    :alt: Fx Paint Un-Paint

|

These 2 buttons are used to paint or delete the mask, the first paints, the second deletes.

.. note::
        Once you press one of these 2 buttons, the mouse cursor will become a brush, and you can paint,
        so you will have entered **Paint Mode**. To exit **Paint Mode** just press again the
        button that was pressed to enter **Paint Mode**, in fact it will become a **Stop**

        .. image:: _static/_images/material_editor/fx_stop_paint_button.webp
            :align: center
            :width: 400
            :alt: Fx Stop Paint Button



**Example with a corner of FX painted:**

.. image:: _static/_images/material_editor/fx_corner_painted_example.webp
    :align: center
    :width: 800
    :alt: Fx Corner Painted Example

------------------------------------------------------------------------------------------------------------------------

Fill Un-Fill
##############

.. image:: _static/_images/material_editor/fx_fill_unfill.webp
    :align: center
    :width: 400
    :alt: Fx Fill Un-Fill

|

These 2 buttons are used to fill or delete the mask, so if you press Fill, the whole object where the material is applied
of the Fx Layer will be filled with a mask, while if you press Un-Fill, the whole mask will be deleted and you will see only the material
underlying.


------------------------------------------------------------------------------------------------------------------------

Dynamic Mask Noise
*******************

.. image:: _static/_images/fx_layer/fx_dynamic_mask_noise_panel.webp
    :align: center
    :width: 400
    :alt: Fx Dynamic Mask Noise


In this mode, the mask will be controlled by a Noise node. This setting is very useful for making the grass or terrain
less uniform, as the Noise node generates a noise that can be used to mask the repetitions of the texture, so as to make
the material more natural.

**Here is an example of Dynamic Mask Noise:**

.. image:: _static/_images/fx_layer/fx_dynmask_noise_grass_example_01.webp
    :align: center
    :width: 800
    :alt: Fx Dynmask Noise Grass Example 01

The Base material is Grass, while the Fx material is another type of Grass. So this Noise effect decides where
show the Fx layer and where not, based on the mask generated by the Noise.

------------------------------------------------------------------------------------------------------------------------

Detailed Deadlift
##################

Detailed Deadlift manage how much the noise effect should be sharp or not, the higher the value, the sharper the noise effect will be,
consequently the Fx Layer will be sharper, while the lower the value, the less sharp the noise effect will be, consequently
the Fx Layer will be more blurred.

**Here is the example of a Deadlift set to 0.883, so quite strength:**

.. image:: _static/_images/fx_layer/fx_detailed_deadlift_example.webp
    :align: center
    :width: 800
    :alt: Fx Detailed Deadlift Example

------------------------------------------------------------------------------------------------------------------------

Invert Mask
############


By pressing the Invert Mask button, you will invert the colors of the noise mask, so where there was black before, now there will be white and vice versa.
consequently the noise effect will be inverted.

**Here is the example of a Invert Mask:**

.. image:: _static/_images/fx_layer/fx_invert_noise_mask_example.webp
    :align: center
    :width: 800
    :alt: Fx Invert Mask Example

------------------------------------------------------------------------------------------------------------------------

Roughness
##########

.. image:: _static/_images/fx_layer/fx_dynamic_mask_noise_roughness.webp
    :align: center
    :width: 400
    :alt: Fx Dynamic Mask Noise Roughness

|

Roughness Sliders is used to adjust the roughness of the noise, the higher the value, the roughness the noise will be, so it will be
more rich in details the detachment between the base material and the Fx material.

.. note::
        This value if set high, increases the rendering time.

------------------------------------------------------------------------------------------------------------------------

Detail
########

.. image:: _static/_images/fx_layer/fx_dynamic_mask_noise_detail.webp
    :align: center
    :width: 400
    :alt: Fx Dynamic Mask Noise Detail

|

Detail Sliders is used to adjust the detail of the noise, the higher the value, the more detailed the noise will be, so it will be
more rich in details the detachment between the base material and the Fx material.

.. note::
        This value if set high, increases the rendering time.

------------------------------------------------------------------------------------------------------------------------

Distortion
###########

.. image:: _static/_images/fx_layer/fx_dynamic_mask_noise_distortion.webp
    :align: center
    :width: 400
    :alt: Fx Dynamic Mask Noise Distortion

|

Distortion Sliders is used to adjust the distortion of the noise.

**Here an example of Distortion set to 4.0:**

.. image:: _static/_images/fx_layer/fx_noise_distortion_example_01.webp
    :align: center
    :width: 800
    :alt: Fx Noise Distortion Example 01

------------------------------------------------------------------------------------------------------------------------


Scale
#######

.. image:: _static/_images/fx_layer/fx_dynamic_mask_noise_scale.webp
    :align: center
    :width: 400
    :alt: Fx Dynamic Mask Noise Scale

|

Scale Sliders is used to adjust the scale of the noise.


------------------------------------------------------------------------------------------------------------------------

Dynamic Mask Worn Edges
************************

.. image:: _static/_images/fx_layer/fx_dynamic_mask_worn_edges_panel.webp
    :align: center
    :width: 400
    :alt: Fx Dynamic Mask Worn Edges

|

.. note::
        This tool is specially designed to work even in Eevee that does not yet have support for the detector
        of edges, so this tool is very useful for Eevee, and it also works in Cycles.


**Here is an example of Dynamic Mask Worn Edges:**

.. image:: _static/_images/fx_layer/fx_worn_edge_example.webp
    :align: center
    :width: 800
    :alt: Fx Worn Edge Example

|


The stressed edges are Pre-Bake, and work as a mask, so this mask will be cooked on the sharpest corners of the object.

------------------------------------------------------------------------------------------------------------------------

Make Worn Edges
################

.. image:: _static/_images/fx_layer/fx_make_worn_edges_button.webp
    :align: center
    :width: 400
    :alt: Fx Make Worn Edges Button

|

By pressing this button, the mask will be baked on the sharpest corners of the object.
This type of Bake is with denoising, so it is much more homogeneous and without noise.

------------------------------------------------------------------------------------------------------------------------

Make Noise Worn Edges
######################

.. image:: _static/_images/fx_layer/fx_make_noise_worn_edges_button.webp
    :align: center
    :width: 400
    :alt: Fx Make Noise Worn Edges Button

|

By pressing this button, the mask will be baked on the sharpest corners of the object, but with a noise effect.
This type of Bake is with noise, so it is much more noisy.

------------------------------------------------------------------------------------------------------------------------

Worn Edge Reset Value
######################

.. image:: _static/_images/fx_layer/fx_worn_edge_reset_value.webp
    :align: center
    :width: 400
    :alt: Fx Worn Edge Reset Value

|

This button resets the value of the sliders to the default value into the Worn Edges panel.

------------------------------------------------------------------------------------------------------------------------

Worn Edge Invert Mask
########################

.. image:: _static/_images/fx_layer/fx_worn_edge_invert_mask.webp
    :align: center
    :width: 400
    :alt: Fx Worn Edge Invert Mask

|

This button inverts the mask, so where there was black before, now there will be white and vice versa.

------------------------------------------------------------------------------------------------------------------------

Worn Edge Expand Edges
########################

.. image:: _static/_images/fx_layer/fx_worn_edge_expand_edges.webp
    :align: center
    :width: 400
    :alt: Fx Worn Edge Expand Edges

|

This slider allows you to expand the mask around the corners, so you can make the mask more or less large.

**Here an example of the expansion of the edges Mask:**

.. image:: _static/_images/fx_layer/fx_expand_edge_mask_example.webp
    :align: center
    :width: 800
    :alt: Fx Expand Edge Mask Example

------------------------------------------------------------------------------------------------------------------------

Edges Strength
################

.. image:: _static/_images/fx_layer/fx_worn_edge_edges_strength.webp
    :align: center
    :width: 400
    :alt: Fx Worn Edge Edges Strength

|

Edges Strength adjust the strength of the mask, the higher the value, the stronger the mask will be, the lower the value, the weaker the mask will be.
So it can be said that a low value of the mask, will make the mask more blurred, while a high value will make the mask stronger.

**Here an example between a low value and a high value of the Edges Strength:**

.. image:: _static/_images/fx_layer/fx_worn_edges_strength_example.webp
    :align: center
    :width: 800
    :alt: Fx Edges Strength Example

------------------------------------------------------------------------------------------------------------------------

Dynamic Mask Z-Mix V2
**********************

.. image:: _static/_images/fx_layer/fx_z_mix_panel.webp
    :align: center
    :width: 400
    :alt: Fx Z-Mix Panel

|

Z-Mix V2 allows you to mix the Fx Layer vertically, useful for simulating the effect of a material that has been consumed
vertically, or to simulate grass or "Climbing" vegetation or moss.

**Here some examples of Z-Mix V2:**

.. image:: _static/_images/fx_layer/fx_dynmask_zmix_v2_example_00.webp
    :align: center
    :width: 400
    :alt: Fx Dynmask Z-Mix V2

.. image:: _static/_images/fx_layer/fx_dynmask_zmix_v2_example_01.webp
    :align: center
    :width: 400
    :alt: Fx Dynmask Z-Mix V2 Example 01

.. image:: _static/_images/fx_layer/fx_dynmask_zmix_v2_example_02.webp
    :align: center
    :width: 400
    :alt: Fx Dynmask Z-Mix V2 Example 02

------------------------------------------------------------------------------------------------------------------------

Z-Mix V2 Reset Value
#####################

.. image:: _static/_images/fx_layer/fx_z_mix_reset_value.webp
    :align: center
    :width: 400
    :alt: Fx Z-Mix V2 Reset Value

|

This button resets the value of the sliders to the default value into the Z-Mix V2 panel.

------------------------------------------------------------------------------------------------------------------------

Z-Mix V2 Altitude Level
########################

.. image:: _static/_images/fx_layer/fx_z_mix_altitude_level.webp
    :align: center
    :width: 400
    :alt: Fx Z-Mix V2 Altitude Level

|

This slider adjusts the height of the Z-Mix V2 level.

**Example of 2 different Altitude Level:**

.. image:: _static/_images/fx_layer/fx_z_mix_altitude_example_01.webp
    :align: center
    :width: 800
    :alt: Fx Z-Mix V2 Altitude Example 01

------------------------------------------------------------------------------------------------------------------------

Z-Mix V2 Dead Line
###################

.. image:: _static/_images/fx_layer/fx_z_mix_dead_line.webp
    :align: center
    :width: 400
    :alt: Fx Z-Mix V2 Dead Line

|


By adjusting this slider you can adjust the Dead Line, i.e. the line of separation between the base material and the Fx material.
A higher value will make the Dead Line sharper, while a lower value will make the Dead Line more blurred.

**Example, on the left a dead line with value 0.0, on the right a dead line with a higher value**

.. image:: _static/_images/fx_layer/fx_z_mix_dead_line_example_01.webp
    :align: center
    :width: 800
    :alt: Fx Z-Mix V2 Dead Line Example 01


------------------------------------------------------------------------------------------------------------------------

Z-Mix V2 Deadline Noise
########################

.. image:: _static/_images/fx_layer/fx_z_mix_dead_line_noise.webp
    :align: center
    :width: 400
    :alt: Fx Z-Mix V2 Deadline Noise

|

.. note::
        If activated, it will give access to other properties described later


Once activated, it will make the deadline between one material and another, more noisy, so more natural.

**Here an example of a Deadline without Noise, and with Noise:**

.. image:: _static/_images/fx_layer/fx_dynmask_zmix_v2_deadline_noise_example.webp
    :align: center
    :width: 800
    :alt: Fx Dynmask Z-Mix V2 Deadline Noise Example

------------------------------------------------------------------------------------------------------------------------

Z-Mix V2 Expand Noise
######################

.. image:: _static/_images/fx_layer/fx_z_mix_expand_noise.webp
    :align: center
    :width: 400
    :alt: Fx Z-Mix V2 Expand Noise

|

Expand Noise allows you to expand the Noise, so to make it more stretched.

**Here an example of Expand Noise, on the left a noise without Expand Noise, on the right a noise with Expand Noise of higher value**

.. image:: _static/_images/fx_layer/fx_zmix_expand_noise_example.webp
    :align: center
    :width: 800
    :alt: Fx Z-Mix V2 Expand Noise Example

------------------------------------------------------------------------------------------------------------------------

Z-Mix V2 Scale
###############

.. image:: _static/_images/fx_layer/fx_z_mix_scale.webp
    :align: center
    :width: 400
    :alt: Fx Z-Mix V2 Scale

|

Scale allows you to adjust the scale of the Noise.

**Here an example of Scale, on the left a noise with small scale, on the right a noise most large scale**

.. image:: _static/_images/fx_layer/fx_zmix_scale_noise_example.webp
    :align: center
    :width: 800
    :alt: Fx Z-Mix V2 Scale Example

------------------------------------------------------------------------------------------------------------------------

Z-Mix V2 Stretch Noise
#######################

.. image:: _static/_images/fx_layer/fx_z_stretch_noise.webp
    :align: center
    :width: 400
    :alt: Fx Z-Mix V2 Stretch Noise

|

Stretch Noise allows you to stretch the Noise, so to make it more stretched or less stretched.

**Here an example of Stretch Noise, on the left a noise with No Stretch Noise, on the right a value of Stretch Noise of 1.0**

.. image:: _static/_images/fx_layer/fx_zmix_stretch_noise_example.webp
    :align: center
    :width: 800
    :alt: Fx Z-Mix V2 Stretch Noise Example

------------------------------------------------------------------------------------------------------------------------

Z-Mix V2 Object Space
######################

.. image:: _static/_images/fx_layer/fx_z_mix_object_space.webp
    :align: center
    :width: 400
    :alt: Fx Z-Mix V2 Object Space

|


**Object Space** Toggle button, if set to Object Space, the Z-Mix is in object space, so if you move the object, the Z-Mix
will always be in the same position (This is the default) if instead you press the button, you will switch to **Global Space**, so
the height of the Z-Mix will depend on the position of the object in global space.

**This is useful if for example you have more objects with Lo Z-Mix, and you want for example, the vegetation, or the erosion is
always at the same height on all objects.**

**Here is an example of setting Z-Mix in Global Space on multiple objects:**

.. image:: _static/_images/fx_layer/fx_z_mix_global_coordinates_example.webp
    :align: center
    :width: 800
    :alt: Fx Z-Mix V2 Global Coordinates Example

------------------------------------------------------------------------------------------------------------------------

Z-Mix Invert Z
###############

.. image:: _static/_images/fx_layer/fx_z_mix_invert_z.webp
    :align: center
    :width: 400
    :alt: Fx Z-Mix V2 Invert Z

|

**Invert Z** Toggle button, if set to Invert Z, the Z-Mix will be inverted.

**Here 2 images, te first with Invert Z disabled, the second with Invert Z enabled:**

.. image:: _static/_images/fx_layer/fx_z_mix_global_coordinates_example.webp
    :align: center
    :width: 800
    :alt: Fx Z-Mix V2 Global Coordinates Example

.. image:: _static/_images/fx_layer/fx_z_mix_global_coordinates_invert_z_example.webp
    :align: center
    :width: 800
    :alt: Fx Z-Mix V2 Global Coordinates Invert Z Example

------------------------------------------------------------------------------------------------------------------------

Mask map
**********

.. image:: _static/_images/fx_layer/fx_layer_mask_map_texture_manager.webp
    :align: center
    :width: 800
    :alt: Fx Layer Mask Map Texture Manager

|

This button is the **Texture Manager** described here: :ref:`texture_manager_panel` and in this case the texture
of the mask will be selected automatically from the material that is being applied as Fx Layer, as explained here


Exclude Mask
**************

.. image:: _static/_images/fx_layer/fx_layer_exclude_mask.webp
    :align: center
    :width: 800
    :alt: Fx Layer Exclude Mask

|


Exclude Mask Button, excludes the mask completely, so the Fx layer will be homogeneous over the entire surface of the object where
the material containing the Fx Layer is present.

------------------------------------------------------------------------------------------------------------------------

Invert Fx
**********

.. image:: _static/_images/fx_layer/fx_layer_invert_fx.webp
    :align: center
    :width: 800
    :alt: Fx Layer Invert Fx

|

Invert Fx Button inverts the Fx Layer Mask, so where there was black before, now there will be white and vice versa.

.. note::
        This button will not be visible if you activate the **Exclude Mask** button described in the previous paragraph.

------------------------------------------------------------------------------------------------------------------------

From Min From Max
******************

.. image:: _static/_images/fx_layer/fx_layer_from_min_max.webp
    :align: center
    :width: 800
    :alt: Fx Layer From Min From Max

|

Normally this is used to adjust the shading between the base material and the Fx material, so as to have a desired shading.

------------------------------------------------------------------------------------------------------------------------


Show Diffuse
**************

.. image:: _static/_images/fx_layer/fx_layer_show_diffuse.webp
    :align: center
    :width: 800
    :alt: Fx Layer Show Diffuse

|

Questo valore serve se vuoi mostrare il colore del materiale base, in modo da poterlo vedere oppure no.
Se non vuoi vederlo, impostalo su 0.0, quindi il colore sarà gestito dal Base color.


------------------------------------------------------------------------------------------------------------------------

Fx Layer Properties
**********************

.. image:: _static/_images/fx_layer/fx_layer_properties.webp
    :align: center
    :width: 400
    :alt: Fx Layer Properties

|

For all the properties that are highlighted, you already have a complete description of them in the paragraph
**Module Material Panel** all the properties, in fact, are the same, so I will not repeat them, but I refer you to
the paragraph **Module Material Panel** :ref:`module_material_panel`


------------------------------------------------------------------------------------------------------------------------

.. _me_simple_pbr_type:

Material Editor (Simple PBR)
=============================

This is the Material Editor panel when you apply a material with the **Simple PBR** method, to choose to apply
the material with the **Simple PBR** method you have to set the material application method to **Simple PBR** here
described: :ref:`pr_op_material_type`

.. image:: _static/_images/material_editor/me_simple_pbr_type.webp
    :align: center
    :width: 400
    :alt: Material Editor Simple PBR Type

|

This panel will be drawn on the **Simple PBR** node standard of Extreme PBR. The Simple PBR node tree is this:

.. image:: _static/_images/material_editor/me_simple_pbr_node_tree_example.webp
    :align: center
    :width: 800
    :alt: Material Editor Simple PBR Node Tree Example

|

.. important::
        The Simple PBR version is a simplified version of the Nexus version, so it does not have all the properties
        that the Nexus version has, but only the essentials to be able to create and manage the material.
        This type of material (Simple PBR) is much faster to manage, and much faster to render. So
        if you need speed, and you don't need all the properties that the Nexus version has, especially for
        as regards painting, then I recommend using the Simple PBR version.


------------------------------------------------------------------------------------------------------------------------

.. _unrecognized_material:

Unrecognized Material
======================

In this case the material is pink, this means that probably the textures to which the material referred
have been moved or deleted, so the situation, selecting the object with the active material, will be this:

All missing textures will be marked in Red, this allows you to enter the **Texture Manager** panel and try
to search for missing textures, using the **Find Lost Images** button that will in turn open a File Browser where you will have to
enter the path of where you think the Images are (In the best case if you have not deleted such files)

.. image:: _static/_images/material_editor/me_unrecognized_material.webp
    :align: center
    :width: 800
    :alt: Unrecognized Material

|


.. important::
    If you are working on a project and want to share your project with other people, or simply, you are thinking
    once finished deleting your texture images on disk, stop and make sure to Pack everything in the project
    otherwise this situation will arise once the texture images have been deleted from the disk.

    Take a look here to understand how to do it: :ref:`troubleshooting_auto_pack_resources`






