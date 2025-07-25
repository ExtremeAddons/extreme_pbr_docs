.. _updates_log:

Updates Log
===========

4.1.134
-------

**Release date: 22-07-2025 (D/M/Y)**

- **Bugfix - Crash when applying procedural materials**

    Crash in Blender when applying procedural materials, this happened especially on Linux and Mac.

- **Bugfix - SuperHive Button**

    Pressing the 'SuperHive' button (Ex 'BlenderMarket'), the browser opened the Extreme PBR documentation page, now it opens to the right page

- **Update - SuperHive Labels and Text**

    Updated the labels and texts where 'BlenderMarket' was present, now it has been replaced with the new name which is 'SuperHive'



--------------------------------------------------------------------------------------------

4.1.133
-------

**Release date: 13-06-2025 (D/M/Y)**

- **Texture paint brushes disappearing in Blender 4.3 and above**

    In Blender 4.3 and above, texture paint brushes were disappearing from the asset browser when Extreme PBR's interface was present. This was due to a Poll function that caused a redraw, leading to a conflict that made the brushes disappear. This version of Extreme PBR resolves this issue completely.



--------------------------------------------------------------------------------------------

4.1.132
-------

**Release date: 17-03-2025 (D/M/Y)**

- **Compatibility with Blender 4.4**

    The APIs of Blender 4.4 to change the Brush have been changed, so this update was necessary to maintain compatibility. Make sure you are using this version of Extreme PBR to avoid errors during painting.



--------------------------------------------------------------------------------------------

4.1.131
-------

**Release date: 16-02-2025 (D/M/Y)**

- **Bugfix for Linux and Mac - Paint Error in Blender 4.3**

    Pressing the button for painting, an error was displayed, and the painting did not start, this happened only on Linux and Mac with Blender 4.3 and not on Windows, this is because the new Extreme PBR creates a custom Brush in the Browser and there was an error in the selection path of such a brush, now it has been corrected. If you are using Blender 4.3 on Linux or Mac and you have encountered this problem, make sure you are using this version or higher



--------------------------------------------------------------------------------------------

4.1.130
-------

**Release date: 20-12-2024 (D/M/Y)**

- **Blender 4.3 Bugfix - Texture Paint**

    In some cases (Still to be clarified well which) the painting of Extreme PBR did not work well, this was due to the impossibility of changing the color of the brush in use. This has been solved by creating the Extreme PBR brush and inserting it into the resources of the new brush asset browser making it selected in the asset browser. This problem probably occurs due to a known problem in Blender, that is when you receive this error: **'Warning: Tool 'builtin_brush.Draw' not found for space 'VIEW_3D''** This Blender bug made it impossible to change the color of the brush. It has been solved.

- **Blender 4.3 improvement - Paint Brush**

    As described above, now the Extreme PBR brush once the texture paint is started, will be created and inserted into the 'LOCAL' asset browser, the brush in question will report the Extreme PBR logo to make it recognizable, but it will be managed autonomously by Extreme PBR

- **Important Improved - Bake System (BSDF Mode)**

    Thanks to some reports I took into consideration to review the Bake system (Only Under the hood for now), Now the resulting Bake maps will be much more accurate than before, as the old system tended not to produce a correct range on the RGB channels of the resulting texture. Especially on Black and white maps, such as: Alpha/Roughness/Metal/Etc. This has been solved by Baking these maps on a Blender Emission node. The whole system uses separate nodes, while previously the Principled BSDF of the material itself was used

- **Improved - Bake Alpha**

    The alpha bake could make the object slightly transparent in points where it should not be. With the new Bake system this has been solved

- **Improved - Bake Options**

    Some users reported to me the difficulty in understanding how to set the Bake, the default bake had the 'Uv Map Source' setting set to 'Use active', this could create confusion especially on less experienced users, making the Bake incorrect. Now the default setting is 'Create New', this makes the Bake much simpler and more intuitive

- **BugFix- Bake Emission Transmission**

    If on the object there were 2 or more materials, of which 1 did not have emission or transmission, the Bake of the emission/transmission was not carried out in the most recent versions of Blender, this has been solved

- **Fix - Bake Emission with paint material**

    If you painted between 2 or more materials, and one of these had the emission and the other did not, the emission map was not correct. This has been corrected by inserting a multiplier with 'Clamp' to keep the range between 0-1 that multiplies the emission strength for the emission map

- **Improved - Bake**

    For security reasons the Bake is performed on a 'Copy' material, this copy material was not named in any way, now a suffix '_TEMP_COPY_BAKE' is added and a property that makes it recognizable by Extreme PBR such copy material. The material is also deleted at the end of the Bake cycle. This makes things less confusing and cleaner.

- **Improved - Bake Error**

    If you abort the Bake with 'ESC' or if an error occurs during the Bake (Without crashing Blender) the objects will be re-selected as they were at the start of the Bake



--------------------------------------------------------------------------------------------

4.1.129
-------

**Release date: 14-11-2024 (D/M/Y)**

- **Blender 4.3 Support - Material Preview**

    Material Preview in Blender 4.3 still had a Bug, there was still a condition in the code that could cause an error in Blender 4.3 as the icon used for the Material, no longer exists in Blender 4.3

- **Blender 4.3 Support - No Module Named toml**

    The Python module 'toml' is no longer included in Blender 4.3, it has been replaced by the tomllib module, this module is used to read the blender_manifest.toml file.

- **Blender 4.3 Support - 'bpy_prop_collection[key]: key shadow_method not found**

    This error is displayed because the new EEVEE_NEXT engine no longer has that property, so a condition has been inserted that checks the version of Blender and if it is greater than 4.2, the shadow_method property is no longer set, as it is no longer necessary. All the code if it encounters the shadow_method property now ignores it if the version of Blender is greater than 4.2

- **Blender 4.3 Support - Some APIs have changed**

    Some Blender APIs such as 'shadow_method', 'use_gtao_bent_normals', 'use_ssr_refraction' etc, related to the EEVEE render engine, have been removed in Blender 4.3 (Rightly) Extreme PBR uses these APIs in previous versions to configure the scene to the best, now they are no longer used so they caused errors. Some conditions check the version of Blender and if this is greater than 4.2, the old APIs are no longer used.



--------------------------------------------------------------------------------------------

4.1.128
-------

**Release date: 10-10-2024 (D/M/Y)**

- **Bug Fix For Blender 4.3 - Show Material Preview Options**

    Show Material Preview option has been removed, as it was not very useful, in addition in Blender 4.3 if 'Show Material Preview' was disabled, the icon that was supposed to be shown created an error, as the icon named 'BRUSH_TEXFILL' is no longer present in the native icons of Blender.

- **Changed - Security check before creating asset browser**

    When starting the creation of the asset browser, a security check checks if the current project is saved, and how many materials, objects or worlds are in the project, this to avoid compromising the project. This limit goes from 5 objects-5 materials-5 worlds to 10 of each type. As some users have set default scenes with more than 5 objects, materials or worlds, always maintaining a safety margin. This is necessary at the moment because the operator that creates the asset browser uses the current project to create the asset and needs to delete the objects in the scene.

- **Error message in Blender 4.2 onwards**

    From Blender 4.2 onwards, it could happen that in the console you could receive an error when applying a material or creating the asset browser that reported 'Unable to set the property' this is now bypassed as these properties were type: 'Blend Mode', 'Shadow mode' etc... All properties that with the integration of Raytracing from Blender 4.2 are no longer present as they are no longer needed.

- **Bug Fix - Error when Removing 'Shader Overlay' Material**

    It could happen that by removing the shader Overlay, an error was reported. This is consistent with the error described above, as the addon was trying to set the old parameters prior to Blender 4.2, a try-except has been inserted to prevent the error from occurring.

- **Bug Fix - Message when Bake is aborted**

    From Blender 4.3 if you open the Bake Panel and do not bake, an error message said that you could not export the FBX because there is no module (Addon) to do it, This is not true. The problem has been solved by moving the check into the Invoke function of that operator, while before it was in the execute function.



--------------------------------------------------------------------------------------------

4.1.127
-------

**Release date: 27-06-2024 (D/M/Y)**

- **Conflict with material preview in Blender 4.2**

    On Blender 4.2 Extreme PBR could conflict with HDRi Maker or other addons due to the new APIs of Blender 4.2 and the new names of the addon modules, this problem has been solved.



--------------------------------------------------------------------------------------------

4.1.126
-------

**Release date: 17-06-2024 (D/M/Y)**

- **Compatibility with Blender 4.2**

    The new extensions/addons system uses a new blender_manifest.toml, which replaces the old bl_info, an update has been made to make Extreme PBR compatible with Blender 4.2 while maintaining retro-compatibility with previous Blender versions

