# Maze Game

## Repository
https://github.com/EmmittStidham/PFDA_FinalProject.git

## Description
For my final project I want to make a simple maze game. I will do this using pygame. This is related to digital arts because it is a video game.

## Features
- Feature 1
	- Player gets to name their character
- Feature 2
	- Move a piece with WASD
- Feature 3 
	- Have surfaces that cannot be moved on (Maze Walls)
- Feature 4
    - Win on maze exit, displays "(insert player's chosen name) Won!"

## Challenges
- I need to reasearch how to map keys to new event types within pygame and a player controllers in general.
- I don't know how I will mimic collision with the maze walls so I will have to research how collision works within pygame.
- Have interactions directly tie to movement of a surface on screen.

## Outcomes
Ideal Outcome:
- My ideal outcome is that I have a fully functional maze with traps that reset the player's position. Once the player exits the maze a score will be displyed (based on how much time it took them to complete and how many times the player was restarted), the time will be displayed, and a text will be displayed at the top saying "(insert player's chosen name) Won!"

Minimal Viable Outcome:
- The minimal viable outcome is a maze that once finished will display text saying "(insert player's chosen name) Won!"

## Milestones

- Week 1
  1. Finish maze design and put it into pygame on same grid as player
  2. Add the arrow keys to the event type that pygame checks for

- Week 2
  1. Get a surface to move on a grid based on arrow input
  2. Get walls to stop player's from moving through them

- Week 3 (Final)
  1. Get traps to send player back to the begginig and deduct from score
  2. Finish timer, score counter, and win screen (Includes making win condition)