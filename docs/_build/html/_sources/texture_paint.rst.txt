
.. _texture_paint:

Texture Paint
================


.. note::
        In order to access the painting you will have to be in Nexus mode TODO: put link to nexus mode preferences
        and you will have to have added a material with the :ref:`add_module` button



.. image:: _static/_images/texture_paint/tp_hand.webp
    :align: center
    :width: 400
    :alt: Texture Paint Hand

This section is dedicated to texture paint and its tools.

.. admonition:: Video Tutorial
    :class: youtube

    Here a video tutorial of texture paint: :ref:`texture_paint_video_tutorial`

------------------------------------------------------------------------------------------------------------------------

Introduction to Texture Paint
---------------------------------

The texture paint is based on a system designed in 2020, this system is based on the painting of a mask, it decides based
on the painted color (The color is not visible because it is a mask) which Module (Material) must be visible in the colored areas.

The painting is based on 4 colors: **Red**, **Green**, **Blue** and **Black**.

This combination, allows you to paint up to 4 material slots, but it is not to be confused with direct painting on an image.
In fact, as mentioned previously, the painting is based on a mask, so it is the mask that is actually painted, and consequently
the materials are displayed based on the mask.

**Here an example of how the color that acts as a mask:**

.. |cube_paint_rgb| image:: _static/_images/texture_paint/tp_painted_cube_rgb_01.webp
                        :width: 400
                        :alt: Texture Paint RGB


.. |cube_paint| image:: _static/_images/texture_paint/tp_painted_cube_01.webp
                    :width: 400
                    :alt: Texture Paint Black


+-------------------+-------------------+
| |cube_paint_rgb|  | |cube_paint|      |
+-------------------+-------------------+

------------------------------------------------------------------------------------------------------------------------

Add material to paint
*******************************

In order to add a material to paint, it is necessary that the material on which you want to paint has been applied with
Extreme PBR in Nexus mode, to do this check the preferences: TODO: put link to nexus mode preferences.

To add a material to paint, refer to this button :ref:`add_module`

------------------------------------------------------------------------------------------------------------------------

Texture Paint Editor
---------------------------------

Here an example of how the texture paint looks like between 3 modules:

.. image:: _static/_images/texture_paint/tp_three_modules_panel.webp
    :width: 800
    :align: center
    :alt: Texture Paint Three Modules

------------------------------------------------------------------------------------------------------------------------

Show Paint Editor
*******************************

.. image:: _static/_images/texture_paint/tp_show_paint_editor.webp
    :width: 800
    :align: center
    :alt: Texture Paint Show Paint Editor

|


The Show Paint Editor button allows you to hide or show the texture paint editor. Useful if you are working on the material and
you want to keep a more compact interface.

------------------------------------------------------------------------------------------------------------------------

.. _tp_texture_paint_tools_button:

Texture Paint Tools Button
*******************************

.. image:: _static/_images/texture_paint/tp_paint_tools_button.webp
    :width: 600
    :align: center
    :alt: Texture Paint Tools Button

|

The texture paint button, allows you to access the Paint Tools panel, which allows you to access the properties of the brush
if you are not very familiar with the classic blender tools. Here the chapter dedicated to :ref:`paint_tools_panel`

------------------------------------------------------------------------------------------------------------------------

Re-Project
*******************************

.. image:: _static/_images/texture_paint/tp_re_project.webp
    :width: 600
    :align: center
    :alt: Texture Paint Re-Project

|

Re-Project Button, allows you to re-project the texture of the painting, in order to fix it. The important use cases

- The texture on the object has anomalies near the edges.
- When you modify an object in its shape and geometry, the texture does not adapt to the new shape, so it is necessary
  re-project the texture.

.. note::
        This button appears only when you are in Paint mode

------------------------------------------------------------------------------------------------------------------------


Paint Module Button
*******************************

.. image:: _static/_images/texture_paint/tp_paint_module.webp
    :width: 600
    :align: center
    :alt: Texture Paint Paint Module

|

These buttons allow you to start or stop painting, and also allow you to select the module to paint.
Once the button is pressed, the mouse cursor will become a brush, and you can start painting on the selected object.

Once the painting session is finished, you can press the button again to finish the painting, in fact
the button in painting mode, will now take on the task **Stop Paint**.

.. important::
        In order to be sure not to encounter confusion, make sure you are working on the selected object and active object.

------------------------------------------------------------------------------------------------------------------------

Fill Module
*******************************

.. image:: _static/_images/texture_paint/tp_fill_module.webp
    :width: 600
    :align: center
    :alt: Texture Paint Fill Module

|

These Buttons allow you to fill the material with the reference module. So if for example you have painted the model,
with this button you will return to having a single material, based on which button of which module you have decided to do a Fill.


















