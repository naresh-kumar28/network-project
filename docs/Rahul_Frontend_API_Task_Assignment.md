# Rahul --- Frontend & API Integration Task Assignment

## Project

**Project Name:** Network Management System

**Role:** Frontend Developer + API Integration

**Primary Stack:** - React - Vite - Tailwind CSS - React Router - Axios
/ Fetch - Django REST Framework APIs - SimpleJWT - Git & GitHub

------------------------------------------------------------------------

# 1. My Overall Responsibility

Rahul's main responsibility is to build the **complete React frontend,
reusable UI components, dashboard screens, frontend state/authentication
flow, and integration with Naresh's DRF APIs**.

### Main ownership

1.  React project architecture
2.  Tailwind UI system
3.  Authentication UI
4.  Member Dashboard
5.  Profile
6.  My Team
7.  Referral Tree
8.  Binary Tree
9.  Plans
10. EPIN activation
11. Income
12. Wallet
13. Withdrawals
14. API integration
15. Loading/error/empty states
16. Protected routes
17. Frontend validation
18. Responsive design
19. Frontend testing
20. Production frontend build

> Rahul should not create duplicate backend business logic in React.
> Business rules such as income calculation, binary placement, wallet
> balance and EPIN validation must come from the backend APIs.

------------------------------------------------------------------------

# 2. Frontend Project Structure

Recommended structure:

``` text
frontend/
├── src/
│   ├── assets/
│   ├── components/
│   │   ├── common/
│   │   ├── forms/
│   │   ├── tables/
│   │   ├── cards/
│   │   └── tree/
│   │
│   ├── layouts/
│   │   ├── AuthLayout.jsx
│   │   └── MemberLayout.jsx
│   │
│   ├── pages/
│   │   ├── auth/
│   │   ├── dashboard/
│   │   ├── profile/
│   │   ├── team/
│   │   ├── plans/
│   │   ├── epins/
│   │   ├── income/
│   │   ├── wallet/
│   │   └── withdrawals/
│   │
│   ├── services/
│   │   ├── api.js
│   │   ├── auth.js
│   │   ├── members.js
│   │   ├── plans.js
│   │   ├── epins.js
│   │   ├── network.js
│   │   ├── income.js
│   │   ├── wallet.js
│   │   └── withdrawals.js
│   │
│   ├── context/
│   │   └── AuthContext.jsx
│   │
│   ├── hooks/
│   ├── utils/
│   ├── routes/
│   └── App.jsx
│
├── package.json
└── .env
```

------------------------------------------------------------------------

# 3. Frontend Foundation

## Responsibility

Create a clean and scalable React foundation before building individual
pages.

### Tasks

-   [ ] React/Vite setup
-   [ ] Tailwind CSS setup
-   [ ] React Router setup
-   [ ] Axios setup
-   [ ] Environment variables
-   [ ] Global CSS
-   [ ] Common typography
-   [ ] Responsive breakpoints
-   [ ] Reusable Button component
-   [ ] Reusable Input component
-   [ ] Select component
-   [ ] Modal component
-   [ ] Table component
-   [ ] Pagination component
-   [ ] Loading component
-   [ ] Empty-state component
-   [ ] Error-state component
-   [ ] Toast/notification component
-   [ ] Confirm dialog
-   [ ] Common Card component

------------------------------------------------------------------------

# 4. Authentication

## Pages

``` text
/login
/register
/forgot-password
/reset-password
```

### Tasks

-   [ ] Login UI
-   [ ] Registration UI
-   [ ] Forgot-password UI if backend supports it
-   [ ] Form validation
-   [ ] API integration
-   [ ] JWT access-token handling
-   [ ] Refresh-token handling
-   [ ] Logout
-   [ ] Auth context/state
-   [ ] Protected routes
-   [ ] Unauthorized handling
-   [ ] Token-expiry handling
-   [ ] Loading states
-   [ ] API error messages

### API Integration

Backend APIs expected:

``` text
POST /api/auth/register/
POST /api/auth/login/
POST /api/auth/token/refresh/
GET  /api/auth/profile/
PATCH /api/auth/profile/
POST /api/auth/change-password/
```

------------------------------------------------------------------------

# 5. Member Layout

Create the main authenticated member application layout.

### Layout

