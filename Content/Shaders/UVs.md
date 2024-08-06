# UVs

UVs are how shaders display objects, represented in 0-1 space, where U is X and V is Y. We represent this in colors (R,G,B) because there are very limited ways of getting information out of the GPU. (1,0) is red because it's (1,0,0). And (0,1) is green is (0,1,0). If UV's had a third dimension, we'd see it in blue.

![UVs](../../Images/UVs.png)

Every model contains baked data which tells the UVs how to project themselves onto the model, which then allows the developer to change how the model looks based onthe projection.

## Example

Here are 3 ways to unwrap a sphere, each sphere has the same shader.

