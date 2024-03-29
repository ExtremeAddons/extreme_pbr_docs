
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

.. image:: _static/_images/material_editor/material_editor_before_add_module.webp
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

.. tip::
        **Only from Extreme PBR Nexus version 4.1.120**

        - Press **Shift** before clicking the button in order to use it exactly as Shader Maker described here: :ref:`shader_maker`
          in order to import your own textures and create your own material.

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


.. tip::
        From Extreme PBR Nexus version 4.1.120, you can use the following shortcuts:

        - Hold **Shift** while pressing this button, and all the modules on this row will be hidden or shown
          together with this module.
        - Hold **Ctrl** while pressing this button, and all the modules and Fxs will be hidden or shown
          together with this module.


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

.. tip::
        **Only from Extreme PBR Nexus version 4.1.120**

        - If you are replacing for example the Asphalt 001 1k Material with Asphalt 001 2k, Extreme PBR recognizes that the material is the same
          and only replaces the textures inside it, keeping the values of the Material Editor settings unchanged.

        - Press **Shift** before clicking the button in order to use it exactly as Shader Maker described here: :ref:`shader_maker`
          in order to import your own textures and create your own material.


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

.. _node_group_popover:

Node Group Popover
*******************

.. image:: _static/_images/material_editor/ng_popover_01.webp
    :align: center
    :width: 600
    :alt: Node Group Popover

|


Use Sockets
############

.. note::
        Not all Nexus Modules will have these options available, all modules created as textures based materials
        will have these options available, procedural ones will not necessarily have them

|


Form this section you can activate and deactivate the sockets to save resources and space in the interface.

**SUBSURFACE**, **TRANSMISSION**, **COAT**, **SHEEN**, **EMISSION**

When you add a Texture type material in Nexus mode, these values are managed intelligently, based on which textures
are in the material and some input values of the group node, so you won't have to worry too much about this.


- **Example 1**

    All values are disabled, the links connected to the BSDF are limited to the basic ones necessary, the interface in
    **Material Editor** panel remains more compact as it will not show the inputs that refer to those values.

.. image:: _static/_images/material_editor/use_sockets_all_off_01.webp
    :align: center
    :width: 800
    :alt: Use Sockets All Off 01

|

- **Example 2**

    All values are enabled, all links that refer to the sockets are connected to the BSDF, the interface in
    **Material Editor** panel will be larger as it will show all the inputs that refer to those values.

.. image:: _static/_images/material_editor/use_sockets_all_on_01.webp
    :align: center
    :width: 800
    :alt: Use Sockets All On 01



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



.. tip::
        In order to activate the emission of a material that is not emissive by Default, make sure to activate the **Emission** button from the
        :ref:`node_group_popover` menu and check "Emission"

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

Subsurface
************

.. tip::
        In order to activate the Subsurface of a material that is not Subsurface by Default, make sure to activate the **Subsurface** button from the
        :ref:`node_group_popover` menu and check "Subsurface"

.. image:: _static/_images/material_editor/me_subsurface_01.webp
    :align: center
    :width: 600
    :alt: Subsurface

|

These values allow you to adjust the Subsurface Scattering of the material.
Subsurface Scattering is the ability of a material to let light pass through it, but not transparently,
but in a diffuse way, as if the light were diffused inside the material, this is very useful for materials
like skin, leaves, ears, rubber, plastic, etc.

**Subsurface Method:**

Rendering method to simulate subsurface scattering.

.. image:: _static/_images/material_editor/me_subsurface_method.webp
    :align: center
    :width: 600
    :alt: Subsurface Method

|

.. note::
        EEVEE does not support the Random Walk methods.

- **Christensen-Burley**

    An approximation to physically-based volume scattering. This method is less accurate than Random Walk however,
    in some situations this method will resolve noise faster.


