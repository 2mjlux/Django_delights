# Django Delights - Project Planning

## End Result (target)

A web-based restaurant inventory management system where the owner can:
- [x] Track ingredient inventory and costs
- [x] Manage menu items and their recipes
- [x] Record customer purchases (sales)
- [x] View profit/revenue reports
- [x] All protected behind authentication

**Tech Stack:**
- Django (backend framework)
- SQLite (database)
- Django templates (frontend)
- Django auth (login system)

---

## Core Objectives

- [x] 4 database models (Ingredient, MenuItem, RecipeRequirement, Purchase)
- [x] CRUD operations for all models
- [x] Inventory tracking that updates on purchases
- [x] Revenue and profit calculations
- [x] Authentication (login required for all views)
- [x] Forms for data entry

---

## Timeline - 1 Week

**Days 1-2:** Setup, models, database
- [x] Virtual env, Django install, Git setup
- [x] Create and test all 4 models
- [x] Load sample data via admin

**Days 3-4:** Views and business logic
- [x] Create all views for displaying data
- [x] Implement profit/revenue calculations
- [x] Test purchase workflow

**Days 5-6:** Templates and forms
- [x] Build all templates
- [x] Create forms for data entry
- [x] Connect forms to views

**Day 7:** Authentication and final
- [x] Add login/logout
- [x] Protect all views
- [x] Test and final commit

---

## Technical Notes

**Database relationships:**
- [x] MenuItem ← RecipeRequirement → Ingredient
- [x] Sale → MenuItem

**Key business logic:**
- [x] Validate inventory before allowing sale
- [x] Decrease quantities when sale recorded
- [x] Revenue = sum of sale prices
- [x] Cost = sum of ingredient costs used
- [x] Profit = revenue - cost
