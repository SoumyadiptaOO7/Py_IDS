# Py_IDS
Cross Platform Intrusion Detection System Using Python

1.	Project Overview:
This project involves the development of a cross-platform Intrusion Detection System (IDS) using Python. The IDS monitors real-time network traffic, captures, and analyzes packets to detect potential security threats based on predefined suspicious IP addresses and ports. Detected anomalies are logged with timestamps in an Excel sheet for future analysis. This project is designed to run on various operating systems, including Windows, Linux, and macOS. It helps enhance network security by detecting unauthorized access attempts and providing a means for continuous monitoring.

2.	Objectives:
The key objectives of this project are:
•	Real-time network traffic monitoring: To capture and analyze packets in real-time.
•	Cross-platform functionality: Ensuring compatibility with Windows, Linux, and macOS.
•	Threat detection: To detect security anomalies based on predefined suspicious IP addresses and ports.
•	User-friendly interface: Utilizing Tkinter to create an easy-to-use GUI for the IDS.
•	Data logging: Storing detected threats in an Excel file for future analysis, even if no anomalies are found during the scan.
•	Customizable scan duration: Allowing users to define the time for scanning the network.

3.	Problem Statement:
As cybersecurity threats continue to evolve, networks are vulnerable to a wide range of attacks, including unauthorized access, data breaches, and malware. Existing solutions can be costly or complex to configure. This project addresses the need for an accessible, cross-platform, and easy-to-use IDS for personal and small-scale organizational use. It provides real-time detection and logging of suspicious network activities based on predefined security rules.

4.	Proposed Solution:
This project proposes a Python-based IDS that utilizes the scapy library for network packet capture and analysis. It will monitor real-time network traffic for suspicious activities and use predefined IP addresses and ports to detect threats. A Tkinter-based graphical user interface will allow users to input the desired scan duration, after which results will be stored in an Excel sheet using the pandas library.
Tools and Libraries:
•	Scapy: For capturing and analyzing network packets.
•	Pandas: For logging detected threats into an Excel file.
•	Tkinter: For building a simple, intuitive user interface.
•	Openpyxl: For saving Excel files across platforms.

5.	Features and Functionalities:
The project will include the following features:
•	Real-time packet capture: Continuous monitoring of network traffic.
•	Threat detection: Identifying suspicious IPs and ports.
•	Logging to Excel: Storing the results in a structured format for future analysis.
•	Cross-platform compatibility: Ensuring the IDS works on Windows, Linux, and macOS.
•	Customizable scan duration: Allowing users to specify how long the network scan should run.
•	User-friendly GUI: Enabling non-technical users to operate the IDS easily.

6.	Risks and Challenges:
•	Cross-platform compatibility: Ensuring the IDS works seamlessly on different operating systems could pose challenges, especially due to system-level network configurations.
•	Mitigation: Extensive testing on Windows, Linux, and macOS, and leveraging Python’s platform-independent libraries.
•	Packet capture limitations: In certain environments, capturing packets without proper permissions (e.g., root or administrator) may be restricted.
•	Mitigation: Providing users with detailed instructions on running the IDS with the required privileges.
•	Performance issues: Real-time packet capture can be resource-intensive, especially on older hardware.
•	Mitigation: Optimizing the packet capture process and setting reasonable scan time limits.

7.	Resources Needed:
i) Python Libraries:
•	Scapy
•	Pandas
•	Tkinter
•	Openpyxl
ii) Testing Platforms:
•	Windows 10/11
•	Linux (e.g., Ubuntu)
•	macOS
iii) Networking Setup:
•	Local network for packet capture testing.
•	Access to router logs for IP analysis (if necessary).

18.	Conclusion:
This IDS project aims to create an effective, easy-to-use, and cross-platform solution for real-time network monitoring and threat detection. By leveraging Python’s libraries, this project provides a cost-effective solution for enhancing network security. The expected outcome is a fully functional IDS that logs network activity and flags suspicious behavior for further investigation.
