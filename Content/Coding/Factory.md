# Factory Design Pattern

The factory design pattern is a frequent one in game and projects where creation is frequent development because it helps increase code readability and abide by the Single Responsibility Principle.

[Here's a wikipedia link](https://en.wikipedia.org/wiki/Factory_method_pattern)

The idea is instead of allowing objects to just create other objects, we instead make a factory that takes orders and gives back objects. 

## Example:
A restaurant in real life is a type of factory. The user places an order, instead of the user making said order, they pass down the responsibility to a provider (The waiter). The waiter completes the order internally which means the user never needs to know about stuff like cleaning the plates or chopping the vegetables because the user only cares about their order. Finally, the provider gives back the final resultant order.

Another example is how Minecraft handles it's bow and arrow firing. When a bow fires an arrow, it doesn't care what arrow is being fired, or how it's created only that it needs to fire an arrow.

So the bow class has a function called abstractArrow() which spawns an arrow entity in the world. The bow then gives the arrow ownership, force, a position and applies any special effects such as flame to the arrow.

## More:

This explanation is a simplification, there are two versions of factory:

Factory and Abstract.

A simple factory can either be a class or function that creates and returns an object given some input.

An Abstract factory is usually done with an interface. This means that the object the factory can create any type of object that implements the interface, and it allows each object to declare how they should be created in the factory. 

[Here's a stack overflow link for another explanation](https://stackoverflow.com/questions/5739611/what-are-the-differences-between-abstract-factory-and-factory-design-patterns)

