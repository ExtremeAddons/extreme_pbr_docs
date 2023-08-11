.. _shader_overlay:

Shader Overlay
==================

.. admonition:: Video Tutorial
    :class: youtube

    Here you can find a video tutorial that shows you how to use Shader Overlay: :ref:`shader_overlay_video_tutorial`


Shader overlay is a very useful tool to mix all selected objects (If they have any base material)
with a material of your choice from the Extreme PBR library or even importing a material via Shader Maker, you can find
the Shader Maker You can find the Shader Maker chapter here: :ref:`shader_maker`


Shader Overlay allows you to make animations of the Overlay material through the mixer, so that you can see the coverage of the materials
underlying in an animated way.


Here an example in 3 separate moments of a scene where the Shader Overlay has been applied to all objects:

**Model Without Shader Overlay:**

.. image:: _static/_images/shader_overlay/mars_one_scene_01.webp
    :align: center
    :width: 800
    :alt: Shader Overlay Example 01

|

**Model with shader overlay adjusted about halfway through the field with tilt:**

.. image:: _static/_images/shader_overlay/mars_one_scene_02.webp
    :align: center
    :width: 800
    :alt: Shader Overlay Example 02

|

**Model completely covered by the shader overlay:**

.. image:: _static/_images/shader_overlay/mars_one_scene_03.webp
    :align: center
    :width: 800
    :alt: Shader Overlay Example 03

|

.. admonition:: Credits CC-BY
    :class: credits

    Model: **"Mars One" Mission - Base** by **admone** from Sketchfab:
    `Link <https://sketchfab.com/3d-models/mars-one-mission-base-83ced347037f47aba8473147d65df074>`_


------------------------------------------------------------------------------------------------------------------------

Shader Overlay Panel
----------------------

Here's what it looks like the Shader Overlay panel looks in the fullness of its functionality, in the example the
Procedural material **Blueprint 002** has been applied so you will see the sliders to control the parameters of the
material mentioned.

.. image:: _static/_images/shader_overlay/shader_overlay_panel_full.webp
    :align: center
    :width: 400
    :alt: Shader Overlay Panel

------------------------------------------------------------------------------------------------------------------------

Add From Library
~~~~~~~~~~~~~~~~~~

.. image:: _static/_images/shader_overlay/so_add_from.webp
    :align: center
    :width: 600
    :alt: Shader Overlay Add From

|

In this situation, no shader overlay has been applied. **Add From** is used to choose where you want to take the
material to apply as a shader overlay.

Add From Library allows you to add the shader overlay directly from the Extreme PBR library, just select
the material you want to apply, from the Extreme PBR library then from the :ref:`material_browser` , and press the button
**Add**, explained later here: :ref:`so_add`

------------------------------------------------------------------------------------------------------------------------

Add from Data Material
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: _static/_images/shader_overlay/so_add_from_data_material.webp
    :align: center
    :width: 600
    :alt: Shader Overlay Add From Data Material

|

By selecting **Add From Data Material** you will have the list of materials present in the current Blender project
and you can choose the material you want to apply as Shader Overlay from that list. Once you have selected the material
you want to apply, press the **Add** button, explained later here: :ref:`so_add`


------------------------------------------------------------------------------------------------------------------------

Mixer Node
~~~~~~~~~~~~~~~~~~

.. image:: _static/_images/shader_overlay/so_mixer_node.webp
    :align: center
    :width: 600
    :alt: Shader Overlay Mixer Node

|

From the Mixer Node menu you can choose the type of Node you want to use to mix the Shader Overlay with the underlying one.
the nodes will allow you to adjust the settings.

The nodes available are described below:

- **Shader Gradient** :ref:`so_shader_gradient`
- **Shader Gradient Glitch V2** :ref:`so_shader_gradient_glitch_v2`

------------------------------------------------------------------------------------------------------------------------

Replace Mixer Node
*********************

Once you have added the Shader Overlay, you can change the type of Node to use for the Mixer, by clicking on the button
Replace Mixer:

.. image:: _static/_images/shader_overlay/so_replace_mixer_node.webp
    :align: center
    :width: 400
    :alt: Shader Overlay Replace Mixer Node

------------------------------------------------------------------------------------------------------------------------


.. _so_add:

Add
~~~~~~~

