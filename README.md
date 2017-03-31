<h3>Python Google-YouTube History Analytics</h3>
<br>A Python Python Google-YouTube History Analytics, which reads your history data you get from Google and provide analytics about your searches on Google, YouTube and YouTube watch history. It provides number of counts for the term you searched for.

<h3>Requirements</h3>
<ul>
<li>Python 3.x, Pandas (Run sudo pip3 install -r requirements.txt to install dependencies</li>
<li>A data downloaded from Google History (You can download from <a href="https://takeout.google.com/settings/takeout">Google History</a>)</li>
<li>Download history for YouTube and Searches. Select None from top and select YouTube and Serches</li>
</ul>

<h3>How To Use</h3>
<ul>
<li>After downloading data from Google, unzip it.From YouTube Takeout folder copy YouTube->history folder and paste where the script is located</li>
<li>Same, from the Searches takeout folder copy the Searches folder and paste where the scrpt is located</li>
<li>Running without parameters will execute for both YouTube and Google Searches</li>
<li>Pass --y Y for running the script on YouTube data</li>
<li>Pass --g G for running the script on Google Searches data</li>
<li>It provide output in the csv files in the working directory</li>
</ul>

<h5>For queries or issues, feel free to contact or open an <a href="https://github.com/srcecde/google-youtube-history-analytics/issues">issue</a></h5>
