# Kigali Express Driver Lookup

## Project Overview

This project explores different ways of searching for a driver using their driver ID.

The three search approaches are:

- Linear Search
- Binary Search
- HashMap

## Problem

Kigali Express has a list of drivers and needs to find a specific driver using their ID.

The goal is to understand how different search algorithms affect the efficiency of finding a driver.

## Search Methods

### 1. Linear Search

Linear search checks each driver one by one until it finds the requested driver.

Time complexity:

O(N)

### 2. Binary Search

Binary search repeatedly divides a sorted search space in half.

Time complexity:

O(log N)

### 3. HashMap

A HashMap stores data using key-value pairs.

For this project:

Driver ID → Driver object

In Python, we use a dictionary (`dict`) as the HashMap.

Building the HashMap takes:

O(N)

Looking up a driver in the HashMap takes:

O(1) average

## Project Goal

The goal is to compare these approaches and understand why a HashMap can provide fast driver lookups when many searches are required.
