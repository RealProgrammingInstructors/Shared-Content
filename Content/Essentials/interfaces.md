Interfaces are 0 weight files that can be used to identify (tag) classes, force logic and create clean code structure. 

[Interfaces wikipedia](https://en.wikipedia.org/wiki/Interface_(object-oriented_programming))

An example of an interface is IDamagable. It's exceptionally useful as there's no parent class that would determine if an object is damagable, yet there are many objects that need to be able to take damage. 
By creating an interface IDamagable we make all inheritors identifable elsewhere as damagable, and force them to tell us what to do if they took damage.

Draw backs of an interface:
* You cannot create variables (0 weight, logic files only)
* You cannot create default implementations of functions in some languages like Java, but you can in languages like C#
* Inheritors MUST implement undefined functions