.. image:: _static/_images/shader_overlay/so_add.webp
    :align: center
    :width: 600
    :alt: Shader Overlay Add

|

The Add button adds to the selected objects the Shader Overlay that you have chosen from the **Add From** menu.
If the Shader Overlay is already present on the selected objects, the Add button replace the previous Shader Overlay
with the new one.

.. important::
        This button adds to all the materials of the selected objects the material chosen as Shader Overlay,
        so if you have selected 10 objects and each of these has 3 materials, the material chosen as Shader Overlay
        will be added to all 30 materials.


------------------------------------------------------------------------------------------------------------------------

.. _so_remove:

Remove
~~~~~~~~~

.. image:: _static/_images/shader_overlay/so_remove.webp
    :align: center
    :width: 600
    :alt: Shader Overlay Remove

|

The Remove button removes the Shader Overlay from the selected objects.

.. important::
        This button removes the Shader Overlay from all the materials of the selected objects,
        so if you have selected 10 objects and each of these has 3 materials, the Shader Overlay
        will be removed from all 30 materials.


------------------------------------------------------------------------------------------------------------------------

.. _so_shader_gradient:

Shader Gradient
~~~~~~~~~~~~~~~~~~

.. image:: _static/_images/shader_overlay/so_shader_gradient.webp
    :align: center
    :width: 600
    :alt: Shader Overlay Shader Gradient

|

The Shader Gradient Mixer Node allows you to mix the material with a detachment effect with the underlying material/s.

------------------------------------------------------------------------------------------------------------------------

Reset Values
****************

.. image:: _static/_images/shader_overlay/so_mg_reset_values.webp
    :align: center
    :width: 600
    :alt: Shader Overlay Reset Values

|

This button resets all the values of the Mixer Node to the Default state.

------------------------------------------------------------------------------------------------------------------------

Tips
********

.. image:: _static/_images/shader_overlay/so_mg_tips.webp
    :align: center
    :width: 600
    :alt: Shader Overlay Tips

|

This button will show the Tips related to the properties of the Mixer Node, additional buttons will be shown that
once clicked, will show a popup window with the description of the selected property.

In order to hide, press the Tips button again.

------------------------------------------------------------------------------------------------------------------------

Location
************

.. image:: _static/_images/shader_overlay/so_mg_location_flip_location.webp
    :align: center
    :width: 600
    :alt: Shader Overlay Location

|

Location, allows you to adjust the position of the Shader Overlay material relative to the underlying material.

Flip Location
****************

If you activate the Flip Location, the position of the Shader Overlay material is inverted with respect to the set position.

------------------------------------------------------------------------------------------------------------------------

Rotation X/Y
**************

.. image:: _static/_images/shader_overlay/so_mg_rotation_xy.webp
    :align: center
    :width: 600
    :alt: Shader Overlay Rotation X/Y

|

These 2 sliders allow you to rotate the detachment of the Shader Overlay material with respect to the underlying material.
This allows you to tilt the Shader Overlay material, so that you can create animations of coverage or
discovery of the underlying material, with various animations.

------------------------------------------------------------------------------------------------------------------------

From Min/Max
****************

.. image:: _static/_images/shader_overlay/so_mg_from_min_max.webp
    :align: center
    :width: 600
    :alt: Shader Overlay From Min/Max

|

These 2 sliders allow you to adjust and therefore fade less the detachment of the Shader Overlay material with respect
to the underlying material.

------------------------------------------------------------------------------------------------------------------------

Strength
************

.. image:: _static/_images/shader_overlay/so_mg_strength.webp
    :align: center
    :width: 600
    :alt: Shader Overlay Strength

|

Strength Slider property allows you to modify the strength of the Shader Overlay material above the underlying material,

- By default the value is 0.0, so it is a basic right blend.
- If you set -1.0 the Shader Overlay material will be completely disappeared.
- If you set 1.0 the Shader Overlay material will be completely visible on the entire underlying material
  (It will be completely covered excluding the Location value).

------------------------------------------------------------------------------------------------------------------------

.. _so_shader_gradient_glitch_v2:

Shader Gradient Glitch V2
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: _static/_images/shader_overlay/so_shader_gradient_glitch_v2.webp
    :align: center
    :width: 600
    :alt: Shader Overlay Shader Gradient Glitch V2