- **Random Walk (Fixed Radius)**

    Provides accurate results for thin and curved objects. Random Walk uses true volumetric scattering inside the
    mesh, which means that it works best for closed meshes. Overlapping faces and holes in the mesh can cause problems.


- **Random Walk**

    Behaves similarly to Random Walk (Fixed Radius) but modulates the Radius based on the Color, Anisotropy, and IOR.
    This method thereby attempts to retain greater surface detail and color than Random Walk (Fixed Radius).


**Subsurface Radius:**

.. image:: _static/_images/material_editor/me_subsurface_radius.webp
    :align: center
    :width: 600
    :alt: Subsurface Radius

|

.. important::

    In order to work into Eevee Engine, you need to Activate the **Translucency** button on the right of the **Subsurface** button

    .. image:: _static/_images/material_editor/me_translucency.webp
        :align: center
        :width: 600
        :alt: Translucency


**Subsurface Strength:**

The strength of the subsurface scattering effect, questo valore da Blender 4.0 Controlla anche il valore "Scale" del nuovo
Principle BSDF, qualsiasi valore Superiore a 0 Attiva il Subsurface Weight e i valori vanno da 0-10 Espressi in unità di
misura del progetto.

.. image:: _static/_images/material_editor/me_subsurface_strength.webp
    :align: center
    :width: 600
    :alt: Subsurface Strength

|

**Sss IOR: (Cycles Only)**

Index of refraction for Subsurface Scattering. (Available only in Random Walk (Skin) mode)

.. image:: _static/_images/material_editor/me_subsurface_ior.webp
    :align: center
    :width: 600
    :alt: Subsurface IOR

|

**Sss Anisotropy: (Cycles Only)**

Controls the directionality of subsurface scattering. (Available only in Random Walk modes)

.. image:: _static/_images/material_editor/me_subsurface_anisotropy.webp
    :align: center
    :width: 600
    :alt: Subsurface Anisotropy


|


**Example of Subsurface Scattering with a light behind the object:**

.. image:: _static/_images/material_editor/subsurface_suzanne.jpg
    :align: center
    :width: 600
    :alt: Subsurface Example


------------------------------------------------------------------------------------------------------------------------

Ambient Occlusion
******************

.. image:: _static/_images/material_editor/me_ambient_occlusion.webp
    :align: center
    :width: 600
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
    :width: 600
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
    :width: 600
    :alt: Specular Tint

|

This 2 properties work in symbiosis:


.. _me_specular:

Specular
#########

This slider adjusts the specular of the material, if a specular map is present, then this slider will only adjust
some areas of the material, while if it is not present, then it will adjust the general specular of the material.


.. _me_specular_tint:

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
    :width: 600
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

.. tip::
        In order to activate the Sheen of a material that is not Sheen by Default, make sure to activate the **Sheen** button from the
        :ref:`node_group_popover` menu and check "Sheen"

.. image:: _static/_images/material_editor/me_sheen_and_tint.webp
    :align: center
    :width: 600
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

Sheen Roughness
################

This slider allows you to adjust the roughness of the sheen, the higher the value, the less the sheen will be visible,
the lower the value, the more the sheen will be visible.

.. image:: _static/_images/material_editor/me_sheen_roughness.webp
    :align: center
    :width: 600
    :alt: Sheen Roughness

------------------------------------------------------------------------------------------------------------------------

Clearcoat / Roughness
**********************

.. image:: _static/_images/material_editor/me_clearcoat.webp
    :align: center
    :width: 600
    :alt: Clearcoat and Roughness

|

Coat
##########

The clearcoat is a layer of varnish that is applied to the material, it is a layer that is applied on top of the material,
this is similar to the clearcoat of a car.

Coat Roughness
###################

In accordance with the clearcoat, this slider allows you to adjust the roughness of the clearcoat.


Coat Tint
############

This is similar to Specular Tint, but it is applied to the coat :ref:`me_specular_tint`
Is used to use the tint of the diffuse color on the coat.

