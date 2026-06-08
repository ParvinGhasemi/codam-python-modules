Module 01 - Code Cultivation
============================

This module introduces object-oriented programming in Python. The goal is to model plants using classes and objects instead of separate variables for each plant.

Important Concepts
------------------

- **Class**

- **Object**

- **Instance**

- **Constructor** and ``__init__()``

- **self**

- **Attribute**

- **Method**

- **Script entry point with** ``if __name__ == "__main__"``

- Shebang

----



Exercise 0 - Garden Intro
-------------------------

Introduces basic Python program structure, variables, printing,

``if __name__ == "__main__"``, and the shebang line.

.. automodule:: ex0.ft_garden_intro
   :members:
   :undoc-members:
   :show-inheritance:

Exercise 1 - Garden Data
------------------------

Introduces the ``Plant`` class and creating multiple objects from the same class.

.. automodule:: ex1.ft_garden_data
   :members:
   :undoc-members:
   :show-inheritance:

Exercise 2 - Plant Growth
-------------------------

Adds behavior to the ``Plant`` class using methods such as ``grow()`` and ``age()``.

.. automodule:: ex2.ft_plant_growth
   :members:
   :undoc-members:
   :show-inheritance:

Exercise 3 - Plant Factory
--------------------------

Improves plant creation by using a constructor to instantiate plants with their starting data immediately.

Instead of creating an empty object and assigning attributes later, each ``Plant`` object is created with its name, height, growth rate, and age.

**Concepts practiced:**

- Constructor-based object creation
- Instantiation
- Instance attributes
- Reusing methods from previous exercises
- Creating multiple objects from the same class
- Storing objects in a list
- Iterating over objects and calling their methods

Example:
~~~~~~~~

.. code-block:: python

   plants = [
       Plant("Rose", 25.0, 0.8, 30),
       Plant("Oak", 200.0, 0.2, 365),
       Plant("Cactus", 5.1, 0.1, 90),
   ]

   for plant in plants:
       plant.show()

.. automodule:: ex3.ft_plant_factory
   :members:
   :undoc-members:
   :show-inheritance:


Exercise 4 - Garden Security System
-----------------------------------

Introduces encapsulation by protecting plant data from invalid values.

In this exercise, the ``Plant`` class uses protected attributes such as
``_height`` and ``_age``. These values should not be modified directly
from outside the class. Instead, the class provides setter methods to
validate new values before updating the object.

Concepts practiced:

- Encapsulation
- Protected attributes
- Getter methods
- Setter methods
- Data validation
- Returning ``True`` or ``False`` to report update success
- Keeping object state valid

Why use setters?
~~~~~~~~~~~~~~~~

Setters allow the class to control how important values are changed.
For example, plant height and age should not become negative. By using
``set_height()`` and ``set_age()``, invalid values can be rejected before
they corrupt the object.

Example:

.. code-block:: python

   rose = Plant("Rose", 15.0, 10)

   rose.set_height(25.0)
   rose.set_age(30)

   rose.set_height(-5.0)  # rejected
   rose.set_age(-10)      # rejected

API Reference
~~~~~~~~~~~~~

.. automodule:: ex4.ft_garden_security
   :members:
   :undoc-members:
   :show-inheritance:


Exercise 5 - Specialized Plant Types
------------------------------------

Introduces inheritance by creating specialized plant classes from the
base ``Plant`` class.

The ``Flower``, ``Tree``, and ``Vegetable`` classes inherit the common
plant attributes and methods from ``Plant``. Each child class then adds
its own specific attributes and behavior.

Concepts practiced:

- Inheritance
- Parent class and child class
- ``super()``
- Method overriding
- Reusing common code
- Specialized attributes
- Specialized behavior
- Polymorphism through shared methods such as ``show()``

Inheritance structure
~~~~~~~~~~~~~~~~~~~~~

The base class is ``Plant``. It contains the common data and behavior:

- name
- height
- age
- ``grow()``
- ``age()``
- ``show()``

The child classes extend this behavior:

``Flower``
    Adds a color and bloom state. It can bloom using ``bloom()``.

``Tree``
    Adds trunk diameter. It can produce shade using ``produce_shade()``.

``Vegetable``
    Adds harvest season and nutritional value. Its nutritional value
    increases when the vegetable ages.

Why use ``super()``?
~~~~~~~~~~~~~~~~~~~~

The child classes use ``super()`` to call methods from the parent
``Plant`` class. This avoids copying the same setup and display logic
into every child class.

Example:

.. code-block:: python

   class Flower(Plant):
       def __init__(
           self,
           name: str,
           height: float,
           age: int,
           color: str,
       ) -> None:
           super().__init__(name, height, age)
           self.color = color

Method overriding
~~~~~~~~~~~~~~~~~

Each specialized class redefines ``show()``. This is called method
overriding.

The child class first calls the parent version using ``super().show()``,
then prints its own extra information.

Example:

.. code-block:: python

   def show(self) -> None:
       super().show()
       print(f"Color: {self.color}")

Example usage
~~~~~~~~~~~~~

.. code-block:: python

   rose = Flower("rose", 15.0, 10, "red")
   oak = Tree("oak", 200.0, 365, 5.0)
   tomato = Vegetable("tomato", 5.0, 10, "April", 0)

   rose.bloom()
   oak.produce_shade()

   for _ in range(20):
       tomato.grow()
       tomato.age()

API Reference
~~~~~~~~~~~~~

.. automodule:: ex5.ft_plant_types
   :members:
   :undoc-members:
   :show-inheritance:


Exercise 6 - Garden Analytics
-----------------------------

Combines the object-oriented concepts from the previous exercises and adds
statistics tracking, static methods, class methods, nested classes, and a
new ``Seed`` class.

This exercise reuses the existing plant hierarchy and extends it with
analytics behavior.

Concepts practiced:

- Nested classes
- Static methods
- Class methods
- Method overriding
- Inheritance chains
- Statistics tracking
- Reusing existing classes
- Polymorphism
- Shared functions that work with different plant types

Nested ``Stats`` class
~~~~~~~~~~~~~~~~~~~~~~

The ``Plant`` class contains a nested ``Stats`` class. This internal class
tracks how many times selected methods are called:

- ``grow()``
- ``age()``
- ``show()``

Each plant owns its own ``Stats`` object, so every plant tracks its own
method calls separately.

Static method
~~~~~~~~~~~~~

The static method checks whether a given age is older than one year.

It does not use ``self`` because it does not need a specific plant object.
It also does not use ``cls`` because it does not need the class itself.

Example:

.. code-block:: python

   Plant.is_older_than_year(400)

Class method
~~~~~~~~~~~~

The class method creates an anonymous plant with default values.

It uses ``cls`` so the class can create a new object of itself.

Example:

.. code-block:: python

   anonymous = Plant.create_anonymous_plant()

Seed class
~~~~~~~~~~

The ``Seed`` class inherits from ``Flower``. It reuses the flower behavior
and adds seed-specific data.

When the seed blooms, it also updates the number of seeds.

Example:

.. code-block:: python

   sunflower = Seed("Sunflower", 80.0, 45, "yellow", 0)
   sunflower.bloom()
   sunflower.show()

Statistics function
~~~~~~~~~~~~~~~~~~~

The ``display_statistics()`` function is not part of any class. It accepts
any ``Plant`` object or child object and displays its statistics.

This works because ``Flower``, ``Tree``, ``Vegetable``, and ``Seed`` all
inherit from ``Plant``.

API Reference
~~~~~~~~~~~~~

.. automodule:: ex6.ft_garden_analytics
   :members:
   :undoc-members:
   :show-inheritance:
