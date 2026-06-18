
.. _update_only_the_addon:

========================
Update The addon
========================

**To check which version of Extreme PBR you are using** and therefore be sure which guide to follow, you can check
the version of the addon in 2 ways:
- Via ``edit > preferences > addons`` and looking for the addon in the list by typing ``Extreme PBR`` in the search bar
- If you have already installed the addon, you can access the preferences, by clicking on the button :ref:`mp_open_options`

So the version is indicated in 2 places in the preferences window like this:

.. image:: _static/_images/installation/see_version.webp
    :align: center
    :width: 800
    :alt: See version

|



.. important::
    While switching from Blender versions lower than 4.2 to 4.2 or higher, there may be residues of "Legacy" addons
    that could create confusion in the correct installation/update of the addon. If you are in Blender 4.2 or higher,
    make sure that the addon is not installed as "Legacy" if it is Uninstall it, save the preferences and restart Blender.


    .. image:: _static/_images/update_the_addon/uninstall_legacy_addon.jpg
        :align: center
        :width: 800
        :alt: Legacy addon




.. _update_from_superhive:

Update from SuperHive (Formerly BlenderMarket)
------------------------------------------------------------

.. image:: _static/_images/logos/superhive_logo_wide_01.webp
   :class: rounded-img
   :width: 100%


From 2026 SuperHive (Formerly BlenderMarket) has introduced its own repository for extensions, this is very convenient,
our addons have supported this functionality for a long time.

1. If you have never configured the SuperHive repository Uninstall Extreme PBR from the list of Blender extensions

    .. image:: _static/_images/update_the_addon/uninstall_extension.jpg
        :align: center
        :width: 800
        :alt: Uninstall addon


2. If you have uninstalled the addon in the previous step, in this case perform the installation as if it were the first installation going here:
    - :ref:`installation`


3. If you have already configured the SuperHive repository, you just need to press the "Update" button as you see in the image below.

    .. image:: _static/_images/update_the_addon/update_extension.jpg
        :align: center
        :width: 800
        :alt: Update addon

4. Relink the libraries: :ref:`relink_libraries`


.. _update_from_other_sources:

Update from Gumroad or other sources
------------------------------------------------------------

.. image:: _static/_images/logos/gumroad_logo_wide_01.webp
   :class: rounded-img
   :width: 100%


1. Download the addon file

In your product page, you can find various files, the main ones for the installation are the following:

- ``extreme_pbr_v4####.zip`` is the addon for blender, this is the first element to download and install,
  the version you have may be different, but the name will always start with
  "extreme_pbr_v..." and end with ".zip"

  .. image:: _static/_images/installation/addon_zipped_01.webp
      :align: center
      :width: 250
      :alt: Addon zipped 01

|

**Here are the main pages where we have our products, remember that you will need to be logged in to access the purchase page:**

- Gumroad: https://app.gumroad.com/library
- SuperHive (Formerly BlenderMarket): https://superhivemarket.com/account/orders



.. Important:: The addon file must remain in zip format! Do not unzip the file, otherwise you will not be able to install it correctly.
              This note is especially for Mac users.


|

2. Once the addon is downloaded, open Blender and make drag and drop of the downloaded file into the Blender window:


.. image:: _static/_images/installation/install_addon_drag_and_drop_file_zip.jpg
    :align: center
    :width: 800
    :alt: Install addon drag and drop file zip

|

3. If everything went well, the addon is in the list of installed addons, you can also search for it by typing "Extreme PBR"
   Mark the checkbox to activate it.

.. image:: _static/_images/installation/install_addon_zip_blender_02.webp
    :align: center
    :width: 800
    :alt: Install addon zip in Blender 2


|

4. Relink the libraries: :ref:`relink_libraries`

.. _relink_libraries:

Relink Libraries
----------------------------


1. Try to Relink Libraries in automatic with the button **Try to re-link all paths automatically** available from version
   4.1.110 onwards, this if the addon has already been installed correctly previously, should automatically relink
   the paths to the Extreme PBR libraries (Including any expansions) If this does not work, go to the next step.

.. image:: _static/_images/installation/auto_relink_libraries.webp
    :align: center
    :width: 800
    :alt: Auto relink libraries

|

2. If the previous step failed, go to the **Libraries** tab and refer to this section that explains how
   the connection to the library paths works :ref:`pr_libraries`

.. image:: _static/_images/preferences/pr_library_management_panel.webp
    :align: center
    :width: 600
    :alt: Pr library management panel
