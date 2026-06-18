.. _installation:

==============================================
Installation
==============================================

**We highly recommend using Blender 4.2 or higher!**

This chapter is dedicated to the first installation of the addon. If you have already installed the addon and want to
update it, you can go to the chapter :ref:`update_only_the_addon`


------------------------------------------------------------------------------------------------------------------------

==============================================
Install the Addon
==============================================

The installation of the addon (Core) depends on where you purchased it. Choose your method below.

- Follow **Method A** if you purchased on SuperHive (Formerly BlenderMarket): :ref:`install_from_superhive`
- Follow **Method B** if you purchased on Gumroad or other sources: :ref:`manual_extension_installation_from_zip`



------------------------------------------------------------------------------------------------------------------------


.. _install_from_superhive:

Method A: SuperHive (Blender 4.2+)
***************************************************************

.. image:: _static/_images/logos/superhive_logo_wide_01.webp
   :class: rounded-img
   :width: 100%


This method is for users who purchased on SuperHive and use Blender 4.2 or later. The new repository system simplifies both installation and future updates.


.. admonition:: Installation From SuperHive
    :class: youtube

        .. raw:: html

            <iframe width="560" height="315" src="https://www.youtube.com/embed/jn2-4e-p1aI?si=D9AE4T7K5dCZbz_2"
            title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media;
            gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

|



1. **Go to your SuperHive Order Page (make sure you are logged in):**
    .. raw:: html

        <a href="https://superhivemarket.com/account/orders" target="_blank" rel="noopener noreferrer">https://superhivemarket.com/account/orders</a>

2. **Drag and drop the addon from the order page directly into your Blender 4.2+ window.**

    .. image:: _static/_images/installation/superhive_drag_and_drop_01.jpg
        :align: center
        :width: 800
        :alt: SuperHive drag and drop 01

3. **Click Add Repository... when prompted (Skip if you already configured it in the past).**

    .. image:: _static/_images/installation/set_sh_repo_01.jpg
        :align: center
        :width: 800
        :alt: Set SuperHive repository in Blender 01

4. **Set Api Token (Skip if you already configured it in the past).**

    .. image:: _static/_images/installation/set_sh_api_token_in_blender_01.jpg
        :align: center
        :width: 800
        :alt: Set SuperHive API token in Blender 01


5. **Make sure to press Install from Extensions:**

    .. image:: _static/_images/installation/first_installation_extension.jpg
        :align: center
        :width: 800
        :alt: Install from SuperHive 01


6. **Ensure the addon is checked and activated in your Addons list.**

    .. image:: _static/_images/installation/check_addon_installed_01.jpg
        :align: center
        :width: 800
        :alt: Check addon installed 01


|

------------------------------------------------------------------------------------------------------------------------


.. _manual_extension_installation_from_zip:

Method B: Manual Zip (Gumroad or others)
********************************************************************

.. image:: _static/_images/logos/gumroad_logo_wide_01.webp
   :class: rounded-img
   :width: 100%


This method is dedicated to those who purchased on Gumroad or prefer a manual installation.


.. admonition:: Installation From Gumroad or other sources
    :class: youtube

        .. raw:: html

            <iframe width="560" height="315" src="https://www.youtube.com/embed/66qbIOgbvO0?si=gZPFzaKlEndyfBg8"
            title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media;
            gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>


|



1. **Download the addon file from your order page:** https://app.gumroad.com/library

    .. image:: _static/_images/installation/addon_zipped_01.webp
        :align: center
        :width: 250
        :alt: Addon zipped 01

    |

.. important::
    The file must remain in **zip format**. Do not unzip it. If your browser automatically unzips the file, compress
    it again or use another browser.

2. **Open Blender and drag the zip file directly into the Blender window.**

    .. image:: _static/_images/installation/install_addon_drag_and_drop_file_zip.jpg
        :align: center
        :width: 600
        :alt: Drag and drop addon 01

3. **Search for Extreme PBR in your installed addons list and mark the checkbox to activate it.**

    .. image:: _static/_images/installation/install_addon_zip_blender_02.webp
        :align: center
        :width: 800
        :alt: Install addon zip in Blender 2



------------------------------------------------------------------------------------------------------------------------

.. _install_library_41100:

==============================================
Install the addon library
==============================================



