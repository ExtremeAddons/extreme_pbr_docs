.. _materials:

=================
Materials
=================

In this section are described the non standard materials present in Extreme PBR, that is the materials with an interface
built specifically for such material.



Blueprint 001 (Node Group)
--------------------------



Inputs:

1. **Emission  (Value)**

 - Base color emissivity

2. **Base Color  (Rgba)**

 - Base Color

3. **Line Color  (Rgba)**

 - Color of the lines

4. **Emission  (Value)**

 - Lines color emissivity

5. **Small Square Line  (Value)**

 - Line size of the smallest squares.

6. **Big Square Line  (Value)**

 - Line size of the largest squares.

7. **Metallic  (Value)**

 - Metallic material intensity, attention, if the diffused color is completely black (RGB 0,0,0) no metallic effect can be displayed, move the color towards dark gray to obtain the desired effect.

8. **Specular  (Value)**

 - Amount of dielectric specular reflection. Specifies facing (along normal) reflectivity in the most common 0 - 8% range.

9. **Roughness  (Value)**

 - Specifies microfacet roughness of the surface for diffuse and specular reflection.

10. **Bump   (Value)**

 - Strength of the bump mapping effect, interpolating between no bump mapping and full bump mapping.

11. **Distance  (Value)**

 - Multiplier for the height value to control the overall distance for bump mapping.

12. **Invert  (Button)**

 - Invert the map to the negative

13. **Transparent  (Value)**

 - Set the transparency. Attention, in Eevee or in preview mode,transparency needs to be activated via the button on the right, otherwise the transparency will not work.

14. **Transparent Invert  (Button)**

 - Invert Transparent, From Base color to Line color

15. **Rotation  (Value)**

 - The amount of rotation along Z axis

16. **lx  (Value)**

 - Move the texture to the X axis

17. **ly  (Value)**

 - Move the texture to the Y axis

18. **Scale  (Value)**

 - Scale the texture to the X-Y-Z axes

19. **World Coordinate  (Button)**

 - If active Projects the texture on world coordinates


------------------------------------------------------------------------------------------------------------------------

.. _mat_blueprint_002:

Blueprint 002 (Node Group)
--------------------------


This material is useful for making project presentations. You can adjust the properties to modify the grid and create a customizable grid

Inputs:

1. **Main Color  (Rgba)**

 - Adjust the main color

2. **Grid Color  (Rgba)**

 - Adjust the grid color

3. **Specular  (Value)**

 - Amount of dielectric specular reflection. Specifies facing (along normal) reflectivity in the most common 0 - 8% range

4. **Roughness  (Value)**

 - Specifies microfacet roughness of the surface for diffuse and specular reflection

5. **Crosses Thickness  (Value)**

 - Adjust the Thickness of the large grid

6. **Crosses Span  (Value)**

 - Adjust the Span of the large grid

7. **S. Crosses Span  (Value)**

 - Adjust the Span of the large grid

8. **S. Crosses Thickness  (Value)**

 - Adjust the Thickness of the large grid

9. **S. Crosses Scale  (Int)**

 - Adjusts the scale of the small grid

10. **Shape Size  (Value)**

 - Adjusts the size of the shape at the intersection of the large grid

11. **Subtract  (Button)**

 - If active, Subtract the Shape from the grid (If not active, it will be added to the grid)

12. **Circle Shape  (Button)**

 - If activated, the shape will be a circle, otherwise it will be a quadrate

13. **Loc X  (Value)**

 - Adjusts the position of the entire grid on the X axis

14. **Loc Y  (Value)**

 - Adjusts the position of the entire grid on the Y axis

15. **Rotation  (Value)**

 - Adjust the Rotation of the entire grid

16. **Scale X  (Value)**

 - Adjust the Scale of the whole grid on the X axis

17. **Scale Y  (Value)**

 - Adjust the Scale of the whole grid on the Y axis

18. **Scale Uniform  (Value)**

 -

19. **UV Coordinate  (Button)**

 - Projects the texture onto the object's UV mapping

20. **World Coordinate  (Button)**

 - If active Projects the texture on world coordinates


