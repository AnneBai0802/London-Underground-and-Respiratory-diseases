# Analysing London\'92s pollution and the effect it has on respiratory diseases. 

This project is meant for the Interdisciplinary Research Computing module at Imperial College London. 

Further information can be found on the project proposal. 

Collaborators: Adheesha Kumarasinghe, Anne Bai, Elise Vong, Jeremy O'Connor

Note that due to prior coding experience, Anne and Jeremy conducted the data analysis. Adheesha and Elise, being medical and life sciences students respectively with less coding knowledge, contributed to the project from a public health perspective, writing the introduction and discussing the results. 


<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#NO2 and COVID-19">NO2 and COVID-19</a></li>
      </ul>
    </li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

A recent study conducted by NHS reveals that respiratory diseases is the third biggest cause of death in England, affecting one in every five people. In addition, hospital admissions for respiratory diseases have risen over the past seven years in a rate three times faster than the total admission [1]. For this reason, we would like to investigate in how pollution in major cities such as London has an impact on the health of the population and their ability to fight off a virus such as COVID-19 with a long-term exposure to high concentration of toxins which are abundant in air pollution. 

We believe that long-term overexposure to air pollution has a severe impact on one’s respiratory health, thus their ability to fight respiratory illness’ such as COVID-19 was significantly less than those who were not exposed to as much air pollution in their lifetimes. We wish to make quantitative analysis on this theory to test its accuracy. 

Use the `README.md` to get started.

<p align="right">(<a href="#readme-top">back to top</a>)</p>




<!-- GETTING STARTED -->
## Getting Started

The program contains a few Python files used to clean data and plot graphs. Below are explanations to each file.

### NO2 and COVID-19

For plotting the correlation between NO2 and mortality rate of COVID-19, four python files are used. The file `Clean_Data_Covid.py` is used to read te data from the two csv files, clean them so that only records in the year 2021 are considered, and calculate mortality rate of each borough in 2021. The file `Site_To_Code.py` is used to separated each of the site in the csv file containing NO2 pollution level into boroughs. The file `Clean_Data_NO2.py` is used to read data from the NO2 csv file and obtain average NO2 level of each borough. Finally, the file `Core.py` is used to study the correlation between the average NO2 level and the mortality rate of each borough.




<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

We greatfully acknowledge our tutor, Jay, for his help and assitance during the project.

* [NO2 data file](https://www.londonair.org.uk/london/asp/datadownload.asp)
* [COVID-19 cases in boroughs](https://data.london.gov.uk/dataset/coronavirus--covid-19--cases)
* [COVID-19 deaths in boroughs](https://data.london.gov.uk/dataset/coronavirus--covid-19--deaths)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

