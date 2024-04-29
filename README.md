# FantasyFootballManager

## Setting up Python Environment

### Prerequisites

Make sure you have Python and pip installed on your system. If not, you can download and install them from [Python's official website](https://www.python.org/downloads/).

### Step 1: Clone the Repository

First, clone the repository to your local machine:

```bash
git clone https://github.com/martimfasantos/FantasyFootballManager.git
cd FantasyFootballManager/
```

### Step 2: Create a Virtual Environment

It's recommended to use a virtual environment to isolate your project dependencies. Navigate to the project directory and create a virtual environment:

```bash
cd FantasyFootballManager/
python -m venv env
```

This will create a directory named "env/" containing a Python interpreter and a copy of the standard Python library.

### Step 3: Activate the Virtual Environment

Before installing any packages, activate the virtual environment:

**For Windows:**

```bash
.\env\Scripts\activate
```

**For macOS and Linux:**

```bash
source env/bin/activate
```

## Step 4: Install Requirements

Once the virtual environment is activated, you can install the required packages listed in the "requirements.txt" file:

```bash
pip install -r requirements.txt
```

This command will install all the necessary dependencies for the project.

## Step 5: Deactivate the Virtual Environment

Once you're done working on your project, you can deactivate the virtual environment:

```bash
deactivate
```
