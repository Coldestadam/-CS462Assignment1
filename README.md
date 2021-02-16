### Assignment 1: Introduction

##### Due: Tuesday 2/16 at the start of class. (2:40pm)

##### 100 points.

Note: please make sure that your name is someplace in your assignment!

To turn in: please submit everything to your github repo. For the written portion of the assignment, please add a document to your repository, as PDF, containing the answers to these questions.

Part 1. (20 points) Consider the following potential AI problems. For each of them, describe whether the environment is: a) static or dynamic b) fully or partially observable c) episodic or sequential d) deterministic or stochastic. Please explain your reasoning.

- A robotic medical assistant that can assist a doctor or nurse. It communicates with patients, administers bloodwork, and takes vitals.
- An agent that plays poker against a human player. Assume that the cards are digital, and that the player interacts with the agent via a touchscreen.
- An agent that can select TV shows and movies for a user. It watches the user's choices, asks the user to rate shows, and gives new shows the user is predicted to like. 
- A digital chatbot for diagnosing mental health issues. It interacts with the user via SMS and makes a prediction about their mental health based on responses.
- A robotic submarine for scientific exploration. It's able to autonomously travel to the ocean floor and collect samples.

Part 2: (20 points) Monkey and Bananas. This is a classic toy problem. For this version, let's assume the following:
Some bananas are hanging from the ceiling in the center of the room. There is a chair in one corner, and a stick on the floor. If the monkey stands on the chair under the bananas, he can hit the bananas with the stick and knock them down. 
Our state will have the following variables:
- holdingStick 
- chairInMiddle
- onChair

Our initial state is: <!holdingStick, !chairInMiddle, !onChair>

Our actions are: grabStick, moveChair, dropStick, getOnChair, getOffChair. moveChair will move the chair from the corner to the middle, or vice versa. Actions that don't make a change have no effect. (for example, grabStick when already holding the stick.)

a) what is the goal state?


b) Draw the state space for this problem. You can leave out actions that don't change the state. (For example, grabbing the stick when you already have the stick.)


Part 3: (20 points) Turing Test. [Kuki](https://www.pandorabots.com/kuki/) is a chatbot developed using Pandorabots chatbot technology. Kuki has won the Loebner Prize for the last five years. You can interface with Kuki in quite a few ways [here](https://www.kuki.ai/).

If you talk with Kuki, you'll see the limits of her responses pretty quickly. Try talking with her about different subjects - movies, music, games, life. 

What are places where Kuki's responses seem artificial? What sorts of responses or conversations does she have problems with?

Now try to have a conversation that generates responses that seem as human as possible. What sorts of phrases and discussions does Kuki do well with?


Part 4. (20 points) This problem will give you some experience coding in Python in an object-oriented style. 
The sample code in the assignment's github repo implements a graph as an adjacency list. Please add methods to implement:
- Breadth-first search
- Depth-first search
- Djikstra's shortest-path algorithm
- Prim's spanning-tree algorithm

There are comments in the code that give more detail.

Part 5: (20 points) This problem will give you some experience working with Pandas. Please add a file called pandasExercise.py to your repo containing this part.

First, read through [10 Minutes to Pandas](https://pandas.pydata.org/docs/user_guide/10min.html#min). There's a ton of other useful documentation of the pandas site as well.

The rest of these exercises use [The Pandas Cookbook](https://github.com/jvns/pandas-cookbook)
We'll also use the breast cancer dataset included in the GitHub repo. This is a classic ML dataset originally from the [UCI ML data repository](https://archive.ics.uci.edu/ml/index.php).

a) read Chapter 1.  Then, write a function that will read in the breast cancer dataset.

b) read Chapter 2. Then, write a function that determines the most common classification for the breast cancer data. (either 'recurrence' or 'no-recurrence')

c) read Chapter 3. Then write a function that determines the most common value for age and menopause for patients with recurrences?

d) Read Chapter 4. Write a function that plots the number of recurrences for each age group.


Part 5 (10 points - 686 students only): A classic thought experiment in response to the Turing Test is the Chinese Room, proposed by John Searle.
To begin, please read [this webpage](https://mind.ilstu.edu/curriculum/searle_chinese_room/searle_chinese_room.html), which presents the Chinese Room thought experiment, intended to show that a computer can manipulate symbols to produce replies without understanding what they mean.

Then, read section 2 (Replies and Rejoinders) of [this page](https://iep.utm.edu/chineser/), which summarizes many of the responses to the Chinese Room argument.

a) Summarize the Chinese Room argument. What does this have to do with computers? Why does Searle believe that it shows that a computer can pass the Turing test without understanding?

b) Do you find Searle's argument convincing? Or do you find one of the responses more appealing? Explain your position. 

Part 6. (10 points - 686 students only): Add a method to the graph code from part 4 to include a method that takes as input a vertex and finds the maximal clique that this vertex belongs to. 