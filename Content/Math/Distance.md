# Distance

## 2D Distance - Pythagorean theorem

[Wikipedia](https://en.wikipedia.org/wiki/Pythagorean_theorem)


### A<sup>2</sup> + B<sup>2</sup> = C<sup>2</sup>

Where C is the hypotenuse (longest side) of a right angle triangle

![Pythag.png](Images%2FPythag.png)

Given two sides (Usually A and B), we can solve the remaining side. This is very powerful because it can tell us the distance between two points.

In 3D it's the same thing, but we  factor z.

A<sup>2</sup> + B<sup>2</sup> + C<sup>2</sup> = D<sup>2</sup>

## Example [In Desmos](https://www.desmos.com/calculator/jv36mbjxxp)

Given two points, find the distance between them.

![PythagTool.png](Images%2FPythagTool.png)

Step 1, given the points a = (5.216, 1.01) and b = (6.465, 2.06), we first need to generate A and B, also called the Rise and Run.

We should get in the habit when subtracting points to subtract b-a. While in this case the order of the points does not matter, in other cases doing b-a creates a vector in which A is pointing towards B.

### 1. Find the Rise (Side A)

Rise = y2 - y1

Rise = 2.06 - 1.01

Rise = 1.05

### 2. Find the Run (Side B)

Run = x2 - x1

(Make sure the order is the same here, if you did point b-a in step 1, do that again.)

Run = 6.465 - 5.216

Run = 1.249

### 3. Calculate the distance

A<sup>2</sup> + B<sup>2</sup> = C<sup>2</sup>

C<sup>2</sup> = A<sup>2</sup> + B<sup>2</sup>

Note: Square root or sqrt is the same as to the power of (1/2)

C = (A<sup>2</sup> + B<sup>2</sup>)<sup>(1/2)</sup>

A = Rise = 1.05

B = Run = 1.249

C = (1.05<sup>2</sup> + 1.249<sup>2</sup>)<sup>(1/2)</sup>

C = 1.63171719363

### 4. Answer:

The distance is approximately 1.632 

TIP: If the distance is ever smaller than the rise or run, something has gone wrong.




