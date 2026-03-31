# HRM-Housing-project
Housing Affordability and Fiscal Sustainability in Halifax 


## Live Dashboard
[View the Streamlit Dashboard here](https://hrm-housing-project-ipzb4fxhbv3d8jhgv9sgdb.streamlit.app/)

## Project Overview
This dashboard supports housing policy decision-making in Halifax by helping users compare renter concentration across zones, track changes over time, and examine the relationship between population and vacancy conditions. Together, these patterns can help identify where housing pressure may be strongest and where policy responses such as zoning reform, supply expansion, or targeted planning attention may be most needed.

## Dashboard Features
- Interactive bar chart comparing percentage of renter households across rental market survey zones
- Interactive line chart showing how percentage of renter households changes over time
- Interactive scatter plot exploring the relationship between population and primary market vacancy rate
- User inputs that allow the viewer to change datasets, variables, and filters

## User Guide
1. Open the live dashboard using the link above.
2. Use the left sidebar to choose a dataset and apply filters.
3. In Visualization 1, compare renter concentration across different rental market survey zones.
4. In Visualization 2, examine how renter concentration changes over time.
5. In Visualization 3, explore the relationship between population and vacancy rate across zones.
6. Use the Decision Support Summary at the bottom to interpret what the patterns may imply for housing policy and planning decisions.

## Repository Structure
- `src/app.py` contains the Streamlit dashboard code
- `data/` contains the datasets used in the dashboard
- `requirements.txt` lists the Python packages needed to run the app

## Decision Statement 

Should the Nova Scotia prioritze zoning reform to enable higher-density housing in established neighbourhoodsor continue expanding housingsupply through suburban greenfield development, in order to improve affordability while maintaining municipal fiscal sustainabilityy over the next decade. 

> [!WARNING]
> There are others doing this already in the class. There is a requirement to be unique to you.  Consider pivoting to your hometown.

## Executive Summary 

Housing affordability in the Halifax Regonal Municipality has become increasingly strained as population growth, low vacancy rates, and rising housing costs placepressure on renters and prospective homebuyers. at the same time, the municipality faces long term fiscal challenges related to infrastructure expansion and service delivery, making decisions about housing development patterns especially consequential. how and where new housing is built therefor has significant implications for both affordability outcomes and municipal financial sustainability.

This project evaluates the tradeoffs between enabling higher density housig through zoning reform in established neighbourhoods and continuing to expand housing supply through suburban greenfield development. using housing and demographic data alongside systems thinking tools, the analysis examines how these strategies influence housing supply, prices, infrastructure costs, and fiscal pressure overtime. The goal is to provide evidence based guidence to support municipal decision makers in balancing housing affordably with long term fiscal sustainability over the next decade. 

[Read more](Background.md)

## Initial CLD

![Casual Loop Diagram](img/cld.png)

## CLD brief description 

The casual loop diagram highlights key feedback mechanisms affecting housing affordability and municipal finances in HRM. Reinforcing loop R1 shows how suburban expansion increases infrastructure costs and fiscal pressure, encouraging continued outward development. Loop R2 illustartes how economic opportunity and percieved desirability attract in migration, increasing housing demand and price pressures. Finally Loop B1 demonstartes how increased zoning permissiveness supports higher density infill development, exopandinng housing supply and eating affordability pressures overtime. 

## Milestone 2 

## Milestone 2: Data Sources summary

Four datasets were used to inform the analysis of housing affordability and supply dynamics across Nova Scotia. The first examined the percentage of renters by community, highlighting variation in rental demand and identifying areas where affordability pressures may be strongest. The second analyzed active residential housing projects by community, showing how development activity is distributed across the province and where supply expansion is most concentrated. The third dataset tracked core housing need over time, providing insight into broader trends in housing adequacy and affordability challenges. The fourth examined rent price trends over time, demonstrating sustained upward pressure on rental costs across Nova Scotia. Together, these data sources helped identify key system variables—such as renter concentration, housing supply growth, development distribution, rent escalation, and affordability pressures—and directly informed the refinement of the Causal Loop Diagram.

## Data Sources 

https://data-hrm.hub.arcgis.com/datasets/HRM::zoning-boundaries/explore?location=44.853757%2C-63.171443%2C8

 https://data-hrm.hub.arcgis.com/datasets/18bd9d8f90c84f2caf80260c0ef91c82_0/explore?location=44.854030%2C-63.171178%2C8
 
 https://lemr.ca/data-maps/halifax/

## Data Wrangling 

![DataWrangling](img/wrangling-flow.png) 

## Visualization 1 

![visualiztion1](img/viz-renter-households-time.png) 

This visualization shows the percentage of rented households in core housing needs. It shows the change over recent years which is lowest at the end of 2022. This matters for the Zoning reform in Nova Scotia as it is expensive to make down payments on houses so with the reform In place it will likely lower cost of living and make it slightly more affordable if multiple units are created into duplexes and stuff rather than massive houses taking up a lot of space.

## Visualization 2 

![visualization2](img/viz-households-vs-renter-households.png) 

This visualization shows relationships between variables of regular households compared to renter households. There are 2 849 975 regular households compared to 1 094 675 renter households. When implementing a working with the reform over the next decade it this will allow cheaper and more affordable rent so people who can’t afford there ow house to be able to live comfortably while paying rent and all other necessities. 

## Visualization 3 

![visualization3](img/Picture_3.png)

This visualization shows the percentage of renters in different parts of nova scotia. This refers to my CLD diagram when breaking down affordability. So, you see that Dartmouth has high renting percentage compared to Bedford as it is more of an affordable place to rent with apartments and duplexes, which are going to be the cheaper option then renting a whole house as Bedford has a more limited option then the higher percentage places.

## Visualization 4 

![visualization4](img/Picture_4.png)

This visualization shows the number of property projects in nova scotia all over. With Halifax having a large amount of the population it is good that they have so many projects on the go. It is important for the zoning reform to have the projects starting now to allow for cheaper living to start developing now. Smaller places like Falmouth would see less projects on the go as population is small and all around more affordable living so its important Halifax is generating a lot of it for people who live in the city. 

## Refined CLD Diagram 

![housingpolicy](img/cld-final.png) 

## Explanation of key feedback loops and impications for the decision 

## Balancing loop 

The balancing loop captures the system’s natural constraints. As housing supply increases, available land for development decreases, especially in high-demand areas like Halifax. Reduced land availability can raise development costs and, in turn, rent prices, which lowers renter affordability. As affordability worsens, pressure may grow to slow development or maintain current regulations, limiting further supply expansion and stabilizing the system rather than allowing continued growth.

## Reinforcing loop 

The reinforcing loop in this system shows how zoning reform can generate self-sustaining improvements in affordability. When zoning reform allows the creation of more duplexes and apartments, housing supply increases. As supply expands, renter affordability improves, which can build political and public support for continued reform. That additional support enables further zoning changes, creating a cycle that strengthens itself over time.

## Implications for the decisions 

The implication of these feedback loops for the decision is that zoning reform has the potential to improve housing affordability, but its impact will depend on how the system’s constraints are managed. The reinforcing loop suggests that reform can generate compounding benefits over time by increasing housing supply and strengthening support for continued density and development. However, the balancing loop shows that land limitations and rising development costs may eventually slow or offset those gains, particularly in high-demand areas like Halifax. This means that zoning reform alone may not be sufficient; to sustain affordability improvements, it likely needs to be paired with policies that address land availability, infrastructure capacity, and cost pressures.

## System Implications 

Overall, the system behaves in a way that produces both growth and constraint at the same time. Zoning reform can trigger reinforcing dynamics that improve housing supply and affordability, but structural limits such as land scarcity and rising costs naturally push the system back toward equilibrium. This means affordability challenges are not caused by a single factor, but by interconnected feedback processes. Long-term improvement will depend on managing these feedback loops strategically rather than expecting one policy change to permanently solve the problem.

## Milestone 3: Path A System Focus

## System Archyetype Identification 

The system underlying housing affordability in Nova Scotia most closely reflects Growth and Underinvestment. In this system, rising housing demand places increasing pressure on the province’s housing suppl and rental market, also affordability. While zoning reform and higher-density development could help relieve this pressure, investment in supportive policies, infrastructure, and regulatory change is often delayed or insufficient relative to the pace of demand growth.

Key Variables in this archetype include:

-Housing Demand 

-Housing Supply

-Rent Prices

-Rent Affordability 

-Active Housing Project 

-Development Approval Capacity

The reinforcing side of the system is that continued demand for housing increases pressure for more development and policy change. However, when reform and supporting investment are delayed, the system cannot expand supply quickly enough, causing affordability problems to persist or worsen.

Evidence from milestone 2 that supports this structure:

-Figure 1 Showed that changes in core housing need over time, indicating that affordability pressure remains a persistent issue accross the province

-Figure 2 Showecd the large difference between regular households and renter households, highlighting the scale of reliance on rental housing and the importance or affordable rental supply

-Figure 3 showed that renter concentration varies accross different parts of nova scotia, suggesting that affordability pressure is unevenly distributed and stronger in some communities than others

-Figure 4 showed that active property development projects are concentrated in a limited number of commmunities, meaning supply growth is not occouriing evenly accross the province

This reflects a system in which growth in housing need is approaching the limits of current planning and development capacity, while deeper structural investment in zonign reform and supply expansion has not fully caught up yet

## System Archetype Diagram 

<img width="1536" height="1024" alt="image" src="https://github.com/user-attachments/assets/a6d02786-f89e-4ac3-a62f-339ac36487fc" />

This reflects a system in which growth in housing need is approaching the limits of current planning anf development capacity, while deeper structural investment in zoning reform and supply expansion has not caught up fully yet 

## Scenario Narratives

## Scenario 1: Status Quo (No Major Change) 

If Nova Scotia continues with its current approach, Housing supply will likely keep increasing, but not at a pace that fully will match rising demand over the next 5 to 10 years. Development would remain uneven accross the province, with some communities seeing more activity than other, while affrodability pressure continue for renters and lower income households. In this scenario, the balancing loop from the CLD remains strong becasue delays in approvals, limited zoning reform, and unevem project distribution continue to slow the system's response. Rent prices may stay high even if vacancy rates improve somewhat, becasue affrodable units would still be limited in many areas. Over time, this could leave the province with continued afforability stress and only modest improvement in overall housing access. 

## Scenario 2: Zoning Reform and Higher Density (Intervention A) 

when decision makers prioritize zoning reform and allow more duplexes, apartments, and mid rise housing in established communities, housing supply could expand more effectively over time. This would strengthen the reinforcing loop in the CLD, because more flexible zoning would make it easier for the system to respond to demand and gradually improve affordability. Over the next 5 to 10 years, this could create a more diverse housing stock, improve renter affordability, and reduce pressure on outward expansion by making better use of existing infrastructure. However, the success of this scenario would still depend on implementation, municipal cooperation, and whether developments can move through the system quickly enough. Public resistance, servicing limits, and construction costs could still slow progress, but this option gives the province the strongest long-term chance of improving affordability.

## Scenario 3: Greenfield and Suburbam Expansion (Intervention B)

If Nova Scotia mainly focuses on suburban and greenfield development, the province may be able to add housing units more quickly in the short term, especially in quickly growing regions with available land. This could reduce some immediate pressure by increasing supply at a larger scale than small infill projects alone. However, this approach would do less to address the structural barriers within established communities, so the core system problem would remain. Over time, this option could strengthen balancing pressures through rising infrastructure costs, more dispersed development, and greater dependence on outward expansion. While more housing would be built, affordability gains may be limited if the new supply is costly to service or not located where rental demand is highest. In the long run, this could create more units without fully solving the province’s affordability challenges.

## Leverage Point Anaylisis 

The most effective leverage point in this system would be:

Accelerating Zoning reform to allow more Higher Density and Multi Unit housing in established communities 

This leverage point has high impact becasue it directly influences the reinforcing loop driving housing supply and renter affordability. By allowing more duplexes, apartments, and mid rise developments, the system becomes more responsive to hosuing demand rather than remaining contrained by outdated land use rules.

This intervention affects multiple variables:

-increases housing supply

-Improves renter affordability 

-reduces pressure on rent prices

-Expands teh creation of duplexs and apartments 

-makes better use of existing infrastructure

It also strengthens the reinforcing loop in the system by making it easier for supply to grow as demand increases. At the same time, it helps weaken the balancing pressures caused by limited housing options, delayed development, and rising affordability challenges.

Potential Risks 

-Public resistance to increased density

-Delays in municipal implementation 

-infrasturcture capacity concerns in some cumminities 

-The possibility that new development may not immediately reach lower income households 

Despite these risks, this leverage point offers the strongest system-wide impact relative to effort because it changes the structure of the housing system rather than only reacting to its symptoms. By removing barriers to denser development, Nova Scotia can better address long-term affordability, reduce pressure on the rental market, and improve the province’s ability to meet future housing demand.

## Impications for this decision 

The analysis suggests that Nova Scotia’s housing system is characterized by rising demand and affordability pressure without a fast enough expansion in housing supply.

Among the options, prioritizing zoning reform and higher-density development appears to be the strongest long-term strategy because it addresses the structural barriers limiting supply rather than only responding to symptoms. While greenfield development may add units more quickly in the short term, it does less to improve efficiency and may create higher long-term infrastructure costs. 

The status quo would likely allow affordability challenges to continue, reinforcing the need for intervention.

Overall, this suggests that decision-makers should prioritize zoning reform as the most effective way to improve housing affordability, strengthen system responsiveness, and support more sustainable growth across Nova Scotia.
