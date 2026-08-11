# Prabhakar --- Admin & CRUD Backend Task Assignment

## Project

**Project Name:** Network Management System

**Role:** Admin Backend Developer / CRUD API Developer

**Primary Stack:** - Python - Django - Django REST Framework -
PostgreSQL - Git & GitHub

**Experience Focus:** Prabhakar is primarily responsible for **Django +
basic DRF backend development**, so his work is centered around
admin-side functionality, CRUD operations, management APIs, KYC, sales
records, notifications, reports, and backend support.

------------------------------------------------------------------------

# 1. Overall Responsibility

Prabhakar owns the **Admin Management Backend**.

His responsibility is to build APIs and Django-side functionality that
allow administrators to manage the complete system.

### Main ownership

1.  Admin/member management
2.  Plans management
3.  EPIN management
4.  KYC management
5.  Sales management
6.  Withdrawal management
7.  Income management/viewing
8.  Notifications
9.  Admin dashboard APIs
10. Reports and filters
11. Search and pagination
12. Django Admin configuration
13. Admin permissions
14. CRUD API testing
15. API documentation/support for Rahul

> Prabhakar should **not duplicate Naresh's core business logic** such
> as binary placement, income calculation, wallet calculation,
> authentication architecture, or financial rules. He should
> consume/reuse the existing backend services and models.

------------------------------------------------------------------------

# 2. Important Ownership Boundary

## Naresh owns

``` text
Core Backend Architecture
Authentication
Custom User
Member Core Logic
Plan Activation Logic
EPIN Core Logic
Sponsor/Referral Logic
Binary Tree
Income Calculation
Wallet Ledger
Withdrawal Financial Logic
Security Architecture
```

## Rahul owns

``` text
React Frontend
Member Dashboard UI
Admin UI
API Integration
Responsive Design
Frontend Validation
```

## Prabhakar owns

``` text
Admin Backend
CRUD APIs
Django Admin
KYC Management
Sales Management
Notification Backend
Reports
Admin Filters/Search/Pagination
Admin Permissions
Admin Dashboard Data APIs
Backend QA for Admin Features
```

------------------------------------------------------------------------

# 3. Backend Apps Prabhakar Will Work On

``` text
backend/
└── apps/
    ├── members/
    ├── plans/
    ├── epins/
    ├── sales/
    ├── kyc/
    ├── notifications/
    ├── income/
    └── withdrawals/
```

Some existing models may be owned by Naresh. In that case, Prabhakar
should build **admin-facing serializers/views/endpoints around the
existing models** instead of changing the core business logic without
coordination.

------------------------------------------------------------------------

# 4. Admin API Structure

Recommended admin API structure:

``` text
/api/admin/
    dashboard/
    members/
    plans/
    epins/
    sales/
    kyc/
    income/
    withdrawals/
    notifications/
    reports/
```

Example:

``` text
GET    /api/admin/dashboard/
GET    /api/admin/members/
GET    /api/admin/members/<id>/
PATCH  /api/admin/members/<id>/
GET    /api/admin/plans/
POST   /api/admin/plans/
PATCH  /api/admin/plans/<id>/
GET    /api/admin/epins/
GET    /api/admin/kyc/
PATCH  /api/admin/kyc/<id>/
GET    /api/admin/sales/
GET    /api/admin/income/
GET    /api/admin/withdrawals/
PATCH  /api/admin/withdrawals/<id>/
GET    /api/admin/reports/
```

Exact endpoints should be finalized with Naresh before implementation.

------------------------------------------------------------------------

# 5. Admin Dashboard

## App/Area

``` text
admin dashboard
```

Prabhakar will provide the backend APIs. Rahul will consume these APIs
to build the React admin dashboard.

### Dashboard data

Possible metrics:

``` text
Total Members
Active Members
Inactive Members
Total Plans
Active Plans
Total EPINs
Unused EPINs
Used EPINs
Pending KYC
Pending Withdrawals
Total Sales
Total Income
```

### Tasks

-   [ ] Create dashboard service/API
-   [ ] Member statistics
-   [ ] Plan statistics
-   [ ] EPIN statistics
-   [ ] KYC statistics
-   [ ] Sales statistics
-   [ ] Withdrawal statistics
-   [ ] Income summary
-   [ ] Recent activities
-   [ ] API permissions
-   [ ] Tests