- If you have installed the addon correctly, now you can proceed with the installation of the library.


Step 1
***********

The first step is to download all the .exapack files you want to install, my suggestion is to start by downloading:

- **XTRPbr_Procedural_Vol_001.exapack** Very small file, contains only procedural materials
- **XTRPbr_05k_vol_001.exapack** Small file, contains only the ½k files, previews, and data files

Save them somewhere, these will be deleted after installation.


**Example of downloaded .exapack files:**

  .. image:: _static/_images/installation/exapack_files_on_computer_01.webp
      :align: center
      :width: 400
      :alt: Exapack files on computer



------------------------------------------------------------------------------------------------------------------------

Step 2
************

When you have finished downloading the **exapack** files you want to install, go to the Extreme PBR Preferences window
and go to the **Install Libraries** (TAB) section and press the "Default Library" button you see in the following image
in red.

.. Tip:: If you do not see the Extreme PBR Welcome panel, you can open it by pressing the "N" key on the keyboard.

.. image:: _static/_images/installation/go_to_install_libraries_01.webp
    :align: center
    :width: 800
    :alt: Go to install libraries 01

When you press button N.4, a file browser will open, you will have to choose a location on your computer where the
root folder of the entire **Default Library** will be created

.. Warning:: 1. Do not choose the path in the path where blender installs the addons!
             2. Avoid choosing paths on LAN connected disks, resources may not be reachable
             3. If you are also installing the expansion.exapack, these will be installed in another root folder, in the same location where the **Default Library** is located
             4. It is not recommended to use an external Hard Disk connected via USB (Unless it is an external SSD disk)


------------------------------------------------------------------------------------------------------------------------

Step 3
*************

Now the situation should look like this, where the **"Choose Exapacks"** button appears.

.. image:: _static/_images/installation/choose_exapacks_ready.webp
    :align: center
    :width: 800
    :alt: Choose Exapacks ready

|

Press the **"Choose Exapacks"** button and select the **.exapack** files you just downloaded. You can choose them all,
just make sure to select them within the File Browser. **(The files not selected will be ignored)**
Then press the button in the file browser window **Choose Exapacks** to confirm



.. image:: _static/_images/installation/browse_exapack_to_install_01.webp
    :align: center
    :width: 800
    :alt: Browse exapack to install 01


------------------------------------------------------------------------------------------------------------------------

Step 4
*****************

Now you should have the list of exapack files selected, in list, ready to be installed, you will just have to press the
**"Install From Exapack Files"** button to proceed with the installation. As follows in this image:

.. Note:: The exapack files are deleted once installed by the addon, this is for space issues
          if you want to keep them (Not Recommended) check the **"Keep Exapack After Install"** box and the files will be kept on the disk.
          But be careful, this means that you will have the weight of the library almost X2

.. image:: _static/_images/installation/install_from_exapack_files.webp
    :align: center
    :width: 800
    :alt: Install from exapack files

|


.. attention::
        For some reason, it could happen that the .exapack file is corrupted. The addon recognizes corrupted files and
        reports them in red. Download the file again, in the meantime you can remove it from the list and proceed anyway
        to the installation, you can also install it later using this same procedure.

        .. image:: _static/_images/installation/broken_exapack_file.webp
            :align: center
            :width: 800
            :alt: Broken exapack file 02




During the installation process of the .exapack packages, the interface will show the progress of the installed packages
You can also stop the process whenever you want (Just press the button (X) next to the big status bar) in this case,
the installed packages will remain installed.


.. Important:: **I want to emphasize:** All installed packages will remain installed, even if the installation process is interrupted.
               If the installation is resumed, the installation process will resume from where it was interrupted,
               because the addon recognizes the already installed files and skips them.


.. image:: _static/_images/installation/exapack_installation_progress.webp
    :align: center
    :width: 800
    :alt: Exapack installation progress


.. note:: The installation speed depends a lot on the type of disk in use, I have done various tests, and the installation on
          SSD is very fast. I do not recommend the use of an external Mechanical Hard Disk connected via USB only for time issues,
          I noticed that these disks are very slow for this process. But if you do not have time problems and you have patience,
          you can decide to use it.



------------------------------------------------------------------------------------------------------------------------

Step 5
----------

When you have completed the entire (or even just in part) installation, the addon will be ready to be used.

