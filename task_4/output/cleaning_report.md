# Data Cleaning Report

## Changes Made

- Removed the second, identical S005 row so each student ID occurs once.
- Changed `ml` and `MACHINE LEARNING` to `ML`; changed `web`, `Web Dev`, and `web development` to `Web`; changed `electronics` to `Electronics`.
- Removed `%` from attendance and converted the column to numbers.
- Treated S007's `-10` and S008's `105%` attendance as invalid. Together with S003's missing attendance, these values were replaced by the valid-column median of 88.
- Converted Isha's score `nine` to 9 and Rohan's study hours `two` to 2.
- Filled S009's missing score with 0 because no recorded score is treated as not scored.
- Converted heights in metres and centimetres into `height_cm` (for example, `1.62 m` became 162).
- Removed `kg` from weights and stored them in `weight_kg`. S003's missing weight was replaced by the median of 58 kg.
- Changed `Yes`, `Y`, and `yes` to `yes`; changed `N`, `no`, and `No` to `no`.

## Why median for missing values?

The median is resistant to extreme values, making it suitable for this small dataset.