### API

``` text
GET /api/admin/dashboard/
```

> Financial totals should come from reliable backend queries/services,
> not frontend calculations.

------------------------------------------------------------------------

# 6. Admin Member Management

## Area

``` text
Admin → Members
```

### Features

``` text
Member List
Member Details
Search
Filter
Status
Plan
KYC Status
Date
```

### Tasks

-   [ ] Member listing API
-   [ ] Member detail API
-   [ ] Search
-   [ ] Pagination
-   [ ] Filtering
-   [ ] Ordering
-   [ ] Member status update
-   [ ] Activate member
-   [ ] Deactivate member
-   [ ] View member profile
-   [ ] View sponsor information
-   [ ] View plan information
-   [ ] View KYC status
-   [ ] Permission checks
-   [ ] Tests

### APIs

``` text
GET   /api/admin/members/
GET   /api/admin/members/<id>/
PATCH /api/admin/members/<id>/
```

> Do not directly modify sensitive member data without proper validation
> and permission checks.

------------------------------------------------------------------------

# 7. Plans Management

## Area

``` text
Admin → Plans
```

### Model

The main Plan model is owned by Naresh.

Prabhakar manages the **admin CRUD side**.

### Tasks

-   [ ] Plan list API
-   [ ] Plan detail API
-   [ ] Create plan API
-   [ ] Update plan API
-   [ ] Activate/deactivate plan
-   [ ] Search/filter if required
-   [ ] Pagination
-   [ ] Validation
-   [ ] Admin permissions
-   [ ] Tests

### APIs

``` text
GET    /api/admin/plans/
POST   /api/admin/plans/
GET    /api/admin/plans/<id>/
PATCH  /api/admin/plans/<id>/
DELETE /api/admin/plans/<id>/
```

> Do not hard-code plan amounts or activation rules. Use the approved
> requirements.

------------------------------------------------------------------------

# 8. EPIN Management

## Area

``` text
Admin → EPIN
```

The core EPIN generation/validation logic belongs to Naresh.

Prabhakar handles the admin management side.

### Tasks

-   [ ] EPIN list API
-   [ ] EPIN detail API
-   [ ] Filter by status
-   [ ] Filter by plan
-   [ ] Search EPIN
-   [ ] Pagination
-   [ ] View usage information
-   [ ] View generated-by information
-   [ ] Block EPIN if approved by business rules
-   [ ] Admin permissions
-   [ ] Tests

### APIs

``` text
GET   /api/admin/epins/
GET   /api/admin/epins/<id>/
PATCH /api/admin/epins/<id>/
```

If bulk EPIN generation is required, coordinate with Naresh before
implementing it.

------------------------------------------------------------------------

# 9. KYC Management

## App

``` text
kyc/
```

## Model: KYC

Possible fields:

``` text
member
document_type
document_number
document_file
status
reviewed_by
reviewed_at
remarks
created_at
updated_at
```

Possible statuses:

``` text
PENDING
APPROVED
REJECTED
```

### Tasks

-   [ ] KYC model if not already created
-   [ ] KYC submission API if required
-   [ ] Admin KYC list API
-   [ ] KYC detail API
-   [ ] Search/filter
-   [ ] Pending KYC filter
-   [ ] Approve KYC
-   [ ] Reject KYC
-   [ ] Reviewer tracking
-   [ ] Remarks
-   [ ] Permission checks
-   [ ] Tests

### APIs

``` text
GET   /api/admin/kyc/
GET   /api/admin/kyc/<id>/
PATCH /api/admin/kyc/<id>/
```

> Never expose sensitive KYC information to unauthorized users.

------------------------------------------------------------------------

# 10. Sales Management

## App

``` text
sales/
```

## Model: Sale

Possible fields:

``` text
member
reference
amount
status
sale_date
created_at
updated_at
```

### Tasks

-   [ ] Sale model if required
-   [ ] Sales list API
-   [ ] Sales detail API
-   [ ] Search
-   [ ] Date filter
-   [ ] Member filter
-   [ ] Status filter
-   [ ] Pagination
-   [ ] Sales summary
-   [ ] Admin permissions
-   [ ] Tests

### APIs

``` text
GET /api/admin/sales/
GET /api/admin/sales/<id>/
```

