# File-Fiesta

Creating realistic test and training environments for file share systems!

# Purpose

When building a training environment it is important to be as accurate as possible to production. One important thing to train on is the building, maintenance, recovery, migration, and decommissioning of a corporation's file share. However, you don’t “normally” want real corporate data in the training environment. How do you simulate managing files without data that takes up real drive space? 

File-Fiesta is here to help you! It is a simple EXE that will generate different files filled with random data. All you need to do is point it at the directory you need filled, set a soft data size limit, and watch it go.

This helps make the training environment feel more realistic without having to move a large amount of data into it. 

Need to see how long it will take for a transfer to complete in a test? File-Fiesta will help you simulate the data size with randomly generated files! Want to make training realistic by making your students backup and restore a large file share? File-Fiesta will make it seem real without risking important data!


# Build Methodology

This project is designed to be small (35MB roughly) so you don't need to migrate allot of data into your training environments. Instead you can just create it. File-Fiesta requires three files in the same directory to run properly. 

- File Fiesta.exe
  - Main python executable
- Randomwords.txt
  - list of random words it uses to name the files
  - This file was kept seperate from the EXE so you can add/remove possible file names. Making customizable to your environment.
- sombrero_PNG7.png
  - Because you can't have a fiesta without it!
  - It also won't run without it....

If your cyber security people are worried about a random EXE you found on the internet making GBs or TBs of data in your systems the code is located in this REPO to ease their mind. 

# Usage

# Support 

This repository is currently maintained by a single IT. Please consider sponsoring 404Staging to help maintain this project and others.