- **Important Note:**

    It is not recommended to save Materials into User Library in Blender 4.2 and use them in previous versions, as the new APIs of Blender especially those of Raytracing are not present in versions prior to 4.1, the use cases in which the properties of such material could be lost, are in Eevee, which: (Transparencies, Transmission, Subsurface Translucency) these 3 properties cannot be saved together with the material, as in Blender 4.2 they are not strictly necessary, unlike previous versions. As for all materials saved in previous versions, including the Default Library, code has been added to recognize these properties and convert them into properties compatible with Blender 4.2, so as not to lose the properties of materials saved in previous versions.



--------------------------------------------------------------------------------------------

4.1.125
-------

**Release date: 09-06-2024 (D/M/Y)**

- **Important Bugfix**

    When trying to do a Worn edges in Blender 4.1 an error appeared that made it impossible to complete the procedure 'copy_ob.data.use_autosmooth' was headed as an error, in fact this is a piece of code that due to an oversight has not been modified as this API in Blender 4.1 is no longer present. This is now fixed

- **Save Material**

    Due to the same problem described above, it could happen that during the saving of the materials, the same error was encountered. This has been corrected



--------------------------------------------------------------------------------------------

4.1.124
-------

**Release date: 20-04-2024 (D/M/Y)**

- **Improved - Autosave Paint Image**

    After various reports from users who complained about the loss of painting done on materials if Blender was closed without saving or due to an anomalous crash, and after ascertaining that it is a known problem of Blender also reported here at this link: https://projects.blender.org/blender/blender/issues/45636 I decided to implement a system of semi-autosave of painting images, now when you enter painting mode with Extreme PBR or press STOP PAINT or use FILL button, all images of type PAINT present in the active material will be analyzed, if even just 1 of these images is_dirty == True this means that the image needs to be saved, so the function will save all the modified images with the operator bpy.ops.image.save_all_modified() This **greatly** reduces potential job losses due to an anomalous crash or an unwanted closure of Blender, in addition it keeps the interface fluid. I could have integrated it during painting, but I preferred to keep the painting as fluid as possible, so I decided to implement it in this way

- **Fix - Bake System**

    The Bake of Extreme PBR allows you to export the model in FBX format, to do this you use one of the addons distributed with Blender whose module is called **io_scene_fbx**, natively this module is active, but it could happen that the module was deactivated by the user. Now if the module is deactivated, during the process of the Bake of Extreme PBR it will be checked if the **io_scene_fbx** module is active, in case it is deactivated, it will be activated avoiding an error during the bake and the consequent block of the process

- **Fix - Material Editor Expansion Nexus Materials**

    Improvement of the reading of Nexus materials in the Material Editor Panel regarding the simplified Nexus modules, that is, those group nodes with a Shader output, for the moment such nodes will be read if Tagged (For example those of Cyber Holograms expansion) At the moment as it is not possible to add an FX Module to them, the FX button will not be shown, and as the simplified Modules do not have the possibility for the moment to be Painted with other standard Nexus modules, the 'Add ... to new Module' button will not be shown

- **Added - Library Info**

    In the 'Info' panel of the material, it is now possible to view information about the current library, so as to understand which version of the library you are using. This was added as an update to our Cyber Holograms expansion library, so as to understand if you are using the old or the new expansion

- **Fix - Microdisplacement not work in Blender 4.1**

    Microdisplacement did not work in Blender 4.1, this is because the new APIs of Blender 4.1 have changed from material.cycles.displacement_method to material.displacement_method, a condition has also been put that makes it backward compatible with previous versions of Blender

- **Fix - data_materials Enum none**

    When a material was removed with Extreme PBR the data_materials enum of Extreme PBR shows None, now when a material is removed with Extreme PBR this property is always set to the first available



--------------------------------------------------------------------------------------------

4.1.123
-------

**Release date: 22-03-2024 (D/M/Y)**

- **BugFix - Error case with apply material**

    In some cases an error appeared when trying to apply a material or replace it, the error was minimal, as it could happen quite casually, this was because in some cases the k_size name selector, the one used to set the type of material, did not have any option selected, so it was null, this happened especially when a material without k_size variations was applied, so no button could be pressed, the material preview had to be changed and returned to it. Now this will not happen anymore as a function has been inserted in the operators that apply the material, which will check that the k_size is selected, otherwise it will be selected through this function

- **BugFix - Material not applied correctly in Blender 3.3**

    The material was applied with the Mix RGB node coming from the Blender 3.6 version, so it was an unknown node in Blender 3.3, the function that was responsible for replacing this node, was not working in the correct way, so it was fixed

- **BugFix - Asset Browser creation in Blender 3.3**

    As above, the function that was supposed to eventually convert the Mix RGB nodes into those for Blender 3.3 was not working, so even the Asset Browser was potentially created incorrectly (Only in Blender 3.3)

- **BugFix - Load Texture with Shift Key**

    In case you were on a USER library, or an Expansion library (With the libraries selector) by pressing the 'SHIFT' key and the ADD NEW button, the file search browser was opened, but when selecting the image files to import as textures, no material was created, this has been fixed

- **Improved - Save Editor**

    It was chosen not to show the 'Save Editor' panel when the selected object had no material, or when no object was selected, this made things complicated if you just wanted to interact with the user libraries, so now the Save Editor panel will also be shown when those 2 cases occur

- **BugFix - Displacement button not show for materials saved as Nexus Modules**

    The displacement button was no longer present if a Nexus module had been saved with the appropriate 'SAVE MODULE' button in the 'SAVE EDITOR' panel, this because the saved material was not recognized as a Nexus material, so to solve the problem the function that shows the displacement button (Obviously if the Bump or Displacement texture is present) will search for Nexus modules, regardless of the type of Material.

- **Added - Activate Material Nodes**

    If some material on the selected object does not have the nodes active (That is mat.use_nodes) a button Activate Material Nodes will be shown in the Material List of Extreme PBR so as to set the mat.use_nodes property to True so that the material can be displayed correctly (If the material has nodes)



--------------------------------------------------------------------------------------------

4.1.122
-------

**Release date: 04-03-2024 (D/M/Y)**

- **Patch - Extreme Addons Tab**

    The Extreme Addons menu was still displayed, this menu has been removed at the moment because the addon no longer needs to be registered on the Extreme-Addons website, this created confusion. It happened in case the (Now removed) setting 'I have an account on Extreme-Addons could result in True

- **BugFix - Import Media Texture Manager**

    The Import Media button inside the Texture Manager, produced an error caused by an update of this operator, it was corrected as this operator now no longer uses the ImportHelper APIs of Blender and the variable of the single file setting had not been updated



--------------------------------------------------------------------------------------------

4.1.120
-------

**Release date: 04-03-2024 (D/M/Y)**

.. raw:: html

    <iframe width="560" height="315" src="https://www.youtube.com/embed/83ZLK41mu40?si=s0iZ0hEFN5gs3hUF" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

|

- **Added - Add material on multiple objects**

    Now by pressing Add Material Button it is possible to add a material to multiple selected objects, provided that the selected objects do not have any assigned material and not even an empty material slot

- **Added - Shortcut to add basic new Material**

    **By pressing the ALT key on the keyboard and pressing the 'Add New' button** from the Extreme PBR panel, a basic material will be added with the basic Principled BSDF and Material Output nodes

- **Added - Shortcut to remove all materials from multiple objects**

    By Pressing **Shift + Remove Material Button** is now possible to remove all the materials from the selected objects

- **Added - Shortcut to Import Texture on the fly**

    By pressing Shift and one of the following buttons: (Add New, Replace Material, Add Fx, Replace Fx, Replace Module) the image search browser will open, this is essentially the equivalent of Shader Maker Auto PBR, only now it is no longer necessary to go to the Shader Maker category to import textures automatically, the operation is the same as before, only with a shortcut

- **Added - Shortcuts Material Editor**

    If you are working with multiple Nexus or Fx modules, you can now close or open a row by pressing the *Shift + Show/Hide Group* button or by pressing *CTRL and Show/Hide Group* to close or open all groups (Modules and Fxs) at the same time

- **Added - Material Preview Finder**

    From this version of Extreme PBR, every time you add a material to an object, it will be stored if the material comes from a library attached to Extreme PBR, through the material icon in the list of material slots on the object, now it is possible to press it, a popup will ask if to proceed, this allows you to set the preview system of Extreme PBR on the material in use. Example: The applied material is Grass 001 version

- **Improved - Replace Material-Replace Module**

    Now if you try to replace a material in which textures are contained, for example at 1k with the same material at 2k (From the library) only the textures will be replaced, this to keep the parameters set by the user, so as not to have to reset the parameters manually every time

