# PC Part Picker

This project aims to assist users in finding the best computer parts for their PC within their assigned budget. 
The program will provide an informative graph to compare each selected part, aiding users in deciding which component best suits their needs. Building a computer can be confusing, especially for those lacking expertise in the field.

## Data Recourse

Every dataset source : [Kaggle.com](https://www.kaggle.com/datasets/dilshaansandhu/general-computer-hardware-dataset)

## Required Files
| File                | Description                                         |
|---------------------|-----------------------------------------------------|
| main.py             | Contain main code to run the program                |
| processing.py       | Process the data such as converting from USD to THB |
| product_value.py    | Contains Enum classes                               |
| Program_UI.py       | Contains UI of the program                          |
| CPUData.csv         | Dataset of CPU                                      |
| GPUData.csv         | Dataset of GPU                                      |
| HDDData.csv         | Dataset of HDD                                      |
| SSDData.csv         | Dataset of SSD                                      |
| RAMData.csv         | Dataset of RAM                                      |
| MotherboardData.csv | Dataset of Motherboard                              |

## UI Screenshot
| Window                     | Screenshots                                                |
|----------------------------|------------------------------------------------------------|
| PC Build Page              | ![Page1.PNG](Screenshots_and_diagrams%2FPage1.PNG)         |
| Build button after clicked | ![Build.PNG](Screenshots_and_diagrams%2FBuild.PNG)         |
| Data Exploration Page      | ![Page3.PNG](Screenshots_and_diagrams%2FPage3.PNG)         |
| Descriptive Statistic Page | ![Page2.PNG](Screenshots_and_diagrams%2FPage2.PNG)         |
| Selection Page             | ![Selection.PNG](Screenshots_and_diagrams%2FSelection.PNG) |
### UML Class Diagram
![UML_ProjectY1.PNG](Screenshots_and_diagrams%2FUML_ProjectY1.PNG)

### UML Sequence Diagram
![SequenceDiagram.PNG](Screenshots_and_diagrams%2FSequenceDiagram.PNG)

## Installation guide

1. Open Terminal or Command prompt
2. Clone GitHub Repository
```commandline
git clone https://github.com/PichapopRo/Year1-Project.git
```
3. Locate and go in the directory
```commandline
cd Year1-Project
```
4. Install all requirement packages in requirements.txt.

```commandline
pip install -r requirements.txt
```

5. Run main.py file

```commandline
python main.py
```

### Creating Virtual Environment

1. Open Terminal Command Prompt.
2. Change directory to the project

```
cd Year1-Project
```

3. Create a Virtual Environment.

```
python -m venv env
```
### Activate Virtual Environment

1. Open Terminal or Command Prompt.
2. Change directory to the project

```
cd Year1-Project
```

3. Activating venv

- macOS/Linux

```
source env/bin/activate
```

- for Windows

```
env\Scripts\activate
```

Deactivating venv

```
deactivate
```

#### Demonstration video
[](https://drive.google.com/file/d/1QnpttBvbPjZhjk9pPkHIklXQS7k7VJ2U/view?usp=sharing)

