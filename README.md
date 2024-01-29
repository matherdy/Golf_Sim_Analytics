# **Golf Simulator Tools**

The following is a list of projects in order of difficulty, where each project will add addtional functionaltiy to make the software tool better. For each tasks we should add notes on more details of what technology is needed or how we can do each part.

## First Project: Swing Replay

For our golf simulator we want to create a system where when you can stream video from your phone to a computer. The computer will start recording when there is a golfer in frame and track their movements. When the player takes his swing, the program will save a video clip of the whole swing and play it on repeat till the next swing occurs. This will not save any of the video data so should not requrie lots of video storage.

### Research:
- https://www.ijraset.com/research-paper/golf-swing-analysis-using-computer-vision
- https://www.commsp.ee.ic.ac.uk/~ng1/pdf/gehrig-et-al-bmvc03.pdf
- https://github.com/wmcnally/golfdb
- https://arxiv.org/abs/1903.06528

### OpenCV course: 
- https://opencv.org/university/free-opencv-course/?utm_source=google_ads_T1&utm_medium=cpc&utm_campaign=obc&utm_id=OBC&gclid=CjwKCAiAk9itBhASEiwA1my_67-DwbSctHNs_1_xh9BEGi0ExuBKjIZvCKEzsIyFX1iP0HyCh36FoBoCku4QAvD_BwE


### _Project Tasks_

1. Make an app that will stream video and send it to a local computer, we can start with a wired connection but eventually we want to transfer this stream via bluetooth or wifi.

2. Make a program that will track the human body and identify when a golfer is set up in a swing posistion so the computer can start recording the stream.

3. Make a program that will either detect when the golfer starts his swing or when the golf ball moves and grab the recording from a second before the swing starts, to the compleation of the swing.

4. Disply the recording on a loop until the next swing occurs and then replace the loop with an updated one.

## Second Project: Face Detection and Video Storage

This will build on the first project by first asking the player to 'sign in' with their face so the system knows which player is currently swinging. We can first use a physical sign in where the player will type their name into the comptuer but eventually a face detection system will be better. We can then add some voice functionallity on the tool so the player can decide if he wants the comptuer to store any of the clips from his session with simple voice commands. The software will store any video the player wishes to keep onto an external hard drive (or whereever we decide to store the clips) so they can be analyzed by the player later.

### _Project Tasks_

1. Find existing face detection software that will distinguish individual people and test it out for accurcay.

2. Make a new player sign in system that will allow new people to create an "account" which will make a new folder in the long term storage location. The short term storage location will be named someting like "Current Session" and be purged at the end of each session, however there should be a popup that will ask the player if they want to save any of the clips from the session.

3. Connect the software to a storage location so the clips can be stored temperarly and looked though at the end of the session. The player will then have the option to move any specific video to a long term storage location. At the end of each session the temperary storage will be purged.

4. Use existing voice to text software that will reconize simple commands. The program will likley need to have a que word or phrase ('hey sim', 'listen here you lil bitch', etc.) that will then be followed up by the command.

   - example commands: "Clip that","Show previous clip", "Delete that clip", "Change player", etc.

5. Find a text to voice tool that will allow the program to talk back to the player to ask questions or remind them of a step they need to do for the program to run at full functionality

## Third Project: Swing Analysis

Using a human body movemnt tracker software like human pose extimation (MoveNet Runs at 30 FPS on android phones, or OpenPifPaf but might need a GPU for it) track the movement of the players broken down into a kinematic view. This way we can track the movements of each of the individual body parts. We shouldn't need to have markers on the players for each of the joint positions but might make the project easier and require less processing power. We can then use this data and compare it to videos of the pros that have been broken down in the same way and compare the differences to help track what could be improved on the swing.

### Project Tasks

1.

# Setup for developement:

- Setup a python 3.x venv (usually in `.venv`)
  - You can run `./scripts/create-venv.sh` to generate one
- `pip3 install --upgrade pip` # need to use pip version 20.3.4 to use pip-compile
- Install pip-tools `pip3 install pip-tools`
- Update dev requirements: `pip-compile --output-file=requirements.dev.txt requirements.dev.in`
- Update requirements: `pip-compile --output-file=requirements.txt requirements.in`
- Install dev requirements `python3 -m pip install -r requirements.dev.txt`
- Install requirements `python3 -m pip install -r requirements.txt`
- `pre-commit install`

## Update versions

`pip-compile --output-file=requirements.dev.txt requirements.dev.in --upgrade`
`pip-compile --output-file=requirements.txt requirements.in --upgrade`

# Run `pre-commit` locally.

`pre-commit run --all-files`