- **Improved - Replace All Materials or some**

    Now if you want to replace a material that is present on multiple objects (Provided that the material is actually the same bpy.data.materials) it is sufficient to select the objects on which you want to replace, it is also possible to select all the objects in the scene as now Extreme PBR will ignore any object that does not support materials, consequently the 'Replace All' button has been removed from the main interface of the addon (Next to the Material List Section) The replace material will continue to replace only 1 material at a time provided that only 1 object is selected

- **Improved - Shader Maker auto PBR Path**

    Before this update Auto PBR (ShaderMaker) always opened the browser on the path of Blender's addons, and did not store the last path, I modified the operator that used ImportHelper, now it no longer uses this tool that limited the functionality, now the browser will always open in the last path used (In the current session of Blender)

- **Update - Support for Smart Shade Smooth for Blender 4.1**

    Some APIs have changed in Blender 4.1 and before this version of Blender 4.1, now the Smart Shade Smooth works equally in Blender 4.1 and also in the previous versions of Blender 4.1. Note: Now The Auto Smooth Angle is set to 30 degrees by default (Like the old Blender Standard)

- **Improved - Smart Shade Smooth**

    In accordance with the point above, the Smart Shade Smooth button has been replaced with a new Popover panel, with new features such as the ability to set a default Smart Shade Smooth when applying the material

- **Update - Shader Overlay**

    On the occasion of Blender 4.1 something had stopped working, now it has been fixed. In addition, a dummy object is temporarily created for Shader Overlay, before this update, every time this object was created and remained in memory, now instead it no longer remains in memory

- **Improved - Bake System**

    In accordance with some valuable feedback received, some functions already present in some versions ago have now been reintegrated, but now they have been improved to have greater control over the bake: **UV MAP SOURCE** Allows you to choose which UV mapping to use for the Bake, if the one already present on the object or a new UV Map. If a new UV Map is chosen, there will be 2 Properties available: **UV MARGIN** which allows you to adjust the margins of the uv mapping before the Bake. **MAKE SMART PROJECTION** allows you to perform an additional Smart projection that allows you to further set a UV mapping on the fly better if the default one does not give satisfactory results

- **Improved - Paint Mask Autosave**

    It has been reported many times that after painting a material, when reopening Blender the painting disappeared, this is because it was not saved before exiting Blender (You need to activate 'Save Prompt' from Blender preferences), now this is no longer necessary as when you press 'Stop Paint', all changes are saved instantly, and there is no longer any need to save the changes to the image. I think this was necessary as many users encountered this problem. This makes the workflow more linear and error-proof

- **Improved - Purge Data**

    When you paint a material or create a mask from the FX Layer, these images are automatically packed into the Blender file so even if the images were no longer present in any material, they were not deleted, now a function has been added that searches for all the textures inside the materials, if these are not present in any material they will be deleted by pressing the 'Purge Data' button of Extreme PBR

- **BugFix - Bake Mode Principled BSDF**

    It also happened that if you chose the Principled BSDF bake mode, and the materials did not contain a Principled BSDF node, the bake did not stop and an error was raised, this because the function used to check the existence of a Principled BSDF did not work well, now it has been fixed and if you try to bake in Principled BSDF mode when even just 1 material of the objects selected for the bake does not contain a Principled BSDF, the bake is blocked and a message is thrown to warn that it is not possible to bake in this mode, as the Principled BSDF is absent in the material node tree

- **BugFix - Purge Unused Slots**

    If the selected objects were in Edit Mode, and the 'Purge Unused Slots' button was pressed, an error occurred, this because the code was not able to manage the objects in Edit Mode, now it has been corrected and it works correctly even in Edit Mode

- **Bug Fix - Panel Labels**

    The Extreme PBR APIs had an error that hid the possible description of the socket above it in the various material editors if such a description was present.

- **Bug Fix - Remove Material remove Displacement**

    When a material was removed from an object and the material was present on multiple objects, the displacement was turned off on all the objects to which the material with the displacement had been applied. Now it no longer happens

- **Bug Fix - Search data materials and apply remove the displacement**

    When a material was applied via the 'Search Data' button, the displacement was turned off on all the objects to which the material with the displacement had been applied. Now it no longer happens

- **Bug Fix - Replace Material remove Displacement**

    When a material was replaced with another material, the displacement was turned off on all the objects to which the material with the displacement had been applied. Now it no longer happens

- **Bug Fix - Transmission is shown in the Material Editor**

    The Transmission property was shown even if it was not set as usable, this created confusion, as the property was not really connected to the Principled BSDF Transmission node

- **Bug Fix - Painter**

    If the material 'Painter' was added from the 'Shader Maker' category, the painted color did not correspond to the one chosen because the Hue parameter was set to 0.0 instead of 0.5 (This only happened from Blender 4.0 onwards)

- **Bugfix - Subsurface always active on Fx Layer**

    From Blender 4.0 onwards, the Fx Layer nodes were set by default with the Subsurface Strength property at 0.05, this was not correct, as it happened on all materials applied as Fx Layer, now it has been set to 0.0

- **BugFix - Documentation Right Click**

    The operator that takes you to the documentation with the Right click was based on a WM_MT_button_context class, this class went into conflict at the time of registration if other addons made use of this class, according to the Blender documentation, that method in addition was already obsolete, so we corrected the use using bpy.types.UI_MT_button_context_menu.append(). This method no longer conflicts with other addons and in addition keeps pace with Blender's APIs

- **BugFix - Secular Value at 0.0**

    In Blender 4.0 or higher versions the Specular value was set to 0, now it is set to 0.1 as it has always been unless the material has its properties registered in the material json file

- **BugFix - Search and replace Module**

    It happened that on the Nexus modules if there were 2 or more modules, when a module of Material type Chess, or others from the procedural library was replaced, the 2 modules that had to be exchanged in position disconnected from the mixer, this was avoided by putting the function to link all the modules to the mixer at the end of the operator, in addition, the mixer was loaded incorrectly if the central modules were replaced when there were 3 or 4 modules present in the material, this because the number of modules present in the material was not counted, this was solved by counting the number of modules present in the mat.node_tree.nodes

- **BugFix - Fill Un-Fill Fx**

    The Fill and Un-Fill Fx buttons did not turn off the Paint and Un-Paint buttons of the Fx, now they do

- **BugFix - Remove Empty Slot remove Displacement**

    The Remove Material button, if an empty material slot was removed, also removed the displacement on the object, now a condition has been put for which if the slot is empty, it does not remove the displacement (Only if there is a material in the ob.data.materials with an active displacement)

- **Removed - I Have an account on Extreme-Addons**

    Due to a problem with those who manage our website, this function has been temporarily removed



--------------------------------------------------------------------------------------------

4.1.115
-------

**Release date: 16-01-2024 (D/M/Y)**

- **BugFix - Reset Offset Button (Alert button)**

    When using the displacement (Modifier) and modifying the following properties (Location, Rotation, Scale) The reset offset button button that rightly appeared as a warning and button, produced an error once pressed. The error was a simple typo in the Python code of a variable, it was fixed.

- **BugFix - Shader Maker Video**

    When adding a video via Shader Maker video, the following values (Hue, Exposure, Saturation) were not set correctly, so the video assumed artifact colors that did not respect the original video, so it was corrected by setting the default values correctly



--------------------------------------------------------------------------------------------

4.1.114
-------

**Release date: 03-12-2023 (D/M/Y)**

- **Fix - Bake Black Edges**

    The Bake produced black edges in the resulting image, this has been fixed

- **Added - Bake Margin-Margin Type**

    Added the 2 parameters that are normally set from the scene, 'Margin' and 'Margin Type', now it is possible to set them directly from the Bake panel

- **Removed - Bake Island Margin**

    This parameter has been removed from the Bake panel as it is no longer necessary in the Bake process

- **Improved - Bake Scene properties**

    The Bake process modified some properties of the scene in use, this was not really the best practice, now before starting the Bake, the properties of the user scene (cycles, bake, eevee) are saved in a dictionary, at the end of the bake these properties will be restored so as to keep the user scene unchanged

- **Added - Texture Manager Texture Icon**

    The texture manager button will now show the icon of the texture in use above the button, previously a generic IMAGE icon of Blender was shown.

- **Optimized - Update Menu**

    The Update menu, in the addon preferences, was very slow, as it examined files on the hard disk many times unnecessarily, now everything is stored in some variables that keep the json files in memory, this has speeder up the menu by about 400x times, which now it is much more fluid than before

