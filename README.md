# discordbot

## General info

simple discord bot capable to send random text on chat, and play sound files.

## Setup
* You need to have ffmpeg added as a system variable on your computer.
* Instal python discordpy library
* Add a new application on your discord account, get token and put it in to token.txt file
* Launch bot.py

## Usage
* -cytat - choses random line from teksty.txt file and prints in on dicord chat (rempember to add your own lines to the file)
* -name_of_file_from_/soundboard plays audio file with that name, you can add your own audio files but you need to create new @client_command

You can also uncomment on_voice_state_uptade function, add your message to message.txt, and each time a person changes it voice state the message will be printed in first text channel


