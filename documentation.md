Description (200 words)
Draw picture of given word

Our web app, similar to "Draw Something with Friends," is a fun and interactive platform that allows users to play a drawing and guessing game with their friends online. The app is designed to be easy to use.
To get started, users can create a game page where they are given a word to draw and their drawing will be sent to a random person in the database. The first player is given a word to draw, and they have to create their masterpiece using the app's drawing tools. The other players must then guess what the word is based on the drawing. 
They will then get immediate feedback whether they are right or wrong and at the same time the artist will get notified the result.
Overall, our "Draw Something with Friends" style web app is a fun and engaging way for friends to connect and have fun online, and we believe it will be a hit with users of all ages.


Main Pages (Provide a sketch of the main pages of the project, the ones where “stuff happens”. For each page, include a sketch, and comment on whether you plan to implement it server-side or via Vue.js and javascript.)

Home Page: This is where the user will land when they first visit your game. It will provide them with options to login, view the instructions, or result of previous game. We will use JavaScript to build an interactive user interface that allows users to easily navigate and interact with the game.
Game Page: This is where the actual gameplay happens. On this page, you will need to display the word that the player needs to draw, provide a canvas for them to draw on, and allow other players to guess the word. We will use JavaScript to build a canvas and form page to submit the answer.

Data Organization (Give a sketch of which database tables will be necessary.  You don’t need to be very precise, but give some idea of how it will work.)

Four database tables:
Authentication : Login with user email
Drawings : Paints of user’s
Words : Subject of the paintings
Guesses :  Answer that user submitted

User Stories (Explain what a user can do, from account creation to the various things they can do.  You can write this as a narration)

The user will first create an account. After logging in they are provided with a word and a canvas to draw. When they are finished with their drawing, it is saved in the database. If there are drawings from other accounts in the database they are given one at random to guess. If there are no other drawings in the database the user is asked to wait.

Implementation Plan (Explain how you are going to divide the work among team members, and how you plan to approach the implementation.  I suggest you divide the work in three two-week periods, and say what you plan to build in each.  We understand that the plan is approximate at this stage)	

Week 1 Drawing/Canvas 
Week 1 Create database of words
Week 2 Create page templates
Week 3 Implement connection between players
