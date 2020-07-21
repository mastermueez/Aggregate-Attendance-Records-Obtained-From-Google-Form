# Update Attendance Using Google Sheets API

## Overview
The script in this repository has been created to keep track of attendance in an organised manner. It allows you to update a pre-existing Google sheets file with 0/1s based on the number of students who filled up a particular (attendance) form. However, before you can use this, you must enable Google Sheets API and certain access privileges. Click [here](https://youtu.be/TQqIDKwov_Ms) to see a tutorial on how to do that followed by a short demo.

## Requirements
* [Python](https://www.python.org/downloads/) (version used: 3.6.8)
* [Gspread](https://gspread.readthedocs.io/en/latest/)

## User Defined Parameters
The following parameters need to be set according to your requirements.

* **cred_file_name**: This is the name of your credential file that you downloaded as show in the tutorial
* **form_file_name**: This is the name of the sheets file that contain your form responses. If you click on Response tab of any Google Form, you will see an Sheets logo on the top right that reads ***View responses in Sheets***. Clicking on that will produce a Sheets file titled ***FormName (Responses)***. Then, share that file with the ***client_email*** present in the ***credentials.json*** file.
* **form_ws_title**: This is the name of the workshet in your responses sheets file. By default it will be **Form Responses 1**.
* **info_file_name**: This is the name of your sheets file which contains a list of all the students (ID required) for a particular course. You need to share this file with the *client_email* from the *credentials* file as well.
* **info_ws_title**: This is the name of the worksheet in your student list sheets file that will be used to keep attendance.
* **non_class_col_count**: This is the number of columns present in your aforementioned worksheet that contains non attendance related columns. For instance, if you have only ID and Name as such columns, the value for this variable should be 2.
* **id_separator**: The IDs for each section are displayed as output. If you can use commas, spaces, etc. as separators. Example: **", "**.
* **update_worksheet**: If this is set to **True**, your previously specificed attendance worksheet will be updated with your form responses. Set this to **False** if you only want to see a list of IDs ordered by course code.

## Additional Notes
The student IDs are extracted from the emails used to submit the form. Therefore, institutional mails must be used to submit the form. Example: *2021000000001@seu.edu.bd*