``` text
┌─────────────────────────────────────┐
│ Header                              │
├────────────┬────────────────────────┤
│ Sidebar    │ Main Content           │
│            │                        │
│ Dashboard  │                        │
│ Profile    │                        │
│ My Team    │                        │
│ Plans      │                        │
│ EPIN       │                        │
│ Income     │                        │
│ Wallet     │                        │
│ Withdrawal │                        │
└────────────┴────────────────────────┘
```

### Tasks

-   [ ] Sidebar
-   [ ] Header
-   [ ] User menu
-   [ ] Notifications UI
-   [ ] Mobile navigation
-   [ ] Breadcrumbs if required
-   [ ] Responsive layout
-   [ ] Protected member layout

------------------------------------------------------------------------

# 6. Member Dashboard

## Route

``` text
/dashboard
```

### Dashboard cards

Possible cards:

``` text
Total Team
Active Members
Total Income
Available Wallet Balance
Total Withdrawal
Current Plan
```

### Tasks

-   [ ] Dashboard layout
-   [ ] Summary cards
-   [ ] Recent transactions
-   [ ] Recent income
-   [ ] Team summary
-   [ ] Current plan
-   [ ] Quick actions
-   [ ] API integration
-   [ ] Loading state
-   [ ] Empty state
-   [ ] Error state
-   [ ] Responsive design

------------------------------------------------------------------------

# 7. Profile

## Routes

``` text
/profile
/profile/edit
/profile/change-password
```

### Tasks

-   [ ] Profile view
-   [ ] Edit profile
-   [ ] Profile image UI if supported
-   [ ] Personal information
-   [ ] Address information
-   [ ] KYC status display
-   [ ] Change password
-   [ ] Form validation
-   [ ] API integration
-   [ ] Success/error messages

------------------------------------------------------------------------

# 8. My Team

## Route

``` text
/team
```

### Tasks

-   [ ] Team summary
-   [ ] Team member list
-   [ ] Search
-   [ ] Filters
-   [ ] Member status
-   [ ] Member details
-   [ ] Sponsor information
-   [ ] Pagination
-   [ ] API integration
-   [ ] Loading/empty/error states

Expected API:

``` text
GET /api/network/my-sponsor/
GET /api/network/my-team/
```

------------------------------------------------------------------------

# 9. Referral Tree

## Route

``` text
/team/referral-tree
```

### Tasks

-   [ ] Referral tree UI
-   [ ] Parent-child visualization
-   [ ] Member cards
-   [ ] Member status
-   [ ] Expand/collapse
-   [ ] Mobile responsive tree
-   [ ] API integration
-   [ ] Loading state
-   [ ] Empty state

Expected API:

``` text
GET /api/network/referral-tree/
```

------------------------------------------------------------------------

# 10. Binary Tree

## Route

``` text
/team/binary-tree
```

### Tasks

-   [ ] Binary tree UI
-   [ ] Left/right positions
-   [ ] Parent node
-   [ ] Child nodes
-   [ ] Member details
-   [ ] Expand/collapse
-   [ ] Tree navigation
-   [ ] Mobile-friendly behavior
-   [ ] API integration
-   [ ] Loading/empty/error states

Expected API:

``` text
GET /api/network/binary-tree/
```

> Do not calculate binary placement in React. React only visualizes the
> structure returned by the backend.

------------------------------------------------------------------------

# 11. Plans

## Routes

``` text
/plans
/plans/:id
```

### Tasks

-   [ ] Plan listing
-   [ ] Plan cards
-   [ ] Plan details
-   [ ] Current active plan
-   [ ] Activation UI
-   [ ] Confirmation modal
-   [ ] EPIN integration flow
-   [ ] API integration
-   [ ] Loading/error states

------------------------------------------------------------------------

# 12. EPIN

## Routes

``` text
/epins
/epins/activate
```

### Tasks

-   [ ] EPIN activation page
-   [ ] EPIN input
-   [ ] Validation UI
-   [ ] Activation confirmation
-   [ ] Success state
-   [ ] Invalid EPIN state
-   [ ] Used EPIN state
-   [ ] EPIN history/list if member-facing API is available

Expected APIs:

``` text
POST /api/epins/validate/
POST /api/epins/use/
```

> EPIN validity must be checked by the backend. Never trust
> frontend-only validation.

