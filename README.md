# FFL_Project_Data2_2022
_______________________________________________________________________________________________________________________________________
# Hello There

My intent for this project is to demonstrate my Git/GitHub, Python, and Tableau knowledge. The Python portion of my project is geared toward data analysis. 

## My Project 
The main goal of this project is to answer a simple question related to fantasy football. Fantasy football predictions and projections can vary widely every year based on a variety of factors. I wanted to keep it simple and look at 50 years of data to determine if a user can find that a certain player position provided more value than another when adding players in free agency. If forced to make a quick decision in a draft or in free agency can player position be used to help facilitate that decision making process based on actual data?

1. Running the program will do the following:
    1. Iterate over a quantity of 50 yearly CSV files containing fantasy football statistics.
    2. The script will add a year column
    3. The script will filter out unwanted/erroneous data.
    4. Finally the script will combine all 50 CSV files into one large master CSV file named "Appended_FFL_data.CSV".
    5. I will then use this master CSV file to do visualizations and analysis in Tableau.

I chose this project to show my skills because I love fantasy football. I wanted to work on a project about a subject that interests me so that I can continue to advance and improve the skills I have learned. I sourced my data from [FantasyDataPros](https://www.fantasyfootballdatapros.com/csv_files).

### My Project Features
Below is information on how to run the program followed by the features I selected to meet my project requirements:

#### Steps to Run My Program:

1. Clone my repository 
2. Navigate to the directory where your virtual environment will be created
    1. Create your virtual environment
    2. Install the required packages using my generated requirements.txt. I created requirements.txt on a windows machine and in standard python. 
    <>For those on other Operating Systems or Anaconda the only libraries/packages/modules that I used were: Pandas, Matplotlib, and ipython/ipykernel for the Jupyter portion. 
3. Navigate back to the cloned directory if different from virtual environment directory. Then run main.py from your command prompt:
    1. Nothing else is required from the user.
        1. The script will iterate over 50 CSV files that contain yearly fantasy football scores. As noted above: The script will then concatenate all 50 CSV files into one large data frame, add a year column, and filter out unwanted data. Finally the script will output one main CSV file. This large master CSV file (named "Appended_FFL_data.CSV") will be used to create visualizations and analyze the fantasy football data.
4. I also created a Juptyer Notebook with markdown to explain each block of my code for documentation.
    1. The user will be able to run this Jupyter notebook if the user has created a virutal environment using my requirements.txt file, which is included in the repository.
        
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
#### Category 3-Visualization usign a Tableau Dashboard
I used Tableau to do my analysis and create a dashboard. The link to the story is [Dustin's Fantasy Analysis Dashboard](https://public.tableau.com/views/FFL_Project_Data_Analysis2_2022/Story1?:language=en-US&publish=yes&:display_count=n&:origin=viz_share_link).
#### Category 4 -Best Practices 
For this requirement I created a virtual environment to complete my project. I used the Python PIP Freeze command to periodically list my document library dependencies via a requirements.txt file, which is in my repository for this project. The use of the requirements.txt file is outlined in the Steps to Run my Program section above. Fortunately I have not added any additional library installs since the beginning of my project. So, even though I have run PIP Freeze command periodically, nothing has changed so the file in GitHub is also unchanged.

At the time of posting this project, I was not aware that PIP Freeze may cause issues for users on other Operating Systems. I left the requirements.txt in tact because I have had other users test it and I know it works on Windows machines. However, I also created a separate requirements file named requirements_multi_OS.txt. This is a pared down version and should allow users with other operating systems to match my libraries for this project. If a user is still having problems the main libraries/packages/modules that I used were: Pandas, Matplotlib, and ipython/ipykernel for the Jupyter portion.

#### Category 5 -Interpretation of the Data
I used Tableau to do my analysis and create visualizations. However I created a jupyter notebook that performs the same functions as my main.py. The difference is I used markdown to explain groups of my code blocks. Additionally, I added some more script to give visual representation of the CSV/Data Frames changing through out the script.

#### Git / GitHub

I continued my utilization of Git and furthered my knowledge on the subject during this project. I learned Git terminal command using GitBash.  I tried to make commits anytime I made changes and pushed those commits to my GitHub repository. Check out my commit history on this project [Here](https://github.com/dust39/FFL_Project_Data2/commits/main). Below are the Git terminal commands I learned and used most often.

- Git init : to initialize my local repository.
- Git status: to check the status of any file changes in my local repository.
- Git add: to add my changed files to a staging area.
- Git commit: to commit my changed files.
- Git push: to push my local commits up to my GitHub repository.

## Conclusion
Is there ever a conclusion in technology??? I learned so much working on this project. It may seem simple on the surface, but the amount the I have learned is incredible. I loved the challenge and I look forward to continuing my coding adventure. Thank You to Code Kentucky for this opportunity and Thank You for looking at my project!