

\# File Hash Calculator – Digital Forensics Tool



\## Project Overview



The File Hash Calculator is a Python-based digital forensics utility developed to calculate cryptographic hash values and verify the integrity of digital files.



The project demonstrates the practical application of cryptographic hashing in digital evidence handling and basic forensic integrity verification.



\## Objectives



\- Calculate cryptographic hashes for digital files.

\- Verify file integrity against previously recorded SHA-256 values.

\- Generate timestamped hash reports.

\- Demonstrate how file modifications affect cryptographic hash values.



\## Features



\- MD5 hash calculation.

\- SHA-1 hash calculation.

\- SHA-256 hash calculation.

\- SHA-256 integrity verification.

\- File size and metadata collection.

\- Timestamped forensic report generation.

\- Chunk-based file processing to reduce memory consumption.



\## Technologies



\- Python 3

\- hashlib

\- pathlib

\- datetime



The application uses Python's standard library and does not require external packages.



\## Project Structure



```text

File\_Hash\_Calculator/

│

├── hash\_calculator.py

├── README.md

└── .gitignore

```



\## Installation and Usage



\### 1. Clone the repository



```bash

git clone YOUR\_GITHUB\_REPOSITORY\_URL

```



\### 2. Navigate into the project



```bash

cd File\_Hash\_Calculator

```



\### 3. Run the application



```bash

python hash\_calculator.py

```



\### 4. Select an operation



Option 1: Calculate file hashes and generate a report.



Option 2: Verify a file against a previously recorded SHA-256 hash.



\## Experimental Testing



The application was tested using a controlled test file.



| Test | Expected result | Observed result |

|---|---|---|

| Calculate MD5, SHA-1 and SHA-256 | Hash values generated | Successful |

| Verify original file | MATCH | Successful |

| Verify modified file against original hash | MISMATCH | Successful |

| Generate hash report | Report saved | Successful |



The controlled modification experiment demonstrated that changing file contents produces a different SHA-256 digest.



\## Digital Forensics Relevance



Cryptographic hashing is an important technique for checking whether digital evidence has changed between two points of comparison.



This project demonstrates basic file integrity verification. It does not independently establish the authenticity, provenance or chain of custody of digital evidence.



MD5 and SHA-1 are included for educational comparison and compatibility with legacy workflows. SHA-256 is used as the primary integrity verification algorithm.



\## Current Limitations and Future Improvements



Planned improvements include:



\- Evidence metadata collection.

\- Verification audit logging.

\- Structured forensic reports.

\- Automated unit testing.

\- Batch file hashing.

\- Improved evidence management.



\## Research and Learning Context



This project forms part of my practical development in Python programming, cybersecurity and digital forensics.



It is intended as an educational prototype demonstrating fundamental digital evidence integrity concepts.



