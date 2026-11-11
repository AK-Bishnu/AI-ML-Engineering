# Used Car Price Prediction — Dataset

## Overview

This dataset contains listings of used cars collected from Bangladeshi automotive marketplaces(bikroy.com). It is intended for regression tasks targeting **used car price prediction** in Bangladeshi Taka (BDT).

The data covers 5,997 car listings across multiple brands, models, fuel types, and transmission configurations, with a strong representation of the Toyota-dominated Bangladeshi secondhand market.

---

## Files

| File | Description |
|------|-------------|
| `README.md` | This file |
| `UsedCarInfo` | Dataset
| `data_dictionary.xlsx` | Detailed field definitions, data types, value ranges, and notes |
| `collection_methodology.pdf` | Description of how the data was collected and cleaned |

---

## Target Variable

`price` — Listed selling price of the used car, formatted as a string (e.g., `Tk 1,350,000`). Participants should parse and convert this to a numeric value for modelling.

---

## Features

| Column | Type | Description |
|--------|------|-------------|
| `title` | string | Full listing title as shown on the marketplace |
| `brand` | string | Car manufacturer (e.g., Toyota, Honda) |
| `model` | string | Car model name (e.g., Corolla, Civic) |
| `transmission` | string | Gear type: `Automatic` or `Manual` |
| `fuel_type` | string | Fuel or energy type(s); may list multiple (e.g., `CNG, Octane`) |
| `year_of_manufacture` | integer | Year the vehicle was manufactured |
| `energy_capacity` | string | Engine displacement (e.g., `1,500 cc`) |
| `kilometers_run` | string | Odometer reading (e.g., `89,000 km`) |
| `car_age` | integer | Age of the car in years at time of listing |

---

## Notes

- The dataset is heavily skewed toward **Toyota** vehicles (~88% of listings), reflecting real market distribution in Bangladesh.
- `fuel_type` often contains multiple comma-separated values indicating dual-fuel configurations.
- Several numeric fields are stored as formatted strings and require parsing before use.
- Outliers exist in `price`, `car_age`, and `kilometers_run` — inspect distributions before modelling.

---

