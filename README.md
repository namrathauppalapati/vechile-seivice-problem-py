# 🚗 Vehicle Service Program

## 📌 Project Overview
The **Vehicle Service Program** is a console-based application developed using **Object-Oriented Programming (OOP)** concepts. It allows users to select a vehicle type (Car or Bike), enter vehicle details, display those details, and view the corresponding service procedure.

This project is designed to help beginners understand how OOP principles can be applied to real-world scenarios in a simple and effective manner.

---

## 🎯 Objectives
- To implement **Object-Oriented Programming concepts**
- To demonstrate **inheritance** using a base class
- To show **method overriding and runtime polymorphism**
- To build a menu-driven console application

---

## 🧱 Project Structure

---

## 🛠️ Technologies Used
- **Programming Languages:** Python 
- **Concepts:** OOP (Inheritance, Polymorphism, Method Overriding)  
- **Interface:** Console-based  

---

## 🧩 Class Description

### 🔹 Vehicle (Base Class)
**Attributes:**
- `model`
- `year`

**Methods:**
- `display()`
- `service()`

---

### 🔹 Car (Derived Class)
**Inherits from:** Vehicle  

**Additional Attribute:**
- `doors`

**Overridden Methods:**
- `display()`
- `service()`

---

### 🔹 Bike (Derived Class)
**Inherits from:** Vehicle  

**Additional Attribute:**
- `abs`

**Overridden Methods:**
- `display()`
- `service()`

---

## ✨ Features
- Menu-driven user interface
- Accepts user input for vehicle details
- Displays vehicle information clearly
- Shows different service procedures for Car and Bike
- Demonstrates runtime polymorphism

---

## ▶️ How to Run the Program

### 🐍 Python
1. Ensure Python is installed on your system.
2. Save the file as `vehicle_service.py`
3. Run the program:
   ```bash
   python vehicle_service.py

