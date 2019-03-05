
#-----Statement of Authorship----------------------------------------#
#
#  This is an individual assessment item.  By submitting this
#  code I agree that it represents my own work.  I am aware of
#  the University rule that a student must not act in a manner
#  which constitutes academic dishonesty as stated and explained
#  in QUT's Manual of Policies and Procedures, Section C/5.3
#  "Academic Integrity" and Section E/2.1 "Student Code of Conduct".
#
#    Student no: 09823239
#    Student name: John Layson
#
#  NB: Files submitted without a completed copy of this statement
#  will not be marked.  Submitted files will be subjected to
#  software plagiarism analysis using the MoSS system
#  (http://theory.stanford.edu/~aiken/moss/).
#
#--------------------------------------------------------------------#



#-----Task Description-----------------------------------------------#
#
#  Publish Your Own Periodical
#
#  In this task you will combine your knowledge of HTMl/XML mark-up
#  languages with your skills in Python scripting, pattern matching
#  and Graphical User Interface design and development to produce a
#  useful application for publishing a customised newspaper or
#  magazine on a topic of your own choice.  See the instruction
#  sheet accompanying this file for full details.
#
#--------------------------------------------------------------------#



#-----Imported Functions---------------------------------------------#
#
# Below are various import statements that were used in our sample
# solution.  You should be able to complete this assignment using
# these functions only.

# Import the function for opening a web document given its URL.
from urllib import urlopen

# Import the function for finding all occurrences of a pattern
# defined via a regular expression.
from re import findall

# A function for opening an HTML document in your operating
# system's default web browser. We have called the function
# "webopen" so that it isn't confused with the "open" function
# for writing/reading local text files.
from webbrowser import open as webopen

# An operating system-specific function for getting the current
# working directory/folder.  Use this function to create the
# full path name to your publication file.
from os import getcwd

# An operating system-specific function for 'normalising' a
# path to a file to the path naming conventions used on this
# platform.  Apply this function to the full name of your
# publication file so that your program will work on any
# operating system.
from os.path import normpath
    
# Import the standard Tkinter functions.
from Tkinter import *

# Import the SQLite functions.
from sqlite3 import *

# Import the date/time function.
from datetime import datetime

#
#--------------------------------------------------------------------#



#-----Student's Solution---------------------------------------------#
#
# Put your solution at the end of this file.
#

# Name of the published newspaper or magazine. To simplify marking,
# your program should publish its results using this file name.
file_name = 'publication.html'

#Create the window
my_window = Tk()

#RSS Feeds
us_url = 'http://www.dailymail.co.uk/ushome/index.rss'
au_url = 'http://www.dailymail.co.uk/auhome/index.rss'
health_url = 'http://www.dailymail.co.uk/health/index.rss'
sports_url = 'http://www.dailymail.co.uk/sport/index.rss'
travel_url = 'http://www.dailymail.co.uk/travel/index.rss'
money_url = 'http://www.dailymail.co.uk/sciencetech/index.rss'

us_feed = urlopen(us_url).read()
au_feed = urlopen(au_url).read()
health_feed = urlopen(health_url).read()
sports_feed = urlopen(sports_url).read()
travel_feed = urlopen(travel_url).read()
science_feed = urlopen(money_url).read()

#Create the variables
national_au_checked = BooleanVar()
us_news_checked = BooleanVar()
health_checked = BooleanVar()
sports_checked = BooleanVar()
travel_checked = BooleanVar()
science_checked = BooleanVar()

#When print is pressed
def press_print():
    html_file = open('publication.html', 'w') #Create the HTML file for 'Writing'
#Write on the file
    html_file.write(
'''<!DOCTYPE html>
<html>

<head>
<meta charset="UTF-8">
<title>Gotham Gazette</title>
<style>
body {background-color:beige;}
hr {border-style: groove; margin-top: 2em; margin-bottom: 2em;}
</style>
</head>

<body>

<h1 style='font-family:Old English Text MT;
font-size:600%;text-align:center'>Gotham Gazette</h1>


<p>
<center><img src='https://d197nsfq0bri0.cloudfront.net
/paper_avatars/079d0670-82e8-012f-25ad-12313d16b843/
2orvn9us303mqe6t8vor/GOTHAM%20GLOBE%20LOGO.png' alt='Gotham Globe'
style="width:300px;height:220px;"></center></p>


<p style="font-family:Century Gothic;font-size:175%;
text-align:center;">Gotham's Latest News</p>

<p style='font-family:Century Gothic;font-size:125%;
text-align:center;'>Editor-in-Chief: John Layson</p>
<hr width = 800px size = 5px>''') 

