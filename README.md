# Process Automation with Python and Pandas Library

## Description

### In my current job, a manual task required Product Managers to create separate .csv files for each bought product, listing all Serial Numbers in the first row. This was necessary for our internal management system to track products and their respective serial numbers in stock.

### To streamline this process, I developed a simple Python script using the Pandas library. This script automates the creation of individual .csv files, each containing the required Serial Numbers. The result? Significant time savings, freeing up Product Managers to focus on more valuable tasks.

## Features

- **Automated CSV Creation and Naming:** The script generates separate .csv files for each product, with the filename matching the product name. The first column of each CSV file lists formatted Serial Numbers, aligning with the internal management system's requirements. The file format for the original file must be .xlsx and it shall have in the first column all Serial Numbers listed. In the second column, it shall have the product name associated with said Serial Number. **A 'sn.xlsx' file is provided as an example.**

- **Serial Number Formatting:** Serial Numbers are automatically formatted to a maximum of 12 characters to meet the limitations of the barcode scanner.

- **Time Efficiency:** By automating this task, i've reduced the time spent on manual file creation and data entry, improving overall efficiency.

## Usage

1. Clone this repository to your local machine.
2. Install the required Pandas library using the following command:

```bash
pip install -r requirements.txt
```
3. Run `view.py`
4. Click on 'Select File' to select the 'sn.xlsx' example file or any other file following the requirements mentioned above.
5. Click on 'Generate'. All files will be created and stored inside the 'serialNumbers' directoy. (if no such directory found, then a new one will be created automaticallly)
