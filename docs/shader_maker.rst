
.. _shader_maker_category:

========================
Shader Maker Category
========================


This special category contains some useful tools to create and import shaders.



.. |shader_maker_icon| image:: _static/_images/shader_maker/shader_maker_icon.webp
                        :width: 200
                        :alt: Shader Maker Icon

.. |sm_painter_icon| image:: _static/_images/shader_maker/sm_painter_icon.webp
                        :width: 200
                        :alt: Shader Maker Icon

.. |video_maker_icon| image:: _static/_images/shader_maker/video_maker_icon.webp
                        :width: 200
                        :alt: Shader Maker Icon


+--------------------+-------------------+-------------------+
| |shader_maker_icon| |sm_painter_icon|   |video_maker_icon| |
+--------------------+-------------------+-------------------+



.. _shader_maker:

Shader Maker
========================


This tool of Extreme PBR allows you to create a material on the fly if you have the textures on your computer
this tool recognizes the names of the textures (Maps) based on the suffix or prefix if it exists, so it is able to place
in the right way the maps, this tool is very useful to create materials quickly and easily.


.. image:: _static/_images/shader_maker/shader_maker_icon.webp
    :align: center
    :width: 200
    :alt: Shader Maker Icon

|

List of map nomenclatures that this tool recognizes:

- **Diffuse**: _diffuse_xtm, _albedo, _basecolor, _base_color, _diffuse, _color, _diff, _dif, _col, diffuse
- **Emission**: _emission_xtm, _emission, _emissive, _emiss, _emis, _emi
- **Occlusion**: _occlusion_xtm, _ambient_occlusion, _ambientocclusion, _occlusion, _ao,  ao
- **Subsurface**: _sss_xtm, _subsurface, _sss, _scattering, _scatter
- **Subsurface Strength**: _sss_strength_xtm
- **Metal**: _metal_xtm, _metalness, _metal, _metallic,  metal ,  metallic
- **Specular**: _specular, _reflection, _mirror, _reflective, _reflex, _spec,  specular
- **Roughness**: _roughness_xtm, _roughness, _glossy, _rough, _gloss, _rgh,  roughness
- **Transmission**: _transmission_xtm, _transmission, _glass
- **Mask**: _mask_xtm
- **Alpha**: _alpha_xtm, _transparent, _alpha
- **Normal**: _normal_xtm, _normal_map, _normal, _norm, _nrm,  normal
- **Bump**: _bump_xtm, _bump_map, _bumpmap, _bump,  bump ,  height
- **Displace**: _displace_xtm, _displace, _height, _disp,  displace

------------------------------------------------------------------------------------------------------------------------

Auto PBR
------------------------


.. image:: _static/_images/shader_maker/sm_auto_pbr.webp
    :align: center
    :width: 400
    :alt: Shader Maker Auto PBR

|

To add a material with Auto PBR, you must select the Shader Maker category and the Shader Maker,
Then you will have a situation like in the image above-

When you are in this special category, the whole addon understands and behaves differently, now for example, the
**Add New** button described here: :ref:`mp_add_new`, becomes, **Auto PBR** and when you press it a window will open
File Browser, where you can select the Files you want to use for the material, based on the convention described
here is also supported the selection of multiple image files, so you can select all the maps you need for the
material.

You can also choose only 1 file (For example: diffuse) even if it does not have a convention, and then add the others
maps via **Texture Manager** Also described here :ref:`texture_manager_panel`

------------------------------------------------------------------------------------------------------------------------

Material Editor (Nexus)
**************************

Here is the Nexus Panel if you have chosen the **Nexus** setting from the Extreme PBR options menu TODO: Put link to Nexus Material options

Having applied the material via Shader Maker (Auto PBR button) now you can edit the material via
Material Editor panel, below you will find the description of the material editor :ref:`module_material_panel`

.. image:: _static/_images/shader_maker/sm_material_editor.webp
    :align: center
    :width: 300
    :alt: Shader Maker Material Editor

------------------------------------------------------------------------------------------------------------------------

Material Editor (Simple PBR)
*******************************

Here is the Simple PBR Panel if you have chosen the **Simple PBR** setting from the Extreme PBR options menu TODO: Put link to Simple PBR options

Having applied the material via Shader Maker (Auto PBR button) now you can edit the material via
Material Editor panel, below you will find the description of the material editor :ref:`me_simple_pbr_type`

.. image:: _static/_images/shader_maker/sm_material_editor_simple_pbr.webp
    :align: center
    :width: 300
    :alt: Shader Maker Material Editor

|

------------------------------------------------------------------------------------------------------------------------

Shader Maker Video
========================

.. image:: _static/_images/shader_maker/video_maker_icon.webp
    :align: center
    :width: 200
    :alt: Shader Maker Video

|


Shader Maker Video allows you to apply a video as a material and easily control it from the panel.

.. image:: _static/_images/shader_maker/sm_shader_maker_video_panel_example.webp
    :align: center
    :width: 400
    :alt: Shader Maker Video Panel Example

|

.. note::
        To add this type of Material, just press **Add New** Ref: :ref:`add_remove_buttons` a material with a demo video will be added
        that you can replace with your video.














