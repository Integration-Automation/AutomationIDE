# Table of contents 
> ITE Intro \
> Editor components \
> GUI Testing components \
> WEB Testing components \
> API Testing components \
> Load & Stress Testing components
---
## What is ITE
> Project Kanban \
> https://github.com/orgs/Integrated-Testing-Environment/projects/4/views/1 \
> Integrated Testing Environment (ITE) 
> * ITE mainly provides an integrated automated testing environment. 
> * ITE is composed of the following components: 
>> * Editor。
>> * GUI Testing。
>> * Web Testing。
>> * API Testing。
>> * Load & Stress Testing。
---
## ITE Testing

> How does ITE perform self-testing?
> * CircleCI & GitHub Actions。
>> * What are the benefits of using CircleCI and GitHub Actions?
>> * They provide GitHub/Gitlab hooks for automated testing on every commit.
>> * They provide detailed test logs.
>> * They allow for automatic deployment to selected environments.
>> * They make it easy to specify branches for testing.
>> * They can parallelize multiple tests for faster execution.
---
## ITE Dev
> * ITE's development process: CI/CD (Continuous Integration/Continuous Deployment).
> * Continuous Integration: The longer the code is away from the last update, the higher the risk, so continuous integration encourages committing and automated testing after completing each part to reduce risk.
> * Continuous Deployment: Continuously deploying the code to the real environment for testing, usually achieved through automation.
---
### Editor components
> A simple text editor for ite 
>> Editor Really?
>> * Why do we need to provide an editor when there are so many text editors and IDEs available?
>> * We provide an editor as a cross-platform and minimalistic solution that comes with ITE, without requiring additional installation. The editor provides basic functionality, including font adjustment, support for other ITE components, basic file management such as saving, opening, and auto-saving, as well as file encoding and code selection integration. Additionally, the editor allows users to view test results through the interface.
>> * The term "minimalistic" refers to the basic functionalities that are essential for a text editor, without the advanced features commonly found in other IDEs or text editors.
---
### GUI Testing components
> Image & Coordinate based GUI Testing \
> GUI automated testing based on image comparison and coordinates. \
> Cross-platform and cross-programming language.\
> Solve problems:
>> * Provide automation execution for repetitive tasks.
>> * Multiple methods are available, including recording, image recognition, and coordinate-based testing.
>> * Tests can be executed remotely through TCP/IP.
>> * Test reports can be generated with records for each action.
>> * The same code can be used for three platforms, reducing the possibility of platform-dependent programs.
>> * Provide hooks for keyboard and mouse events and state checks (including using code to simulate key presses).
>> * Can use keywords for development to improve readability.
---
### WEB Testing components
> Multiton Selenium Instance testing \
> The WEB Testing component is a web automation testing solution based on Selenium. \
> It wraps Selenium and therefore has all the functionality of Selenium. \
> What problems does it solve? 
>> * Automatically downloads and updates the required web driver, so users no longer need to install it manually.
>> * Provides the ability to simultaneously run and monitor multiple Selenium instances.
>> * Provides a keyword-based testing approach that Selenium does not have.
>> * Can produce test reports that record actions taken during the test.
>> * Can execute tests remotely through TCP/IP.
>> * Offers a CLI mode for Web Testing.
---
### API Testing components
> Simple way to testing HTTP/S & Soap \
> Wrapper for Requests package, designed for those with experience using Requests. \
> Send HTTP/S and SOAP requests with a simple line of code or keyword. \
> Detailed information on Requests and Responses. \
> Solves problems such as:
>> * Detailed testing reports on Requests and Responses.
>> * Testing for SOAP protocol.
>> * Data comparison for each Request.
>> * API Testing in pure CLI mode.
---
### Load & Stress Testing components
> Locust Wrapper \
> Wrapper for Locust, simplifying complex Locust configurations. \
> Solves problems:
>> * Checking Requests & Response for each load test
>> * Load testing for SOAP protocols
>> * Comparison of numerical values for each load test
>> * Detailed load test reports for each test.
---

### Features

> * ITE GUI for beginner
> * GUI testing (use AutoControl)
> * API testing (use APITestka)
> * Web testing (use WebRunner)
> * Loading testing (use LoadDensity)
> * Multi test task runner (multi process)
> * you can run multi testing on same time
> * open log window to check testing result
> * Send mail when testing failure (need to setting mail)

---

[![Codacy Badge](https://app.codacy.com/project/badge/Grade/b7d32ed8600b4bd2a2f3e960f46f2ad0)](https://www.codacy.com/gh/JE-Chen/Integration-testing-environment/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=JE-Chen/Integration-testing-environment&amp;utm_campaign=Badge_Grade)

[![CircleCI](https://dl.circleci.com/status-badge/img/gh/JE-Chen/Integration-testing-environment/tree/main.svg?style=svg)](https://dl.circleci.com/status-badge/redirect/gh/JE-Chen/Integration-testing-environment/tree/main)

[![ITE GitHub Actions Dev](https://github.com/JE-Chen/Integration-testing-environment/actions/workflows/ITE-github-actions_dev.yml/badge.svg)](https://github.com/JE-Chen/Integration-testing-environment/actions/workflows/ITE-github-actions_dev.yml)

[![ITE GitHub Actions Stable](https://github.com/JE-Chen/Integration-testing-environment/actions/workflows/ITE-github-actions_stable.yml/badge.svg)](https://github.com/JE-Chen/Integration-testing-environment/actions/workflows/ITE-github-actions_stable.yml)

### install
#### we suggest install full package
* pip install integration_testing_environment[full_extension]
#### if we don't want to use send after test
* pip install integration_testing_environment
