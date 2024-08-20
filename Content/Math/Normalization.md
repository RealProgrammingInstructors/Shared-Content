# Vector Normalization

Vector normalization is about making a vector with a magnitude/length/distance (these all mean the same thing) of 1.

This is useful because it allows us to control the speed of objects that are moving towards each other.

To normalize a vector we first need to know the [Distance](Distance.md), rise and run. Then we simply divide the distance by rise and run.

## Example

Copied from [Distance](Distance.md)

Given two points, create a UNIT VECTOR between them that points from A to B

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

The distance is approximately 1.632 

### 4. Normalization

newX = Run/distance

newX = 1.249/1.632

newX = 0.765318627

newY = Rise/distance

newY = 1.05/1.632

newY = 0.643382353

New vector = (0.765318627, 0.643382353)

### 5. Proof

If we want to prove that the vector has a distance of 1, we just need to do pythag again.

C = (A<sup>2</sup> + B<sup>2</sup>)<sup>(1/2)</sup>

1 = (0.765318627<sup>2</sup> + 0.643382353<sup>2</sup>)<sup>(1/2)</sup>
