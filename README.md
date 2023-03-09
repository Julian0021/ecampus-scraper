# ecampus-scraper

A simple script to scrape your grades from the THM eCampus Platform. This script is very robust and easy to use unlike some Rust(y) soulutions out there. Simply
create a ``constants.py`` and define the ``JSESSIONID`` cookie along with the URL of your individual Exams Extract. The script takes the module ID as argument and prints the desired grade to the console as soon as it is published. The module ID can be found found in your module handbook.<br>

Inspired by [Daniel Brunner](https://www.dbrunner.de)
