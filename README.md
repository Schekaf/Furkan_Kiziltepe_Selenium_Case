# Pytest Selenium Framework for Web Automation

## Overview

This repository contains a robust framework for automating web applications using Selenium and pytest. The framework is designed to facilitate the creation and execution of automated tests for web applications, providing a clear structure and easy-to-use functionalities.

## Features

- **Modular Design:** The framework follows a modular structure, allowing easy addition of new tests and functionalities.
- **Dynamic Waits:** Utilizes explicit waits to handle dynamic content and ensure elements are interactable.
- **Screenshot on Failure:** Automatically captures screenshots when a test fails for easier debugging.
- **Cross-Browser Testing:** Supports multiple browsers, including Chrome and Firefox.

## Requirements

- Python 3.10 or higher
- pytest
- Selenium WebDriver
- Other dependencies as specified in `requirements.txt`

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Schekaf/InsiderOne-Selenium.git
   
2. Install requirements:
    ```bash
    pip install -r requirements.txt
   
3. Setup Chrome or Firefox:
- **For Chrome Visit:** https://sites.google.com/chromium.org/driver/downloads
- **For Firefox Visit:** https://github.com/mozilla/geckodriver/releases
    
   
## Running Test

1. To Execute tests:
    ```bash
    pytest tests/test_insider.py