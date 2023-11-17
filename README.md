# Makeup Style Recommendation

## Resources
[Question List](https://www.quizexpo.com/dear-peachie-makeup-quiz/)

[Miniconda](https://docs.conda.io/projects/miniconda/en/latest/)

[Raspberry Pi Documentation](https://www.raspberrypi.com/documentation/)

[Facial Recognition Tutorial](https://www.youtube.com/watch?v=o-x1PE0LVKM&t=251s&ab_channel=CoreElectronics)

# Running the app

## Launching the executable
Open `quizApp.exe`

or alternatively:

## Launching the app using code
Download and Install Miniconda

Open Anaconda Prompt and enter the following instruction:
```sh
conda create –n py38 python=3.8
```
```sh
y
```
```sh
conda activate py38
```

We need to install the mentioned libraries in order to run our program:
```sh
pip install PyQt5
```

Check if the above programs have been installed:
```sh
pip list
```
### In VSCode
Open `quizApp.py`
```
Ctrl + Shift + P 
```
> Python: Select Interpreter

Select the `py38` environment you created using miniconda

```
Run without Debugging (Ctrl+F5)
```

# File Documentation
### quizApp.py

### AdditionalClasses.py

### quizData.py

### userInteraction.py

### userTest.py

### CategoryArchetypes

### CategoryImages

### QuestionImages
Contains images for each question

## Questions
1. which one better describes your face shape?
    - rounded
    - oval
    - pear
    - square
    - heart
    - diamond
    - rectangle
    - oblong
2. how would you describe your jawline?
    - very soft and rounded
    - slightly soft and rounded
    - rounded but soft
    - slightly angular but mostly soft
    - not too round
    - not too sharp
    - slightly sharp and angular
    - extremely bony
3. how does your face's lower third look?
    - it's visibly shorter than other parts of my face
    - it’s slightly shorter
    - it’s almost equal to other parts
    - it’s slightly longer than the other parts
    - it’s equal to other parts
    - it’s longer than the other parts
    - it’s visibly longer (but slightly rounded)
    - it’s longer than the other parts (and it’s sharp)
4. in general, would you say your facial features are round or angular?
    - very rounded
    - rounded
    - slightly rounded 
    - slightly rounded in some areas
    - not too rounded, not too sharp
    - slightly angular in some areas
    - sharp (in most areas)
    - very sharp and angular
5. what is your eye shape?
    - round 
    - almond
    - upturned
    - hooded
    - slightly rounded
    - downturned
    - protruding
    - wide-set
6. what kind of lids do you have?
    - thick double eyelids
    - thin double eyelids
    - moderate double eyelids
    - hooded eyelids
    - tempered eyelids
    - partial eyelids
    - monolid
    - no eyelid
7. whats your nose like?
    - rounded and soft
    - slightly rounded and soft
    - moderatly soft and rounded
    - slightly sharp but soft
    - not too rounded, not too sharp
    - slightly sharp and angular
    - very sharp and angular
    - bony, sharp, and very prominent
8. what shape are your brows?
    - very arched and soft
    - slightly arched and soft
    - moderately arched and soft
    - slightly straight but soft
    - not too arched, not too soft
    - very sharp and angular
    - very arched but also very angular
    - straight, sharp and prominent
9. what shape are your lips?
    - small and rounded
    - not so small but very rounded
    - slightly wide but very rounded
    - slightly small but not so rounded
    - not too round, not too angular
    - slightly small but angular
    - wide and angular
    - very wide, sharp and prominent
10. how would you describe the size of your eyes?
    - very wide and round
    - slightly wide and round
    - moderately wide but not too round
    - slightly narrow but also rounded
    - not too wide, not too narrow
    - slightly narrow
    - very narrow
    - hooded and narrow
11. which one best describe the height of your nose?
    - very short
    - slightly short
    - moderately short
    - slightly long
    - not too short, not too long
    - long
    - very long
    - long, bony and prominent
12. choose the description that fit’s the width of your nose alar
    - it’s smaller than the distance between my eyes
    - it’s slightly smaller than the distance between my eyes
    - it’s moderately smaller than the distance between my eyes
    - it’s slightly wider than the distance between my eyes
    - it’s equal to the distance between my eyes
    - it’s visibly wider than the distance between my eyes
    - it’s very wider than the distance between my eyes
    - it’s wider, bony, and prominent
13. which statement is true about your mouth’s size?
    - visibly smaller than the rim of my pupils.
    - slightly smaller than the rim of my pupils
    - moderately smaller than the rim of my pupils
    - slightly wider than the rim of my pupils
    - not too wide, not too small
    - moderately wider than the rim of my pupils
    - visibly wider than the rim of my pupils
    - wide, angular, and prominent
14. what’s your style like?
    - cute
    - chic
    - sexy
    - grunge
    - casual
    - trendy
    - classic
    - formal
15. how old are you?
    - 16 or younger
    - 17-19
    - 20-24
    - 25-29
    - 30-35
    - 36-39
    - 40-45
    - 46 or older