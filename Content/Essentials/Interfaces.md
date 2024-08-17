# Interfaces

Interfaces are a part of Object Oriented (OOP) abstraction. They are 0 weight files that can be used to identify (tag) classes, force logic and create clean code structure. 

[Interfaces wikipedia](https://en.wikipedia.org/wiki/Interface_(object-oriented_programming))

Some benefits of an interface:
* Many languages prevent mutliple parents due to diamond problem, but you can have unlimited interfaces without issue*
* Can be used to identify classes
* Zero weight
* For rules and organization

Draw backs of an interface:
* You cannot create variables (0 weight, logic files only)
* You cannot create default implementations of functions in some languages like Java, but you can in languages like C#
* Inheritors MUST implement undefined functions

## Example
An example of an interface is IDamagable. It's exceptionally useful as there's no parent class that would determine if an object is damagable, yet there are many objects that need to be able to take damage. 
By creating an interface IDamagable we make all inheritors identifable elsewhere as damagable, and force them to tell us what to do if they took damage.


To clarify, it makes sense to say a box and a player are both damagable, and both gameObjects. but if we edit GameObject then suddenly everything is damagable including walls and ui. By making an interface, we can target specific things and the only thing they need to share in common is the fact they're damagable.