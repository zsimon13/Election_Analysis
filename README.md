# Election Audit Analysis

## Overview of the Electoin Audit
A Colorado Board of Elections employee was given a project to analyze data from a recent congressional election. He was given a dataset in a .csv file that included voter ID, candidate name, and the county whcih the vote was cast. He asked to find the following data:
1. Total number of votes cast
2. The percentage of votes cast in each county
3. The number of votes that were cast in each county
4. The county with the largest turnout of voters\
5. The candidates who recieved votes
6. Number of votes each candidate recieved
7. The percentage of votes each candidate recieved
8. The winner of the election based on popular vote

## Election Audit Results

- A total of 369,711 votes were casted in this congressional election
- The voter turnout fo each county was:
  - Denevr County casted **306,055 votes** or **82.2%** 
  - Jefferson County casted **38,855 votes**, or **10.5 %**
  - Arapahoe County casted **24,801 votes** or **6.7%.**
-  Denver County had the largest amount of votes
-  The candidates recieved the following maount of votes
  - Charles Casper Stockham recieved **85,213 votes** or **23.0%** of the total vote
  - Diana DeGette recieved **272,892 votes** or **73.8%** of the total vote
  - Raymon Anthony Doane recieved **11,606 votes** or **3.1%** of the total vote
- Diana DeGette won the election with **73.8%** of the toal vote, totalling **272,892 votes**

![election_results](https://user-images.githubusercontent.com/102814578/167333074-59fb0b3a-b444-4c42-a1e4-409a85b98f5a.png)

## Election Audit Summary 
The script used to to perform this analysis showed good performance for a relatively large dataset, and ease of use when pulling the data from a independent file. It efficiently analyzed the avaliable data from the candidate and county perspective. This script is capable of scaling up to a statewide election with no alterations being necessary. It is built to pull information from a dataset with no magical numbers or hard values.

The script could be used to show other trends in the data with minor alterations. One example would be and addition of a loop to determine the percentage and total number of votes each candidate recieved from each indidvidual county. With minor alterations it could analyze the votes cast by each city or district in the state. It would have no issue scaling to a nationwide election and analyze votes by state or region as well. It was built with versaitilty in mind.

I am open to converstaion on how this could be used in future audit analysis and how it can be improved to handle projects you may have.
