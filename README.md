# FroggerTangles

I decided to keep my updates history from one day to the next. Maybe it will show some part of my evolving thought process
I'm upgrading my box-prototype-frogger to its own repo. It's frogger but made of rectangles. 

This is something of an attempt to create a rudimentary version of "Frogger" using nothing but rectangles in pygame. The rectangles aren't even surfaces, in fact. Everything's a rectangle and that's it.

The green square is supposed to be the frog. 

---

This is the first day since the latest archival/refactor started as mentioned below. I'd like to believe I've made a lot of progress but I'm kind of on the fence if I have.

I have made progress in the sense I'm programmatically bringing in vehicles using elements of a list rather than specific element numbers. I don't know if that makes sense or not.

I mean I'm saying carList[vehic].xpos rather than either carList[0].xpos or normalCar.xpos. Something like that. I'm iterating through an existing list of vehicle objects rather than address one specific vehicle object at at a time. It may not sound impressive but it's taken a long time to get to this point. And I am putting 3 vehicles up on the screen now. I mean they're a little "jiggly" and I can't seem to go higher than 3 and also one of them randomly changes color (or the z-order is messed up?). But it's a lot further than I was yesterday so I'm trying to embrace it.

Here's the most signifcant bit of the past 4 or so hours. See if you can figure out what it's doing. I'm only somewhat sure I know.

```Python
        for vehic in range(NumberOfCars):
            carList[vehic].moveDirLeft()
            
            if  carList[vehic].xpos - vehicTracker == cmn.screen_rect.right - (cmn.cellWidth * 2):
                vehicTracker = 0
                nextCarStart = True
            elif carList[vehic].xpos - 1 == cmn.screen_rect.right - (cmn.cellWidth * 2) :
                vehicTracker = 1
                nextCarStart = True
            elif carList[vehic].xpos - 2 == cmn.screen_rect.right - (cmn.cellWidth * 2) :
                vehicTracker = 2
                nextCarStart = True
            elif carList[vehic].xpos - 3 == cmn.screen_rect.right - (cmn.cellWidth * 2):
                vehicTracker = 3
                nextCarStart = True
            if nextCarStart:
                if vehic <= 2: # I need to take this out

                    print(f"carList[vehic].xpos evaluates to {carList[vehic].xpos - 2} and cmn.screen_rect.right - (cmn.cellWidth * 2) is {cmn.screen_rect.right - (cmn.cellWidth * 2)} for vehic number {vehic}")
                    if carList[vehic].xpos - vehicTracker == cmn.screen_rect.right - (cmn.cellWidth * 2): # and carList[vehic].xpos != carList[vehic - 1].xpos:

                        if vehic + 1 < NumberOfCars:
                            carList[vehic + 1].xpos = carList[vehic].xpos + cmn.cellWidth * 3
                            print(f"bool(carList[vehic].draw()) evaluates to {bool(carList[vehic].draw())} for vehic number {vehic}")
                            nextCarStart = False                            
```

---

I've basically started over, at least for the vehicle class. I kept the "common" class, the frog class and the rectangle boiler plate class. Then cleaned up as much left over commented out code as possible in main.py and all the other files. I'm glad I spent so much time unsuccessfully working on this though or this re-re-refactoring would have been much harder.

So far I already like the current results much more than the prior results: I have the first car going across the screen and at a specified moment start a second car across the screen. I've creating these two cars using a while loop in the vehicles.py file and adding them both to a list then in main.py calling the draw and moveDirLeft() methods on both using the subscript like this:

```Python
        carList[0].draw()
        carList[0].moveDirLeft()
```

It's working but it doesn't seem like it will scale very well if at all.

I've also re-done the window size to be multiples of 320 x 240. I'm hoping I can figure out a way to have it to evenly scale to different sizes of the screen. I might end up deciding on a different window size ratio. I haven't decided yet.

Here's my method of creating those two cars:

```Python
carCount = 0
carList = []    

while carCount <= 1:
    newCar = Vehicle(
        cmn.screen_rect.right + cmn.cellWidth * 2, 
        cmn.screen_rect.centery,
        cmn.cellWidth * 2,
        cmn.vehicleHeight,
        cmn.colorList[carCount]
        )
    carCount += 1
    carList.append(newCar)
```
I actually have a list of 9 colors. I was going to create car, one for each color. The obvious flaw in this being one of those cars will be the same as the fill color and thus invisible. But minor detail for later. Easiest way to prevent that is to define a fill color in the common class and use that for the fill color then use a if statement to skip over the "fill color" in the common class. I mean I assume there's superior ways to do it.

Overall I'm glad I took this step to do a major re-factoring. 

---

I don't know how many times I need to learn this before it sinks in, but asking ChatGPT for help pretty much always ends in taking more time than it would have taken had I not bothered using it.

Anyway, I'm going to archive my current set of files and start over from scratch. And this time I'll just GPT as a way to summarize documentation when necessary instead of just asking it about a specific script.

