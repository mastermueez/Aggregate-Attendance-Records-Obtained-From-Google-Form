# Update Attendance Using Google Sheets API

## Overview
The script in this repository has been created to keep track of attendance in an organised manner. It allows you to update a pre-existing Google sheets file with 0/1s based on the number of students who filled up a particular (attendance) form. However, before you can use, you must enable Google Sheets API and enable access privileges. Click [here](https://youtu.be/TQqIDKwov_Ms) to see how you can do that.


## A Brief Outline of the Contents

* **Raspberry Pi**: This folder contains files that have been written to run on a Raspberry Pi equipped with openCV, scikit-learn and pandas library:
  * **tain.py**: With this program running when a fruit is placed on the rotating platform, the sonar detects it and asks the user to enter an appropirate ripeness index for it. Then five images are captured with the servo rotating 72 degrees after each capture. Simultaneously, for each image captured, values for the following attributes -	*hue1,	sat1,	val1,	hue2,	sat2,	val2,	hue3,	sat3,	val3,	ripenessIndex* are written to a CSV file.
  * **test.py**: Similary, when this program is run and a fruit is placed on the podium, using the previously generated dataset, the program predicts a ripeness value. Based on whether this value is even or odd, the servo attached on either side of the structure pushes the fruit towards the left or the right.