- **Bug Fix - Remove Volume Installed**

    There was a bug in the operator to remove the installed exapack volumes that did not allow to display the Popup message before starting the operation, in addition this operator did not remove from the registry of the installed exapack, the volume just deleted, these errors have been corrected

- **Bug Fix - Convert to Nexus Material Button**

    When even a single texture found in the material to be converted had the name without the extension, an error was raised. This was corrected by assigning the extension to the name of the texture, in case it was not assigned previously, the recognition takes place thanks to the native method of blender image.file_format

- **Bug Fix - User Library Material**

    Due to an error in a function, if the materials of the User Library were those saved in a version prior to Extreme PBR Nexus, an error was raised that warned that the path did not exist, an exception was put that avoids this error and allows to reload the materials of the User Library correctly

- **Bug Fix - Shader Overlay Material**

    Due to a function that did not copy the enum properties of the nodes to be copied into the destination node (Shader overlay) the Mix nodes and other nodes could not be set correctly on their enum property (data_type, blend_type) now the materials are created correctly and copied correctly

- **Bug Fix - User Library Multiple Module**

    If the saved materials contained 2 or more Nexus modules created with Extreme PBR in Blender version prior to 4.0, the addon converted the modules but did not reconnect them to the mixer, this made the materials unusable unless the 'Adjust Node Tree' button was pressed now this no longer happens, the modules are correctly connected to the mixer

- **Bug Fix - Shader Maker**

    Applying a material via the shader maker in Nexus mode, if only one image was selected, this was also set in the nodes of the 'Normal Generator' but then the color space of this image was changed, this made the diffuse image with a wrong color space. Now it has been corrected and the image maintains the original color space



--------------------------------------------------------------------------------------------

4.1.113
-------

**Release date: 24-11-2023 (D/M/Y)**

- **Fix - Metal Maps**

    Due to an error in the code, some Metallic maps were not recognized

- **Improved - Convert to Nexus Material Button**

    Now this operator also searches in the groups and subgroups of the group nodes present in the material, so as to be able to convert even the materials that have group nodes with standard nomenclature textures inside them

- **Improved - Texture Nomenclature**

    The search for Nomenclature in the name of the textures, now takes place by comparing the name of the texture in lowercase and the nomenclature standard in lowercase, this allows a greater possibility of match, since the outside is not yet well known a standard, and many people adopt Uppercase or Lowercase. So this makes the addon more compatible with textures that have a different nomenclature from the standard one

- **Bug Fix - Convert to Nexus Material Button**

    In some cases it could happen to encounter an error during the conversion, the message reported that the TextureNomenclature class did not have node_tag as an attribute, this has been fixed



--------------------------------------------------------------------------------------------

4.1.112
-------

**Release date: 23-11-2023 (D/M/Y)**

- **Fix - Misc Tab N-Panel**

    Some Extreme PBR popover panels were not registered correctly, so a TAB with the name Misc appeared, this was not an expected behavior, in addition by pressing on Misc tab Blender went into crash, this was solved by inserting bl_category = 'Extreme PBR' in all the popover panels of Extreme PBR

- **Change - Material Editor for Simple PBR and other Materials**

    Now the Material Editor if you are working on a Simple PBR material or any other material that is not Nexus type will be drawn with the Blender standard. This was necessary as the materials can be very complex or even simple, and needed a well-designed standard interface. Materials with Nexus nodes will continue to use the special Extreme PBR interface as it is dedicated and very functional

- **Added - Convert Material To Nexus Button**

    In accordance with the previous point, in the Material Editor panel, if the context material is not Nexus type, a 'Convert to Nexus' button will appear, this is used to convert materials based on textures, and will only work if the nodes contain images with standard nomenclature, otherwise it will not convert the material to Nexus

- **Improved - Try to get Displace for Any Material**

    The displace button, in the past, only worked for Nexus and Simple PBR materials of Extreme PBR, now instead the button tries to recover the displace map provided that there is a texture nomenclature of the material with the classic nomenclature standard (eg: Diffuse = diffuse, col, diff, etc ..., Normal = normal, nor, etc ...), if the displace or bump map does not exist, the button will not appear

- **Improved - Displace Type Property**

    The displace type property, before it was linked to the scene, now it is linked to the object. This is because previously switching from Displace Modifier to Microdisplacement, all the objects in the scene were converted to the chosen displacement. This was not good practice, as unselected objects should not change the type of displacement. Now this updates the type of displacement only on the active object and on all its materials (If they have active displacement) and possibly on the objects with the same data (Mesh)

- **Improved - Anti Tile For All Materials**

    The anti-tile now works on Texture-Based materials even if not created with Extreme PBR, the condition for which they work must be to have in the node tree A Coordinate node connected to the Mapping node, which in turn is connected to the texture images node and a principled BSDF and a texture connected to the Base Color input of the Principled BSDF, this is quite the standard of a simple material based on textures

- **Fix - Use Anti tile on Shader Overlay**

    Due to a code error, in the previous version it was not possible to apply an anti tile to the shader overlay material, now the possibility of applying an anti tile has been added also to the shader overlay materials directly from the shader overlay panel.

- **Fix - Panels Draw**

    Some panels were not drawn correctly regarding the nodes and their sliders both in Shader Overlay and Material Override, this has been fixed

- **Optimized - Add Material time**

    Although optimizations had already been made in the previous update, an unnecessary check was still performed on images when loading materials from the Extreme PBR Default library, this wasted too many milliseconds and unnecessarily delayed the creation of materials. Now this is optimized and the time to create the material is reduced



--------------------------------------------------------------------------------------------

4.1.111
-------

**Release date: 17-11-2023 (D/M/Y)**

- **Added - Anti Tile**

    A new anti-tile function has been added for all materials based on textures, even for those imported with Shader Maker

- **Bug Fix - Asset Browser Creation**

    An error occurred randomly, we think we fixed it by fixing the function that copied the context with bpy.context.copy(), now the context is no longer copied

- **Fixed - Asset Browser Creation Time (For Blender 4.x)**

    Speeder up the process of creating the asset browser in Blender 4, in this version of Blender, it was very slow, this has been fixed

- **Fixed - Time to create the material**

    The time to create the material via the Add-New button has been speeder up by about x4 times, as the reloading of the textures was unnecessarily attempted in the function of assigning the textures in the image nodes, now an exception has been put that prevents the reloading as it was useless

- **Bug Fix - Auto Re-Link Libraries Button**

    The Auto Re-Link button introduced in the previous version, if pressed without any .json files with the logs, this produced an error message, now instead a Popup message will be displayed that will warn that there are no libraries to be linked

- **Added - Asset Browser Size Choice**

    Added a property to select which size to choose for the creation of the asset browser, now you can choose whether to create only assets from 1/2k, 1k, 2k, 4k, 8k or All, that is all the available versions of the material (If installed) Procedural materials are always created, as they do not have a size expressed in pixels



--------------------------------------------------------------------------------------------

4.1.110
-------

**Release date: 13-11-2023 (D/M/Y)**

- **Added: Works on Blender 4.0**

    Extreme PBR now works on Blender 4.0 and also on previous versions from 3.3 onwards

- **Improved: Add material 2x faster for Nexus Texture Materials**

    A new smart system makes the creation of Materials (So the addition) much faster, as Eevee takes much less time to compile the shader, this was possible by managing the unused internal nodes and putting them on mute if they are not used

- **Removed: Subsurface Color**

    In accordance with the new Blender 4.0 which has removed the Subsurface Color socket in Blender 4.0 now the Subsurface Color will be guided by Base Color

- **Improve: Rotation XYZ**

    For some reason, the Nexus node had its XYZ Rotation properties set to Float and not Angle, now these properties will be in degrees as they already should be.

- **Added: Normal Map Space Type**

    Added in the panel the possibility to choose the type of space for the normal map, this was necessary so as not to have to open the node tree and manually modify the normal map node, based on all the normal map nodes, the Space properties of each of them will be displayed, by default Extreme PBR has only 2 at most, the classic, and the one for the clearcoat (If present)

- **Bug Fix: Clearcoat Bump Map**

    The Clearcoat Bump Map node was not created correctly, in its place a Normal Map node was created, this was not right. Now it has been fixed

- **Improve: Mapping Type and Coordinate**

    Before the Coordinate system relied on the options of the material or those of the group node, now the coordinate system is no longer managed by the mapping menu, but directly under the Material Editor, it works as before, with the difference that you can choose the coordinate system of the material and the type of Projection on the texture nodes, directly in the Material editor. This to avoid confusion, as each Extreme PBR Module can now have its own different coordinate system, which was not possible before, as it was managed by a single material property

- **Fix: Paint Mode**

    The paint mode could start in 'Gradient' mode instead of 'Color' this could be confusing as the paint could not work, now the brush will default to Color