If sales creation affects income, coordinate with Naresh before
implementing the integration.

------------------------------------------------------------------------

# 11. Income Management

The **income calculation engine** belongs to Naresh.

Prabhakar manages the admin-facing viewing/reporting side.

### Tasks

-   [ ] Income list API
-   [ ] Income detail API
-   [ ] Filter by member
-   [ ] Filter by income type
-   [ ] Date filter
-   [ ] Status filter
-   [ ] Pagination
-   [ ] Income summary
-   [ ] Export-ready query structure if required
-   [ ] Permission checks
-   [ ] Tests

### APIs

``` text
GET /api/admin/income/
GET /api/admin/income/<id>/
GET /api/admin/income/summary/
```

> Do not independently rewrite the income calculation logic.

------------------------------------------------------------------------

# 12. Withdrawal Management

The core wallet/withdrawal financial logic belongs to Naresh.

Prabhakar handles the **admin workflow/API layer**.

### Features

``` text
Pending
Approved
Rejected
Processing
Completed
```

### Tasks

-   [ ] Withdrawal list API
-   [ ] Withdrawal detail API
-   [ ] Filter by status
-   [ ] Filter by member
-   [ ] Date filter
-   [ ] Pagination
-   [ ] View withdrawal details
-   [ ] Approve action
-   [ ] Reject action
-   [ ] Remarks
-   [ ] Permission checks
-   [ ] Tests

### APIs

``` text
GET   /api/admin/withdrawals/
GET   /api/admin/withdrawals/<id>/
PATCH /api/admin/withdrawals/<id>/
```

### Important

For approval/rejection:

``` text
Admin API
   ↓
Permission check
   ↓
Naresh's financial service
   ↓
Transaction.atomic()
   ↓
Wallet/Withdrawal update
```

Do not manually modify wallet balances from the admin view.

------------------------------------------------------------------------

# 13. Notifications

## App

``` text
notifications/
```

### Possible Model

``` text
Notification
```

Possible fields:

``` text
recipient
title
message
notification_type
is_read
created_at
```

### Tasks

-   [ ] Notification model if required
-   [ ] Notification list API
-   [ ] Notification detail API
-   [ ] Mark as read
-   [ ] Mark all as read
-   [ ] Admin notification creation if required
-   [ ] Filtering
-   [ ] Pagination
-   [ ] Permissions
-   [ ] Tests

### APIs

``` text
GET   /api/notifications/
PATCH /api/notifications/<id>/
POST  /api/notifications/mark-all-read/
```

------------------------------------------------------------------------

# 14. Django Admin Panel

Prabhakar should properly configure Django Admin for backend management
and debugging.

### Tasks

-   [ ] Register important models
-   [ ] `list_display`
-   [ ] `list_filter`
-   [ ] `search_fields`
-   [ ] `ordering`
-   [ ] `readonly_fields`
-   [ ] `fieldsets`
-   [ ] Useful admin actions
-   [ ] Avoid exposing sensitive fields unnecessarily
-   [ ] Improve admin usability

Models:

``` text
User
MemberProfile
Plan
MemberPlan
EPIN
Network/Sponsor models
IncomeTransaction
Wallet
WalletTransaction
Withdrawal
KYC
Sale
Notification
```

> Do not change core model ownership without coordinating with Naresh.

------------------------------------------------------------------------

# 15. Search / Filter / Pagination

All admin listing APIs should support these where appropriate.

### Search

Examples:

``` text
member_id
name
email
phone
EPIN code
```

### Filters

Examples:

``` text
status
plan
KYC status
income type
withdrawal status
date range
```

### Pagination

Use DRF pagination consistently.

Example:

``` text
?page=1&page_size=20
```

------------------------------------------------------------------------

# 16. Permissions

Admin APIs must never be public.

Possible permission levels:

``` text
Authenticated User
Staff
Admin
Super Admin
```

### Tasks

-   [ ] Admin permission class
-   [ ] Staff permission
-   [ ] Object-level permissions where required
-   [ ] Unauthorized response
-   [ ] Forbidden response
-   [ ] Tests

Example:

``` text
Member
   ❌ Cannot access /api/admin/members/

Staff/Admin
   ✅ Can access according to permissions
```

Coordinate with Naresh before creating a new permission architecture.

------------------------------------------------------------------------

