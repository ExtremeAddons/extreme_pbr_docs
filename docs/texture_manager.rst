
.. _texture_manager_panel:

Texture Manager Panel
=========================

.. seealso::
    In order to access the Texture Manager panel, refer to the :ref:`texture_manager_button` chapter


The texture manager panel is used to access the texture management features of the current material,
please note, the material must be created with Nexus setting TODO: link to nexus material preferences

Here's how the texture manager looks, in an example from the diffuse property:

.. image:: _static/_images/texture_manager/tm_panel_diffuse.webp
    :align: center
    :width: 800
    :alt: Texture Manager Panel

.. note::
        The texture manager can be of 3 types, for 3 types of Texture Map: **RGB Map**, **Black and White** and **Normal Map**



.. tip::
        The Texture Manager panel is very interesting, as it allows you to access all the materials present in the library
        of Extreme PBR and therefore to change the texture on the fly on the current material. This allows you to change
        also the roughness maps or any other map, so you can edit the maps of a material
        and customize the situation at will.

------------------------------------------------------------------------------------------------------------------------

.. _texture_manager_rgb:

Texture Manager RGB
-------------------------

This is the Texture Manger panel to manage RGB type textures:

.. image:: _static/_images/texture_manager/tm_panel_rgb_type.webp
    :align: center
    :width: 400
    :alt: Texture Manager RGB

------------------------------------------------------------------------------------------------------------------------

.. _material_browser:

Material Browser
*****************

.. image:: _static/_images/texture_manager/tm_material_browser.webp
    :align: center
    :width: 400
    :alt: Material Browser

|

From Material Browser you can choose the material present in the selected category and then access its textures, if present
in the chosen material.

------------------------------------------------------------------------------------------------------------------------

Search Category
*****************

.. image:: _static/_images/texture_manager/tm_cat_browser.webp
    :align: center
    :width: 400
    :alt: Search Category

|


By clicking on the category search button, you can choose the category of materials from which to choose the material.
You can enter the name to search for the material you are interested in.

------------------------------------------------------------------------------------------------------------------------

Search Material
*****************

.. image:: _static/_images/texture_manager/tm_search_material.webp
    :align: center
    :width: 400
    :alt: Search Material

|

By clicking on the Search Material button you can search for the material you are interested in, entering the name of the
material to search for. Once identified, it will be shown in the preview :ref:`material_browser` and you can access its textures.

------------------------------------------------------------------------------------------------------------------------

Texture Browser
*****************

.. image:: _static/_images/texture_manager/tm_texture_browser.webp
    :align: center
    :width: 400
    :alt: Texture Browser

|

By clicking on Texture Browser you will have access to the preview of all the textures present in the material selected in the :ref:`material_browser`.
You can import and replace the current texture with the one selected via the **Add** button explained below.

------------------------------------------------------------------------------------------------------------------------

Add
*****************

.. image:: _static/_images/texture_manager/tm_add.webp
    :align: center
    :width: 400
    :alt: Add

|

The Add button allows you, once you have chosen the texture to apply (or replace) to apply it to the current property
in this case the **Diffuse**.
The texture applied will be shown in the preview of the texture used.

------------------------------------------------------------------------------------------------------------------------

Texture resolution
*******************

.. image:: _static/_images/texture_manager/tm_resolution.webp
    :align: center
    :width: 400
    :alt: Texture resolution

|

By the resolution selector, you can choose which resolution to use for the selected texture.

.. note::
        This will only take effect by applying the texture, it will not affect the texture already in use.

------------------------------------------------------------------------------------------------------------------------

Search Data Images
*******************

.. image:: _static/_images/texture_manager/tm_search_data_images.webp
    :align: center
    :width: 400
    :alt: Search Data Images

|

By clicking on the **Search Data Images** button you can search for the images present in the scene, that is in the **bpy.data.images**
of the current project. It allows you to view and search among all the images you are using in the project.
This is useful for reusing images already present in the project and not having to search for them every time, so as to
have the project cleaner and less heavy.

------------------------------------------------------------------------------------------------------------------------

Texture Name
*******************

.. image:: _static/_images/texture_manager/tm_texture_name.webp
    :align: center
    :width: 400
    :alt: Texture Name

|

By this text box, you can view the name of the current Texture Image and also edit it if necessary,
simply by clicking on it and typing the new name.

















