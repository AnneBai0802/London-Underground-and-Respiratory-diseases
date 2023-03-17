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
        <li><a href="#Introduction"Introduction</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#NO2 and COVID-19">NO2 and COVID-19</a></li>
      </ul>
    </li>
    <li>
        <li><a href="#Discussion">Discussion</a></li>
    </li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

A recent study conducted by NHS reveals that respiratory diseases is the third biggest cause of death in England, affecting one in every five people. In addition, hospital admissions for respiratory diseases have risen over the past seven years in a rate three times faster than the total admission [1]. For this reason, we would like to investigate in how pollution in major cities such as London has an impact on the health of the population and their ability to fight off a virus such as COVID-19 with a long-term exposure to high concentration of toxins which are abundant in air pollution. 

We believe that long-term overexposure to air pollution has a severe impact on one’s respiratory health, thus their ability to fight respiratory illness’ such as COVID-19 was significantly less than those who were not exposed to as much air pollution in their lifetimes. We wish to make quantitative analysis on this theory to test its accuracy. 

Use the `README.md` to get started.

### Introduction (Adheesha)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## SARS-CoV-2 2 is a virus affecting primarily the respiratory system that resulted in a global pandemic starting in December 2022. There have been upwards of 6.8 million deaths recorded as being due to the infection as of March 2022. 
In terms of pathophysiology, the virus binds to ACE2 on respiratory epithelial cells using its spike protein, entering the cell and using its genetic machinery to proliferate. 
Presentation can range from asymptomatic to severe pneumonia and lung failure. Most symptoms are respiratory in nature, such as coughing, and fever is also common. However, the virus also affects processes in  other components of the body, such as blood clotting times. 
The pandemic had a massive impact not only in terms of deaths caused directly on the virus, but also by delaying routine procedures for other illnesses. It also compromised key determinants of health, such as exercise and socialising, by limiting peoples' ability to leave their homes. 
Mortality from COVID varies based on multiple risk factors. Established ones include advanced age, higher BMI and existing respiratory illnesses. 
Given that existing respiratory dysfunction predisposes mortality from COVID, and pollutants such as nitrogen dioxide have been suspected of causing respiratory damage, we were interested in seeing the correlation between nitrous oxide levels and COVID mortality in different London boroughs. 
We predicted there would be a positive correlation, but also noted that there could be multiple confounding factors affecting the relationship.


<!-- GETTING STARTED -->
## Getting Started

The program contains a few Python files used to clean data and plot graphs. Below are explanations to each file.

### NO2 and COVID-19 (Anne)

For plotting the correlation between NO2 and mortality rate of COVID-19, four python files are used. The file `Clean_Data_Covid.py` is used to read te data from the two csv files, clean them so that only records in the year 2021 are considered, and calculate mortality rate of each borough in 2021. The file `Site_To_COde.py` is used to separated each of the site in the csv file containing NO2 pollution level into boroughs. The file `Clean_Data_NO2.py` is used to read data from the NO2 csv file and obtain average NO2 level of each borough. Finally, the file `Core.py` is used to study the correlation between the average NO2 level and the mortality rate of each borough. The outcome is as shown in the figure
<div align="center">
  <a href="https://github.com/AnneBai0802/London-Underground-and-Respiratory-diseases">
    <img src="Percentage Death 2021 against NO2 in 2015-2023.png" alt="Mortality Rate of COVID-19 against NO2" >
  </a>


<!-- DISCUSSION -->
## Discussion
(Adheesha) We did not get a positive correlation as expected, instead getting a negative one (albeit with a small correlation coefficient). Disregarding the possibility of an error in data analysis, there could be two possibilities for this. Either higher nitrogen dioxide levels are genuinely associated with lower COVID morality, or there are confounding factors at play. Given that COVID-19 mortality has been established to be multifactorial, the second option is certainly most likely. For instance, higher nitrogen dioxide levels may be found in more urbanised London boroughs, which also generally have better access to healthcare. Also, more urbanised boroughs have younger populations in general, and young people are less likely to die from COVID. The effect of these confounding factors seems to be more significant than that of nitrogen dioxide. The next logical step would be to perform a multivariate analysis, looking at the correlation coefficient between nitrogen dioxide and COVID mortality having accounted for factors such as age. If the correlation is different to that in the univariate analysis that we have conducted, confounding is indicated.

<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

We greatfully acknowledge our tutor, Jay, for his help and assitance during the project.

* [NO2 data file](https://www.londonair.org.uk/london/asp/datadownload.asp)
* [COVID-19 cases in boroughs](https://data.london.gov.uk/dataset/coronavirus--covid-19--cases)
* [COVID-19 deaths in boroughs](https://data.london.gov.uk/dataset/coronavirus--covid-19--deaths)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

