# Object pooling

Object pooling is an optimization design pattern based around recycling objects. 


[Here's a wikipedia link](https://en.wikipedia.org/wiki/Object_pool_pattern)

The idea is straight forward, instead of deleting objects and re-creating them frequently, let's just recycle them. We do this because whenever we see the "new" keyword, we're allocating memory onto the heap (RAM), if we do this too much we can very easily cause our computer to lag.
When we offload assets and onload assets, our ram sorts itself to optimize how the data is retrieved, and by asking our RAM to do this frequently, we increase strain significantly. 
## Example:

All particle systems are pooled. We do this because we are constantly destroying and creating new particles. If we know how many particles there could ever be at a time, and then pre-make an array of that size, we can reduce the overall cost of the system, especially when sending commands to the GPU




