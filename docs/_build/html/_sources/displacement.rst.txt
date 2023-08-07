Displacement
==================

In order to access the displacement panel, you need to activate the displace from the Main Panel at the section :ref:`displace_on_off`.
Only then you will be able to see the displacement panel.

Make sure you have selected the material that has the active displacement from the :ref:`material_list` otherwise you will not
see the displacement panel.



.. image:: _static/_images/displacement/displace_on_button_with_example.png
    :align: center
    :width: 800
    :alt: Displace On Button With Example

|

.. note::
        Some materials, for example **Car Paint** or **Water** once applied you will not see the **Displacement** button.
        This is intended, as these materials do not need displacement. The button will be visible, only if in the
        material there is a Bump or Displacement map.


Introduction to the displacement modifier
-----------------------------------------

Il displacement può essere usato in due modi:

Displacement Modifier
**********************

It works in Eevee and Cycles mode, in fact it uses the Blender Modifiers to create the displacement,
this is very useful if you do not want to use Cycles, but also if you use Cycles, the displacement will work anyway.

Here's what it does exactly once you activate the displacement from the button in the :ref:`displace_on_off`:

.. image:: _static/_images/displacement/displace_modifier_corrispective_modifiers_01.jpg
    :align: center
    :width: 800
    :alt: Displace Modifier Corrispective Modifiers 01

|


Microdisplacement
**********************




Displacement Panel (Modifier)
-----------------------------

Here is how the displacement panel looks like once you activate the **Displacement** button.
By default it will be set to **Modifiers**

.. image:: _static/_images/displacement/displacement_panel_modifier_01.jpg
    :align: center
    :width: 400
    :alt: Displacement Panel Modifier 01

|





Toggle Wireframe
*******************

This button allows you to control the mesh of the selected model, it also allows you to see all the subdivisions
that have been applied to the model by the modifier

.. image:: _static/_images/displacement/toggle_wireframe.png
    :align: center
    :width: 800
    :alt: Toggle Wireframe







