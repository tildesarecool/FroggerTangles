# FroggerTangles
I'm upgrading my box-prototype-frogger to its own repo. It's frogger but made of rectangles. 

This is something of an attempt to create a rudimentary version of "Frogger" using nothing but rectangles in pygame. The rectangles aren't even surfaces, in fact. Everything's a rectangle and that's it.

The green square is supposed to be the frog. 

The current status is attempting proper placement of the "lanes" for the cars, safe sidewalk and river where the logs will eventually go. I also have an "end zone" where the win condition will eventually go.

I was trying to create the lanes and rectangles etc relative to each other to make some semblance of resolution indipencance. Although I'm sure now I should bother with thinking of that at this stage. For instances lane one will start at "screen height - (2 * frog height) and the lane height will be "frog height * 3.5". Then the safe side walk's "bottom" will start the the "top" of sidewalk one and have a height of "frog * 1.5". So on and so forth. Like I said it's more theoretical at this point.

When I eventually get to the vehicles section I may just figure out if I can utilize a timer with the Clock() method. Have to see if that is a good approach or not.

It did eventually occur to me that the frog is supposed to "hop" e.g. move some amount of space and stop, then another amound of space and stop. Right now it's just repeats moving as long as the 'w' key is held. Eventually I'll figure out how fix this.