**Example, First Image Clearcoat 0.0, Second Image Clearcoat 1.0 and Roughness 0.0, Third Image Clearcoat 1.0 and Roughness 0.25**

.. image:: _static/_images/material_editor/me_clearcoat_example.webp
    :align: center
    :width: 800
    :alt: Clearcoat Example

|

Coat IOR
##########

.. note::
        Only Available from Blender 4.0

.. image:: _static/_images/material_editor/me_coat_ior.webp
    :align: center
    :width: 600
    :alt: Coat IOR




------------------------------------------------------------------------------------------------------------------------

Transmission
*************

.. image:: _static/_images/material_editor/me_transmission_section.webp
    :align: center
    :width: 600
    :alt: Transmission

|

The transmission is the ability of a material to let light pass through it, this is very useful for materials
like glass, water etc.

This property works in symbiosis with the **IOR** and **Transmission Roughness** properties

The value of the transmission is a value between 0.0 and 1.0, where 0.0 means no transmission, while 1.0
means maximum transmission (To simulate a normal glass it will have 1.0 of transmission)

Ray Tracer Button
##################

.. image:: _static/_images/material_editor/me_raytracer_button.webp
    :align: center
    :width: 600
    :alt: Raytracer Button

|

The button Raytracer, activate or deactivate, the Screen Space Refractions (For the Glass). Eevee only, in Cycles, this is not necessary,
in Eevee Render it is really necessary to activate it if you want to get a realistic result even if not perfect.

This button activates or deactivates the **Screen Space Refractions** in the material properties and deactivates the property
**Subsurface Translucent** if it is active, otherwise they will go into contrast (This is only necessary for the
Eevee rendering engine, it is not necessary in Cycles)


IOR
*****

The IOR is the index of refraction, it is a value that is used to calculate the refraction of the material.
For example the IOR of the glass is 1.45, the IOR of the water is 1.33, the IOR of the diamond is 2.42 etc...

.. note::
        Form Blender 4.0 the IOR also regulates the specular ior so the reflections will adapt to the value set here.

.. image:: _static/_images/material_editor/me_ior.webp
    :align: center
    :width: 600
    :alt: IOR

|

Transmission Roughness (Deprecated into Blender 4.0)
#####################################################

This slider allows you to adjust the roughness of the transmission. The transmission Roughness will make the material
more or less transparent, the higher the value, the less transparent the material will be, the lower the value, the more transparent
the material will be.

------------------------------------------------------------------------------------------------------------------------

Normal
*******

.. image:: _static/_images/material_editor/me_normal.webp
    :align: center
    :width: 600
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

.. important::
        Bump / Distance adjust the Microdisplacement in Cycles render in Microdisplacement Mode: :ref:`microdisplacement`

.. image:: _static/_images/material_editor/me_bump_and_distance.webp
    :align: center
    :width: 600
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
    :width: 600
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
    :width: 600
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
    :width: 600
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
    :width: 600
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
    :width: 600
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
    :width: 600
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

.. _use_anti_tile:

Use Anti Tile
--------------

This checkbox will activate the anti-tile, the anti tile is useful on Materials such as Terrain and Vegetation, to avoid
that the repetition of the texture is noticed.

..

.. admonition:: Video Tutorial
    :class: youtube

        Here you can find a video tutorial on how to use the Anti Tile: :ref:`vt_anti_tile`



.. image:: _static/_images/anti_tile/anti_tile_checkbox_01.webp
    :align: center
    :width: 600
    :alt: Anti Tile Checkbox 01

|

.. note::
        The anti tile will only have effect on materials based on Texture Images, it will not have effect on procedural materials
        as the latter do not need anti tile.



.. image:: _static/_images/anti_tile/anti_tile_cover.webp
    :align: center
    :width: 600
    :alt: Anti Tile Cover

|

Organic Anti tile Panel
###########################