# 17. API Validation

Every CRUD API should validate:

``` text
Required fields
Data types
Duplicate values
Invalid IDs
Invalid status
Unauthorized access
Invalid relationships
```

### Error response should be consistent

Example:

``` json
{
    "success": false,
    "message": "Invalid request.",
    "errors": {
        "status": [
            "Invalid status value."
        ]
    }
}
```

Follow the project's final API response convention decided by Naresh.

------------------------------------------------------------------------

# 18. API Documentation

For every API, document:

``` text
Endpoint
Method
Authentication
Permission
Query Parameters
Request Body
Response
Possible Errors
```

Example:

``` text
GET /api/admin/members/

Authentication:
JWT

Permission:
Admin

Query:
?page=1
&search=ABC001
&status=active
```

Keep documentation synchronized with Rahul's frontend integration needs.

------------------------------------------------------------------------

# 19. Testing

Prabhakar should test all admin CRUD functionality.

### Members

-   [ ] List members
-   [ ] Search
-   [ ] Filter
-   [ ] Pagination
-   [ ] Detail
-   [ ] Status update
-   [ ] Permission

### Plans

-   [ ] Create
-   [ ] Read
-   [ ] Update
-   [ ] Delete/deactivate
-   [ ] Validation

### EPIN

-   [ ] List
-   [ ] Search
-   [ ] Filter
-   [ ] Status
-   [ ] Permissions

### KYC

-   [ ] List
-   [ ] Approve
-   [ ] Reject
-   [ ] Permissions

### Sales

-   [ ] List
-   [ ] Detail
-   [ ] Filters

### Withdrawals

-   [ ] List
-   [ ] Detail
-   [ ] Approve
-   [ ] Reject
-   [ ] Permissions

### Notifications

-   [ ] List
-   [ ] Read
-   [ ] Mark all read

------------------------------------------------------------------------

# 20. GitHub Branch Strategy

## Main branches

``` text
main
develop
```

Recommended workflow:

``` text
feature branch
      ↓
Pull Request
      ↓
Code Review
      ↓
develop
      ↓
Testing
      ↓
main
```

Never directly push feature work to `main`.

------------------------------------------------------------------------

# 21. Prabhakar's Exact Feature Branch Sequence

## Phase 1 --- Admin Backend Foundation

### Branch

``` text
feature/admin-backend-foundation
```

### Use for

-   Admin API URL structure
-   DRF configuration needed for admin APIs
-   Admin permissions
-   Common admin serializer/view patterns
-   Pagination/filter configuration
-   Common admin API response structure

### Depends on

Naresh's core authentication/permission architecture.

------------------------------------------------------------------------

# 22. Phase 2 --- Admin Members

### Branch

``` text
feature/admin-members
```

### Use for

-   Member list
-   Member detail
-   Search
-   Filter
-   Pagination
-   Status update
-   Admin permissions
-   Tests

------------------------------------------------------------------------

# 23. Phase 3 --- Admin Plans

### Branch

``` text
feature/admin-plans
```

### Use for

-   Plan CRUD
-   Plan list
-   Plan detail
-   Activate/deactivate
-   Search/filter
-   Validation
-   Tests

------------------------------------------------------------------------

# 24. Phase 4 --- Admin EPIN

### Branch

``` text
feature/admin-epins
```

### Use for

-   EPIN list
-   EPIN detail
-   Search
-   Status filter
-   Plan filter
-   Usage information
-   Admin actions if approved
-   Tests

------------------------------------------------------------------------

# 25. Phase 5 --- KYC

### Branch

``` text
feature/admin-kyc
```

### Use for

-   KYC management
-   Pending KYC
-   Approve
-   Reject
-   Remarks
-   Reviewer information
-   Filters
-   Tests

------------------------------------------------------------------------

# 26. Phase 6 --- Sales

### Branch

``` text
feature/admin-sales
```

### Use for

-   Sales list
-   Sale details
-   Filters
-   Search
-   Date range
-   Pagination
-   Summary
-   Tests

------------------------------------------------------------------------

# 27. Phase 7 --- Income Management

### Branch

``` text
feature/admin-income
```

### Use for

-   Income list
-   Income details
-   Income type filters
-   Member filters
-   Date filters
-   Summary
-   Reports
-   Tests

