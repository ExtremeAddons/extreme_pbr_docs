Main Panel
===========================

Il pannello principale di Extreme PBR Nexus dalla versione 4.1.100

.. |main_panel| image:: _static/_images/main_panel/main_panel_01.png
                    :width: 800
                    :alt: Main Panel 01



+--+-------------------------------------+-+
|  |  1. :ref:`libraries_selector`       | |
|  |  2. :ref:`material_browser`         | |
|  |  3. :ref:`tag_search_size_selector` | |
|  |  4. :ref:`add_remove_buttons`       | |
|  |  5. :ref:`material_list`            | |
|  |  6. :ref:`box_utility`              | |
+--+-------------------------------------+-+
|  | |main_panel|                        | |
+--+-------------------------------------+-+

------------------------------------------------------------------------------------------------------------------------

.. _libraries_selector:

Libraries selector
------------------

    - This area is used to choose the library, the category (of the library) and the category search via the text field.


.. image:: _static/_images/main_panel/main_panel_magnify_library_selector_01.png
    :align: center
    :width: 800
    :alt: Libraries selector

------------------------------------------------------------------------------------------------------------------------

Helps Button
************

    - This button opens the Help section in the addon preferences window. This is useful to find more information
      on how to use the addon


.. image:: _static/_images/main_panel/helps_button_main_panel_01.png
    :align: center
    :width: 800
    :alt: Helps Button


------------------------------------------------------------------------------------------------------------------------

Library Selector (Drop-down menu)
*********************************

    - This allows you to select the background library you want to use. All libraries added via
      "Libraries" in the addon preferences menu will be displayed in this drop-down menu.
      By default this Drop-down menu, contains the "Default" library, which is the library that comes with the addon.
      and the "User" library, which is the library where you can add your saved backgrounds.


.. image:: _static/_images/main_panel/libraries_selector_popup_01.png
    :align: center
    :width: 400
    :alt: Libraries selector


------------------------------------------------------------------------------------------------------------------------

Minimize Button
***************

    - This button allows you to minimize the main panel, to have more space in the 3D view.


.. image:: _static/_images/main_panel/minimize_main_panel_01.png
    :align: center
    :width: 800
    :alt: Minimize Button


------------------------------------------------------------------------------------------------------------------------

Search Category
***************

This Button allows you to search for a category without opening the drop-down menu.

.. image:: _static/_images/main_panel/search_category_botton_01.png
    :align: right
    :width: 600
    :alt: Search Category

|

.. note::
        The categories are relative to the selected library, at the moment the categories contained in a non-selected library will not be displayed


------------------------------------------------------------------------------------------------------------------------

Category Selector (Drop-down Menu)
************************************

   - This allows you to select the category (Each library will have its own category)

.. image:: _static/_images/main_panel/category_popup_01.png
    :align: center
    :width: 800
    :alt: Category Selector


------------------------------------------------------------------------------------------------------------------------

.. _material_browser:

Material Browser
-------------------

    - This section is dedicated to displaying the material previews.


.. image:: _static/_images/main_panel/material_browser_01.png
    :align: center
    :width: 800
    :alt: Material Browser


------------------------------------------------------------------------------------------------------------------------

Preview Popup
*************

   - This allows you to select the background (Each library will have its own background), a pop-up window will appear
     with the list of preview backgrounds

.. image:: _static/_images/main_panel/material_browser_popup_01.png
    :align: center
    :width: 800
    :alt: Preview Popup

------------------------------------------------------------------------------------------------------------------------

Up/Down Arrow
**************

    - These two buttons allow you to switch to the previous or next category.

.. image:: _static/_images/main_panel/scroll_up_down_category_01.png
    :align: center
    :width: 800
    :alt: Up/Down Arrow


------------------------------------------------------------------------------------------------------------------------

Left/Right Arrow
*****************

    - These two buttons allow you to switch to the previous or next material in the current category.

.. image:: _static/_images/main_panel/scroll_left_right_material_01.png
    :align: center
    :width: 800
    :alt: Left/Right Arrow


------------------------------------------------------------------------------------------------------------------------

Open Options
**************

    - This button will open the Extreme PBR preferences exactly in the Options section