- **Improve: Normal Map Space**

    Now from the 'Material Editor' panel it is possible to modify the Space Type of the Normal Map type nodes

- **Moved: UV Mapping Type (Mapping Editor)**

    In accordance with the previous changes, now the UV Mapping Type property will no longer be present in the Mapping Editor panel, but will be present in the material panels, at the bottom. In these panels: Material Editor, Shader Overlay, Material Override

- **Improved: Interface**

    The main box in the Material Editor, Shader Overlay, Material Override panels has been removed to give more space to the panel, in fact the global Box tended to reduce the space of the panel, now it has been removed, and the panel is slightly more spacious in width

- **Improved: Material Editor Panel**

    The Material Editor panel disappeared if you did not select an Object with an active material, this was to avoid confusion, but the interface update was not very responsive, so it may be necessary to click 2 times on the object to update the interface. Now the Material Editor panel will always be shown, with a warning message if the object or material does not exist.

- **Removed: Individual Vectors**

    The individual vectors have been removed, now they are no longer present in the Texture Manager Panel, this is for Shader Calculation savings

- **Improved: Purge Unused**

    The function that eliminated Material - Group Nodes - Images It has been improved, when you delete a material, all these objects are deleted if they were present in the Blender data but no longer used. Before it happened in a much less precise way, now it should be much more precise

- **Bugfix: Hide Microdisplacement**

    When you press the button to hide the displacement and you are in microdisplacement mode, only the subdivision modifiers were deactivated and the Displacement node was not muted, now it has been fixed, the Displacement node is muted

- **Improved: Auto Link to Asset**

    On Blender startup, if Extreme PBR has been installed, if the libraries are linked, it is checked if the asset_browser library exists in these libraries, if so, the library is added to the list of asset_browser libraries in Blender. To deactivate, set the 'Auto link asset' function to False from the addon options

- **Improved: Asset Browser Creation**

    The modal operator that creates the Asset Browser libraries has been improved to avoid as many anomalous crashes as possible

- **BugFix: Reuse images**

    The texture image loading script analyzed whether the image was already present in the project and checked whether the image had the data via image.has_data, this could happen if the image did not have has_data an error was raised in the texture loading. The script has been improved and if there is no has_data, the image is now reloaded correctly

- **Removed: Subsurface Bake**

    Since Blender 4.0 no longer has the 'Subsurface' (Color) input in the inputs of the Principled BSDF node, I decided to remove the Subsurface Bake function, as it is no longer necessary

- **BugFix: Download This Material Button Continues to Appear**

    If you had installed the libraries via server and some materials had not been downloaded, under the material preview the button 'Download This material' appeared even after installing all the materials via Exapack, now the button no longer appears, unless you activate the option 'I have an account on Extreme Addons', in this case it will be present again

- **Improved: Nexus Mixer (Only on Blender 4.0 or higher)**

    The new Nexus 4.0 system (Only on Blender 4.0) no longer needs the Mixer when 1 Nexus Module is present, this saves resources and connects the module or Fx directly to the Principled BSDF

- **Improved: Nexus Use Socket (Only from Blender 4.0 or higher)**

    Now the sockets are connected in a smarter way, they have been divided into categories: 'SUBSURFACE', 'ANISOTROPIC', 'COAT', 'SHEEN', 'EMISSION', 'TRANSMISSION', this allows you to choose whether to show the inputs of the nexus module, and consequently disconnect or connect the links to the Principled BSDF, this allows you to save resources and space in the panel, if for example you are not using the Coat (Ex Clearcoat), the sockets are automatically set at the time of creation of the material, but can be managed by the drop-down menu present in the bar to the right of the Module Material Panel

- **Improved: Popup Utility Panel Replaced**

    In order to make the interface more comfortable, I am replacing the old popup panels with popover panels, so the old popup panel that disappeared as soon as a button inside it was pressed, has been replaced with a popover panel

- **Patch: No Transmission for Ice Materials**

    By applying the materials of the Ice category, the Transmission was not set as it was not present in the mat_info.json file, now all the Ice materials are corrected with the Transmission set to 1.0

- **BugFix: Add Material problem with exapack versions**

    It happens that if the addon library has been downloaded from the extreme-addons site, and then the exapack are installed, the files not completely downloaded from Extreme-Addons are not updated, and an exa_files.json file remains, if this happened, once the button was pressed to add the material, an error appeared: 'Attention, this material version has yet to be downloaded from extreme-addons, to download this material version... etc.' now an additional case has been added in which if the material files are already present, this message is skipped and the material can be added again

- **BugFix: Shader Overlay disappears**

    If there was an overlay shader on the material and a Module was added for painting or an Fx, the node containing the overlay shader disappeared, now it no longer happens and remains inside the material

- **BugFix: Error when bake with a Shader Overlay**

    When you tried to Bake in 'Bsdf' mode and the Shader Overlay was present, an error was raised because the BSDF node was not directly connected to the material output node, this was omitted, in any case the 'Bsdf' bake with the shader overlay applied is no longer allowed, and a popup will be shown that warns that the Bake with shader overlay applied can only be done in 'Cycles Standard' and 'Combined' mode

- **BugFix: Switch from modules**

    When you tried to change the nexus module (Replacement between modules Search Module button) this once replaced did not respect the inputs values of the previous position, I proceeded to update and correct the operator which now stores the default_value values and replaces them, maintaining the logic

- **Improved: Draw Material Editor Speed**

    The time to draw the entire Material Editor panel has been improved, now it is about x2 times faster than before

- **Moved: Displacement Panel**

    The 'Displacement' panel has been moved to the 'Box Utility' bar, now it is in the form of a Popover, to be more comfortable and close to the displacement activation button (The button will be visible only if the displacement is active)

- **BugFix: Add Module o Replace in Simple PBR material_type**

    It happened that if you added a material in Nexus Mode, and then switched to Simple PBR mode, Trying to Add a Nexus Module or trying to replace it, an error was raised, as the addon tried to add a Simple PBR instead of a Nexus module. This was corrected with a condition for which the mode is changed to Nexus and the Simple PBR mode is restored at the end of execution

- **Improved: Add Material With Numeric Suffix**

    It happened that when adding some materials from the library if they were saved with a suffix for example .001 .002 .003 now at the time of import the renaming of it is attempted without a numeric suffix (Only if a material with that name is not already present in the project)

- **Fix: Simple PBR Specular**

    In most cases when the material with Simple PBR setting was applied, the Specular remained set to 0.5 if the specular map did not exist, now it is set to 0.1 by default

- **Fix: Re-Project Problem**

    When you add a Module for painting, an UV layer is automatically created, but it was not projected with the smart projection, the painting worked correctly but when you pressed 'Re-Project' the UV map was projected for the first time damaging the mapping of the current painting even if right, now this is solved by an initial projection equal to that which is carried out using the 'Re-Project' button so as not to confuse. Note: The 'Re-Project' button was created to re-project the UV mapping in case you modify the object in use, this does a correct projection, but breaks the painting (Expected behavior) use with caution!

- **Anti: Crash improved**

    The function that preserves from the crash has been improved, as it was annoying because if you were on the Cycles render engine in Preview or Solid mode, the function set Eevee, now it sets it and brings it back to the previous render engine without changing the mode to the user, this function preserves from crashes and anomalous errors that have been present for some years in Blender, the anti-crash is active by default

- **Added: Auto Re-Link Libraries Button**

    In order not to have to restart Blender once the addon has been updated, if Extreme PBR 4.x.x was already in use previously, a button appears in the context of the library menus, this once pressed will try to reconnect the addon to the previous paths to the libraries, this to avoid the annoyance of having to restart Blender because the function was and is still executed when Blender is started or a new project is loaded



--------------------------------------------------------------------------------------------

4.1.101
-------

**Release date: 04-09-2023 (D/M/Y)**

- **Improve: Paint Mask Between 4 Nexus Materials**

    The painting mask for Nexus modules, is now much more precise, the RGB channels have been replaced by painting with the values R: (1, 0, 0) G: (1, 2, 0) B: (1,0,1) this eliminates that annoying halo of material n 4 if you are painting between 4 different material modules. Now the painting mask is much more precise. I thank the user who reported the problem, it was really useful and was solved 24 hours after the report

- **Fix: Paint mode problem when you press Fill**

    Pressing the FILL button when you are in Texture Paint, resuming the painting could cause the brush not to work. Now for safety, when you press FILL, the Texture Paint stops

- **Fix: Search-Replace-Add Data material**

    When using one of these two buttons to add or replace the data material to the object, to the added or replaced material the nodes sockets were hidden, this happened to all materials not created with Extreme PBR and was annoying, now this happens only to the Nexus type nodes, and only in the node_tree of the material not to that of the group nodes

