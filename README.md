Cuddly Toys OOP Project
Overview

This Python project models a toy manufacturer that creates cuddly toys of various types and sizes using object-oriented programming principles. The hierarchy demonstrates inheritance, polymorphism, and class attributes in a clear and practical scenario.

The toys are divided as follows:

Types: Teddy bears and Bunny rabbits

Sizes: Small, Medium, Large

Roles & Colors:

Blue Teddy → Engine Driver

Red Teddy → Gardener

White Bunny → Clown

Black Bunny → Bank Manager

Sounds:

Teddy bears → Growl

Bunny rabbits → Squeak

Every toy can introduce itself, stating its job, color, size, and the noise it makes.

Class Hierarchy
CuddleToys (Base Class)
│
├── Teddy (Intermediate)
│   ├── EngineDriver (Lowest)
│   └── Gardener (Lowest)
│
└── Bunny (Intermediate)
    ├── Clown (Lowest)
    └── BankManager (Lowest)


CuddleToys: Base class handling toy size and validation.

Teddy / Bunny: Intermediate classes defining noise and type-specific behavior.

EngineDriver, Gardener, Clown, BankManager: Lowest-level classes defining job and color attributes.

Features

Dynamic Object Creation: Create toy objects via base class references.

Polymorphic Method: .talk() allows any toy to introduce itself and make its characteristic noise.

Validation: Only allows specified sizes (small, medium, large).

Clean OOP Design: Demonstrates inheritance, attributes, and method overriding.

Usage Example
def main():
    toys = [
        EngineDriver("large"),
        Gardener("small"),
        BankManager("medium"),
        Clown("large")
    ]
    
    for toy in toys:
        toy.talk()

if __name__ == "__main__":
    main()


Sample Output:

Hi! I am a blue Teddy! I am a Engine Driver, and my size is: large. I can Growl too!
Hi! I am a red Teddy! I am a Gardener, and my size is: small. I can Growl too!
Hi! I am a black Bunny! I am a Bank Manager, and my size is: medium. I can Squeak too!
Hi! I am a white Bunny! I am a Clown, and my size is: large. I can Squeak too!
