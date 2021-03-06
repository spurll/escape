Escape
======

Procedurally-generated escape rooms.

Usage
=====

Installation
------------

TODO

Requirements
------------

TODO

Basic Usage
-----------

Once installed, run `escape`.

Configuration
-------------

TODO

Implementation Plan
===================

**This might make for a good PICO-8 project...**

Start by making it a puzzle game/escape room. Maybe turn it into a procedurally generated
adventure game.

Could generate things backward:

1. start by creaating the goal
2. randomly create an obstacle
3. randomly create 1-3 items (1 of which can remove the obstacle)
4. repeat steps 2-3 for a while

But there's no reason that we couldn't go forward:

1. Start by randomly generating 1-3 obstacles
2. Generate 1-3 items, at least 1 of which can take down the obstacle
3. When an obstacle is taken out, it generates either the goal item or 1-3 items/obstacles
   (if items are generated this way, at least one must be able to interact with an extant
   obstacle; if obstacles are generated, at least one must be solvable with an extant
   item)

In order for seed to be meaningful, entire room graph must be generated up-front.

The goal could be an object or an exit, and it will have certain properties governing how
it can appear (can it fit in a box? is it a door?).

Make a "solver" that recursively verifies all paths (there is probably only one) and
ensures the game is solvable and that there are no dead-ends.

After the puzzle game, create something where items/obstacles are in different "rooms",
which must be moved to before objects can be interacted with (also need inventory system).

Show seed for room. If no seed is input generate a random seed.

"Meditative" mode that tracks things and keeps going forever (like Desert Golfing).

Items
-----

Each item has a set of "attributes" (sharp, key, sticky, expensive, etc.).

Each obstacle will have multiple ways past (use something heavy, use something expensive,
use something sharp, etc.).

Items that can interact with each other to combine into a new item.

When obstacles are passed, depending on the item used it may yield a new item (e.g., bash
door with baseball bat, get a wood plank); the item generated must be taken into account
for future obstacles (make sure you don't generate two items, each of which could be used
to pass the current obstacle, but only one of which yields the item needed to pass the
next obstacle).

Have multiple obstacles active at once (you need to pass one to get at the item to pass
another).

Descriptions
------------

Each unique item/obstacle has a location description (table/wall/floor) and a used/unused
description (locked/closed/broken/open) that is changed depending on what item was used on
it. To describe the room, go through each possible location and list all objects on it.
(Also assign random flourishes to a room, like colour, wall paper, Art Deco, columns, old,
musty, dark, lit by a single bulb, etc.)

Make the data structures and just take a look at them to make sure they're solvable before
proceeding. Look into dependency trees, because you don't know much about them and it
seems like they're probably relevant here.

Describe in text, with objects that can be interacted with highlighted in green (objects
already interacted with have their text changed appropriately and are no longer
highlighted).

"You are trapped in (random name warehouse/emporium)..." Randomly generate a noun, then
pick a name that starts with the same letter/sound (sh/th/ch)

Structure
---------

* `Room` class
    * `name`: the name of the room (e.g., "Wallace's Window Warehouse")
    * `decorations`: list of descriptive flourishes
    * `obstacles`: list of `obstacle` objects
    * `items`: list of `item` objects
    * `graph`: the graph of obstacles and items (obstacles lock away items)
* `Graph` class
    * ...
* `Object` class
    * `used`: boolean
    * `attributes`: set of `attribute` objects
* `Obstacle` class (child of `object`)
    * ...
* `Item` class (child of `object`)
    * ...
* `Attribute` class
    * ...

Hints
-----

Hints ("something heavy can be used to break something wooden"). Track hints used. Track
moves made. Know optimal moves.

Syntax
------

```[use/put/combine] object [preposition] object/obstacle```

```save/load/exit```

Bugs and Feature Requests
=========================

Feature Requests
----------------

None

Known Bugs
----------

None

License Information
===================

Written by Gem Newman. [Website](http://spurll.com) | [GitHub](https://github.com/spurll/) | [Twitter](https://twitter.com/spurll)

This work is licensed under Creative Commons [BY-SA 4.0](http://creativecommons.org/licenses/by-sa/4.0/).

Remember: [GitHub is not my CV](https://blog.jcoglan.com/2013/11/15/why-github-is-not-your-cv/).

