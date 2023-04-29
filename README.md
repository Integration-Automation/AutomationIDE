# Table of contents
> Editor components \
> GUI components \
> WEB components \
> API components \
> Load components
---
## What is Automation Editor
> Project Kanban \
> https://github.com/orgs/Intergration-Automation-Testing/projects/2/views/1 \
> Tool for automation
> * Automation Editor is composed of the following components: 
>> * Editor。
>> * GUI Automation。
>> * Web Automation。
>> * API Automation。
>> * Load Automation。
---
### JEditor
> * JEditor is a simple text editor, but it has all the necessary features.
> * JEditor is one of the components of ITE, but modularization allows it to be used separately.
> * JEditor defaults to using a dark interface as shown below:
>> * JEditor has the following features:
>>    * Font change.
>>    * Font size change.
>>    * Auto-save (after first save or open).
>>    * Tree file structure browsing.
>>    * Save and open files.
>>    * Python formatting check using yapf.
>>    * Run python programs.
>>    * Run shell commands.
---
### GUI Automation components
> Image & Coordinate based GUI Automation \
> GUI automated based on image comparison and coordinates. \
> Cross-platform and cross-programming language.\
> Solve problems:
>> * Provide automation execution for repetitive tasks.
>> * Multiple methods are available, including recording, image recognition, and coordinate-based automation.
>> * Tests can be executed remotely through TCP/IP.
>> * Test reports can be generated with records for each action.
>> * The same code can be used for three platforms, reducing the possibility of platform-dependent programs.
>> * Provide hooks for keyboard and mouse events and state checks (including using code to simulate key presses).
>> * Can use keywords for development to improve readability.
---
### WEB Automation components
> Multiton Selenium Instance Automation \
> The WEB Automation component is a web automation solution based on Selenium. \
> It wraps Selenium and therefore has all the functionality of Selenium. \
> What problems does it solve? 
>> * Automatically downloads and updates the required web driver, so users no longer need to install it manually.
>> * Provides the ability to simultaneously run and monitor multiple Selenium instances.
>> * Provides a keyword-based automation approach that Selenium does not have.
>> * Can produce test reports that record actions taken during the test.
>> * Can execute tests remotely through TCP/IP.
>> * Offers a CLI mode for Web automation.
---
### API Automation components
> Simple way to Automation Requests HTTP/S & Soap \
> Wrapper for Requests package, designed for those with experience using Requests. \
> Send HTTP/S and SOAP requests with a simple line of code or keyword. \
> Detailed information on Requests and Responses. \
> Solves problems such as:
>> * Detailed automation reports on Requests and Responses.
>> * Automation for SOAP protocol.
>> * Data comparison for each Request.
>> * API automation in pure CLI mode.
---
### Load & Stress Automation components
> Locust Wrapper \
> Wrapper for Locust, simplifying complex Locust configurations. \
> Solves problems:
>> * Checking Requests & Response for each load test
>> * Load automation for SOAP protocols
>> * Comparison of numerical values for each load test
>> * Detailed load test reports for each test.
---

### Features

> * GUI Automation (use AutoControl)
> * API Automation (use APITestka)
> * Web Automation (use WebRunner)
> * Loading Automation (use LoadDensity)
> * Multi test task runner (multiprocess, but without AutoControl)
> * you can run multi automation on same time
> * open log window to check automation result
> * Send mail when automation failure (need to setting mail)

---

[![Codacy Badge](https://app.codacy.com/project/badge/Grade/b7d32ed8600b4bd2a2f3e960f46f2ad0)](https://www.codacy.com/gh/JE-Chen/Integration-testing-environment/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=JE-Chen/Integration-testing-environment&amp;utm_campaign=Badge_Grade)

[![CircleCI](https://dl.circleci.com/status-badge/img/gh/Integrated-Testing-Environment/Integration-testing-environment/tree/main.svg?style=svg)](https://dl.circleci.com/status-badge/redirect/gh/Integrated-Testing-Environment/Integration-testing-environment/tree/main)

[![GitHub Actions Dev](https://github.com/JE-Chen/Integration-testing-environment/actions/workflows/ITE-github-actions_dev.yml/badge.svg)](https://github.com/JE-Chen/Integration-testing-environment/actions/workflows/ITE-github-actions_dev.yml)

[![GitHub Actions Stable](https://github.com/JE-Chen/Integration-testing-environment/actions/workflows/ITE-github-actions_stable.yml/badge.svg)](https://github.com/JE-Chen/Integration-testing-environment/actions/workflows/ITE-github-actions_stable.yml)

### install
#### we suggest install full package
* pip install automation_editor[full_extension]
#### if we don't want to use send after test
* pip install automation_editor