I was trying to figure out how to use custom events or a timer to space out putting in vehicles. But it didn't work. In fact it's worse now than before.

So the status of this readme file as of now is "I started over". If you want to see the last version of the script look in the "unnecessary backups" folder.

---

It doesn't feel like I have made a lot of progress. I have refactored a bit and ended up pretty much the point where I started functionally. I mean I have the vehicle moving right/left. Technically there's two vehicles but i didn't add any timing so one is just over lapping the other. I do believe I know where to go from where I am though: a method to create a bunch of car type vehicles - one for each predefined color - and add them all to a list and sprite group. That would just a utility function that runs as soon as the game runs or whatever. It just has to run once when the game starts is the point. Something roughly like pre-caching. Then a separate method or function for sending the vehicles across the screen with the timing.


---

I've started the process of re-factoring such that I can create a bunch of vehicles and send them.

Actually, I thought of the idea of pre-creating all the cars when the game launches so they're already in memory that simply sending them out as needed. This seems much better than having to create the vehicle, send it across the screen then delete it, then generate a nearly identical if not identical one. 

So I started the process of trying to figure that out but it went wrong some where in the process: first I don't think I'm even doing that "pre-caching" as described correctly, and secondly I can send through the coordinates of the vehicle I have right now but the rectangle doesn't actually show up visible on the screen. I think I did too many steps at once so I have take a step back and do one step at a time. 

I think I'm doing my rectangle creation and drawing in a very round-about and odd way.

So that's the current status as of this update. The vehicle is invisible because I broken the draw process. But it otherwise works. 

---

I did a bunch of refactoring around the car spawning system: I'm hoping I'm working up to an approach that will allow me to spawn traffic lanes worth of vehicles at a time such that eventually there will be three car lanes - two moving right/left and one moving left/right. Or the other way around. I am also hoping to vary the vehicle type (car or bus) and go through a range of colors.

Right now there's just one car moving right/left but it is smoothly scrolling in and out so that's an improvement. 

Right now I'm having something of an issue with the initial x coordinate of this vehicle. But I think I have solution to that and when there's an endless queue of vehicles going across the position of the first car won't really be noticable. At least that's what I'm going with. Since it does respawn off the screen to the right.


---

I thought about this a little over night. I don't think I want to spawn in multiple vehicles like it is now. 

Keeping in mind I only have 3 vehicles at the moment. In one continuous line of vehicles this wouldn't really be an issue. 

What I'm saying is: right now the three vehicles start on the right and move left. When the last car goes off screen *all three* vehicles pop into existence at the same time at a specific point. Well technically even that is broken at the moment but you get what I'm 
saying. I don't need them all to pop into existence at the same time, I need a never ending loop of vehicles starting off the screen to the right and scrolling to the left.

So what I *really* need is for each individual car to spawn off screen, roll into the screen on the right, scroll off the left and when it disappears off the left get deleted entirely. 

Or each individual car to get reset in a queue to eventually scroll across the screen. 

Either way I think I need to operate on an individual car basis rather than a group of cars at a time. 

I was trying to think of which way would make randomized vehicles eventually a thing that could be implemented. Deleting each vehicle as they disappeared off screen would free up a place in "line" for an entirely new vehicle.

In other words a queue of vehicles consisting of buses and cars initially with one of 3 colors. At the start of the game the queue is filled with random amounts of buses and cars with random colors. 

Then as each car disappears it's replaced with a new random type with a random color. 

Additional vehicle types and more than 3 colors notwithstanding. 

I'm not sure how much refactoring I have to do to implement this new approach.

It also occurred to me I've already implemented pretty much this exact thing in my semi-original game, "UFO invasion", with the way the bullets work. I'd be doing the same thing but without the spacebar to activate the rectangles and some other mechanism to "fire" the rectangles so they move across the screen. But it's all there: spawning into a group and a particular screen location, moving across the screen at a specific speed, and getting deleted from memory after hitting the edge of the screen. I should really just copy that. 

---

With my lanes solution in place it was fortunately easy to re-adjust the height of the main traffic lane: 3 times the vehicle height plus 30. This way I can have 3 lanes of traffic with some space between each row of traffic. 

As for adding the traffic I still can't get it work quite right. This lead to some re-thinking and a mini-refactoring of the appraoch. I was doing too much in the main.py file for instance so I moved a lot of functionality over to a separate py file. 

My initial idea was the seperate instancess of the vehicle class consisting of at least cars and busses with perhaps other types later: the vehicles types would be randomized so there would be a different combination of vehicle types the as the game played. But now I'm re-thinking the approach to just have one long row of vehicles and the whole thing is a loop. That has some issues too. I'll keep thinking about it. The three test vehicles I have now transition smoothly off the side on the left but just kind of pop into place on right. So I'm still kind of thinking about it. 

The script works that far for the one car. The second two vehicles are just stuck in place. So you could say the script is broken.



