# Django Delights - Project Planning

## End Result (target)

A web-based restaurant inventory management system where the owner can:
- [ ] Track ingredient inventory and costs
- [ ] Manage menu items and their recipes
- [ ] Record customer purchases (sales)
- [ ] View profit/revenue reports
- [ ] All protected behind authentication

**Tech Stack:**
- Django (backend framework)
- SQLite (database)
- Django templates (frontend)
- Django auth (login system)

---

## Core Objectives

- [x] 4 database models (Ingredient, MenuItem, RecipeRequirement, Purchase)
- [x] CRUD operations for all models
- [ ] Inventory tracking that updates on purchases
- [ ] Revenue and profit calculations
- [ ] Authentication (login required for all views)
- [ ] Forms for data entry

---

## Timeline - 1 Week

**Days 1-2:** Setup, models, database
- [x] Virtual env, Django install, Git setup
- [x] Create and test all 4 models
- [x] Load sample data via admin

**Days 3-4:** Views and business logic
- [ ] Create all views for displaying data
- [ ] Implement profit/revenue calculations
- [ ] Test purchase workflow

**Days 5-6:** Templates and forms
- [ ] Build all templates
- [ ] Create forms for data entry
- [ ] Connect forms to views

**Day 7:** Authentication and final
- [ ] Add login/logout
- [ ] Protect all views
- [ ] Test and final commit

---

## Technical Notes

**Database relationships:**
- [x] MenuItem ← RecipeRequirement → Ingredient
- [x] Sale → MenuItem

**Key business logic:**
- [ ] Validate inventory before allowing sale
- [ ] Decrease quantities when sale recorded
- [ ] Revenue = sum of sale prices
- [ ] Cost = sum of ingredient costs used
- [ ] Profit = revenue - cost
