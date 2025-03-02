# Polymorphism in OOP

![oopPillars.png](Resources/oopPillars.png)

Polymorphism is a powerful principle in object-oriented programming (OOP) that enables objects of different classes to be treated as instances of a common superclass. This means that a single interface can represent different underlying forms, allowing for flexible and interchangeable code.

## What is Polymorphism?

Polymorphism, derived from the Greek words for "many" and "form," refers to the ability of different objects to respond to the same method call in a way that is specific to their own class implementation. This is achieved primarily through method overriding, where a subclass provides its own version of a method defined in its superclass.

[Wikipedia](https://en.wikipedia.org/wiki/Polymorphism_(computer_science))

## Benefits of Polymorphism

- **Flexibility:** Allows you to write more generic and reusable code.
- **Maintainability:** New types can be introduced with minimal changes to existing code.
- **Interchangeability:** Different objects can be used interchangeably if they share a common interface.
- **Simplified Code:** Reduces complexity by allowing a single method call to operate on objects of different types.

## Example

Consider a scenario where you have a base class `Animal` and two subclasses, `Dog` and `Cat`. Each subclass implements its own version of the `makeSound()` method. When a method is called on an `Animal` reference, the correct overridden method is executed based on the actual object's type.

```java
// Base class: Animal
public class Animal {
    public void makeSound() {
        System.out.println("The animal makes a sound.");
    }
}

// Subclass: Dog, overrides makeSound
public class Dog extends Animal {
    @Override
    public void makeSound() {
        System.out.println("The dog barks: Woof!");
    }
}

// Subclass: Cat, overrides makeSound
public class Cat extends Animal {
    @Override
    public void makeSound() {
        System.out.println("The cat meows: Meow!");
    }
}

// Demonstration of polymorphism
public class Main {
    public static void main(String[] args) {
        // Create an array of Animal objects
        Animal[] animals = { new Dog(), new Cat() };

        // Each animal makes its respective sound
        for (Animal animal : animals) {
            animal.makeSound(); // Polymorphic call
        }
    }
}
```
In this example, both Dog and Cat are treated as Animal objects. Despite the uniform method call makeSound(), the program executes the subclass-specific implementation, demonstrating polymorphism.

This is useful because if we were to open a PetShop, we could sort by class category (Dog or Cat), or search by Type Animal, and we'd see the expected results. Additionally, it simplifies work we'd need to do updating out tools. Instead of creating a list of cats and another for dogs, we can create one for animals and keep both cats and dogs together in the list (as they are both animals).

## More
Polymorphism is central to creating extensible and modular systems. By designing methods that operate on the superclass level, you can introduce new classes with specialized behaviors without altering the code that interacts with them. This aligns with the Open/Closed Principle—your code remains open for extension but closed for modification—making your system robust and scalable.