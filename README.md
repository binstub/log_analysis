# LOG Analysis
_Internal reporting tool_ for a newspaper site that will use information from the database to discover what kind of articles the site's readers like. The database contains newspaper articles, as well as the web server log for the site. The project will run from the command line. It won't take any input from the user. Instead, it will connect to that database, use SQL queries to analyze the log data, and print out the answers to some questions.
##### Questions to answer:
-What are the most popular three articles of all time?
-Who are the most popular article authors of all time?
-On which days did more than 1% of requests lead to errors?
This is one of the projects required to complete Full Stack Web Developer nanodegree program at Udacity
### Getting Started
We are using a virtual machine (VM) to run an SQL database server and a Python script that uses it
#### Prerequisites
To start on this project, you'll need database software (provided by a Linux virtual machine) and the data to analyze
#### Install VirtualBox
VirtualBox is the software that actually runs the virtual machine. You can download it from [virtualbox.org]. Install the platform package for your operating system. You do not need the extension pack or the SDK. You do not need to launch VirtualBox after installing it; Vagrant will do that.
Ubuntu users: If you are running Ubuntu 14.04, install VirtualBox using the Ubuntu Software Center instead. Due to a reported bug, installing VirtualBox from the site may uninstall other software you need.
#### Install Vagrant
Vagrant is the software that configures the VM and lets you share files between your host computer and the VM's filesystem. Download it from [vagrantup.com]. Install the version for your operating system.
Windows users: The Installer may ask you to grant network permissions to Vagrant or make a firewall exception. Be sure to allow this.
This will give you the PostgreSQL database and support software needed for this project. If you have used an older version of this VM, you may need to install it into a new directory.
From your terminal, inside the vagrant subdirectory, Bring VM up and running with  vagrant up. Then log into it with vagrant ssh.

#### Download the data
You can [download data here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip). The file inside is called _newsdata.sql_. Put this file into the vagrant directory, which is shared with your virtual machine.
To load the data, cd into the vagrant directory and use the command
```
psql -d news -f newsdata.sql
```
Running this command will connect to your installed database server and execute the SQL commands in the downloaded file, creating tables and populating them with data
### Views
Log into database from shell with command psql news. Run following script to create the following view in the database
```
CREATE OR REPLACE VIEW view_log AS
SELECT CAST(time as date) AS request_date, count(*) AS total_views,
SUM(CASE WHEN status LIKE '40%' THEN 1 ELSE 0 END) AS failed_views
FROM log
GROUP BY request_date;
```

### Running the tests
Type python **log_analysis.py** from inside the VM. output_file contains a snapshot of the output the is displayed upon running the command
### Coding Style
Code confirms to **PEP8** standard
### Authors
Bindu Govindaiah