------------------------------------------------------------------------

# 13. Income

## Routes

``` text
/income
/income/history
```

### Tasks

-   [ ] Income summary
-   [ ] Total income
-   [ ] Referral income
-   [ ] Binary income
-   [ ] Pair income
-   [ ] Income history
-   [ ] Filters
-   [ ] Date filter
-   [ ] Pagination
-   [ ] API integration
-   [ ] Loading/error/empty states

Expected APIs:

``` text
GET /api/income/
GET /api/income/summary/
GET /api/income/history/
```

------------------------------------------------------------------------

# 14. Wallet

## Routes

``` text
/wallet
/wallet/transactions
```

### Tasks

-   [ ] Wallet balance card
-   [ ] Credit/debit summary
-   [ ] Transaction history
-   [ ] Transaction type filters
-   [ ] Date filters
-   [ ] Pagination
-   [ ] API integration
-   [ ] Loading/error/empty states

Expected APIs:

``` text
GET /api/wallet/
GET /api/wallet/transactions/
```

> Wallet balance shown in React must always come from the backend.

------------------------------------------------------------------------

# 15. Withdrawals

## Routes

``` text
/withdrawals
/withdrawals/request
/withdrawals/:id
```

### Tasks

-   [ ] Withdrawal request form
-   [ ] Available balance display
-   [ ] Amount validation
-   [ ] Payment method UI
-   [ ] Payment details
-   [ ] Confirmation modal
-   [ ] Withdrawal history
-   [ ] Withdrawal status badges
-   [ ] Withdrawal details
-   [ ] API integration
-   [ ] Success/error handling

Expected APIs:

``` text
POST /api/withdrawals/
GET  /api/withdrawals/
GET  /api/withdrawals/<id>/
```

> Minimum withdrawal amount, wallet balance and approval rules must be
> validated by the backend.

------------------------------------------------------------------------

# 16. API Service Layer

Do not write API calls randomly inside every component.

Create centralized services:

``` text
services/
├── api.js
├── auth.js
├── members.js
├── plans.js
├── epins.js
├── network.js
├── income.js
├── wallet.js
└── withdrawals.js
```

Example responsibility:

``` text
auth.js
    ↓
login()
register()
refreshToken()
getProfile()
logout()
```

### Tasks

-   [ ] Axios instance
-   [ ] Base URL from `.env`
-   [ ] Authorization header
-   [ ] JWT refresh strategy
-   [ ] Common API error handling
-   [ ] Service files
-   [ ] Request/response handling

------------------------------------------------------------------------

# 17. State Management

Start simple.

Use:

``` text
Context / Hooks
```

for authentication and small global state.

### Tasks

-   [ ] AuthContext
-   [ ] Current user
-   [ ] Login state
-   [ ] Logout state
-   [ ] Token state
-   [ ] Protected route state
-   [ ] Loading state

Do not introduce Redux/Zustand unless project requirements justify it.

------------------------------------------------------------------------

# 18. Form Validation

Every important form should have frontend validation.

### Forms

-   [ ] Register
-   [ ] Login
-   [ ] Profile
-   [ ] Change password
-   [ ] EPIN activation
-   [ ] Withdrawal request

Validation should improve UX, but backend validation remains the source
of truth.

------------------------------------------------------------------------

# 19. UI/UX Quality

Rahul owns frontend consistency.

### Requirements

-   [ ] Responsive desktop
-   [ ] Responsive tablet
-   [ ] Responsive mobile
-   [ ] Consistent spacing
-   [ ] Consistent typography
-   [ ] Consistent buttons
-   [ ] Consistent form controls
-   [ ] Consistent cards
-   [ ] Consistent tables
-   [ ] Status badges
-   [ ] Loading skeletons/spinners
-   [ ] Empty states
-   [ ] Error states
-   [ ] Toast notifications
-   [ ] Accessible labels
-   [ ] Keyboard-friendly forms

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

Do not directly develop features on `main`.

------------------------------------------------------------------------

# 21. Rahul's Feature Branches --- Exact Order

## Phase 1 --- Frontend Foundation

### Branch

``` text
feature/react-foundation
```

### Use for

-   React/Vite
-   Tailwind
-   Router
-   Axios
-   Project structure
-   Global styles
-   Common components
-   `.env.example`

