# Qorvo Intern Project - Automated Au Consumption Tracking for PLS Toolset

## Overview

This project, **Automated Au Consumption Tracking for PLS Toolset**, was developed during an internship at Qorvo. The primary goal was to create an automated system that tracks gold (Au) consumption in the plating process, ensuring no manual tracking is required. This solution aims to eliminate potential gold depletion in the Au plate bath concentration and prevent loss in the semiconductor manufacturing process. Automating the gold consumption tracking improves operational efficiency, reduces manual operator intervention, and results in significant cost savings.

## Table of Contents
- [Project Description](#project-description)
- [Current Problem](#current-problem)
- [Target State](#target-state)
- [Automation Workflow](#automation-workflow)
- [Results](#results)
- [Requirements](#requirements)
- [Installation](#installation)
- [Acknowledgments](#acknowledgments)

## Project Description

The **Automated Au Consumption Tracking** project automates the monitoring of critical bath parameters in the PLS (Plating Line System) toolset. The previous system relied on manual tracking by operators, which was prone to errors and inefficiencies. The new automated system tracks the amp-hours accumulated during the plating process and alerts engineers when Au additions are required. This automation prevents gold depletion and eliminates the need for manual intervention, saving both time and resources.

## Current Problem

The current state of gold consumption tracking includes manual resets and tracking by engineers, which introduces several issues:
- **Manual Corrections**: Engineers manually check the amp-hour accumulations and adjust for any false resets.
- **Time Consuming**: Engineers spend up to 10 minutes per shift tracking and correcting these values.
- **Risk of Gold Depletion**: Without proper tracking, the gold concentration could be depleted, potentially leading to significant losses in chemistry replacements costing up to $150,000.

## Target State

The project aims to:
- **Automate Au Consumption Tracking**: Completely remove manual tracking and ensure real-time monitoring of wafer processing and Au consumption.
- **Increase Efficiency**: Save 10 minutes of operator time per shift and ensure smooth operations.
- **Prevent Loss**: Avoid depletion of gold concentration and prevent the need for expensive chemistry replacements.

## Automation Workflow

The workflow includes several steps:
1. **Event Listener Setup**: An ActiveMQ consumer listens to the EES (Equipment Execution System) for reset events and other messages.
2. **Data Query**: Python scripts using SQL queries retrieve relevant data from the `FDCDB_trace` database.
3. **Message Parsing**: XML messages from the event listener are parsed to extract information like `event_time` and `chamber_ID`.
4. **Amp-Hour Tracking**: Python scripts parse the amp-hour data, calculate the accumulated amp-hours, and update the backend system.
5. **Automatic Updates**: When a reset event is detected, the system automatically updates the amp-hour counter to ensure accurate tracking.

## Results

The project delivered several key benefits:
- **Real-Time Tracking**: Fully automated system tracks critical bath parameters in real time.
- **Cost Savings**: Saves $2,400 annually by removing the need for manual operator tracking. It also prevents potential chemistry replacement costs of up to $150,000.
- **Operational Efficiency**: Eliminates manual errors and reduces operator workload, improving overall efficiency in the production line.

## Requirements

To run this project, the following dependencies are required:
- **Programming Languages**: Python, Java
- **Libraries**: 
  - Python: pandas, pyodbc, SQLAlchemy
  - Java: ActiveMQ libraries
- **Database**: Access to the `FDCDB_trace` database
- **Additional Tools**: Jupyter Notebook for running Python scripts

You can install the necessary dependencies via `pip` for Python:
```bash
pip install pandas pyodbc sqlalchemy
```

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Fijuwat1032/Qorvo_Au_Consumption_Tracking.git
   ```

2. **Navigate to the Project Directory**:
   ```bash
   cd Qorvo_Au_Consumption_Tracking
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Notebook**:
   Launch the Jupyter Notebook and open the file `Query Automation for bins.ipynb` to start the automation.


## Conclusion

The **Automated Au Consumption Tracking for PLS Toolset** project successfully addresses the critical issue of gold depletion in the wafer plating process. By automating the tracking of amp-hours and monitoring the Au concentration in real time, this solution not only eliminates the need for manual intervention but also significantly enhances operational efficiency. The automated system ensures precise tracking of critical bath parameters, preventing costly mistakes such as gold depletion and reducing the time engineers spend manually adjusting and monitoring the system. 

Through this project, Qorvo can expect both immediate and long-term cost savings, as well as a more efficient production line. The automation of this process serves as a scalable solution that can be expanded to other areas of semiconductor manufacturing where manual tracking remains a bottleneck.

The successful implementation of this system underscores the value of integrating automation and real-time data tracking in industrial processes, highlighting the impact of data-driven solutions on cost savings and operational improvements. This project paves the way for further innovations in manufacturing automation at Qorvo.

## Acknowledgments

I would like to extend my gratitude to **Eric McComick** for his guidance and support throughout the project. Special thanks to **Phuong-Thao Ton-Nu** for mentorship and valuable input during my internship at Qorvo.

