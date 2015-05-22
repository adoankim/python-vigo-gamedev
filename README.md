# Python Vigo Game Dev

Slides and examples about basics of game development for [Python Vigo Dev Group](https://www.python-vigo.es) presentation.

[Presentation slides](http://adoankim.github.io/python-vigo-gamedev/#/)

## Examples structure

All the examples are hosted inside de *src* folder, and it's structured in the following way:

 Path                            | Description
-------------------------------- | -------------
src/structure_and_effectsContent | Initial examples that explains basics about window generation, layer management and actions
src/interaction                  | Examples about event handling, collision and objects spawning
src/goodies                      | These ones show how to the handle music&sound player, and on the other hand, how to make animations based on spritesheets


### Examples execution
First of all you must satisfy the dependencies required for the demos, they are listed in *requirements.txt* file.

In order to install these dependencies you can just type: ```pip install -r requirements.txt```. I suggest you to build a [virtualenv](https://virtualenv.pypa.io/en/latest/) environment to maintain clean your Python installation.

In order to execute them just type: ``` python src/demo_folder/demo_file.py```