------------------------------------------------------------------------

## Phase 2 --- Authentication

### Branch

``` text
feature/frontend-auth
```

### Use for

-   Login
-   Register
-   Forgot password if required
-   AuthContext
-   JWT handling
-   Protected routes
-   Logout
-   Authentication error states

------------------------------------------------------------------------

## Phase 3 --- Member Layout

### Branch

``` text
feature/member-layout
```

### Use for

-   Sidebar
-   Header
-   Mobile navigation
-   Member layout
-   Navigation
-   Common dashboard structure

------------------------------------------------------------------------

## Phase 4 --- Dashboard

### Branch

``` text
feature/member-dashboard
```

### Use for

-   Dashboard cards
-   Summary
-   Recent activity
-   Team summary
-   Current plan
-   API integration

------------------------------------------------------------------------

## Phase 5 --- Profile

### Branch

``` text
feature/member-profile
```

### Use for

-   Profile
-   Edit profile
-   Change password
-   KYC status
-   Profile API integration

------------------------------------------------------------------------

## Phase 6 --- Team

### Branch

``` text
feature/member-team
```

### Use for

-   My Team
-   Sponsor
-   Team members
-   Search/filter
-   Pagination

------------------------------------------------------------------------

## Phase 7 --- Referral Tree

### Branch

``` text
feature/referral-tree-ui
```

### Use for

-   Referral tree
-   Member nodes
-   Expand/collapse
-   API integration
-   Responsive tree

------------------------------------------------------------------------

## Phase 8 --- Binary Tree

### Branch

``` text
feature/binary-tree-ui
```

### Use for

-   Binary tree
-   Left/right nodes
-   Parent/child
-   Navigation
-   API integration

------------------------------------------------------------------------

## Phase 9 --- Plans

### Branch

``` text
feature/plans-ui
```

### Use for

-   Plan listing
-   Plan details
-   Current plan
-   Activation flow

------------------------------------------------------------------------

## Phase 10 --- EPIN

### Branch

``` text
feature/epin-ui
```

### Use for

-   EPIN activation
-   Validation
-   Confirmation
-   Error/success states

------------------------------------------------------------------------

## Phase 11 --- Income

### Branch

``` text
feature/income-ui
```

### Use for

-   Income dashboard
-   Income summary
-   Income history
-   Filters
-   Pagination

------------------------------------------------------------------------

## Phase 12 --- Wallet

### Branch

``` text
feature/wallet-ui
```

### Use for

-   Wallet balance
-   Transactions
-   Filters
-   Pagination

------------------------------------------------------------------------

## Phase 13 --- Withdrawals

### Branch

``` text
feature/withdrawal-ui
```

### Use for

-   Withdrawal request
-   Withdrawal history
-   Withdrawal details
-   Status
-   API integration

------------------------------------------------------------------------

# 22. GitHub Commit Convention

### Good commits

``` text
feat: setup react project structure
feat: configure tailwind css
feat: add axios api client
feat: implement login page
feat: add jwt auth context
feat: create protected route
feat: build member dashboard
feat: add profile page
feat: implement team listing
feat: add referral tree visualization
feat: add binary tree visualization
feat: integrate wallet API
feat: implement withdrawal form
fix: handle expired access token
fix: show api validation errors
test: add login form tests
refactor: extract reusable table component
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

# 23. Pull Request Format

Every PR should contain:

``` text
## What was done?

## Pages/components added

## APIs integrated

## Validation

## Responsive testing

## Screenshots

## Known issues
```

Example PR title:

``` text
feat: implement member dashboard
```

------------------------------------------------------------------------

# 24. API Integration Workflow With Naresh

``` text
Naresh
  ↓
DRF API completed
  ↓
Endpoint + request/response documented
  ↓
Rahul integrates API
  ↓
Frontend testing
  ↓
Issues reported to Naresh
  ↓
Final integration
```

### For every API, confirm:

-   [ ] Endpoint
-   [ ] HTTP method
-   [ ] Authentication requirement
-   [ ] Request body
-   [ ] Response structure
-   [ ] Error response
-   [ ] Pagination if applicable
-   [ ] Filters if applicable

------------------------------------------------------------------------

# 25. Backend Dependency Rule

Rahul should not block frontend development while waiting for every
backend API.

Use:

``` text
Mock data
   ↓