> Do not modify Naresh's income calculation engine without coordination.

------------------------------------------------------------------------

# 28. Phase 8 --- Withdrawal Management

### Branch

``` text
feature/admin-withdrawals
```

### Use for

-   Withdrawal list
-   Details
-   Pending filter
-   Approve
-   Reject
-   Remarks
-   Permissions
-   Tests

> Financial operations must call the approved backend service. Do not
> directly change wallet balances.

------------------------------------------------------------------------

# 29. Phase 9 --- Notifications

### Branch

``` text
feature/notifications
```

### Use for

-   Notification model
-   List
-   Read/unread
-   Mark as read
-   Mark all as read
-   Admin notification functionality if required
-   Tests

------------------------------------------------------------------------

# 30. Phase 10 --- Admin Dashboard

### Branch

``` text
feature/admin-dashboard-api
```

### Use for

-   Dashboard statistics
-   Member counts
-   Plan counts
-   EPIN counts
-   KYC counts
-   Sales summary
-   Income summary
-   Withdrawal summary
-   Recent activities

------------------------------------------------------------------------

# 31. Phase 11 --- Django Admin Improvements

### Branch

``` text
feature/django-admin
```

### Use for

-   Model registration
-   `list_display`
-   Filters
-   Search
-   Ordering
-   Read-only fields
-   Admin actions
-   Better fieldsets
-   Admin usability

------------------------------------------------------------------------

# 32. Phase 12 --- Admin QA & API Cleanup

### Branch

``` text
feature/admin-api-qa
```

### Use for

-   API testing
-   Permission testing
-   Validation fixes
-   Pagination fixes
-   Search/filter fixes
-   Error response consistency
-   Documentation fixes
-   Cleanup/refactoring

------------------------------------------------------------------------

# 33. Commit Convention

### Good commits

``` text
feat: create admin member list API
feat: add member status filter
feat: implement admin plan CRUD
feat: add EPIN admin filters
feat: implement KYC approval API
feat: add sales reporting API
feat: add admin withdrawal filters
feat: create notification API
feat: add admin dashboard statistics
test: add admin member API tests
test: add KYC permission tests
fix: prevent unauthorized admin access
fix: correct withdrawal status validation
refactor: extract common admin filters
```

### Avoid

``` text
update
changes
final
final2
test
abc
done
```

------------------------------------------------------------------------

# 34. Pull Request Format

Every PR should contain:

``` text
## What was done?

## APIs added/changed

## Models changed

## Permissions

## Filters/Search/Pagination

## Tests

## Screenshots if applicable

## Notes / Breaking Changes
```

Example:

``` text
feat: implement admin member management API
```

------------------------------------------------------------------------

# 35. Working With Naresh

Prabhakar should coordinate with Naresh before changing:

``` text
User
MemberProfile
Plan
EPIN
Network
Income
Wallet
Withdrawal
```

### Workflow

``` text
Requirement
    ↓
Discuss with Naresh
    ↓
Confirm model/API contract
    ↓
Implement admin API
    ↓
Write tests
    ↓
PR
    ↓
Naresh reviews
    ↓
develop
```

------------------------------------------------------------------------

# 36. Working With Rahul

Rahul will consume Prabhakar's admin APIs for the React Admin Dashboard.

For every completed API, provide:

``` text
Endpoint
Method
Authentication
Permission
Request
Response
Filters
Pagination
Error response
```

### Integration flow

``` text
Prabhakar
    ↓
Admin API
    ↓
API documentation
    ↓
Rahul
    ↓
React Admin UI
    ↓
Integration testing
```

------------------------------------------------------------------------

# 37. Do Not Duplicate Core Logic

This is extremely important.

### Wrong

``` text
Admin Withdrawal View
       ↓
manually subtract wallet balance
```

### Correct

``` text
Admin Withdrawal View
       ↓
Permission Check
       ↓
Withdrawal Service
       ↓
Wallet Service
       ↓
Database Transaction
```

Same principle applies to:

``` text
Income
EPIN
Plan Activation
Wallet
Binary
Referral
```

Prabhakar should **reuse existing services/models** wherever available.

------------------------------------------------------------------------

# 38. Definition of Done

An admin task is **DONE** only when:

