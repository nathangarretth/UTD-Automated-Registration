# UTD-Automated-Registration

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
      </ul>
    </li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project

This project was built for course registration at the exact time it opens.

### Built With

* ![Selenium](https://img.shields.io/badge/-selenium-%43B02A?style=for-the-badge&logo=selenium&logoColor=white)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

To use this project, you will need to install Python if you do not already have it and install some packages. Included in the repo is the web driver you will need.

### Prerequisites

If you do not already have Python you can download it at [https://www.python.org/](https://www.python.org/) for Windows and macOS, and most Linux distros come with Python.

1. First, clone this repo using Git. 
* to clone the repo
   ```sh
   git clone https://github.com/nathangarretth/UTD-Automated-Registration.git
   ```
2. Next, change directories to the project and install the packages required:
* install from the requirements file
   ```sh
   pip install -r requirements.txt
   ```

### Running The Script

After that, youll be able to run the main.py script two ways.
* enter login at runtime
   ```sh
   python main.py
   ```
* enter login as flags
   ```sh
   python main.py -u [USERNAME] -p [PASSWORD]
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>
