.. _troubleshooting:

Troubleshooting
===============

In this section there are some tips to solve known problems.
This section will be updated over time based on the major problems encountered by users.
Problems related to Extreme PBR bugs are usually solved. Here are some of the most common problems.
Question and answer


I do not receive mail from BlenderMarket
-----------------------------------------

Make sure you consented to receive emails from creators in your Blender Market account preferences:
https://blendermarket.com/account/privacy-center/consents

------------------------------------------------------------------------------------------------------------------------

Find Options Menu
------------------

To go to the Extreme PBR options, you have to go to the addon preferences. But to make this process easier there is
a button directly in the Extreme PBR interface:

.. image:: _static/_images/troubleshooting/options_button_01.webp
    :align: center
    :width: 600
    :alt: Options Button 01

------------------------------------------------------------------------------------------------------------------------

Relink Libraries
-----------------

If for some reason, for example:

- You moved the Extreme PBR libraries to another folder
- You copied the Extreme PBR libraries to another computer

You have to indicate the paths of the Extreme PBR libraries which are usually 2 folders called respectively:

- **EXTREME_PBR_DEFAULT_LIB** (Extreme PBR default library)
- **EXTREME_PBR_USER_LIB** (Extreme PBR User Library, which could also be empty, since it is the one where you can
  save your personal libraries)

So go to ``edit--> Preferences--> Addons--> Extreme PBR --> Libraries``

Now indicate the paths to the folders mentioned above.


.. seealso::
    Here is the link to the page that refers to the libraries section: :ref:`pr_libraries`

------------------------------------------------------------------------------------------------------------------------

Pink Materials
-----------------

It may happen that there are files that referred to the material that have been moved, so the material
no longer has a reference image.

Here's how to do it: :ref:`pr_op_fix_materials`

.. image:: _static/_images/troubleshooting/pink_materials.webp
    :align: center
    :width: 600
    :alt: Pink Materials


------------------------------------------------------------------------------------------------------------------------

Black Materials
----------------

In this case there may be a problem when creating a file in a newer version of Blender, and then after saving the project
it is opened in a previous version of Blender.

Sometimes Blender updates its nodes, so it may be that the nodes are no longer retro compatible with the previous version.
To solve this I have provided a function that tries to replace the "Unknown" nodes

You can find it in the Extreme PBR Options menu in this paragraph: :ref:`pr_op_adjust_all_material_node_tree`



------------------------------------------------------------------------------------------------------------------------

Moving libraries to another computer
------------------------------------

To move the libraries to another computer, just copy the "EXTREME_PBR_DEFAULT_LIB" and "EXTREME_PBR_USER_LIB" folders


If once connected the libraries from the "Libraries" menu in Extreme PBR preferences the addon does not work,
it could be that in the folders mentioned above, the "._data" folders are missing, so make sure they are inside each library.

.. image:: _static/_images/troubleshooting/data_folder.webp
    :align: center
    :width: 600
    :alt: Data Folder

|

- **To Show the hidden folders in Windows:**

    1. Open File Explorer from the application bar.
    2. Select View > Options > Modify folder and search options.
    3. Select the View tab and in Advanced settings, select Show hidden folders, files and drives and OK.

- **To Show the hidden folders in Mac:**

    1. Access the folder where you think there are hidden files.
    2. Step 2: Press the keys "Command + Shift + (.)"

    Or:

    1. In Finder, open up your Macintosh HD folder
    2. Press Command+Shift+Dot
    3. Your hidden files will become visible. Repeat step 2 to hide them again!

- **To Show the hidden folders in Linux:**

    Press the menu button in the top-right corner of the window and select Show Hidden Files, or press Ctrl+H.

------------------------------------------------------------------------------------------------------------------------

.. _troubleshooting_auto_pack_resources:

Why if I export the project to another computer I can no longer see the materials?
------------------------------------------------------------------------------------

