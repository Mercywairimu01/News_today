# News_today
## By Mercy Wairimu
## Description
This is an application that consumes a news API to show the lists and previews of news articles from various sources.   

## Technologies used
Python
Flask
HTML
CSS3

## Requirements
VS code with Python version 3 installed,a terminal and a browser.

## Setup and Instruction
Clone the repository.
* Extract and open the folder on VS code or navigate to the folder on your terminal.
* On the terminal, create a virtual environment python3 -m venv virtual and activate it source virtual/bin/activate. 
* Pip install dependancies highlighted on the requirements.txt by running pip install -r requirements.txt
* Create a start.sh file in the root directory of the folder and define the api key. You can generate the api key from the News API here
* Run chmod +x start.sh and ./start.sh respectively on the terminal.

## Behaviour Driven Development
BDD focuses on how the user will interact with the application and read various news  worldwide.
| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
| User loads application | **On page load** | List of various news articles and news sources displayed |
| Display articles from a  source | **Click a see article** | Redirected to a page with articles from the source |
| To read more articles from one source | **Click more news  button** | Redirected to the  source's site to read all news articles from the source |

## Development
To fix a bug or enhance an existing module, follow these steps:

* Fork the repo
* Create a new branch (git checkout -b improve-feature)
* Make the appropriate changes in the files
* Add changes to reflect the changes made
* Commit your changes (git commit -am 'Improve feature')
* Push to the branch (git push origin improve-feature)
* Create a Pull Request
## Known Bugs
No known bug at pduring development.If you come across a bug reach out to the contacts below.

License
MIT

Copyright (c) 2022 Mercy Wairimu

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
## Authors Info
Email: mercy.mambui@student.moringaschool.com