The access to the anti-tile panel is possible only if the **Use Anti Tile** checkbox is active, otherwise the panel
will not be visible.

.. image:: _static/_images/anti_tile/organic_anti_tile_v1.webp
    :align: center
    :width: 400
    :alt: Organic Anti Tile V1

|

- **Blend Scale**
        Adjusts the scale of the blend between tiles, the higher the value the finer the noise will be, the lower the value the larger the noise will be.

- **Edge Wobble**
        Adjusts the amount of wobble on the edges, the higher the value the more wobble will be present, the lower the value the more wobble will be absent.
        This makes it possible to make the edge between the tiles less linear.

- **Edge Blend**
        Adjusts the amount of blend on the edges, the higher the value the more blend will be present, the lower the value the more blend will be absent.
        This makes it possible to make the edge between the tiles less linear.

- **Seed**
        By changing the value, the seed will be changed, so you will change the randomness of the pattern.

- **Expand Seam**
        This value is used to expand (enlarge) the randomly generated tiles, useful for further adjusting the pattern, in case
        that the texture is not seamless.

- **Hue Min**
        This minimum value to which the color can be moved, if the value is 0.5, the color will not change.

- **Hue Max**
        This maximum value to which the color can be moved, if the value is 0.5, the color will not change.

- **Exposure Min**
        This minimum value to which the exposure can be moved, if the value is 0.0 the exposure is neutral.

- **Exposure Max**
        This maximum value to which the exposure can be moved, if the value is 0.0 the exposure is neutral.

- **Color Var Scale**
        This adjusts the size of the size of the patches based on the HUE and EXPOSURE adjustment. A high value
        corresponds to a larger size. If 0 The value coincides with the random tiling generated
        by the anti-tile.

- **Is Voronoi - Is Noise**
        This button allows you to change the algorithm that controls only HUE and EXPOSURE.

- **Random Rotation**
        This button (Which is always active by default) allows you to randomly rotate the tiles if active, if instead
        is disabled, the original texture will not be randomly rotated.

- **Hide Anti Tile**
        If active, it hides the anti-tile effect without deactivating it, this is useful for seeing the original texture
        without anti-tile effect vs the texture with anti-tile effect.









------------------------------------------------------------------------------------------------------------------------

.. _me_projection_settings:

Projection Settings
--------------------

This Menu is present in all Nexus and Non Nexus Type materials, and is used to set the **Coordinates**, **Projection** and **Normal Space Map**

.. image:: _static/_images/material_editor/me_projection_settings.webp
    :align: center
    :width: 600
    :alt: Projection Settings

|

Coordinate
**********

The coordinates (If present in the menu) refer to the Coordinate node preset in the modules or materials of Extreme PBR,
even materials created with the Shader Maker have this menu.

.. image:: _static/_images/material_editor/ps_coordinate.webp
    :align: center
    :width: 600
    :alt: Coordinate

|


The **Coordinate** property is based on the outputs sockets present on the node tagged as COORDINATE in the Extreme PBR system
this allows based on the sockets present in the output node to show in the list all the possible sockets to link to the
next node, here is the example of the Coordinate node:


.. image:: _static/_images/material_editor/ps_coordinate_sockets_example.webp
    :align: center
    :width: 400
    :alt: Coordinate Node Sockets Example

|

Projection
*************


The **Projection** property (If present) allows you to set on all Texture Image nodes present in the material
and to change their Projection property in one go

.. image:: _static/_images/material_editor/ps_projection_type.webp
    :align: center
    :width: 600
    :alt: Projection Type

|

As explained above, this property sets the projection type on all nodes (Only those tagged by Extreme PBR) so if you are mixing
more modules, each module will have its own type of projection. Here is the example in the node:

.. image:: _static/_images/material_editor/ps_tex_image_node_projection_example.webp
    :align: center
    :width: 600
    :alt: Tex Image Node Projection Example

|