- **Improve: Make user lib Data folder**

    The user library identification system has been improved from the previous version, now the USER library is automatically added to the ._data folder, while in version 4.1.100 it had to be done manually

- **Added: Color Ramp Widget in the interface**

    If a Color Ramp node is present in the Nexus material useful for editing the material, it can now be shown in the material editor and in general in all areas of the interface that are drawn by the appropriate function

- **Added: Material Random Location**

    Added a button to randomly change the location of the material in the material editor, useful especially on fences or objects that need a variation in the position of the material as they are very close together, Available in all Nexus type materials

- **Improved: Paint Preview Material slot disable Render**

    During the paint Mode if the Extreme PBR material slot was displayed, with each brush stroke, the material slot was updated, this slowed down the paint mode because of the render that had to be done on the material preview. Now during the paint Mode the material preview is replaced by a MATERIAL icon so that the paint is much less slow. This was done to speed up the paint mode. Pay attention to the Blender Material Slot, if opened the problem will persist, it is advisable to close any interface that shows the material slot, this will slow things down a lot if you are using the paint mode.

- **Bug Fix: Microdisplacement with multiple modules**

    When a Microdisplacement was added to the material, and then a module was added for the texture paint, the Displacement node was disconnected. It was fixed by updating the function that connects the sockets from the mixer to the other nodes



--------------------------------------------------------------------------------------------

4.1.100
-------

**Release date: 20-08-2023 (D/M/Y)**

- **Added: Space Colors Management**

    Many users have rightly reported that Extreme PBR materials only worked in the sRGB and Non-Color color space, now from the options menu it is possible to change the default color spaces of the project

- **Changes: BW Map Colorspace for Nexus materials**

    The color space in the Modules and Fx of the Nexus materials, before was managed in sRGB even the BW maps, then they were converted into a color space 'Non-Color' Through a Gamma node. Now given the change and the support of more colors, the Gamma node would no longer convert correctly, if not using sRGB, so it was chosen to change the color space directly in the texture node, the 'Non-Color' button in texture manager now it will no longer be present in new projects.

- **Bug Fix: Download Materials Stuck**

    Added a condition on os.remove('exa_files.json') this generated an error that blocked the download of materials, in some cases.

- **Added: Displacement Menu**

    A separate menu for displacement has been added and replaced the previous one, it is displayed only when an object is selected, and contains a displacement activated by Extreme PBR, this was done because some people had trouble finding the displacement menu under the properties of the material editor menu.

- **Added: Toggle Wireframe**

    Added a button in the Displacement menu, so that you can quickly view the wireframe of the selected object

- **Added: Library Path Management**

    The library management system now also stores that of the expansions, if an expansion is added it is also stored inside a .json file, so that if you change the version of Blender and if you install Extreme PBR again at the first start it will recognize the library paths and set them automatically. This was done so as not to have to indicate the paths every time you reinstall Extreme PBR (The json file will be saved inside the folder above that of the addons and is named ExtremeAddons)

- **Improved: Regeneration of Preview Icons**

    The button to regenerate the preview of the material icons (Under the preview material), now also regenerates the icons damaged by the Beta-Alpha versions of Blender, so they are regenerated simply by copying and deleting the damaged icons and reloading the material preview.

- **Improved: Total regeneration of all icons**

    Always for the reason in the previous point (Damaged Previews) The *Patch previews* button now becomes *Regenerate Previews and Icons* so it will regenerate all the material icons and also those of the interface. The Beta and Alpha versions of Blender 3.6 had also damaged the icons. This allows you to regenerate and reload them

- **Improved: New interface**

    The interface has been divided into several UI panels so that they can be reordered and closed at will

- **Added: Right Click Online Documentation Button**

    On every Extreme PBR button or property, by right clicking, you can choose to open the online documentation, so you can read the explanation of each function. Note: At the moment the properties of the material sliders do not work, because they refer to the official Blender documentation

- **Bugfix: Bake Dynamic Mask GPU**

    It often happened that during the Make Dynamic Mask, the Bake lasted too long, this is because the Bake was sometimes set to CPU, now it is set to GPU by default, so it should work correctly and be faster

- **Bugfix: Add Fx Layer, wrong map**

    When adding an Fx layer, for an error, in most cases a diffuse texture was chosen, now the function that chooses the correct texture has been reversed, and it should choose the correct texture because the necessary mask should be in black and white, and only if it does not exist, in extreme cases choose the diffuse

- **Improved: New Docs right click button**

    In almost all the buttons and properties of Extreme PBR, a function has been added where by right clicking with the mouse, a button will be shown (Extreme PBR Online Manual) which will lead to the explanation of that button or property

- **Improved: New Documentation**

    The new documentation is much more complete than the previous one, in addition it is much faster, now we use a new site for the documentation which is much faster, in addition we use a Readthedocs theme just like that of Blender

- **Dismissing: Support for Blender less than 3.3**

    Due to the new Blender nodes, we cannot continue to offer support for versions less than Blender 3.3, the nodes present in Extreme PBR, may no longer work correctly on versions less than Blender 3.2, so now you will have to have at least a version of Blender 3.3 or higher (Better if higher)



--------------------------------------------------------------------------------------------

4.0.207
-------

**Release date: 05-07-2023 (D/M/Y)**

- **Patch: Stuck during the material download phase**

    During the download phase an error was raised during the execution of os.remove() of the file 'exa_files.json' this blocked the download. Now an exception in case 'exa_files.json' does not exist, no longer raises errors as it is checked with os.path.isfile ()



--------------------------------------------------------------------------------------------

4.0.206
-------

**Release date: 10-05-2023 (D/M/Y)**

- **Patch: Previews Disappear into Blender 3.6 alpha**

    Using Blender 3.6 Alpha, for some reason it damages the preview images of the materials, once damaged, not even using another version of Blender will be displayed correctly. I added a button in Options (Patch Preview) that should solve the problem by regenerating the previews that are no longer displayed



--------------------------------------------------------------------------------------------

4.0.205
-------

**Release date: 30-12-2022 (D/M/Y)**

- **Bug Fix: They don't show the properties**

    With the advent of Blender 3.4 the RGB Mix node has changed, so also some functions that referred to it, no longer worked. I added a check that understands if the node is MixRGB or Mix, as the number of inputs in the Mix node has increased, and this made it unrecognizable.



--------------------------------------------------------------------------------------------

4.0.204
-------

**Release date: 26-12-2022 (D/M/Y)**

- **Patch: Black Material (Combine/Separate RGB)**

    With the new Blender 3.3 the Separate/Combine RGB node has changed, so if you open the project in Blender 3.3 or higher and save the project to then return to a previous version, the Combine/Separate RGB node is no longer recognized. I made a second patch to better solve this problem

- **Patch: For Black Material Mix RGB**

    The previous patch, now in Blender 3.4 creates confusion, as the Mix RGB node, is now also changed. This patch should solve the problem of Black materials with a Mix RGB not recognized, or a Mix node (New) changed by the previous patch.

- **Added: Reload Mixers Nodes**

    Added a button (Into Options) to reload the Mixers nodes, in case of problems with the Mixers nodes, or if you want to reload the Mixers nodes, without in only one click.



--------------------------------------------------------------------------------------------

4.0.203
-------

**Release date: 11-11-2022 (D/M/Y)**

- **BuxFix: Bake Error Copy Attributes**

    Error in copying scene attributes on some occasions. For now it has been solved using the try-except method.

- **Patch: Black Material**

    Opening old projects in Blender 3_3 version the Separate RGB and Combine RGB node were not recognized. So a small feature was created that arranges the black materials. The button will be located in Extreme PBRs Options, and is called Adjust All material Node Tree. It was already present in previous versions, but a new function has been added in addition to the other previous ones.



--------------------------------------------------------------------------------------------

4.0.202
-------

**Release date: 19-07-2022 (D/M/Y)**

- **BuxFix: Mirco-displacement Not Work**

    An oversight was left behind. The function to update the displacement (On Off) of the microdisplacement, had not been replaced with the new one. I proceeded to insert the new function, as the system of nodes (Normal, Bump, Displacement) has changed slightly in this version.



--------------------------------------------------------------------------------------------

4.0.201
-------

**Release date: 19-07-2022 (D/M/Y)**

- **BuxFix: Error during Save material**

    On some operating systems, an error was encountered during the Save Material process. the Preview function did not return the name of the material contained in it.

- **BuxFix: Bake Alpha Image**

    Bake Alpha In separate texture, it had a bug about the name. In the function, a variable was set to the object and not to the name