#Determine which checkbox/es are selected
    topics = [us_news_checked.get(), national_au_checked.get(),
          health_checked.get(), sports_checked.get(), travel_checked.get(),
              science_checked.get()]

    global urls
    global url
    global current_time
    global current_times
    current_times = []
    urls = []

#If US News is selected
    if topics[0]:
        item = findall('(?s)<item>(.*?)</item>', us_feed)
        category = 'UShome | Mail Online'
        url = 'http://www.dailymail.co.uk/ushome/index.rss'
        title = findall('(?s)<title>\n*(.*)\n*</title>', item[0])
        photo = findall('<enclosure url="(.*?)"', item[0])
        summary = findall('(?s)<description>\n(.*)\n*</description>', item[0])
        date = findall('<pubDate>(.*)</pubDate>', item[0])
        progress_text.insert(END, 'Printing: Latest US News... \n')
        urls.append(url)
        current_time = str(datetime.now().replace(microsecond=0))
        current_times.append(current_time)


        html_file = open('publication.html', 'a')
        html_file.write('''<div style="font-family:Verdana;text-align:center;">
    <item>
<h1>''' + category + '''</h1>
<h2>'''  + title[0] + '''</h2>
<p><img src="''' + photo[0] + '''" style="width:300px;height:220px;"></p>
<p>''' + summary[0] + '''</p>
<p>''' + date[0] + '''</p>
<p><a href="''' + url + '''">RSS Feed</a></p>
    </item>
</div>
<hr width = 800px size = 5px>''')
        html_file.close()

#If Australia News is selected
    if topics[1]:
        item = findall('(?s)<item>(.*?)</item>', au_feed)
        category = 'Auhome | Mail Online'
        url = 'http://www.dailymail.co.uk/auhome/index.rss'
        title = findall('(?s)<title>\n*(.*)\n*</title>', item[0])
        photo = findall('<enclosure url="(.*?)"', item[0])
        summary = findall('(?s)<description>\n(.*)\n*</description>', item[0])
        date = findall('<pubDate>(.*)</pubDate>', item[0])
        progress_text.insert(END, 'Printing: Latest Australia News... \n')
        urls.append(url)
        current_time = str(datetime.now().replace(microsecond=0))
        current_times.append(current_time)
        
        html_file = open('publication.html', 'a')
        html_file.write('''<div style="font-family:Verdana;text-align:center;">
    <item>
<h1>''' + category + '''</h1>
<h2>'''  + title[0] + '''</h2>
<p><img src="''' + photo[0] + '''" style="width:300px;height:220px;"></p>
<p>''' + summary[0] + '''</p>
<p>''' + date[0] + '''</p>
<p><a href="''' + url + '''">RSS Feed</a></p>
    </item>
</div>
<hr width = 800px size = 5px>''')
        html_file.close()

#If Health News is selected
    if topics[2]:
        item = findall('(?s)<item>(.*?)</item>', health_feed)
        category = 'Health | Mail Online'
        url = 'http://www.dailymail.co.uk/health/index.rss'
        title = findall('(?s)<title>\n*(.*)\n*</title>', item[0])
        photo = findall('<enclosure url="(.*?)"', item[0])
        summary = findall('(?s)<description>\n(.*)\n*</description>', item[0])
        date = findall('<pubDate>(.*)</pubDate>', item[0])
        progress_text.insert(END, 'Printing: Latest Health News... \n')
        urls.append(url)
        current_time = str(datetime.now().replace(microsecond=0))
        current_times.append(current_time)

        html_file = open('publication.html', 'a')
        html_file.write('''<div style="font-family:Verdana;text-align:center;">
    <item>
<h1>''' + category + '''</h1>
<h2>'''  + title[0] + '''</h2>
<p><img src="''' + photo[0] + '''" style="width:300px;height:220px;"></p>
<p>''' + summary[0] + '''</p>
<p>''' + date[0] + '''</p>
<p><a href="''' + url + '''">RSS Feed</a></p>
    </item>
</div>
<hr width = 800px size = 5px>''')
        html_file.close()

