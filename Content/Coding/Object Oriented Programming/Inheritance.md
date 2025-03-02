# Inheritance in OOP

![oopPillars.png](Resources/oopPillars.png)

Inheritance is a core principle in object-oriented programming (OOP) that allows a new class (the subclass) to acquire the properties and behaviors of an existing class (the superclass). This mechanism promotes code reuse, establishes a natural hierarchy, and enables polymorphism.

Arguably, inheritance is the most core pillar of Object Oriented Programming, as developers can save loads of time re-using code.

## What is Inheritance?

Inheritance enables you to create a new class based on an existing class. The new class inherits attributes and methods from the parent class while also having the ability to override or extend them with its own specific behaviors. This approach reduces code duplication and organizes related classes in a logical, hierarchical structure.

[Wikipedia](https://en.wikipedia.org/wiki/Inheritance_(object-oriented_programming))

## Benefits of Inheritance

- **Code Reuse:** Common functionality is defined in a base class and reused by multiple subclasses.
- **Hierarchical Organization:** Classes are structured in a hierarchy that reflects natural relationships.
- **Extensibility:** Subclasses can add their own behaviors or modify existing ones.
- **Polymorphism:** A parent class reference can point to objects of any subclass, enabling flexible and dynamic code.

## Example

Consider a simple example with a base class called `Animal` and two subclasses: `Dog` and `Cat`. The `Animal` class defines a general behavior common to all animals, and each subclass customizes that behavior to suit its specific needs.

```java
// Base class: Animal
public class Animal {
    // Protected attribute accessible by subclasses
    protected String name;

    // Constructor to initialize the animal's name
    public Animal(String name) {
        this.name = name;
    }

    // A general method for making a sound
    public void makeSound() {
        System.out.println("Some generic animal sound");
    }
}

// Subclass: Dog inherits from Animal, A Dog IS AN Animal
public class Dog extends Animal {
    public Dog(String name) {
        super(name); // Call the constructor of the superclass
    }

    // Override makeSound to provide a dog-specific implementation
    @Override
    public void makeSound() {
        System.out.println(name + " says: Woof Woof!");
    }
}

// Subclass: Cat inherits from Animal, A Cat IS AN Animal
public class Cat extends Animal {
    public Cat(String name) {
        super(name); // Call the constructor of the superclass
    }

    // Override makeSound to provide a cat-specific implementation
    @Override
    public void makeSound() {
        System.out.println(name + " says: Meow!");
    }
}
```
In this example, both Dog and Cat inherit the name attribute and the makeSound() method from the Animal class. Each subclass then provides its own implementation of makeSound(), demonstrating how inheritance allows for shared behavior while supporting specialization.

## More
Inheritance is essential for building scalable and maintainable systems. It not only promotes code reuse and organization but also provides a framework for polymorphism—where a single interface can represent different underlying forms. By leveraging inheritance, you can design flexible systems that adapt to evolving requirements while keeping your codebase clean and efficient.
