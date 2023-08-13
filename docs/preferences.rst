======================
Preferences
======================

In order to access the preferences there are several ways:


- **By Extreme PBR (If already installed and operational)**

From the Extreme PBR panel, click on the ``Options`` button, this will open the preferences in the **Options** tab.

.. image:: _static/_images/preferences/pr_panel_button.webp
    :align: center
    :width: 800
    :alt: Preferences Panel Button

|

- **By Blender Preferences**

From Blender's main menu, select ``Edit`` and then ``Preferences``, this will open Blender's preferences window.
Go to ``Add-ons`` and search for ``Extreme PBR`` and click on the checkbox to activate it (If it's not already active).


.. image:: _static/_images/preferences/pr_edit_preferences.webp
    :align: center
    :width: 800
    :alt: Blender Preferences Button


------------------------------------------------------------------------------------------------------------------------

Options
======================

Le Opzioni sono suddivise in diverse aree di interesse:

- **General Options:** Ref: :ref:`pr_general_options`
- **Interface Options** Ref: :ref:`pr_interface_options`
- **Fix Options** Ref: :ref:`pr_fix_options`
- **Experimental Options** Ref: :ref:`pr_experimental_options`


.. image:: _static/_images/preferences/pr_options_example.webp
    :align: center
    :width: 800
    :alt: Preferences Options Example

------------------------------------------------------------------------------------------------------------------------

.. _pr_general_options:

General Options
----------------------

.. image:: _static/_images/preferences/pr_general_options.webp
    :align: center
    :width: 600
    :alt: Preferences General Options

|

Bellow are explained the various properties

------------------------------------------------------------------------------------------------------------------------

.. _pr_op_material_type:

Material Type
**********************

.. image:: _static/_images/preferences/pr_op_material_type.webp
    :align: center
    :width: 600
    :alt: Preferences Material Type

|

This selector allows you to choose which type of setting to use when creating a material:

- **Nexus:**
    - This type of setting allows you to create materials in Nexus mode, this means that you will have access to
      the **Texture Paint**, described here: :ref:`texture_paint` and to the creation of **Fx Layers**, described here: :ref:`fx_layer` and to all
      its **Dynamic Mask** described here: :ref:`fx_dynamic_mask`

- **Simple PBR:**
    - This type of material setting allows you to create simple materials, so that you have "Light" materials
      for your project, the render will be much faster, but you will not have access to the functions of the **Nexus**
      materials. **Simple PBR** example is here: :ref:`me_simple_pbr_type`


------------------------------------------------------------------------------------------------------------------------

Check For updates Every
****************************

.. image:: _static/_images/preferences/pr_op_check_for_updates_every.webp
    :align: center
    :width: 600
    :alt: Preferences Check For updates Every

|

This property allows you to choose how often Extreme PBR should check for updates.

.. important::
        I strongly advise you not to leave **Never** as a value, as Extreme PBR is constantly evolving and
        there may be important updates to fix bugs or add new features, so
        if you leave **Never** you will not see the new update alerts.
        you can always refer to **Check For Updates** described here: TODO: Put reference to Check For Updates button

------------------------------------------------------------------------------------------------------------------------

Show Hidden Sockets
************************


Show Hidden Sockets allows you to show or hide the sockets of the Extreme PBR Nexus nodes, by default the unused sockets
are hidden for a matter of node interface cleaning.

.. image:: _static/_images/preferences/pt_op_show_hidden_sockets.webp
    :align: center
    :width: 600
    :alt: Preferences Show Hidden Sockets

|

Here is an example of what happens to the nodes when you activate or deactivate this **Show Hidden Sockets**:

.. image:: _static/_images/preferences/pr_op_show_hidden_sockets_example.webp
    :align: center
    :width: 800
    :alt: Preferences Show Hidden Sockets Example

------------------------------------------------------------------------------------------------------------------------

Show Group Options
************************

Show Group Options allows you to show or hide the options of the Extreme PBR Nexus nodes, by default the options are
hidden for a matter of node interface cleaning.

.. image:: _static/_images/preferences/pt_op_show_group_options.webp
    :align: center
    :width: 600
    :alt: Preferences Show Group Options

|

Here is an example of what happens to the nodes when you activate or deactivate this **Show Group Options**:

.. image:: _static/_images/preferences/pt_op_show_group_options_example.webp
    :align: center
    :width: 800
    :alt: Preferences Show Group Options Example

------------------------------------------------------------------------------------------------------------------------

Default Mapping Type
************************

Default Mapping Type allows you to choose the default mapping type for the textures, by default the mapping type is
**UV**

.. image:: _static/_images/preferences/pt_op_default_mapping_type.webp
    :align: center
    :width: 600
    :alt: Preferences Default Mapping Type

|

In order to see better what it is, refer to: :ref:`mapping_editor_panel`


.. tip::
        You can always modify each Texture Image material individually at a later time.
        My suggestion if you have little experience is to leave UV as the default for now.


------------------------------------------------------------------------------------------------------------------------

.. _pr_op_texture_color_space:

Texture Color Space
************************


Texture Color Space allows you to choose the default color space for the textures, by default the color space is **sRGB**
but this also allows you to choose other color spaces if you are using different ACES configurations.

Once you have chosen the color space, this will be applied to all the textures that will be created by Extreme PBR and also
to those already applied.

.. image:: _static/_images/preferences/pr_op_texture_colorspace_section.webp
    :align: center
    :width: 600
    :alt: Preferences Texture Color Space Section

|


.. hint::
        if your **ACES** list is very long, you can search by name, and the list will narrow down so as not to be confused.
        This tool was designed specifically for those who use ACES configurations other than the default one.


RGB
^^^^

Rgb Color Space allows you to change the color space of all textures to RGB (Type diffuse, emission, etc ...)

.. image:: _static/_images/preferences/pt_op_texture_color_space_rgb.webp
    :align: center
    :width: 600
    :alt: Preferences Texture Color Space

|

.. important::
        This function will change the color spaces only of the materials applied with Extreme PBR, no material coming
        from other sources will be modified, nor those created manually.
        In addition, only nodes of type **Image Texture** will be identified

BW
^^^^

BW Color Space allows you to change the color space of all textures to BW (Type normal, roughness, etc ...)

.. image:: _static/_images/preferences/pt_op_texture_color_space_bw.webp
    :align: center
    :width: 600
    :alt: Preferences Texture Color Space

|

.. important::
        This function will change the color spaces only of the materials applied with Extreme PBR, no material coming
        from other sources will be modified, nor those created manually.
        In addition, only nodes of type **Image Texture** will be identified

|


Try to reset to default
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. image:: _static/_images/preferences/pt_op_texture_color_space_reset.webp
    :align: center
    :width: 600
    :alt: Preferences Texture Color Space

|

This button, if pressed, will try to reset the color spaces of all textures to the default ones, **sRGB** and **Non-Color**,
and also in the buttons **RGB** and **BW** :ref:`pr_op_texture_color_space`

------------------------------------------------------------------------------------------------------------------------

.. _pr_interface_options:

Interface Options
----------------------

From this section you can modify some settings of the Extreme PBR interface.

.. image:: _static/_images/preferences/pr_op_interface_options_panel.webp
    :align: center
    :width: 600
    :alt: Preferences Interface Options

|

Show material popup label
****************************

This option allows you to show or hide the preview material labels in the material browser popup.
Reference here to the material Browser: :ref:`mp_material_browser`


.. image:: _static/_images/preferences/pr_op_show_material_popup_label.webp
    :align: center
    :width: 600
    :alt: Preferences Show Material Popup Label


|


**Show material popup label On**

.. image:: _static/_images/preferences/pr_op_popup_label_example_on.webp
    :align: center
    :width: 800
    :alt: Preferences Show Material Popup Label Example On

|

**Show material popup label Off**

.. image:: _static/_images/preferences/pr_op_popup_label_example_off.webp
    :align: center
    :width: 800
    :alt: Preferences Show Material Popup Label Example Off

------------------------------------------------------------------------------------------------------------------------

Icon Preview Dimension
****************************

This option allows you to change the size of the material preview icons in the Material Browser, reference here to the
material Browser: :ref:`mp_material_browser`

.. image:: _static/_images/preferences/pr_op_icon_preview_dimension.webp
    :align: center
    :width: 600
    :alt: Preferences Icon Preview Dimension

|


.. |1_0| image:: _static/_images/preferences/pr_op_icon_preview_dimension_1_0.webp
        :align: top
        :width: 800
        :alt: Preferences Icon Preview Dimension 1.0


.. |1_7| image:: _static/_images/preferences/pr_op_icon_preview_dimension_1_7.webp
        :align: top
        :width: 800
        :alt: Preferences Icon Preview Dimension 1.7


In this example the left panel can be much smaller.

+----------------------------------+----------------------------------+
| **Icon Preview Dimension 1.0**   | **Icon Preview Dimension 1.7**   |
+==================================+==================================+
| |1_0|                            | |1_7|                            |
+----------------------------------+----------------------------------+


------------------------------------------------------------------------------------------------------------------------

Icons Popup Size
****************************

This option allows you to choose the size of the icons of the material preview popup, reference here to the
material Browser: :ref:`mp_material_browser_popup`


.. image:: _static/_images/preferences/pr_op_icons_popup_size.webp
    :align: center
    :width: 600
    :alt: Preferences Icons Popup Size

|

Example with **Icons Popup Size 1.0**

.. image:: _static/_images/preferences/pr_op_preview_popup_size_1_0.webp
    :align: center
    :width: 800
    :alt: Preferences Icons Popup Size 1.0

|

Example with **Icons Popup Size 2.0**

.. image:: _static/_images/preferences/pr_op_preview_popup_size_2_0.webp
    :align: center
    :width: 800
    :alt: Preferences Icons Popup Size 1.7

------------------------------------------------------------------------------------------------------------------------

.. _pr_hide_shader_overlay_panel:


Hide Shader Overlay Panel
****************************

This panel can be hidden if you want to have a less small addon interface.

Reference: :ref:`shader_overlay`

.. image:: _static/_images/preferences/pr_op_hide_shader_overlay_panel.webp
    :align: center
    :width: 600
    :alt: Preferences Hide Shader Overlay Panel

------------------------------------------------------------------------------------------------------------------------

.. _pr_hide_material_override_panel:

Hide Material Override Panel
****************************

This panel can be hidden if you want to have a less small addon interface.

Reference: :ref:`material_override`

.. image:: _static/_images/preferences/pr_op_hide_material_override_panel.webp
    :align: center
    :width: 600
    :alt: Preferences Hide Material Override Panel

------------------------------------------------------------------------------------------------------------------------





.. _pr_fix_options:

Fix Options
----------------------

TODO

------------------------------------------------------------------------------------------------------------------------

.. _pr_experimental_options:

Experimental Options
----------------------

TODO








