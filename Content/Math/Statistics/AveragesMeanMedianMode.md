# Averages (Mean Median Mode)

## What is it?

Averages are crucial for everyone studying mathematics and sciences to understand. There are 3 general ways we process averages at a lower level, mean median and mode.


## Mean
[Wikipedia](https://en.wikipedia.org/wiki/Mean)

Generally when we think of "Average" we are actually thinking of the mean. 
The mean is the result of adding every number from a set together, and then dividing by the number of items in the set.

Consider the following set of numbers:

    1,2,5,5,6

To compute the mean, we add all the numbers together, and then divide by how many numbers there were.

    (1+2+5+5+6)/5

This will give us a result of:

    3.8

While mean is generally the preferred choice for averages, one major issue is outliers. Consider the following data set

    1,2,5,5,6, 1000

This will give us a mean of:

    (1+2+5+5+6+1000)/6 = 169.833333

The resulting number is not useful because it doesn't accurately describe any data. 

So, we can solve this problem by removing outliers. To be able to calculate outliers, we need to determine standard deviation, and that's a conversation for another day.

## Median
[Wikipedia](https://en.wikipedia.org/wiki/Median)

Median is the second most popular form of average. Median works well with statistical outliers, but can create issues of the standard deviation is very high.

The median is simply the number in the middle of a **sorted data set**.

Consider the following set of numbers:

    1,5,6,5,2

FIRST WE MUST SORT THE DATA SET UNLESS WE KNOW IT'S ALREADY SORTED

    1,2,5,5,6

Then, simply choose the number in the middle, there are 5 numbers, so 5/2 is 2.5 and then we round down and choose the element at index 2. (5)

    Result is 5. (index 2)

When we have an even numbered data set, we do the following:

    1,2,3,5,5,6

We first divide by length, just like last time. 6/2 is 3, but because there are "two numbers in the middle", we also need to consider index 2. So we simply subtract 1 from 3 (index 2), and then we add the value from index 2 to the value of index 3, and divide by 2 just like we would for the mean.

    (3 (index 2) + 5 (index 3))/2 = 4

So even though 4 is not included in our data set, it would be our median.

## Mode
[Wikipedia](https://en.wikipedia.org/wiki/Mode_(statistics))

The mode is the final form of average. The mode should be considered when you have non-ordinal (not numbers) sets of data, this means if you're trying to find what type of fruit is being purchased the most.

Mode is also good because it does not have issues with outliers

Consider the following data set:

    1,2,5,5,6

The mode is simply the most frequently appearing number. So, we tally all the numbers in a table

    1: 1
    2: 1
    5: 2
    6: 1
    
    Therefore the answer is 5 (2 instances)

However, when using the mode, the result can be strange. Consider the following data set

    1,1,1,3,4,5,6

The mean would be: 3

The median would be: 3

The mode would be: 1

It is for this reason, the mode is often not considered.

Another important thing to know about the mode, is that there can be multiple answers.

Consider the following set:

    1,2,5,6

Depending on your implementation, there either is no mode or every number is the mode.

Consider the following set:

    1,1,2,5,6,6

In this set, there are two modes, both 1 and 6.

## Quiz

### Knowledge
1. **Question 1: Mean Calculation**  
   Given the data set: `2, 4, 6, 8, 10`, what is the mean of these numbers?
   <details>
   <summary>Show Answer</summary>
   **Answer:** The mean is calculated as (2 + 4 + 6 + 8 + 10) / 5 = 30 / 5 = 6.
   </details>

2. **Question 2: Median Calculation**  
   For the data set: `3, 1, 4, 1, 5, 9`, what is the median after sorting the set?
   <details>
   <summary>Show Answer</summary>
   **Answer:** First, sort the data to get: 1, 1, 3, 4, 5, 9. Since there are 6 numbers, the median is the average of the 3rd and 4th numbers: (3 + 4) / 2 = 3.5.
   </details>

3. **Question 3: Mode Calculation**  
   Determine the mode of the following data set: `5, 3, 5, 2, 5, 3, 2, 3`.
   <details>
   <summary>Show Answer</summary>
   **Answer:** Both 5 and 3 appear 3 times, which is more frequent than 2 (which appears 2 times), so the modes are 3 and 5.
   </details>

### Application
1. **Question 1: What is the formula for calculating the mean of a set of numbers?**
   <details>
   <summary>Show Answer</summary>
   **Answer:** Add all the numbers together and then divide by the number of items in the set.
   </details>

2. **Question 2: How is the median determined in a sorted data set with an odd number of elements?**
   <details>
   <summary>Show Answer</summary>
   **Answer:** The median is the number in the middle of the sorted list.
   </details>

3. **Question 3: What is one potential drawback of using the mean when a data set contains outliers?**
   <details>
   <summary>Show Answer</summary>
   **Answer:** Outliers can significantly skew the mean, making it less representative of the data.
   </details>