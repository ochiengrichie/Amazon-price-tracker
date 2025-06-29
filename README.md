# Amazon Price Tracker

A Python-based automation tool that tracks the price of a product on Amazon and sends you an email alert when the price drops below a desired threshold.

---

## Table of Contents

- [Purpose](#purpose)
- [Prerequisites & Installation](#prerequisites--installation)
- [Usage](#usage)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)


## Purpose

This project automates the task of monitoring product prices on Amazon. Instead of manually checking the site, you’ll get a real-time email alert when the price falls below your target.


## Prerequisites & Installation

### Requirements
- Python 3.6+
- A Gmail account (with app password or "less secure apps" enabled)
- pip

### Installation
git clone https://github.com/ochiengrichie/Amazon-price-tracker.git
cd Amazon-price-tracker
pip install -r requirements.txt
Create a .env file in the root folder and add:


Email=youremail@example.com
PASSWORD=your-password-here
Make sure .env is listed in .gitignore.

Usage
Run the script:
python main.py
If the price drops below your target (e.g. $100), you’ll get an email alert.

Features
Real-time Amazon price tracking
Email alert system
Secure credential handling via .env
Easy setup and customization

Technologies Used
requests
BeautifulSoup
smtplib
python-dotenv

Contributing
Contributions are welcome!
Fork the repo
Create a branch
Push your changes and open a pull request

License
Licensed under the MIT License.

Contact
Author: Richard Onyango
📧 Email: ochiengrichie24@gmail.com