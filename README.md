
# Flow Log Analyzer

## **Introduction**

The Flow Log Analyzer is a Python-based program designed to process AWS VPC flow logs, map them to tags based on a lookup table, and generate a summarized report. This tool only supports the default AWS VPC flow log format (version 2) and assumes that the logs are correctly formatted. 
The specified format is : ```version, account-id, interface-id, srcaddr, dstaddr, srcport, dstport, protocol, packets, bytes, start, end, action, log-status```

## **Assumptions**

- **Log Format**: The program only supports the default AWS VPC flow log format. Custom log formats are not supported.
- **Log Version**: Only version 2 of the flow logs is supported.
- **Case Insensitivity**: The program treats protocols in a case-insensitive manner, ensuring consistency in mapping tags.
- **Input Files**: The program assumes that the `lookup.csv` file and log files are present and correctly formatted.

## **Program Structure**

### **1. `flowLog_Analyzer.py`**
   - **Purpose**: Analyzes AWS VPC flow logs, counting occurrences of tags and port/protocol combinations.
   - **Key Functions**:
     - `process_log(filename)`: Processes the entire log file.
     - `process_line(line)`: Processes a single log line, updating counts for tags and port/protocol combinations.
     - `_get_protocol(protocol_number)`: Converts protocol numbers to protocol names.

### **2. `lookup_table.py`**
   - **Purpose**: Manages the lookup table, mapping port/protocol combinations to tags.
   - **Key Functions**:
     - `load(filename)`: Loads the lookup table from a CSV file.
     - `get_tag(port, protocol)`: Retrieves the corresponding tag for a given port/protocol combination.

### **3. `main.py`**
   - **Purpose**: The main entry point of the program, orchestrating the overall flow.
   - **Key Steps**:
     - Loads the lookup table.
     - Processes the flow logs.
     - Writes the summarized output.

### **4. `outputWrite.py`**
   - **Purpose**: Handles writing the results of the analysis to a CSV file.
   - **Key Functions**:
     - `write(tag_counts, port_protocol_counts, output_filename)`: Writes the counts to the specified output file.

### **5. Unit Tests**
   - **Files**: 
     - `test_flow_log_analyzer.py`
     - `test_lookup_table.py`
     - `test_output_writer.py`
   - **Purpose**: Ensures the correctness of the core functionality in each module.
   - **Challenges**: Handling the mocking of file writes due to `csv.writer` calls.

## **Usage Instructions**

### **1. Installation**
Ensure you have Python 3.x installed on your system.

### **2. Running the Program**
To run the program, use the following command:

```bash
python main.py <log_filename> <lookup_filename> <output_filename>
```

- **`<log_filename>`**: The file containing the AWS VPC flow logs (e.g., `sampleFlowLogs.txt`).
- **`<lookup_filename>`**: The file containing the lookup table (e.g., `lookup.csv`).
- **`<output_filename>`**: The file where the output will be written (e.g., `output.csv`).

### **3. Running Tests**
To run the unit tests, use the following command:

```bash
python -m unittest discover
```

## **Output**

The output will be a CSV file containing:

- **Tag Counts**: A summary of the number of matches for each tag.
- **Port/Protocol Combination Counts**: A summary of the number of matches for each port/protocol combination.

## **Analysis and Notes**

- **Log Format and Version**: The program strictly supports version 2 of the AWS VPC flow logs in their default format. Custom formats or other versions are not supported and could result in errors or incorrect processing.
- **Case Insensitivity**: Protocols are matched in a case-insensitive manner, ensuring that differences in case do not affect the tag mapping.
- **File Handling**: The program assumes that input files are correctly formatted. Errors in file structure or content could lead to skipped lines or incorrect outputs.

## **Concluding Remarks**

Future enhancements could include support for custom log formats, additional versions, and more sophisticated error handling.
