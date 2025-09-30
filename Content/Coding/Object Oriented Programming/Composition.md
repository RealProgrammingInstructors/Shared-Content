# Composition in OOP

![Puzzle.png](Resources/Puzzle.png)

Composition is a fundamental principle in object-oriented programming (OOP) that allows you to build complex functionality by combining simpler, reusable components. Instead of relying solely on inheritance, composition models relationships using object references, enabling more flexible and maintainable designs.

## What is Composition?

Composition is the practice of constructing classes by including instances of other classes to provide functionality, rather than inheriting from them. This models a "has-a" relationship, as opposed to inheritance’s "is-a" relationship.

For example, a `Car` *has a* `Engine` rather than *is an* `Engine`.

[Wikipedia](https://en.wikipedia.org/wiki/Object_composition)

## Benefits of Composition

- **Flexibility:** You can swap or change behaviors at runtime by using different component objects.
- **Encapsulation:** Each component is responsible for its own behavior, reducing interdependencies.
- **Reusability:** Components can be reused across different classes without code duplication.
- **Maintainability:** Reduces tight coupling associated with deep inheritance hierarchies.
- **Favors Composition Over Inheritance:** Promotes cleaner designs and avoids the pitfalls of rigid inheritance chains.

## Example

Consider a scenario where you have a `Car` that is composed of an `Engine`. Instead of extending from `Engine`, the `Car` class contains an `Engine` instance.

```java
// Component: Engine
public class Engine {
    public void start() {
        System.out.println("Engine starts...");
    }
}

// Another component: Radio
public class Radio {
    public void playMusic() {
        System.out.println("Radio is playing music.");
    }
}

// Composite class: Car (uses Engine and Radio)
public class Car {
    private Engine engine;
    private Radio radio;

    public Car(Engine engine, Radio radio) {
        this.engine = engine;
        this.radio = radio;
    }

    public void drive() {
        engine.start();
        System.out.println("Car is driving...");
    }

    public void listenToMusic() {
        radio.playMusic();
    }
}

// Demonstration of composition
public class Main {
    public static void main(String[] args) {
        Engine engine = new Engine();
        Radio radio = new Radio();

        Car car = new Car(engine, radio);

        car.drive();
        car.listenToMusic();
    }
}
```
In this example, the Car class doesn’t inherit from Engine or Radio.
Instead, it uses them through composition. 
This makes it easy to replace or update the behavior of Engine or Radio without modifying the Car class itself.

This is useful because if we wanted different types of cars (e.g., ElectricCar or SportsCar),
 we could simply give them different Engine implementations while reusing the same Car class design.
