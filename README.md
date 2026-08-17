#  Expense Tracker – Dockerized Flask Application

A simple and user-friendly Expense Tracker web application built using **Python Flask**, **SQLite**, and **Docker**.

The application allows users to add, view, calculate, and delete expenses. SQLite is used for persistent data storage, while Docker provides a consistent and portable environment for running the application.

---

## Project Overview

The Expense Tracker is a web-based application designed to help users manage their daily expenses.

Users can:

- Add new expenses
- Select an expense category
- View all recorded expenses
- View total spending
- Delete expenses
- Check application health
- Run the application inside a Docker container
- Persist expense data using a Docker volume

---

## Features

### Expense Management
- Add expense description
- Enter expense amount
- Select expense category
- View previously added expenses
- Delete expenses

### Expense Summary
- Automatically calculates total spending
- Displays all stored expenses


The database is stored at:

```text
/app/data/expenses.db
