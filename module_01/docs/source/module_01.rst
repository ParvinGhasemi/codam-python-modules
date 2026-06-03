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
