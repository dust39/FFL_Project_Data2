# FFL_Project_Data2_2022
_______________________________________________________________________________________________________________________________________
# Hello There

My intent for this project is to demonstrate my Git/GitHub, Python, and Tableau knowledge. The Python portion of my project is geared toward data analysis. 

## My Project 
The main goal of this project is to answer a simple question related to fantasy football. 
1. What position scores the most points in an average year?

1. Running the program will do the following:
    1. Outline step 1 
    2. Outline step 2 
    3. Outline step 3
    4. Finally the program will create and save a .jpg file titled with the selected year.

I chose this project to show my skills because I love fantasy football. I wanted to work on a project about a subject that interests me so that I can continue to advance and improve the skills I have learned.

### My Project Features
Below is information on how to run the program followed by the features I selected to meet my project requirements:

#### Steps to Run My Program:

1. Clone my repository 
2. Navigate to the directory where your virtual environment will be created
    1. Create your virtual environment
    2. Install the required packages using my generated requirements.txt. I created requirements.txt on a windows machine. 
    <>For those on other Operating Systems I created a pared down version named requirements_multi_OS.txt
3. Run main.py from your command prompt:
    1. Create list here
        1. Create sublist here
        
**Thats it! Now on to how I met my project requirements below.**

#### Category 1- Reading in multipe data files(CSV)
I load 50 data sets, which are CSV files. There is one data set for each year from 1970 to 2019. 

#### Category 2- Merging Data Sets
- While I did not specifically use the merge or join command, I used the concat method to combine all 50 data sets into one large data set. I create a list from all 50 of the files in the "/yearly" directory and iterate over the list.
- I iterate over each CSV file, each iteration adds the year from which the data is pulled. Example all data pulled from the 1970.CSV file, will have 1970 displayed in the year column. 
- I create one large data set, by combining all 50 smaller data sets into one
- I clean and filter the data
    - I removed erroneous columns using drop
    - I removed all rows for which the listed player did not have a listed position by using `.query`.
#### Category 3-Choose from featue list 
Explain how I met this requirement
#### Category 4 -Best Practices 
For this requirement I created a virtual environment to complete my project. I used the Python PIP Freeze command to periodically list my document library dependencies via a requirements.txt file, which is in my repository for this project. The use of the requirements.txt file is outlined in the Steps to Run my Program section above. Fortunately I have not added any additional library installs since the beginning of my project. So, even though I have run PIP Freeze command periodically, nothing has changed so the file in GitHub is also unchanged.

At the time of posting this project, I was not aware that PIP Freeze may cause issues for users on other Operating Systems. I left the requirements.txt in tact because I have had other users test it and I know it works on Windows machines. However, I also created a separate requirements file named requirements_multi_OS.txt. This is a pared down version and should allow users with other operating systems to match my libraries for this project. If a user is still having problems the main libraries/packages/modules that I used were: Pandas, Matplotlib, and ipython/ipykernel for the Jupyter portion.
#### Git / GitHub

I continued my utilization of Git and furthered my knowledge on the subject during this project. I learned Git terminal command using GitBash.  I tried to make commits anytime I made changes and pushed those commits to my GitHub repository. Check out my commit history on this project [Here](https://https://github.com/dust39/FFL_Project_Data2/commits/main). Below are the Git terminal commands I learned and used most often.

- Git init : to initialize my local repository.
- Git status: to check the status of any file changes in my local repository.
- Git add: to add my changed files to a staging area.
- Git commit: to commit my changed files.
- Git push: to push my local commits up to my GitHub repository.

## Conclusion
Is there ever a conclusion in technology??? I learned so much working on this project. It may seem simple on the surface, but the amount the I have learned is incredible. I loved the challenge and I look forward to continuing my coding adventure. Thank You to Code Kentucky for this opportunity and Thank You for looking at my project!