This is quite normal, by default blender does not package images in .blend files, to do this you have to go to

- File > External Data > Automatically Pack Resources

Then save the project, and finally you can move it to any other computer. It will contain all the images you used.

Pay attention to this, because your .blend files after these operations will contain all the image files present
in your project is present an image of 100MB (For example) your .blend file will become 100MB more.


.. image:: _static/_images/troubleshooting/auto_pack_resources_01.png
    :align: center
    :width: 600
    :alt: Auto Pack Resources 01


------------------------------------------------------------------------------------------------------------------------

What has changed from 4.0.X series to 4.1.X series?
-----------------------------------------------------

The new features and changes described here: :ref:`updates_log`

The important change that occurs in the new Extreme PBR 4.1.x series is the fact that now the libraries are in .exapack
format, this is a format for distributing the files of the library (Just like in HDRi Maker) that allows you to install
the libraries in a simple and fast way.



.. important::

        The change of course towards the distribution of libraries in .exapack format took place for 2 substantial reasons:

        - Some users found that having to register for free on Extreme-Addons.com to be able to download the libraries
          was a nuisance (And I understand it)

        - In some parts of the world, the server speed for downloading libraries was slow (In any case
          on request I have already provided the libraries several times via an alternative download. This was the most annoying
          of the problems and I understand how annoying it was to contact me for this.

        So for this reason I decided to keep the download service active for those who wanted to continue using it
        but substantially I'm trying to move towards the .exapack format.

        **My consideration:**

            I apologize for the server speed inconvenience, but I really did my best to solve the problem
            with those who are managing the site for me at the moment.

        **With this distribution system you will no longer need to download the libraries from Extreme-Addons.com and
        consequently there is no need to register on it**




If you want to continue using the extreme-addons service

- you just have to go to the addon options and click on **I have an Extreme Addon account** from the addon oprions
  here is how to do it: :ref:`pr_op_i_have_an_account_on_extreme_addons`


------------------------------------------------------------------------------------------------------------------------


Fix Materials of Extreme PBR created with the version of Blender 3.x.x in Blender 4.x.x or vice versa
---------------------------------------------------------------------------------------------------------


.. image:: _static/_images/troubleshooting/wrong_nexus_system_example_01.webp
    :align: center
    :width: 600
    :alt: Wrong Nexus System Example 01

|

Between versions 3.x.x and 4.x.x of Blender the Principled BSDF node of Blender has changed, there are 2 ways to solve
this problem, Extreme PBR will automatically recognize the version in use and will convert the materials in order to
make them compatible with the version of Blender you are using.

- **Solution 1:**

    - Select the object that contains the material, if the nodes present are not compatible select the material and press
      the **Convert Module System** button this button will convert all the materials present in the project to the system
      of nodes necessary to work correctly in the version you are using of Blender.

    .. image:: _static/_images/troubleshooting/convert_module_system_button_01.webp
        :align: center
        :width: 400
        :alt: Convert Module System Button 01



- **Solution 2:**

    - Go to the Extreme PBR Options menu and press the **Adjust all material node tree** button this button will convert
      all the materials present in the project to the node system necessary to work correctly in the version you are using
      of Blender. Here is the reference to the indicated button :ref:`pr_op_adjust_all_material_node_tree`

    .. image:: _static/_images/troubleshooting/open_options_02.webp
        :align: center
        :width: 400
        :alt: Open Options 02



------------------------------------------------------------------------------------------------------------------------


Why are the materials black sometimes?
---------------------------------------

This could depend on which version of Blender you are using, in particular if for example you used a
New version of Blender or in Alpha or Beta version.

In the first case, if you created a project in Blender (For example in blender 3.5) and you opened the project in an older version of blender
(For example Blender 3.0) it could happen that the materials are black. This depends on the fact that
in Blender 3.5 there are new nodes that did not exist in blender 3.0, so it may have damaged the project.

This can be solved: Make sure you have a version of Extreme PBR 4.0.205 or higher and by going to "Options"
from the Extreme PBR preferences menu and from there press the button
"Adjust all material node tree" this should fix the nodes no longer recognized.


------------------------------------------------------------------------------------------------------------------------


I have the library on One Drive, I can't hook Extreme PBR to that library
---------------------------------------------------------------------------

First of all make sure that the synchronization is complete, as the files may not have been downloaded yet
on your computer via One Drive.


And Pay attention to this:

One Drive shares files on the cloud, so they may not be physically on that path, so Extreme PBR will not be able to
communicate with the files that are on the cloud, since it does not have access to the One Drive APIs. This is a known
problem, but it doesn't really depend on Extreme PBR or Blender. This should be handled so that the libraries are physically
on your Hard Disk.



.. important::

        In the 100% of the cases that have been reported to me, this problem is always related to the synchronization with One Drive
        so make sure you manage your files with your One Drive as best you can, because Extreme PBR only works if the files are really
        synchronized and present on your Hard Disk.
        Take a moment to check your One Drive situation carefully



------------------------------------------------------------------------------------------------------------------------


I can't find the paths of the libraries on my Nas
---------------------------------------------------


This is solvable simply by copying and pasting the paths into the address bar of your operating system's file manager
and then pasting them into the Extreme PBR library path text field.


.. image:: _static/_images/troubleshooting/copy_path_nas_01.webp
    :align: center
    :width: 600
    :alt: Copy Path Nas 01

------------------------------------------------------------------------------------------------------------------------


Material icons not visible
---------------------------


A problem is quite well known with the Blender Template Preview Icons, which in some situations may not be
loaded correctly by the addon, to solve this problem a Button has been inserted which once pressed, reloads
the Icons, making it possible to view them correctly. Here you will find the paragraph that indicates the button::ref:`mp_reload_preview_icons`


.. image:: _static/_images/troubleshooting/preview_icons_not_load_01.webp
    :align: center
    :width: 600
    :alt: Preview Icons Not Load 01


------------------------------------------------------------------------------------------------------------------------

How do I check the version of the addon?
------------------------------------------

If the addon is installed, press the button that sends to the options, a popup will open directly on the addon preferences,
where the version is also shown:

.. image:: _static/_images/troubleshooting/check_addon_version.webp
    :align: center
    :width: 800
    :alt: Check Addon Version

|

If the addon is not active, you can check the version of the addon by going to: ``Edit--> Preferences--> Addons``
and looking for the addon ``Extreme PBR``

.. image:: _static/_images/troubleshooting/check_addon_version_02.webp
    :align: center
    :width: 800
    :alt: Check Addon Version 02


------------------------------------------------------------------------------------------------------------------------


I get an error when activating the addon
------------------------------------------


Sometimes when installing a new version of Extreme PBR if we already had one installed previously, some modules
Python could create conflicts, so it will not be possible to activate the addon.

If this is your case (That is, you were updating to a newer version of the addon, follow these steps indicated
below the image:


.. image:: _static/_images/troubleshooting/error_at_activation.webp
    :align: center
    :width: 600
    :alt: Error At Activation

|


- **Step 1:**
    Unistall the addon by pressing Remove Button:

    .. image:: _static/_images/installation/uninstall_example_panel.png
        :align: center
        :width: 600
        :alt: Uninstall Example Panel

- **Step 2:**
    Save the preferences by pressing the button: ``Save Preferences``

    .. image:: _static/_images/troubleshooting/save_blender_preferences.webp
        :align: center
        :width: 600
        :alt: Save Blender Preferences

- **Step 3:**

    Close all Blender windows and reopen Blender

- **Step 4:**

    Reinstall the addon by following the update instructions: :ref:`update_only_the_addon`


If this does not solve the problem, I invite you to contact me and report the error you receive,
it could be a Bug :ref:`contact_assistance`

