- **BugFix: Save Material**

    On some occasions, during the Save Material, an error could occur, this error was in case the material contained a Packed image from another file, then the unpack method (method = USE_ORIGINAL) function, did not work. I put an exception with the unpack method (method = USE_LOCAL) This solved the problem



--------------------------------------------------------------------------------------------

4.0.200
-------

**Release date: 19-07-2022 (D/M/Y)**

- **BuxFix: RGBA Error During the Bake**

    During the Bake, if the scene was set to a movie (Like MP4) or an image that did not allow the Alpha channel, you would get an error like this: Cannot set RGBA in color_mode, the script stopped, it was necessary to set an image also PNG to avoid the error. Now this has been fixed

- **Added: Shader Overlay (Experimental)**

    This new feature allows you to apply a material to all selected objects, plus there is also a Gradient mixer to adjust the mix position of the material in the Overlay. Useful for presentations with Blueprinting or the overlay of material with special effect

- **Change: Normal and Bump Node**

    Now the Normal and Bump Node are no longer in a group node. This is to eventually save resources. The nodes are interactive and are connected only if really needed

- **Improved: Get Library Register**

    Multithreading support added, now the interface no longer freezes when using the 'Get The Register' button

- **Improved: Create Library Structure**

    Multithreading support added.

- **Fixed: Create Library Structure**

    Multithreading support added.

- **Improved: Installer And Server Api**

    With this version the installation of the materials happens faster, due to the API change of our server. Now the calls are much less, and we have a cleaner data flow. Older versions will still work on the site's old APIs, but it is recommended that you update the addon

- **Improved: Material Installer Multithreading**

    Multithreading was added for library download. now you can continue to use Blender, without having to open another Blender to continue working while downloading materials

- **Improved: First Installation Interface**

    The first install interface has been improved to make it less confusing. Now the steps are drawn separately with Back-Next buttons to easily continue the installation without too much confusion as in the previous version.

- **Improved: Force reload Preview Material Icons**

    We have found that in Blender 3.2 some times the material preview icons are not loading correctly. I inserted a button to force reload the preview of the icons. It is now located in the Box, Tag and material options Panel, just below the Material Preview.

- **BugFix for Blender 3.2 - Material Previews form Search material list**

    The icons of the materials listed in the Search Material were no longer loaded correctly in Blender 3.2. They will now load correctly.

- **Added: Material Override (Experimental)**

    Material Override, overrides for a view on the fly, all the materials of the selected objects. It makes use of the Geometry Nodes System. It is very quick to change material, unlike Shader Overlay. The phase is still experimental, they await feedback from users



--------------------------------------------------------------------------------------------

4.0.131
-------

**Release date: 10-04-2022 (D/M/Y)**

- **BuxFix: Search material Grease Pencil Error**

    When trying to add a grease pencil material (From project material list) an error was shown. Has been solved.

- **BuxFix: ColorSpace Error, with ACES OCIO**

    This is not really a good FIX, but there is a warning message, if the user uses ACES expansions, it is reported that it is not possible to set the sRGB or Non-Color color space correctly, for now it is a sort of Patch , we are studying a better fix for this situation. For now, the error will be avoided and consequently the interruption of the Extreme PBR operators will be avoided

- **BuxFix: Painter Problem with erase**

    While painting, the Strength Slider did not work in the texture manager, making it impossible to adjust the Black and White (Strength) of the paint, which also made it impossible to erase the paint just made.

- **BuxFix And Improved - BSDF Bake Type**

    There was a problem with BSDF bake mode, if for example no node was connected to the BSDF input to bake, (for example Base Color), the result was completely wrong. Now to overcome this, a Node (Fake Map) is created which simulates itself. In case of firing an RGB Socket, an RGB node is created and connected to Base Color, then rendered. If it were the cooking of a socket of type Value, a Node Value type is created, in order to make a Bake always connecting it to the Bsdf Base Color socket. This is essential if there are different materials on the same object, especially if they are materials without any links connected to the inputs of the BSDF node and you intend to bake them too.

- **Improved: Bake Flip X Axis**

    Improvement for bake with Export FBX, especially for Unreal Engine, as the Unreal Engine's Global axes are different from those of Blender, If you check the Flip X Axis checkbox before doing the Bake (Activating Export FBX Object) , it will be possible to try to flip the X axes, in order to have the object as it is in Unreal. This setting is currently experimental, so it needs user feedback. If you are having trouble, uncheck this box



--------------------------------------------------------------------------------------------

4.0.130
-------

**Release date: 09-03-2022 (D/M/Y)**

- **BuxFix: No Preview in data image list**

    No Preview for the images in the list in the generation of normal maps and into search data images (Ops). We fixed it.

- **Improved: Re-projection button on Fx Layer Menu**

    Added a Re-project button on Fx Layer Menu. This button was only present in the inter-module painting.

- **Improved: FAQs Button**

    A FAQs button has been added in some parts of the addon. It will also be accessible by pressing the Helps button in the Main interface

- **Fixed: ShaderMaker Paint Error**

    Error when trying to add a Shadermaker Paint to a Curve object

- **Added-Fixed: Create New UV Map added into Bake editor**

    After a few Bake reports, we have found a solution to Bake so that if the object does not have a correct UV mapping, you can choose to Create a new UV map. It will be projected with the Blender Pack Islands system. While previously a Smart Projection method was used, which did not meet the need, we had provisionally removed it, but many inexperienced users were expecting immediate Bake without having to change the UV mapping (Rightly so). We think this is my best method for now. Looking forward to new features

- **Fixed: Error when UV Maps are 8-slot**

    Blender has a limit of 8 UV Layers, so we had an Error when some Operators gave Error if the UV Layers were 8. An additional check has been added, and a message will be shown if this happens

- **improvement: Bake improvement**

    The bake has been improved. Now you can do 3 different types of Bake. It is now also possible to bake non-Extreme PBR materials. The three types are 1 - Bake Based on BSDF Principled Materials. 2: Classic Bake by Cycles. 3 - Classic Bake Combined by Cycles. Everything is ready to bake in just a few steps. In addition Previously in Bake we used a Smart Projection, but it was not a good idea, now we use the PackIsland method, this greatly improves the output uv mapping.

- **improvement: Texture Browser Added**

    In the material shader editor you can now access the new Texture Browser menu. All textures present in Extreme PBR can now be searched through this menu, and added directly to a Texture Image node in the node tree

- **improvement: Panel Builder Helper**

    The Panel Builder Helper has now been improved. It turns out cleaner and less confusing. A Socket slot viewer has also been added.

- **improvement: Simple PBR material options Added**

    Now it is possible to create simple PBR materials, without Nexus node tree, so as to create a Base node tree, which you can modify at will. PLEASE NOTE: it is not possible to paint over it for the moment or add a fx layer. if you want to do this you have to use Nexus materials!

- **improvement: Painter**

    Now the default Painter shows all the maps turned off (Mute), except the diffuse one. This is to avoid problems on the Macintosh Users, as Macintosh does not currently support many textures on the same material

- **Provisional Patch: Texture Limiter**

    Due to limitations on Mac systems, as it is known that there is a maximum number of textures on a single material, and it is very limited. A function has been added that recognizes if the computer is a Mac System. So it automatically limits the use of textures on materials, so you can mix more of them. This is a momentary patch pending Vulkan on Blender API, hopefully they will be added as soon as possible, this is a limitation for Macintosh users.

- **improvement: Old Extreme PBR (Combo-Evo) panel properties**

    Now, in the panel it is possible to return to view the sliders of the old Extreme PBR (Combo-Evo) materials, it is not identical to before, but it is quite similar.

- **improvement: Slider On the Extreme PBR panel**

    If you are using a material based on a Principled BSDF node connected directly to the output, you can now view the sliders in the Extreme PBR panel. If the inputs of the Principled BSDF are connected, the sliders of the node from which they are connected will also be shown (Both Normal Node and Group node)

- **bug fix- Add Material From User Library**

    An error occurs when the material is applied, this did not compromise the correct functioning, but it was very annoying. Fixed



--------------------------------------------------------------------------------------------

4.0.129
-------

**Release date: 30-12-2021 (D/M/Y)**

- **BuxFix: Expansion Libraries**

    We have fixed some errors in the management of Expansion Libraries.



--------------------------------------------------------------------------------------------

4.0.128
-------

**Release date: 24-12-2021 (D/M/Y)**

- **Improved: Access Data Stored**

    A new folder will be created with the right credentials to ensure that the last correct credentials with which the addon was activated are always available, in case of update.

- **Fix: Message Incompatibility with Beta-Alpha Version**

    Fixed Incompatibility with Beta-Alpha Version Message