.. Image:: _static/_images/installation/addon_ready_01.webp
    :align: center
    :width: 600
    :alt: Addon ready 01

.. Note:: The  ½k, 1k, 2k, 4k, 8k versions are present in the complete edition. Some versions may not contain all the resolution versions.
          If you want to upgrade to the full version, you only pay the difference

------------------------------------------------------------------------------------------------------------------------

At the end of this process, on your computer, in the indicated path, 2 folders will have been created

- **EXTREME_PBR_DEFAULT_LIB** (This folder contains all the files of the Extreme PBR libraries)
- **EXTREME_PBR_USER_LIB** (This folder is an empty folder, and will be used in case you want to save your personal HDRi)


To manipulate the paths to the libraries, it is enough to go to the Extreme PBR settings and go to the **Libraries** (TAB) section

For more information on this section you can find the chapter :ref:`pr_libraries`


.. image:: _static/_images/installation/libraries_manipulation_01.webp
    :align: center
    :width: 600
    :alt: Libraries manipulation 01


------------------------------------------------------------------------------------------------------------------------

Remove Exapack From Installer
------------------------------

These buttons allow you to remove the .exapack files so that you do not have to install them in case you have
added a file by mistake or do not want to install a particular file.

.. image:: _static/_images/installation/remove_exapack_from_installer_01.webp
    :align: center
    :width: 600
    :alt: Remove exapack from installer 01



------------------------------------------------------------------------------------------------------------------------


About Exapack
================

As for the libraries, from version 3.0.100 onwards, they will be distributed in the form of exapack packages.
All new packages will be in the form of numbered volumes Here is an example of nomenclature

Default Library
-----------------------

- **XTRPbr_05k_vol_1.exapack**: Contains files from ½k, previews, and data files
- **XTRPbr_1k_vol_1.exapack**: Contains files from 1k, previews, and data files
- **XTRPbr_2k_vol_1.exapack**: Contains files from 2k, previews, and data files
- **XTRPbr_4k_vol_1.exapack**: Contains files from 4k, previews, and data files
- **XTRPbr_8k_vol_1.exapack**: Contains files from 8k, previews, and data files
- **XTRPbr_Procedural_Vol_1.exapack**: Contains procedural files, previews, and data files


The packages are consecutive, Vol_1, Vol_2, Vol_3, I tried to limit as much as possible the size of the packages,
so that their maximum is around 4GB (Some can reach 4.3GB).
This limit to avoid download and installation problems, since those who have a slower connection, could
encounter timeout problems.

.. Note::
        The large size packages like 4k, 8k will have more volumes, because they are much larger.
        The small size packages like ½k, 1k, 2k  will have fewer volumes, because they are much smaller.

------------------------------------------------------------------------------------------------------------------------


The **.exapack** files are installed by the addon, they do not need to be installed manually! After installing the
Extreme PBR addon, it will manage your exapack packages and install them. (You will see in the following steps)



.. important::
        **For Mac users:** it often happens that Safari Browser is set to decompress .zip files, make sure this does not happen,
        otherwise the .zip file will no longer be a .zip file and you will not be able to install the addon as follows.

        Just go to the Safari menu bar at the top left and click on Safari>Preferences, then remove the check mark from
        "Open safe files after download" in the "General" window. Done, if in the future you download zipped files with safari,
        they will no longer be unzipped.


------------------------------------------------------------------------------------------------------------------------

Bundle Installation SuperHive
================================

This step is only necessary if you purchased the **Bundle Version** of Extreme PBR on SuperHive (Formerly BlenderMarket)

.. image::
    _static/_images/installation/bundle_april_2025.webp
    :align: center
    :width: 600
    :alt: Bundle installation

|


- Download the 3 zip files named **XPBR_Part_1.zip, XPBR_Part_2.zip and XPBR_Part_3.zip**
- Extract all 3 zip files into a folder of your choice
- Proceed with the classic installation of the addon as explained below

.. image::
    _static/_images/installation/bundle_files_01.webp
    :align: center
    :width: 600
    :alt: Bundle installation


|


Once unzipped you should have these files as you see in the image:

.. image::
    _static/_images/installation/bundle_files_02.webp
    :align: center
    :width: 400
    :alt: Bundle installation

|

You can now proceed with the installation of the addon as explained in the next chapter





