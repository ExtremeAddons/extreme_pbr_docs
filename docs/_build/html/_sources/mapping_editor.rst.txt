
.. _mapping_editor_panel:

Mapping Editor
================

.. note::
    In order to access the **Mapping Editor** panel you must be in the **Main Panel** and press the button with the symbol
    of the Texture. Here the **Main Panel** section: :ref:`mapping_editor_button`

    .. image:: _static/_images/main_panel/mapping_editor_button_01.png
        :align: center
        :width: 400
        :alt: Mapping Editor Button 01

Mapping editor is a tool to manipulate UV mapping without necessarily having to use the Blender UV editor.
This tool was built to **Scale**, **Move** and **Rotate** UV maps on the fly without having to enter
in the UV editor. Clearly it is not a substitute for the UV editor, but it contains the most used functions, especially in the field
of architecture.

.. image:: _static/_images/mapping_editor/mapping_editor_panel.jpg
    :align: center
    :width: 800
    :alt: Mapping Editor Panel

|

.. important::
        This tool has nothing to do with **Scale** **Rotate** or **Location** of the material, this tool is
        able to translate the UV coordinates present on the object. This is necessary especially if you are using the displacement
        in **Modifier** mode to also move the displacement coordinates. The displacement section can be found here: TODO: Put link to the displacement section

------------------------------------------------------------------------------------------------------------------------

Brief introduction
--------------------

There are two ways in which you can manipulate mapping:

In this example a texture is placed into the Square Texture space (left), an UV Map of the object lays on top (Center)
and a correspondence is set between faces of the object and colors of the texture (right)

.. image:: _static/_images/mapping_editor/uv_mapping_example_01.jpg
    :align: center
    :width: 800
    :alt: UV Mapping Example 01

|

.. _mapping_method_01:

Method 01
************

The first method is to move, rotate and scale the Map, so to vary the correspondence between Texture space and Map.

.. image:: _static/_images/mapping_editor/uv_mapping_example_02.jpg
    :align: center
    :width: 800
    :alt: UV Mapping Example 02

|


Method 02
************

The second method is to move, rotate and scale the Texture: so to vary the correspondence between Texture image and Texture space.

.. image:: _static/_images/mapping_editor/uv_mapping_example_03.jpg
    :align: center
    :width: 800
    :alt: UV Mapping Example 03

|

Using the Mapping Editor lets you use the :ref:`mapping_method_01`: **manipulating the correspondence between Texture space and Map**


------------------------------------------------------------------------------------------------------------------------

.. _me_uv_mapping_type:

UV Mapping Type
----------------

.. image:: _static/_images/mapping_editor/uv_mapping_type.jpg
    :align: center
    :width: 400
    :alt: UV Mapping Type

|

This selector allows you to choose the type of Mapping you want to use on the selected active object.

Bellow the corresponding example of a **UV**, **Box**, **Sphere** and **Tube** (Cylinder) mapping.

.. image:: _static/_images/mapping_editor/mapping_types_example_01.jpg
    :align: center
    :width: 800
    :alt: UV Mapping Type


------------------------------------------------------------------------------------------------------------------------

Reset All Parameter
---------------------

.. image:: _static/_images/mapping_editor/reset_all_parameter_01.jpg
    :align: center
    :width: 400
    :alt: Reset All Parameter 01

|

It resets all the mapping parameters, bringing them back to the default values, but only in the panel, it will have no effect
on the object.

------------------------------------------------------------------------------------------------------------------------

Select Face
------------

.. image:: _static/_images/mapping_editor/select_face_01.jpg
    :align: center
    :width: 400
    :alt: Select Face 01

|

Select the face / faces of the active object, based on the material selected in the material list. Here the section on
material list: :ref:`material_list`

------------------------------------------------------------------------------------------------------------------------

Lock X/Y
----------

.. image:: _static/_images/mapping_editor/lock_x_y_01.jpg
    :align: center
    :width: 400
    :alt: Lock x y 01

|


If the checkbox on one of the two axes is active, it will lock the scale of the corresponding axis, so you can
scale only along the other axis during the UVS Size operation described below

------------------------------------------------------------------------------------------------------------------------

UVS Size
----------

.. image:: _static/_images/mapping_editor/uv_size_01.jpg
    :align: center
    :width: 400
    :alt: UV Size 01

|

This resizes the UV map, if you increase the value, the UV map enlarges, if you decrease the value, the UV map decreases.

------------------------------------------------------------------------------------------------------------------------

UVs Pos X/Y
------------

.. image:: _static/_images/mapping_editor/uvs_pos_x_y_01.jpg
    :align: center
    :width: 400
    :alt: UVs Pos X Y 01

|

These two sliders are used to translate the UV map on its X and Y axes depending on the slider you are using.

------------------------------------------------------------------------------------------------------------------------

UVs Rot
--------

.. image:: _static/_images/mapping_editor/uvs_rot.jpg
    :align: center
    :width: 400
    :alt: UV Rot

|

This slider is used to rotate the UV map.


------------------------------------------------------------------------------------------------------------------------

Cube Projection
----------------

.. image:: _static/_images/mapping_editor/cube_projection.jpg
    :align: center
    :width: 400
    :alt: Cube Projection

|

This button allows you to make a cubic mapping on the fly. Useful to re-project a UV mapping when you modify the geometry
of the object.

------------------------------------------------------------------------------------------------------------------------

Smart Projection
-----------------

.. image:: _static/_images/mapping_editor/smart_projection.jpg
    :align: center
    :width: 400
    :alt: Smart Projection

|

This button allows you to make a smart mapping on the fly. Useful to re-project a UV mapping when you modify the geometry


------------------------------------------------------------------------------------------------------------------------

Mapping Box Type
-----------------

.. image:: _static/_images/mapping_editor/mapping_box_type.jpg
    :align: center
    :width: 400
    :alt: Mapping Box Type

|


In this mode, the addon sets the nodes with image textures (if present) in **Box** mode. In addition, the **Blend** slider
allows you to control the corresponding Blend values of the image texture nodes.


Here the Material nodes in Box Mode:

.. image:: _static/_images/mapping_editor/box_blend_example.jpg
    :align: center
    :width: 800
    :alt: Box Blend Example