UI completed
   ↓
DRF API available
   ↓
Replace mock service
   ↓
Real API integration
```

But mock data must be clearly separated from production API services.

------------------------------------------------------------------------

# 26. Frontend Testing

### Test critical areas

-   [ ] Login
-   [ ] Register
-   [ ] Protected routes
-   [ ] Logout
-   [ ] Token expiry
-   [ ] Profile form
-   [ ] EPIN validation UI
-   [ ] Withdrawal form
-   [ ] API error handling
-   [ ] Mobile responsiveness

------------------------------------------------------------------------

# 27. Production Checklist

Before frontend is considered complete:

-   [ ] Production API URL configured
-   [ ] `.env` values handled correctly
-   [ ] No secrets committed
-   [ ] No hard-coded localhost API URL
-   [ ] Production build works
-   [ ] Routing works after deployment
-   [ ] API errors handled
-   [ ] Loading states handled
-   [ ] Mobile UI checked
-   [ ] Console errors removed
-   [ ] Unused code removed
-   [ ] README updated

------------------------------------------------------------------------

# 28. Definition of Done

A frontend task is **DONE** only when:

``` text
UI created
    ↓
Responsive design
    ↓
Frontend validation
    ↓
API integrated
    ↓
Loading/error/empty states
    ↓
Tested
    ↓
Screenshots checked
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

# 29. Important Rules

1.  Do not directly push feature code to `main`.
2.  Do not duplicate backend business logic in React.
3.  Never trust frontend-only validation for financial/security
    operations.
4.  Never store secrets in source code.
5.  Do not commit `.env`.
6.  Keep API calls inside the service layer.
7.  Keep reusable UI components reusable.
8.  Do not create fake commits.
9.  Test mobile responsiveness for every major page.
10. Keep loading, error and empty states in every API-driven screen.
11. Coordinate API changes with Naresh.
12. Use meaningful commit messages.
13. Create a Pull Request for every feature branch.
14. Do not merge breaking API changes without coordination.
15. Keep the frontend structure clean and scalable.

------------------------------------------------------------------------

# 30. Final Ownership Summary

  Area                    Owner
  ----------------------- ---------------
  React Architecture      **Rahul**
  Vite Setup              **Rahul**
  Tailwind CSS            **Rahul**
  React Router            **Rahul**
  Authentication UI       **Rahul**
  JWT Frontend Handling   **Rahul**
  Member Layout           **Rahul**
  Member Dashboard        **Rahul**
  Profile                 **Rahul**
  My Team                 **Rahul**
  Referral Tree UI        **Rahul**
  Binary Tree UI          **Rahul**
  Plans UI                **Rahul**
  EPIN UI                 **Rahul**
  Income UI               **Rahul**
  Wallet UI               **Rahul**
  Withdrawal UI           **Rahul**
  API Integration         **Rahul**
  Responsive UI           **Rahul**
  Frontend Testing        **Rahul**
  Backend APIs            **Naresh**
  Admin/CRUD Backend      **Prabhakar**

------------------------------------------------------------------------

# 31. Current Status

``` text
React/Vite Foundation       ⬜
Tailwind                    ⬜
Router                      ⬜
Axios/API Layer             ⬜
Authentication              ⬜
Member Layout               ⬜
Dashboard                   ⬜
Profile                     ⬜
My Team                     ⬜
Referral Tree               ⬜
Binary Tree                 ⬜
Plans                       ⬜
EPIN                        ⬜
Income                      ⬜
Wallet                      ⬜
Withdrawals                 ⬜
Testing                     ⬜
Production Build            ⬜
```

## Immediate Next Task

``` text
feature/react-foundation
        ↓
feature/frontend-auth
        ↓
feature/member-layout
        ↓
feature/member-dashboard
        ↓
feature/member-profile
        ↓
feature/member-team
        ↓
feature/referral-tree-ui
        ↓
feature/binary-tree-ui
        ↓
feature/plans-ui
        ↓
feature/epin-ui
        ↓
feature/income-ui
        ↓
feature/wallet-ui
        ↓
feature/withdrawal-ui
```

### First Milestone

Complete:

``` text
React Foundation
      +
Authentication UI
      +
Protected Member Layout
```

Then integrate Naresh's first stable authentication APIs.