#If Sports News is selected
    if topics[3]:
        item = findall('(?s)<item>(.*?)</item>', sports_feed)
        category = 'Sport | Mail Online'
        url = 'http://www.dailymail.co.uk/sport/index.rss'
        title = findall('(?s)<title>\n*(.*)\n*</title>', item[0])
        photo = findall('<enclosure url="(.*?)"', item[0])
        summary = findall('(?s)<description>\n(.*)\n*</description>', item[0])
        date = findall('<pubDate>(.*)</pubDate>', item[0])
        progress_text.insert(END, 'Printing: Latest Sports News... \n')
        urls.append(url)
        current_time = str(datetime.now().replace(microsecond=0))
        current_times.append(current_time)

        html_file = open('publication.html', 'a')
        html_file.write('''<div style="font-family:Verdana;text-align:center;">
    <item>
<h1>''' + category + '''</h1>
<h2>'''  + title[0] + '''</h2>
<p><img src="''' + photo[0] + '''" style="width:300px;height:220px;"></p>
<p>''' + summary[0] + '''</p>
<p>''' + date[0] + '''</p>
<p><a href="''' + url + '''">RSS Feed</a></p>
    </item>
</div>
<hr width = 800px size = 5px>''')
        html_file.close()

#If Travel News is selected
    if topics[4]:
        item = findall('(?s)<item>(.*?)</item>', travel_feed)
        category = 'Travel | Mail Online'
        url = 'http://www.dailymail.co.uk/travel/index.rss'
        title = findall('(?s)<title>\n*(.*)\n*</title>', item[0])
        photo = findall('<enclosure url="(.*?)"', item[0])
        summary = findall('(?s)<description>\n(.*)\n*</description>', item[0])
        date = findall('<pubDate>(.*)</pubDate>', item[0])
        progress_text.insert(END, 'Printing: Latest Travel News... \n')
        urls.append(url)
        current_time = str(datetime.now().replace(microsecond=0))
        current_times.append(current_time)

        html_file = open('publication.html', 'a')
        html_file.write('''<div style="font-family:Verdana;text-align:center;">
    <item>
<h1>''' + category + '''</h1>
<h2>'''  + title[0] + '''</h2>
<p><img src="''' + photo[0] + '''" style="width:300px;height:220px;"></p>
<p>''' + summary[0] + '''</p>
<p>''' + date[0] + '''</p>
<p><a href="''' + url + '''">RSS Feed</a></p>
    </item>
</div>
<hr width = 800px size = 5px>''')
        html_file.close()

#If Money News is selected
    if topics[5]:
        item = findall('(?s)<item>(.*?)</item>', science_feed)
        category = 'Sciencetech | Mail Online'
        url = 'http://www.dailymail.co.uk/sciencetech/index.rss'
        title = findall('(?s)<title>\n*(.*)\n*</title>', item[0])
        photo = findall('<enclosure url="(.*?)"', item[0])
        summary = findall('(?s)<description>\n(.*)\n*</description>', item[0])
        date = findall('<pubDate>(.*)</pubDate>', item[0])
        progress_text.insert(END, 'Printing: Latest Science News... \n')
        urls.append(url)
        current_time = str(datetime.now().replace(microsecond=0))
        current_times.append(current_time)

        html_file = open('publication.html', 'a')
        html_file.write('''<div style="font-family:Verdana;text-align:center;">
    <item>
<h1>''' + category + '''</h1>
<h2>'''  + title[0] + '''</h2>
<p><img src="''' + photo[0] + '''" style="width:300px;height:220px;"></p>
<p>''' + summary[0] + '''</p>
<p>''' + date[0] + '''</p>
<p><a href="''' + url + '''">RSS Feed</a></p>
    </item>
</div>
<hr width = 800px size = 5px>''')
        html_file.close()
    progress_text.insert(END, 'Done!!!')
    html_file = open('publication.html', 'a') #Open the file again to close HTML tags in 'Append' mode
    html_file.write(
        '''
</body>
</html>''')
    print current_times

