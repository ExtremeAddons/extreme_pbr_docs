.. _materials:

=================
Materials
=================

In this section are described the non standard materials present in Extreme PBR, that is the materials with an interface
built specifically for such material.

------------------------------------------------------------------------------------------------------------------------



Glass (Node Group)
------------------

.. image:: _static/_images/materials/glass.png
    :align: center
    :width: 200
    :alt: Glass

|


.. image:: _static/_images/materials/ng_glass.webp
    :align: center
    :width: 400
    :alt: Ng Glass

|

Inputs:

1. **Glass Color  (Rgba)**
***************************

 - Change the color of the glass (All white for a neutral glass)

2. **IOR  (Value)**
********************

 - Change the index of IOR, which is the refractive index. Consult the refractive indices of various materials online.

3. **Mirror Fx  (Value)**
**************************

 - Adds a further Reflection effect to the Glass, taking advantage of the metallic map. This is a trick, for best results it should be used with caution.

4. **Dirty Roughness  (Value)**
********************************

 - Increases the dirty effect to the glass according to the texture that has been assigned. See the Texture Manager section to change image textures

5. **Scale Uniform  (Value)**
******************************

 - Scale the size of the Dirty Roughness map. The scaling effect is seen only if a value other than 0 has been set in the Dirty Roughness property


------------------------------------------------------------------------------------------------------------------------


Basic water (Node Group)
------------------------

.. image:: _static/_images/materials/basic_water.png
    :align: center
    :width: 200
    :alt: Basic Water

|

.. image:: _static/_images/materials/ng_basic_water.webp
    :align: center
    :width: 400
    :alt: Ng Basic Water

|


This material allows you to simulate the effect of animated water, it works once you start the Blender timeline



Inputs:

1. **RGB  (Rgba)**
*******************

 - Water Color

2. **Water / Fluid  (Button)**
*******************************

 - Water to fluid switch

3. **Water Speed  (Value)**
****************************

 - Set the speed of the waves

4. **Wave Strength  (Value)**
******************************

 - General height of all waves (Simulated with a bump)

5. **Scale  (Value)**
**********************

 - Change the size of the waves

6. **Roughness  (Value)**
**************************

 - Roughness, it might come in handy, if you use the Metallic Fluid parameter or Fluid Button

7. **Metallic Fluid  (Value)**
*******************************

 - It makes water look like a metallic fluid, such as mercury

8. **Flowing water  (Value)**
******************************

 - Simulates a moving watercourse, to choose the direction of the watercourse use the "Rotation" parameter

9. **Reverse  (Button)**
*************************

 - Reverse the water flow

10. **Flow Direction  (Value)**
********************************

 - Adjusts the overall rotation of the waves. Useful when the water is animated in one direction


------------------------------------------------------------------------------------------------------------------------

Rubber tires (Node Group)
-------------------------

.. image:: _static/_images/materials/rubber_tires_basic_001.png
    :align: center
    :width: 200
    :alt: Rubber Tires Basic 001

|

.. image:: _static/_images/materials/ng_rubber_tires.webp
    :align: center
    :width: 400
    :alt: Ng Rubber Tires

|





Inputs:

1. **Color  (Rgba)**
*********************

 - Change the color of the tire rubber

2. **Scale Uniform  (Value)**
******************************

 - Scale the Roughness (Only if it is different from the value 0)

3. **Roughness  (Value)**
**************************

 - Adjusts the intensity of the roughness, which is the one that simulates the difference between smooth and slightly rough areas on the tire rubber

4. **Specular  (Value)**
*************************

 - Adjust the reflection on the tire rubber






