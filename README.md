# 💼 Deloitte Data Analytics Virtual Experience Project (Forage)
## **Daikibo Factory Downtime & HR Equality Review Analysis**

Welcome to my completed project for the **Deloitte Data Analytics Virtual Experience** hosted on [Forage](https://www.theforage.com/). This simulation replicates real client-facing work at Deloitte, where I used **Tableau**, **Excel**, and **Python** to solve business problems and deliver actionable insights.

---

## 📌 Project Summary

**Client:** Daikibo Corporation – a global manufacturing company  
**Tools Used:** Tableau Public, Excel, Python (Colab)  
**Skills Demonstrated:** Data wrangling, dashboard design, logic classification, stakeholder-focused storytelling

| Task | Objective |
|------|-----------|
| 🏭 Machine Downtime Analysis | Identify factories and device types with the highest machine downtime |
| 👥 HR Equality Review Analysis | Classify performance review fairness based on quantitative equality scores |

---

## 📊 Task 1: Machine Downtime Analysis (Tableau)

### 🧠 Problem Statement 
Daikibo's leadership team wanted to understand:
1. **Which factory had the most machine downtime?**  
2. **Which devices contributed most to breakdowns at that factory?**

### 📁 Dataset Overview  
**File Name:** `daikibo-telemetry-data.json` (converted to CSV via Python)  
**Rows:** 2,300+ telemetry records  
**Main Columns:**

| Column Name         | Description                                                                 | Sample / Values                          |
|---------------------|-----------------------------------------------------------------------------|-------------------------------------------|
| `deviceID`          | Unique identifier for each machine device                                   | `19ff3161-2b3a-40a3-8604-bdc6532d0dab`    |
| `deviceType`        | Category of the machine                                                     | 'AirWrench', 'CNC', 'ConveyorBelt', 'Furnace', 'HeavyDutyDrill', 'LaserCutter', 'LaserWelder', 'MetalPress', 'SpotWelder' |
| `timestamp`         | UNIX timestamp of the machine's health status record                        | `1619816400000` (in milliseconds)         |
| `location_country`  | Country of the factory                                                      | 'china', 'germany', 'japan'                                   |
| `location_city`     | City of the factory                                                         | 'berlin', 'osaka', 'shenzhen', 'tokyo'                    |
| `location_area`     | Industrial area where factory is located                                    | `keiyō-industrial-zone`                   |
| `location_factory`  | Full name of the factory                                                    | 'daikibo-berlin', 'daikibo-factory-meiyo', 'daikibo-factory-seiko', 'daikibo-shenzhen'                   |
| `location_section`  | Section of the factory where the machine is installed                       | `section-1`, `section-2`, etc.            |
| `data_status`       | Operational health of the machine                                           | `healthy`, `unhealthy`                    |
| `data_temperature`  | Temperature (°C) of the machine at time of recording                        | `27`, `35`, etc.                          |


> Each “unhealthy” record = 10 minutes of downtime.

### 🛠️ What I Did
- Flattened a complex telemetry JSON into a structured CSV using Python
- Calculated downtime: each `"unhealthy"` status = 10 minutes
- Built an interactive Tableau dashboard with:
  - Downtime per Factory chart
    
    <p align="center">
      <img src="./images/downtime_per_factoryLocation.png" alt="Downtime per Factory chart" width="800"/>
    </p>
    
  - Device Type chart (updates dynamically by selected factory)
 
   <p align="center">
      <img src="./images/downtype_by_deviceType.png" alt="Device Type chart" width="800"/>
   </p> 
    
- Enabled clear business exploration of machine issues by site

### 📊 Key Insights  
✅ **Osaka** factory had the **most total downtime**.  
✅ **LaserWelder** machines in Osaka were the top contributors to downtime.  
✅ Delivered a interactive dashboard

<p align="center">
  <img src="./images/Machine_Downtime_Analysis-DB.png" alt="Tableau Dashboard" width="800"/>
</p>

👉 [Click here to view the interactive dashboard](https://public.tableau.com/views/Daikibo-Telemetry/Machine_Downtime_Analysis-DB?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link)

### 💥 Business Impact  
- Leadership can now **prioritize maintenance** and improve uptime.  
- Dashboards simplify identifying bottlenecks across sites.

---

## 🧮 Task 2: Equality Score Classification (Excel)

### 🧠 Problem Statement  
Daikibo’s HR team struggled to interpret raw equality scores in performance reviews and wanted a **clear system** to identify fairness or potential bias in evaluations.

### 📁 Dataset Overview  
**File Name:** `Equality Table.xlsx`  
**Rows:** 100 employee review records  
**Columns:**

| Column           | Description                                      | Sample / Values |
|------------------|--------------------------------------------------|------------------|
| `Employee ID`    | Unique employee identifier                       | e.g., `EMP001` |
| `Manager ID`     | Manager who conducted the review                 | e.g., `MGR09` |
| `Department`     | Department of the employee                       | `Operations`, `HR`, `Finance`, etc. |
| `Review Date`    | Date of performance evaluation                   | `2023-09-15` |
| `Equality Score` | Score showing fairness (0 = fair, ± = bias)     | e.g., `-25`, `+12`, `0` |
| `Classification` | **Added column**: Label for fairness level      | `Fair`, `Unfair`, `Highly Discriminative` |

### 🛠️ What I Did
- Created a new column to classify scores as:
  - `Fair` (±10)
  - `Unfair` (< -10 or >10)
  - `Highly Discriminative` (< -20 or >20)
- Used a clear, scalable formula:
  ```excel
  =IF(ABS(A2)<=10, "Fair", IF(ABS(A2)<=20, "Unfair", "Highly Discriminative"))

### 📊 Key Insights  
- Around **65%** of reviews were labeled **Fair**, but others showed signs of **potential bias**.  
- HR can now **easily filter and investigate** reviews marked "Highly Discriminative".

### 💥 Business Impact  
- Improved **transparency and fairness** in evaluations.  
- HR can take **proactive action** based on unbiased metrics.

---

## 📈 Results Summary

| Area        | Outcome                                                                 |
|-------------|-------------------------------------------------------------------------|
| Operations | Identified most affected factory (Osaka) and device (LaserWelder)       |
| HR         | Classified reviews into Fair, Unfair, or Discriminative for action      |
| Executive Use | Dashboards and logic sheets support informed, timely decision-making  |

---

## 🚀 Conclusion

This project demonstrates my ability to solve business problems with data using real-world tools and logic. From operational root cause analysis to fairness in HR practices, I delivered structured, clear, and actionable insights — just like I would in a client-facing role at Deloitte or any data-driven organization.

---

## 💼 Get In Touch

- 🔗 [LinkedIn](https://www.linkedin.com/in/kishan-patel-kp1629/)




> Thanks for visiting my portfolio! I'm actively seeking opportunities in data analytics, business analysis, or data science. Feel free to explore, star, and connect.