#Read button function        
def read():
    webopen('publication.html')


#PART B -  SQL
#Create Save function
def save():
    connection = connect('internet_activity.db')
    cursor = connection.cursor()
    delete = "DELETE FROM Recent_Downloads"
    cursor.execute(delete9)
    counter = 0
    for each_link in urls:
        cursor.execute("INSERT INTO Recent_Downloads VALUES (?,?)", (current_times[counter], each_link))
        counter += 1
        connection.commit()
    connection.close()
    
#Window GUI
my_window.geometry('280x500')

#Give the window a title
my_window.title('My publisher')

#Change background
my_window['bg'] = 'Silver'



#Prompts user to pick topics
Label(my_window, text = 'Get updates on:', font = 'AgencyFB', \
      fg = 'Black', bg = 'Silver')\
      .grid(row = 0, column = 0, rowspan = 1, columnspan = 3, sticky = 'W')

#Create the checkbuttons
Checkbutton(my_window, text = 'NationalAU', bg = 'Silver', font = 'AgencyFB',
            fg = 'Black', variable = national_au_checked)\
                                .grid(row = 1, column = 0, sticky = 'W')
Checkbutton(my_window, text = 'US News', bg = 'Silver', font = 'AgencyFB',
            fg = 'Black', variable = us_news_checked)\
                                 .grid(row = 2, column = 0, sticky = 'W')
Checkbutton(my_window, text = 'Health', bg = 'Silver', font = 'AgencyFB',
            fg = 'Black', variable = health_checked)\
                                  .grid(row = 1, column = 2, sticky = 'W')
Checkbutton(my_window, text = 'Sports', bg = 'Silver', font = 'AgencyFB',
            fg = 'Black', variable = sports_checked)\
                              .grid(row = 2, column = 2, sticky = 'W')
Checkbutton(my_window, text = 'Travel', bg = 'Silver', font = 'AgencyFB',
            fg = 'Black', variable = travel_checked)\
                              .grid(row = 3, column = 0, sticky = 'W')
Checkbutton(my_window, text = 'Science', bg = 'Silver', font = 'AgencyFB',
            fg = 'Black', variable = science_checked)\
                              .grid(row = 3, column = 2, sticky = 'W')

#Let the user know what print button is for
Label(my_window, text = 'Print the latest news for these topics',\
      font = 'AgencyFB', bg = 'Silver', fg = 'Black')\
                 .grid(row = 4, column = 0, rowspan = 1, columnspan = 3,\
                        sticky = 'W')
#Print button
print_button = Button(my_window, text = 'Print', bg = 'Dark Orange', width = 10,
                      command = press_print)\
                      .grid(row = 5, column = 1, sticky = 'E')

#Progress message
Label(my_window, text = 'Watch the progress', font = 'AgencyFB', bg = 'Silver',\
      fg = 'Black').grid(row = 6, column = 0, columnspan = 3, sticky = 'W')

#Progress box
margin_size = 3
progress_text = Text(my_window, borderwidth = margin_size, width = 34, \
                     height = 10, bg = 'White', relief=GROOVE)
progress_text.grid(row = 7, column = 0, sticky = 'W', columnspan = 3)

#Read newspaper message
Label(my_window, text = 'Get updated!', font = 'AgencyFB', bg = 'Silver',\
      fg = 'Black').grid(row = 8, column = 0, columnspan = 3, sticky = 'W')

#Read button
read_button = Button(my_window, text = 'Read', bg = 'Dark Orange', width = 10,
                     command = read).grid(row = 9, column = 1, sticky = 'W')

#Save data message
Label(my_window, text = 'Save data', font = 'AgencyFB', bg = 'Silver',\
      fg = 'Black').grid(row = 10, column = 0, columnspan = 3, sticky = 'W')

#Save button
save_button = Button(my_window, text = 'Save', bg = 'Dark Orange', width = 10,
                     command = save).grid(row = 11, column = 1, sticky = 'W')
#Wait for user inputs
my_window.mainloop()