Bellow the corresponding example of a **Flat**, **Box**, **Sphere** and **Tube** (Cylinder) mapping.

(Into image UV as Flat)

.. image:: _static/_images/mapping_editor/mapping_types_example_01.jpg
    :align: center
    :width: 800
    :alt: UV Mapping Type


|

Box Blend
***********

In this mode, the addon sets the nodes with image textures (if present) in Box mode. In addition, the Blend slider
allows you to control the corresponding Blend values of the image texture nodes.

Here the Material nodes in Box Mode:

.. image:: _static/_images/material_editor/box_blend_example.webp
    :align: center
    :width: 800
    :alt: Box Blend Example


|


Normal Map Space
******************

Tangent, Object and World space. Tangent space normal maps are the most common, as they support object transformation
and mesh deformations. Object space normal maps keep sticking to the surface under object transformations, while World
normal maps do not.

This property is exactly the one exposed in the Blender Normal Map node, this makes it accessible directly
from the Extreme PBR panel, without having to open the material node tree:

.. image:: _static/_images/material_editor/ps_normal_map_node_example.webp
    :align: center
    :width: 600
    :alt: Normal Map Node Example


------------------------------------------------------------------------------------------------------------------------

Convert Module System
----------------------

Convert the modular system of Extreme PBR between Blender versions to maintain system compatibility.

(From Extreme PBR version 4.1.110 Only)

This button will be displayed if the Extreme PBR material was created inside a version of Blender prior to 4.0 or vice versa,
if it was created in a version 4.0 and you are opening in Blender 3.6.



.. image:: _static/_images/material_editor/me_convert_module_system_button.webp
    :align: center
    :width: 600
    :alt: Convert Module System

|

This appears because the Principled BSDF nodes of Blender, sometimes they are Modernized and improved as in the case of the passage
from Blender 3.6 to Blender 4.0 where the Principled BSDF node has different inputs, with different names and slightly different functions.

In addition in Blender 4.0 with Extreme PBR 4.1.110 or higher, the Module node is connected directly to the Principled BSDF node
without going through the Extreme PBR Mixer, this to improve performance and compatibility with Blender 4.0

Here is an example on the left of a Material created in blender 3.6 and on the right the material converted in Blender 4.0


.. image:: _static/_images/material_editor/nexus_module_conversion_nodes_example.webp
    :align: center
    :width: 800
    :alt: Nexus Module Conversion Nodes Example


------------------------------------------------------------------------------------------------------------------------

.. _add_fx_layer:

Add Fx Layer
-------------

.. image:: _static/_images/material_editor/me_add_fx_layer.webp
    :align: center
    :width: 400
    :alt: Add Fx Layer

|

.. tip::
        **Only from Extreme PBR Nexus version 4.1.120**

        - Press **Shift** before clicking the button in order to use it exactly as Shader Maker described here: :ref:`shader_maker`
          in order to import your own textures and create your own material.

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




.. image:: _static/_images/material_editor/fx_layer_panel_01.webp
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


This panel will be the same even for materials not coming from Extreme PBR, the same interface has been chosen
that adopts blender.

.. note::
        As for the microdisplacement it will be manageable from this panel in this mode the interface will appear
        of the Displace node, if in fact a displacement of type "Microdisplacement" has been applied.

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


Convert to Nexus
-----------------


This button when present, allows you to try to convert the material into a Nexus type material, this is useful if you
want to paint or add an Extreme PBR material on top of this material, since the Nexus type materials have been studied
on purpose.

.. note::
        This converter only works if the contextual material is of type **Simple PBR** or any material as long as it contains
        the textures with standard nomenclature, see here the standard nomenclature: :ref:`texture_nomenclature`



.. image:: _static/_images/material_editor/me_convert_to_nexus_button.webp
    :align: center
    :width: 400
    :alt: Material Editor Convert To Nexus Button




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


------------------------------------------------------------------------------------------------------------------------

.. _