- **Improved: Keep track of libraries**

    Now the addon keeps track of where the libraries are, automatically recognizes the paths (if they still exist) useful for multiple installations of Extreme PBR on various versions of Blender

- **Improved: Added first boot message System**

    At the first launch of Extreme PBR, a message may be displayed with the important news of the update

- **Improved: Improved the fluidity of the interface**

    Improved the fluidity of the interface, now the panels in general are more fluid with less 'Lag'. We will continue to try to improve fluidity with future releases as well.

- **Improved: Increased the timeout**

    We have raised the timeout threshold to improve the download while the user is not at the computer. Translated, there is less risk of the download stopping while it is downloading by itself. We are still trying to improve the speed service.



--------------------------------------------------------------------------------------------

4.0.127
-------

**Release date: 19-12-2021 (D/M/Y)**

- **BugFix: Save Material Preview Icons**

    It was impossible to change the type of Previews icon, and also the background for the lighting. We fixed it.

- **Improved: Get Register Button**

    We have added a modal and a progress bar to not freeze the interface while getting the library list.

- **Improved: Create Library Structure**

    We have added a modal for creating the library structure. A progress bar has also been added. This no longer freezes the Blender interface

- **Added: Installed Library Percentage**

    Added a status bar on the installation of the entire library. Viewable in Options. It is used to see how much of the online library has been installed.

- **Fix: Problem 'License in use on another computer'**

    This annoying problem has been solved. The problem was on computers with multiple network cards or with WiFi and Lan connections. It can now store up to 3 different computer configurations. You will need to perform a Device Reset to take effect!



--------------------------------------------------------------------------------------------

4.0.126
-------

**Release date: 10-12-2021 (D/M/Y)**

- **BugFix: SSL Certificate Verify**

    We changed the SSL certificates, so the installer should work better now. Some were having problems with increasing response time to our server because of this. Please install this version

- **Improved: Helps Text**

    Added some more help messages for beginners.



--------------------------------------------------------------------------------------------

4.0.125
-------

**Release date: 08-12-2021 (D/M/Y)**

- **BugFix: Save Material with FX**

    An error was shown when saving the complete material with FX Module and made it impossible to save a material with an Fx Layer inside it

- **Improved: Check Updates Panel**

    New buttons to show or hide all update details

- **BugFix: Search Image From Texture Manager Panel**

    The search for images was aborted if an image did not actually exist. This was due to a preview error, as it did not exist.

- **Improved: License Check**

    A 36 character license length check was added, many users were confused about which license to enter. This additional check indicates if the license entered is not of the correct length.

- **Fix: Image lost data (has_data API)**

    Officially, Blender 3.0.0 has an API bug. So it is no longer possible to check if the texture is still connected on the disk. We have made a temporary system that checks that the textures are still linked to the file. Only if the textures are not Packed



--------------------------------------------------------------------------------------------

4.0.124
-------

**Release date: 05-12-2021 (D/M/Y)**

- **SSL Certificate Problem Blender 3.0**

    On Blender 3.0 we encountered problems with connection certificates to our server. This made it impossible to connect again to download the libraries. We have now fixed this. If you are unable to update with Update core. You will need to download the addon from the MarketPlace you purchased it from and replace it.



--------------------------------------------------------------------------------------------

4.0.123
-------

**Release date: 04-12-2021 (D/M/Y)**

- **Fixed: Bake with Smart Projection**

    We noticed that Bake remained with a smart projection, while programming Extreme PBR we had escaped to disable Smart Projection during Bake, this did Bake objects with a new smart mapping. This was awful, and we had forgotten it turned on. Now the Bake will use the user's active UV mapping. We thank our very scrupulous user for this report.

- **Fixed: Fx Layer Decals Bug**

    The mask used when applying a decal FX Layer was not placed correctly on the Alpha map, and therefore the result was an unexpected transparency. Now this has been fixed, and the Alpha map will act as a Mask map, as it was originally meant to be.

- **Fixed: Fx Layer**

    The Alpha texture was disconnected from the Mapping node, so it was impossible to scale it along with the entire FX Layer. Now solved

- **Added: Bake Device Selection**

    Added choice for Bake (Cpu-Gpu)



--------------------------------------------------------------------------------------------

4.0.122
-------

**Release date: 29-11-2021 (D/M/Y)**

- **Fixed: Bug on Bake**

    When trying to bake an object with multiple maps, with the Normal map mode active, it gave an error. It is now solved.

- **Added: New text Box into installer**

    A new box for communication texts during installation of libraries has been added.

- **Added: Debug Checkbox for installer stats**

    A new button to show more statistics during installation has been added in the Options menu.



--------------------------------------------------------------------------------------------

4.0.121
-------

**Release date: 26-11-2021 (D/M/Y)**

- **Fixed: Bug on Search Module/Fx Button**

    When trying to search for a Module or a Layer Fx, using the small buttons (m) and (fx), an error appeared and made it impossible to replace. Resolved



--------------------------------------------------------------------------------------------

4.0.120
-------

**Release date: 24-11-2021 (D/M/Y)**

- **Fixed: Emission on Blender 2.83 to Blender 2.9**

    We fixed a bug that occurred on Versions prior to 2.91 through 2.83. The emissivity property was not controllable. We have reactivated a multiplier node for emissivity. (Press Adjust node tree to fix if you are in production)

- **Implemented: Multiple Adjust Node**

    We have added a button (Adjust All Material node Tree) in the Options menu. This fixes all possible broken Materials, or possibly for a passage of a project created with Blender 2.83 to Blender 2.93+ due to the fact that the nodes are slightly different due to the missing Emission Strength socket. This operator fixes everything in one go.



--------------------------------------------------------------------------------------------

4.0.119
-------

**Release date: 22-11-2021 (D/M/Y)**

- **Remove Material Bug On lower versions of Blender 2.91**

    We have excluded the APIs showing this error on versions prior to Blender 2.91. Everything works the same as before on the higher versions.

- **Emission Bug On lower versions of Blender 2.91**

    On versions prior to 2.91 some materials looked White, actually it was the emissivity set to white by default on the Principled BSDF, now it is set to Black, so no emissivity effect that gave the White effect will happen again.



--------------------------------------------------------------------------------------------

4.0.118
-------

**Release date: 19-11-2021 (D/M/Y)**

- **Security Check Error Fix.**

    For security reasons we have blocked some operators who use our server. This Block was giving an error. It has now been fixed.

- **Bug on Get Register Fix**

    We fixed a communication error with our server that happened when this operator was pressed.



--------------------------------------------------------------------------------------------

4.0.117
-------

**Release date: 15-11-2021 (D/M/Y)**

- **Bugfix: Password Bug**

    Users reported that if they used some special characters in the password (such as quotation marks) it was not possible to activate the addon. We have now solved the problem. We thank some customers for reporting.



--------------------------------------------------------------------------------------------

4.0.116
-------

**Release date: 12-11-2021 (D/M/Y)**

- **Improved: Displacement**

    Now if the object has other modifiers, the Modifier's subdivision, as a precaution, is set to 1. The displace will always keep a smart subdivision count, based on how many polygons the object you are working on has. This is to keep Blender from freezing too long on complex objects.

- **FIx: Show Hidden Password/License**

    We noticed that some users were having trouble figuring out if the Mail/Password/License was right. We have put Show / Hide buttons next to each field in the license activation menu



--------------------------------------------------------------------------------------------

4.0.115
-------

**Release date: 06-11-2021 (D/M/Y)**

- **Fix: First Installation Issue**

    Problem when the user tries to move the libraries, and by mistake does the 'First Installation' the process starts over. Now this has been fixed.

- **Fix: Installation Interface Hidden**

    During installation, the Extreme PBR interface has been made hidden so as not to create a situation of being able to use Extreme PBR during installation as it could be a risk of installation breakdown. Fixed



--------------------------------------------------------------------------------------------

4.0.113
-------

**Release date: 02-11-2021 (D/M/Y)**

- **BugFix: Material Boolean Button**

    On some occasions, the boolean button in the material properties showed an error. We fixed it



--------------------------------------------------------------------------------------------

4.0.112
-------

**Release date: 01-11-2021 (D/M/Y)**

- **BugFix: Libraries Bug**

    Fixed the problem that occurred on Mac and Linux, after pressing 'Create Structure' the folders were created incorrectly (Only on Mac and Linux)

- **BugFix: Options Button**

    It happened that by pressing the 'Options' button a CONTEXT error was shown. Resolved



--------------------------------------------------------------------------------------------

4.0.111
-------

**Release date: 29-10-2021 (D/M/Y)**

- **BugFix: Bake Error**

    We fixed the API error about tile_x / tile_y, as these bees in Blender 3.0 have changed.

