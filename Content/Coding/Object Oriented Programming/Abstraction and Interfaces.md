# Abstraction and Interfaces in OOP

![oopPillars.png](Resources/oopPillars.png)

Abstraction and interfaces are core principles in object-oriented programming (OOP) that help manage complexity by separating the “what” from the “how.” They enable developers to focus on high-level functionality without getting bogged down in implementation details.

## Abstraction

Abstraction involves modeling complex systems by exposing only the relevant features and hiding the underlying details. This allows you to work with simplified representations of objects. In essence, abstraction lets you focus on what an object does rather than how it does it.

[Wikipedia](https://en.wikipedia.org/wiki/Abstraction_(computer_science))

## Interfaces

Interfaces define contracts for what methods or behaviors a class must implement without dictating how those methods are carried out. They allow different classes to be used interchangeably as long as they adhere to the same set of functionalities. This promotes loose coupling and enhances flexibility in your code.


[Wikipedia](https://en.wikipedia.org/wiki/Interface_(object-oriented_programming))


## What the difference
In an abstract class, it's a regular class with a new feature: Abstract functions. Abstract functions are functions that force child classes to create those functions.

In an interface, it's a 0-weight contract. This means no variables can exist within an interface. Additionally, because it's like a contract, everyone that inherits from the interface MUST implement every function within the interface. Another advantage to interfaces is in most languages classes can inherit infinite interfaces, but only 1 class.

Interfaces are very confusing at first, but if you understand their potential, it will significantly elevate your programming skill.

## Example

Imagine you are developing a media player application. You can define an interface called `Playable` that specifies methods like `play()`, `pause()`, and `stop()`. Different types of media, such as audio, video, or streaming content, can implement this interface to provide their own specific behavior while guaranteeing a common set of actions.

```java
//Create an interface for anything that can be playable
public interface Playable {
    // All inheritors must define these functions.
    void play();
    void pause();
    void stop();
}

//We are saying an Audio is Playable
public class Audio implements Playable {
    @Override
    public void play() { 
        System.out.println("Playing audio...");
    }
    @Override
    public void pause() {
        System.out.println("Pausing audio...");
    }
    @Override
    public void stop() {
        System.out.println("Stopping audio...");
    }
}

//We are saying an Audio is also playable
public class Video implements Playable {
    @Override
    public void play() {
        System.out.println("Playing video...");
    }
    @Override
    public void pause() {
        System.out.println("Pausing video...");
    }
    @Override
    public void stop() {
        System.out.println("Stopping video...");
    }
}
```
In this scenario, the media player interacts with any object that implements the Playable interface. This means the player doesn’t need to know the specifics of whether it’s dealing with audio, video, or any other media type—it simply calls the methods defined in the interface.

This is also really powerful because perhaps we want to stop every playable, with abstraction we don't care whether it's a Video or an Audio. All that matters is that it's a Playable.

## More
The combination of abstraction and interfaces allows you to design systems that are modular, maintainable, and easily extendable. By hiding complex details behind simple abstractions and enforcing consistent behavior with interfaces, you can build robust applications where components can be updated or replaced without impacting the overall system.

This approach not only improves code readability and maintainability but also adheres to the Single Responsibility Principle, ensuring that each class or component has a clear and focused role.