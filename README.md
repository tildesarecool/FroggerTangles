# FroggerTangles
I'm upgrading my box-prototype-frogger to its own repo. It's frogger but made of rectangles. 

This is something of an attempt to create a rudimentary version of "Frogger" using nothing but rectangles in pygame. The rectangles aren't even surfaces, in fact. Everything's a rectangle and that's it.

The green square is supposed to be the frog. 

With my lanes solution in place it was fortunately easy to re-adjust the height of the main traffic lane: 3 times the vehicle height plus 30. This way I can have 3 lanes of traffic with some space between each row of traffic. 

As for adding the traffic I still can't get it work quite right. This lead to some re-thinking and a mini-refactoring of the appraoch. I was doing too much in the main.py file for instance so I moved a lot of functionality over to a separate py file. 

My initial idea was the seperate instancess of the vehicle class consisting of at least cars and busses with perhaps other types later: the vehicles types would be randomized so there would be a different combination of vehicle types the as the game played. But now I'm re-thinking the approach to just have one long row of vehicles and the whole thing is a loop. That has some issues too. I'll keep thinking about it. The three test vehicles I have now transition smoothly off the side on the left but just kind of pop into place on right. So I'm still kind of thinking about it. 

The script works that far for the one car. The second two vehicles are just stuck in place. So you could say the script is broken.



