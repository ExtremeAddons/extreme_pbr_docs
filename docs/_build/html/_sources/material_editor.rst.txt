
.. _material_editor:

Material Editor (Nexus)
=========================

.. seealso::

        Here you can find the section dedicated to video tutorials, it may be useful to you: :ref:`vt_material_editor`

The material editor is a very important panel, and it takes many different forms depending on the type of material applied
**Nexus** / **Simple PBR** (Explained here: TODO: Link to the options of the preferences)


Example Material Editor Nexus with 4 Modules for painting:

.. image:: _static/_images/material_editor/material_editor_nexus_four_modules.jpg
    :align: center
    :width: 800
    :alt: Material Editor Nexus Four Modules

|

From this panel you can also access painting and many other features!

------------------------------------------------------------------------------------------------------------------------

Material Nexus type
--------------------


If you are in Nexus mode, or have applied materials that support nexus modules, (Type **Car Paint** or **Water**)
The panel looks like this:


.. image:: _static/_images/material_editor/material_editor_before_add_module.jpg
    :align: center
    :width: 400
    :alt: Material Editor Before Add Module


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
    or you can add via TODO: Link to shader maker for the materials you want to import.

    Add Module will not work with Non Nexus type materials!

------------------------------------------------------------------------------------------------------------------------

Show / Hide Group
-------------------

This button allows you to hide or show all the properties of a group (Nexus Module), it is useful if you are using the
FX Module, it makes the workspace cleaner and allows you to focus only on what you are doing.

.. image:: _static/_images/material_editor/me_show_hide_group_01.png
    :align: center
    :width: 400
    :alt: Material Editor Show Hide Group


------------------------------------------------------------------------------------------------------------------------

Search Module
--------------

.. note::
      Useful only if there are 2 or more modules present in the material.


This button opens a search menu, which allows you to replace / move the modules present in the material.
As soon as you select a module, the module from where you are starting will be replaced with the one you have chosen and vice versa.

.. image:: _static/_images/material_editor/me_search_module.png
    :align: center
    :width: 400
    :alt: Material Editor Search Module


------------------------------------------------------------------------------------------------------------------------

Module Name (Group Name)
-------------------------

From here you can view and also change the name of the group (Nexus Module) you are using.

.. image:: _static/_images/material_editor/me_module_name.png
    :align: center
    :width: 600
    :alt: Module Name

------------------------------------------------------------------------------------------------------------------------

Replace Module
---------------


The Replace Module button allows you to replace the module you are using by loading another module, in accordance with the preview
of the :ref:`material_browser` you have chosen.

.. image:: _static/_images/material_editor/me_replace_module.png
    :align: center
    :width: 400
    :alt: Replace Module

------------------------------------------------------------------------------------------------------------------------

Reset Values
------------

The Reset Values Button allows you to reset the properties of the module you are using to the default values.

.. image:: _static/_images/material_editor/me_reset_values.png
    :align: center
    :width: 600
    :alt: Reset Values

------------------------------------------------------------------------------------------------------------------------

Info
-----

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

Tips
-----

This button allows you to view or hide the hint next to each slider of the module you are using.
so by pressing the hint buttons, you will see a window appear with a description of the parameter you are using.


.. image:: _static/_images/material_editor/me_tips.png
    :align: center
    :width: 600
    :alt: Tips


------------------------------------------------------------------------------------------------------------------------

.. _texture_manager_button:

Texture Manager Button
-----------------------

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
--------------

This color box allows you to choose a color to apply to the diffuse texture, in case there is no texture, this takes the place of the texture as a solid color.

.. note::
        If the texture is present, this color works in accordance with the :ref:`colorize_strength`

.. image:: _static/_images/material_editor/me_diffuse_color.png
    :align: center
    :width: 800
    :alt: Diffuse Color

------------------------------------------------------------------------------------------------------------------------

.. _color_lab_button:

Color Lab Button
------------------


Color Lab Button gives you access to the popup panel for color management, you can find a detailed explanation
here: :ref:`color_lab`


.. image:: _static/_images/material_editor/color_lab_button.jpg
    :align: center
    :width: 800
    :alt: Color Lab Button


------------------------------------------------------------------------------------------------------------------------

.. _colorize_strength:

Colorize Strength
------------------

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
----------------

By activating this button, 2 new sliders will appear, the first allows you to choose the color to be sampled, the second
is the **Tolerance** which allows you to choose how much the sampled color must be similar to the original color to be
replaced.

So in accordance with these settings, now the colorization will only color the parts that have the color similar to that.

.. image:: _static/_images/material_editor/me_colorize_sample.webp
    :align: center
    :width: 800
    :alt: Colorize Sample


------------------------------------------------------------------------------------------------------------------------

Emission
---------

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

Transparent
------------

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

Transparent Mode
*****************

This button actually manages the **Blend Mode** and **Shadow Mode** of the material

.. image:: _static/_images/material_editor/blend_mode_shadow_mode.webp
    :align: center
    :width: 400
    :alt: Blend Mode Shadow Mode

Settings only for Eevee Render:

- **Is Opaque:** Blend Mode: Opaque, Shadow Mode: Opaque
- **Is Blend:** Blend Mode: Alpha Blend, Shadow Mode: Alpha Ashed
- **Is Hashed** Blend Mode: Alpha Hashed, Shadow Mode: Alpha Hashed (The best, but requires more rendering samples to get a good result)
- **Is Clip** Blend Mode: Alpha Clip, Shadow Mode: Alpha Clip

------------------------------------------------------------------------------------------------------------------------

Subsurface/Radius
------------------

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
------------------

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
---------

.. image:: _static/_images/material_editor/me_metallic.webp
    :align: center
    :width: 400
    :alt: Metallic

|

This slider allows you to adjust the Metallic of the material, if a Metallic map is present, if it is not present
then this slider will adjust the general metallic of the material, the whole material in this case will be metallic
depending on the set value, a metallic value of 1.0 and a Roughness of 0.0, will render the material as a
shiny metal, while a metallic value of 0.0 and a Roughness of 1.0 will render the material as a non-metallic material


.. hint::
        On a completely black material, setting the Metallic will have no effect, as the black color
        does not reflect light, so no effect will be seen, to see the effect of the Metallic, it is necessary
        set a color other than black, even if it is a very dark color, in this way you will see the effect of the Metallic.
        In short, everything except total black 😊



















































