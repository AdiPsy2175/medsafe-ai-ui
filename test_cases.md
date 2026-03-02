# MedSafe AI – Test Cases

This document describes the manual test cases performed to validate
the functionality of the MedSafe AI user interface.

---

## Test Case 1: Medicine Interaction – Valid Input
**Input:** Paracetamol, Ibuprofen  
**Expected Result:** System displays an interaction warning with risk level  
**Actual Result:** Warning message and medium risk level displayed  
**Status:** Pass  

---

## Test Case 2: Medicine Interaction – Empty Input
**Input:** (No medicine entered)  
**Expected Result:** Error message asking user to enter medicine names  
**Actual Result:** Error message displayed  
**Status:** Pass  

---

## Test Case 3: Symptom Analysis – Valid Input
**Input:** Headache, mild nausea  
**Expected Result:** Educational guidance with urgency level  
**Actual Result:** Guidance displayed with low urgency  
**Status:** Pass  

---

## Test Case 4: Symptom Analysis – Empty Input
**Input:** (No symptoms entered)  
**Expected Result:** Error message asking user to describe symptoms  
**Actual Result:** Error message displayed  
**Status:** Pass  
