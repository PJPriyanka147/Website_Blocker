# Website_Blocker

## Overview
**Website_Blocker** is a Python-based tool designed to help users enhance productivity by blocking access to distracting websites during specified hours. This tool modifies the system’s hosts file to redirect specified websites to localhost, effectively preventing access to them during working hours.

## Features
- **Block Specific Websites**: Easily block access to websites that you find distracting.
- **Customizable Blocking Schedule**: Set specific hours during which the websites will be blocked.
<!-- **Logging**: Keep a log of the websites that were blocked, along with timestamps.-->
<!-- **Cross-Platform**: Works on Windows, macOS, and Linux.-->

## Prerequisites
- Python 3.10.11
- Administrator or root access (to modify the hosts file)

## Installation
1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/Website_Blocker.git
   cd Website_Blocker
## Usage 🚀

1. **Edit the `websites.txt` File**
   - List the URLs of the websites you want to block, one per line.
   - **Example:**
     ```
     www.facebook.com
     www.youtube.com
     ```
2. **Configure the Blocking Schedule**
   - Modify the `start_hour` and `end_hour` Variables.
   - Adjust these variables in the script to set the blocking period.
   - **Example:**
     ```python
     start_hour = 9
     end_hour = 17
     ```
3. **Run the Script**
   ```
   python website_blocker.py
   ```
4. **Stopping the Block**
   - To stop the block and revert changes, either wait for the blocking period to end or manually remove the entries from the hosts file.
   
## How it Works
- The script reads the list of websites from websites.txt.
- During the specified hours, it writes entries to the system’s hosts file, redirecting the websites to 127.0.0.1 (localhost).
- After the blocking period, the script removes these entries, restoring normal access.



