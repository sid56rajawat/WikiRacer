![Wikiracer](https://user-images.githubusercontent.com/90323915/216801410-0233de2f-b0ec-4801-9aaf-68983f03ffba.png)

# WikiRacer
A tool that gives you a sequence of pages which can be followed to reach one Wikipedia page from another.

![GitHub last commit (branch)](https://img.shields.io/github/last-commit/sid56rajawat/wikiracer/master)

## Libraries Used
The program is built on Python 3.9.4 <br>
The following libraries were used:
- httplib2
- time
- bs4
  - BeautifulSoup
  - SoupStrainer
- Django(framework)

## Testing
Built and tested
on Windows 10(21H2) and Python 3.9.4 using pip for package management.
Dependencies are listed in requirements.txt

## Installation
![wikiracerDemo](https://user-images.githubusercontent.com/90323915/216811434-7d11884a-40be-4674-9d1c-4e2198ba0f77.gif)

Step1: Clone the repository
```shell
$ git clone https://github.com/sid56rajawat/wikiracer
```
Step2: Open the wikiracer directory and create a virtaul environment
```shell
$ python -m venv venv
```
Step3: activate the virtual environment(admin access required)
```shell
$ venv\Scripts\activate
```
Step4: install required packages
```shell
$ pip install -r requirements.txt
```
Step5: run the application
```shell
$ python manage.py runserver
```
Step6: open the browser and paste "localhost:8000/wikiracer"

Step7: Enter only the name of the start and target page .e.g,<br>
Start: fruit<br>
Target: mango

## Milestones
✓ Milestone 1 : Simple Breadth First Search (BFS)

## Acknowledgements
### BFS Algorithm
[GeeksForGeeks](https://www.geeksforgeeks.org/breadth-first-search-or-bfs-for-a-graph/)
### Links Scraping
[Misha Sv](https://www.youtube.com/watch?v=MUxM5V-6m-Y&ab_channel=MishaSv)
### Django
[IDG TECHtalk](https://www.youtube.com/watch?v=ZsJRXS_vrw0&ab_channel=IDGTECHtalk)<br>
[Dennis Ivy](https://www.youtube.com/watch?v=0sMtoedWaf0&t=168s)<br>
And many more...
### Documentation
[The Git Guild](https://www.youtube.com/watch?v=a8CwpGARAsQ&ab_channel=TheGitGuild)