.. image:: _static/_images/main_panel/open_options_button_01.png
    :align: center
    :width: 800
    :alt: Open Options

------------------------------------------------------------------------------------------------------------------------

Reload Preview Icons
*********************

    - It may happen that the material icons are not loaded correctly, this button allows you to reload the material icons.
      in addition, it also reloads the interface icons

.. image:: _static/_images/main_panel/reload_preview_icons_01.png
    :align: center
    :width: 800
    :alt: Reload Preview Icons



------------------------------------------------------------------------------------------------------------------------


.. _tag_search_size_selector:

Tag Search Size Selector
------------------------

    - This small menu in the box, allows you to Select the size / version of the material (If there is an alternative)
      Contains The search for tag / background name and information on the background currently in the preview.


.. image:: _static/_images/main_panel/tag_search_size_selector_01.png
    :align: center
    :width: 800
    :alt: Tag Search Size Selector


------------------------------------------------------------------------------------------------------------------------

Search for tag
**************

   - This allows you to search for a background by typing the name of the tag
      - In the upper field, you can enter the name of the tag you want to include in the search
      - In the lower field, you can enter the name of the tag you want to exclude from the search

      Keep the tags separated with a space if you want to include more than one tag in the search.

      In this way, the categories and the previews will be filtered according to the tags entered.

.. image:: _static/_images/main_panel/tag_search_menu_button_01.png
    :align: center
    :width: 800
    :alt: Search for tag

------------------------------------------------------------------------------------------------------------------------

Search Background by entering text
**********************************

   - This allows you to search for a background by typing the name of the background (It work with the tag Restrictions if you need)

.. image:: _static/_images/main_panel/search_background_dropdown_01.png
    :align: center
    :width: 600
    :alt: Search Background by entering text


------------------------------------------------------------------------------------------------------------------------

Info & Tag
**********

    - This button will open a dialog window with information about the background currently in preview.
      inside there will be information about the author, the license.
      There will also be the tags that have been assigned to the material, they can also be modified from here.

.. image:: _static/_images/main_panel/info_tag_panel_popup_01.png
    :align: center
    :width: 600
    :alt: Info & Tag Panel

------------------------------------------------------------------------------------------------------------------------


Show info
#############

    - By pressing the arrow-shaped button, the section will be shown or hidden where there is information
      on the material in preview (If existing)

.. image:: _static/_images/main_panel/show_info_panel_01.png
    :align: center
    :width: 600
    :alt: Show info

------------------------------------------------------------------------------------------------------------------------

Edit Tags
#########

    - In the info & Tag panel you can edit the tags assigned to the background.
      To do this, just click on the **Edit Tags** button and enter the desired tags.
      You can also delete existing tags, just press on them, and a dialog box will be displayed
      that will ask you if you want to delete the tag.
      This tag will then be useful for searching for material by tag.


.. image:: _static/_images/main_panel/edit_tags_01.png
    :align: center
    :width: 600
    :alt: Edit Tags

|

.. Note::
    - Tags can only be edited if you have checked the "Edit Tags" box


------------------------------------------------------------------------------------------------------------------------

Material Version Selector
*************************

    - If in the library there are different versions of the same material, this selection allows you to choose which version to load

      **This will only take effect when loading the material, it will not affect the material already loaded in the scene**

.. image:: _static/_images/main_panel/material_version_selector_01.png
    :align: center
    :width: 400
    :alt: Material Version Selector

|

.. note::
    - The versions of the materials will be shown only if they are greater than 1, if for example a material has only one version, this will not be shown
      because it would not make sense to select a version if there is only one.


------------------------------------------------------------------------------------------------------------------------

.. _add_remove_buttons:

Add Remove Buttons
------------------

    - Add (From the preview) / Remove (From the scene) buttons


..
    .. image:: _static/_images/main_panel/add_remove_buttons_01.png
        :align: center
        :width: 300
        :alt: Add Remove Buttons

------------------------------------------------------------------------------------------------------------------------

.. _material_list:

Material List
-------------

    - This is the list of materials that are in the current active object.


------------------------------------------------------------------------------------------------------------------------

.. _box_utility:

Box Utility
-----------

    - This box contains some useful and fundamental functions of Extreme PBR










