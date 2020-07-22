# Automate Attendance Records Using Google Sheets API

## Overview
Are you a teacher? Do you have your students fill up a Google Form every class to record their attendance? Do you wish you could aggregate all the form data into one place? Then, you've found a script that does exactly that. The script in this repository updates a pre-existing Google sheets file (preferrably one containing the list of all the students enrolled in a particular course) with 0/1s based on the students who filled up a (attendance) form. However, before you can use this, you must enable Google Sheets API and certain access privileges. Click [here](https://youtu.be/8JgztFMGR38) to see a tutorial on how to do that followed by a short demo.

![Demo:](https://github.com/mastermueez/Automate-Attendance-Records-Using-Google-Sheets-API/blob/master/Demo.jpeg?raw=true)

## Requirements
* [Python](https://www.python.org/downloads/) (version used: 3.6.8)
* [Gspread](https://gspread.readthedocs.io/en/latest/)

## User Defined Parameters
The following parameters need to be set according to your requirements.

* **cred_file_name**: This is the name of your credential file that you downloaded as shown in the tutorial. Make sure the file is in the same directory as the script.
* **form_file_name**: This is the name of the sheets file that contains your form responses. If you click on Response tab of any Google Form, you will see an Sheets logo on the top right that reads ***View responses in Sheets***. Clicking on that will produce a Sheets file titled ***FormName (Responses)***. Then, share that file with the ***client_email*** present in the ***credentials.json*** file.
* **form_ws_title**: This is the name of the workshet in your responses sheets file. By default it will be **Form Responses 1**.
* **info_file_name**: This is the name of your sheets file which contains a list of all the students (ID required) for a particular course. You need to share this file with the *client_email* from the *credentials* file as well.
* **info_ws_title**: This is the name of the worksheet in your student list sheets file that will be used to keep attendance.
* **non_class_col_count**: This is the number of columns present in your aforementioned worksheet that contains non attendance related columns. For instance, if you have only ID and Name as such columns, the value for this variable should be 2.
* **id_separator**: The IDs for each section are displayed as output. If you can use commas, spaces, etc. as separators. Example: **", "**.
* **update_worksheet**: If this is set to **True**, your previously specificed attendance worksheet will be updated with your form responses. Set this to **False** if you only want to see a list of IDs ordered by course code.

## Additional Notes
* The student IDs are extracted from the emails used to submit the form. Therefore, institutional mails must be used to submit the form. The fucntion **get_id_from** returns the first 13 characters of a provided email address as that particular student's ID. It can be changed as required. This has been done to eliminate the possibility of a student missing out on their attendance because they typed their ID wrong.
* If you have multiple sections in one class, you must use the keyword **Course Code** in your form or modify the script. Otherwise, in the console, student IDs won't by shown by order of course code.

