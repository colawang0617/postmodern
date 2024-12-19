# PostModern

## Project Overview

Post-Modern is a secure, 3D-printed mailbox equipped with a keypad, designed to open using either the owner's code or a single-use delivery code assigned to each package. Once a delivery code is used, it is marked as “invalid” in the external database, and an email notification is sent to the owner. To deter theft, the mailbox emits a sound and sends notifications if left open for too long. Additionally, it provides auditory feedback when keys are pressed. Orders can still be processed through a program that adds entries with order information to the database. This database stores contact information, order details, and passwords, and the mailbox accesses it to verify entered passwords. In the event of a power outage, the mailbox reboots automatically.

## Authors 
* Ethan Zhu
* Junhwan Hyun
* Oleksandr Danchenko
* Lishinong Chen
* Haotai Wang

## Project Setup
![](../../../../../../Desktop/2024-12-19 09.41.54.jpg)

## Technologies Used
* Software
  * Python 3.11.2
  * RPi.GPIO python library to operate Raspberry Pi's GPIO pins
  * pygame python library to play sound
  * MySQL
  * mysql.connector python library to work with a database
  * smtplib python library to send automated emails
* Hardware
  * Raspberry Pi 4 Model B
  * 12V electric solenoid lock
  * 4x4 matrix keypad
  * Portable computer speaker
  * 3D printed mailbox body

## Project Schematic
![](../../../../../../Desktop/Untitled Diagram.png)
