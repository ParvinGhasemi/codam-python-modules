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

