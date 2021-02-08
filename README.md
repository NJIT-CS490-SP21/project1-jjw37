Getting it working
==================
Must follow these following steps to be able to run the app.
1. Create spotify account or sign in. 
2. create new app in your spotify dashbourd.
4. create a .env file in the main project directory, write 2 lines export SPOT_KEY='your secret key' and export SPOT_ID='your app ID'
5. In your enviroment install flask, if not installed, with pip install flask.
3. next install requests, pip install requests.
5. Now install python-dotenv, pip install -U python-dotenv.
After completeing these steps you should now be able run this app. 

Explanation
============
the spotify account and app are to access spotify's API which is used fetch the song data through the requests library 
the request library enables python to send http get/post requests.
creating the .env file and writing those 2 lines allows you to securely store your spotify secret key and ID.
python will read the .env file with the dotenv libary, allowing to to access the spotify API.
flask lets you run the app on your local machine.

Techincal issues
================
# 1
    The first problem I encountered was getting the data from the json object after making the spotify request.
    I found it difficult to navigate to the data I was trying to get and felt I wasting time and being inefficient. 
    Doing a google search I found a very usefull website, https://jsonformatter.curiousconcept.com/ , that made it much easier.
    This tool allowed me to input the json data from the Spotify documentation 
    and easily navigate it so I could be much faster getting the data, and made the process much less frustrating.
# 2 
    Another issue I had was styling with HTML and CSS.
    being the first time using these it was difficult to get everything the way I wanted it
    to be layed out. For example I wanted everything centered on the screen. Following some tutorials on, https://www.w3schools.com/ 
    , I was able to do understand the basics of how CSS can format elements.
    .The I was able to do things like make the image rouned with a border and how to orient everything in
    the center in CSS.
# 3
    One issue I had was getting the access token from the spotify API. at first I was using a get request 
    to try and get it but was failing. I then read up on a tutorial, https://stmorse.github.io/journal/spotify-api.html,
    on how authorization flow and realized I was supposed to be doing a post request not a get request. 
    Also in general in wrting spotify API requests this was helpful in formating the API requests later on.
  
  
 Future considerations/problems
 ==============================
 # 1
    One thing I would like to have done better is organize my code better, I feel like I didn't put enough effort
    into making my code organized and neat. I feel this is important for if someone else needs to read and undestand 
    my code or if additons need to be made. Going foward I want to foucs on that and ensure my code is better.
 # 2
    I would had liked to add some code so that if there is no song preview instead of having the audio player still there
    instead it could display some text saying that there is no preview avabile. This would make it a bit more user friendly
    in the currect state the user may think there is preview avabile when there is not and get confused when it doesn't work.