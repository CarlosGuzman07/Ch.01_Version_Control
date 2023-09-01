'''
1.0 Jedi Training (17pts)  Name:Carlos Guzman


1. Define Forking (1pt): Forking is when you create a copy of a read-only repositories

2. Define Cloning (1pt): Once a repository is forked it is than a cloned to the local computer so the code can be worked
 on

3. Define Branching (1pt):Branching is when there are multiple forks of a code that are in used for multiple reasons and
 can be put back in the master branch

4. Define Committing (1pt): A commit is a checkpoint in the development of a project

5. Define Merging (1pt): Merging is when a side branch is put in the master branch

6. Define Pushing (1pt): Pushing is when we move our local repository to our remote repository(GitHub.com)

7. Define Pull Request (1pt):Asking the project owner to "pull" their changes and merge them into the original code


8. TURTORIAL ART (10pts.)

Modify the starter code below to create your own cool drawing. 
Make sure you keep the last two lines of code!!!! 
Your first and last name must be written on your art.
The last line keeps the window open until you click to close.
Turtle Documentation: https://docs.python.org/3.3/library/turtle.html?highlight=turtle
'''
import turtle
tina = turtle.Turtle()
tina.color('blue')
tina.shape("turtle")
tina.begin_fill()
tina.goto(200,200)
tina.goto(200,-200)
tina.goto(-200,-200)
tina.goto(-200,200)
tina.goto(200,200)
tina.end_fill()


yoda.write('Carlos Guzman',font=("Arial", 16, "normal")) # signs your name to your art
turtle.exitonclick() #Keeps pycharm window open so we can see the drawing
