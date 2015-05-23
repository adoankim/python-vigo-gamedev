# Python Vigo Game Dev

Slides and examples about basics of game development for [Python Vigo Dev Group](https://www.python-vigo.es) presentation.

[Presentation slides](http://adoankim.github.io/python-vigo-gamedev/#/)

## Examples structure

All the examples are hosted inside de *src* folder, and it's structured in the following way:

 Path                                   | Description
--------------------------------------- | -------------
src/pyvigo/structure_and_effects        | Initial examples that explains basics about window generation, layer management and actions
src/pyvigo/interaction                  | Examples about event handling, collision and objects spawning
src/pyvigo/goodies                      | These ones show you how to manage the music/sound player, and also, how to make spritesheet based animations for your game.

### Examples execution
First of all you must satisfy the dependencies required for the demos, they are listed in *requirements.txt* file.

In order to install these dependencies you can just type: ```pip install -r requirements.txt```. I suggest you to build a [virtualenv](https://virtualenv.pypa.io/en/latest/) environment to maintain clean your Python installation.

In order to execute them just type: ``` python src/pyvigo/demo_folder/demo_file.py```