``` text
API created
    ↓
Validation added
    ↓
Permission added
    ↓
Search/filter/pagination added where required
    ↓
Tests added
    ↓
API documented
    ↓
Rahul informed
    ↓
Meaningful commit
    ↓
Pull Request
    ↓
Code Review
    ↓
Merged into develop
```

------------------------------------------------------------------------

# 39. Important Rules

1.  Do not directly push feature code to `main`.
2.  Do not modify Naresh's core business logic without coordination.
3.  Do not duplicate income/wallet/binary logic.
4.  Never expose admin APIs publicly.
5.  Use proper permission classes.
6.  Never commit `.env` or secrets.
7.  Validate all CRUD input.
8.  Add pagination to large lists.
9.  Add search/filter where required.
10. Write tests for important admin operations.
11. Never manually modify wallet balances from a simple CRUD view.
12. Coordinate API changes with Rahul.
13. Use meaningful Git commits.
14. Create a Pull Request for every feature branch.
15. Do not create fake commits.
16. Keep Django Admin useful for development and emergency backend
    management.
17. Ask Naresh before changing shared models or migrations.
18. Follow the project's final API response format.

------------------------------------------------------------------------

# 40. Final Ownership Summary

  Area                             Owner
  -------------------------------- ---------------
  Admin Backend Architecture       **Prabhakar**
  Admin Member APIs                **Prabhakar**
  Admin Plan CRUD                  **Prabhakar**
  Admin EPIN Management            **Prabhakar**
  KYC Management                   **Prabhakar**
  Sales Management                 **Prabhakar**
  Admin Income APIs                **Prabhakar**
  Admin Withdrawal APIs            **Prabhakar**
  Notifications                    **Prabhakar**
  Admin Dashboard APIs             **Prabhakar**
  Django Admin                     **Prabhakar**
  Admin Search/Filter/Pagination   **Prabhakar**
  Admin API Testing                **Prabhakar**
  React Admin Dashboard UI         **Rahul**
  Core Authentication              **Naresh**
  Core Member Logic                **Naresh**
  Binary/Network Logic             **Naresh**
  Income Calculation               **Naresh**
  Wallet Logic                     **Naresh**
  Financial Logic                  **Naresh**

------------------------------------------------------------------------

# 41. Current Status

``` text
Django Admin Foundation       ⬜
Admin Permissions             ⬜
Admin Members                 ⬜
Admin Plans                  ⬜
Admin EPIN                   ⬜
Admin KYC                    ⬜
Admin Sales                  ⬜
Admin Income                 ⬜
Admin Withdrawals            ⬜
Notifications                ⬜
Admin Dashboard API          ⬜
Django Admin Improvements    ⬜
Admin API QA                 ⬜
```

------------------------------------------------------------------------

# 42. Exact Branch Order

``` text
feature/admin-backend-foundation
        ↓
feature/admin-members
        ↓
feature/admin-plans
        ↓
feature/admin-epins
        ↓
feature/admin-kyc
        ↓
feature/admin-sales
        ↓
feature/admin-income
        ↓
feature/admin-withdrawals
        ↓
feature/notifications
        ↓
feature/admin-dashboard-api
        ↓
feature/django-admin
        ↓
feature/admin-api-qa
```

------------------------------------------------------------------------

# 43. First Milestone

Prabhakar's first milestone should be:

``` text
Admin Backend Foundation
        +
Admin Permissions
        +
Admin Member Management
        +
Admin Plan CRUD
```

After this:

``` text
EPIN → KYC → Sales → Income → Withdrawals
```

Then:

``` text
Notifications → Admin Dashboard → Django Admin → QA
```

------------------------------------------------------------------------

# 44. Final Team Structure

``` text
                    NETWORK MANAGEMENT SYSTEM
                              │
             ┌────────────────┼────────────────┐
             │                │                │
          Naresh            Rahul          Prabhakar
             │                │                │
      Core Backend       React Frontend     Admin Backend
             │                │                │
      Django + DRF       API Integration     Django + DRF
             │                │                │
      Business Logic      Member UI          CRUD APIs
      Network             Admin UI           KYC
      Income              Responsive UI      Sales
      Wallet              Testing            Reports
      Withdrawal                              Notifications
```

**Goal:** Each team member has clear ownership, but all three
collaborate through well-defined APIs, Git branches, Pull Requests, and
code reviews.
