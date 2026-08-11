# Naresh Kumar --- Backend Lead Task Assignment

## Project

**Network Management System**

**Role:** Backend Lead / Backend Architecture

**Stack:** Python, Django, Django REST Framework, SimpleJWT, PostgreSQL,
Git & GitHub

------------------------------------------------------------------------

## 1. My Overall Responsibility

I own the **core backend architecture, database models, REST APIs,
authentication, security, and business logic**.

### Main ownership

-   Authentication & Accounts
-   Members
-   Plans
-   EPIN
-   Network / Sponsor / Binary Structure
-   Income Engine
-   Wallet
-   Withdrawals
-   Common API architecture
-   Permissions and validation
-   Backend testing
-   API documentation
-   Backend integration support for Rahul and Prabhakar

> **Important:** Binary income, referral income, pair calculation, plan
> activation and withdrawal rules must be approved by Sir before final
> implementation.

------------------------------------------------------------------------

# 2. Backend App Structure

``` text
backend/
├── apps/
│   ├── accounts/
│   ├── members/
│   ├── plans/
│   ├── epins/
│   ├── network/
│   ├── income/
│   ├── wallet/
│   └── withdrawals/
├── config/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
├── manage.py
├── requirements.txt
└── .env
```

------------------------------------------------------------------------

# 3. Accounts App --- `accounts`

## Model: User

Responsibilities: - Custom User model - UserManager - Authentication
identity - Password handling - Active/inactive status - Staff/admin
flags - Roles - Timestamps

### Tasks

-   [ ] Custom `User` model
-   [ ] `UserManager`
-   [ ] Register API
-   [ ] Login API
-   [ ] SimpleJWT configuration
-   [ ] Refresh-token API
-   [ ] Profile API
-   [ ] Change-password API
-   [ ] Permission classes
-   [ ] Authentication tests

### APIs

``` text
POST   /api/auth/register/
POST   /api/auth/login/
POST   /api/auth/token/refresh/
GET    /api/auth/profile/
PATCH  /api/auth/profile/
POST   /api/auth/change-password/
```

------------------------------------------------------------------------

# 4. Members App --- `members`

## Model: MemberProfile

Possible fields:

``` text
user
member_id
phone
profile_image
date_of_birth
address
city
state
pincode
status
kyc_status
created_at
updated_at
```

### Tasks

-   [ ] Create MemberProfile
-   [ ] Unique Member ID generation
-   [ ] User ↔ MemberProfile relationship
-   [ ] Member serializer
-   [ ] Profile API
-   [ ] Update profile API
-   [ ] Member status
-   [ ] Validation
-   [ ] Permissions
-   [ ] Tests

### APIs

``` text
GET    /api/members/profile/
PATCH  /api/members/profile/
GET    /api/members/
GET    /api/members/<id>/
```

------------------------------------------------------------------------

# 5. Plans App --- `plans`

## Models

### Plan

Possible fields:

``` text
name
code
amount
description
status
created_at
updated_at
```

### MemberPlan / PlanActivation

Possible fields:

``` text
member
plan
activation_amount
activated_at
status
```

### Tasks

-   [ ] Plan model
-   [ ] MemberPlan / PlanActivation
-   [ ] Plan CRUD APIs
-   [ ] Plan validation
-   [ ] Active/inactive plans
-   [ ] Member plan activation
-   [ ] EPIN integration
-   [ ] Permissions
-   [ ] Tests

> Do not hard-code final plan amounts until Sir approves the plan rules.

------------------------------------------------------------------------

# 6. EPIN App --- `epins`

## Model: EPIN

Possible fields:

``` text
code
plan
amount
status
generated_by
used_by
used_at
expires_at
created_at
```

Possible statuses:

``` text
UNUSED
USED
EXPIRED
BLOCKED
```

### Tasks

-   [ ] EPIN model
-   [ ] Secure/random EPIN generation
-   [ ] Duplicate prevention
-   [ ] EPIN validation
-   [ ] EPIN usage tracking
-   [ ] EPIN status
-   [ ] Expiry handling if required
-   [ ] Plan activation integration
-   [ ] Admin APIs
-   [ ] Permissions
-   [ ] Tests

### APIs

``` text
POST /api/epins/validate/
POST /api/epins/use/
GET  /api/epins/
GET  /api/epins/<id>/
```

------------------------------------------------------------------------

# 7. Network App --- `network`

This is one of the most important backend modules.

## Models

### Sponsor / Referral Relationship

``` text
member
sponsor
created_at
```

### BinaryNode / NetworkMember

Possible fields:

``` text
member
parent
position
left_child
right_child
level
created_at
```

Possible position values:

``` text
LEFT
RIGHT
```

### Tasks

-   [ ] Final network database design
-   [ ] Sponsor relationship
-   [ ] Parent-child relationship
-   [ ] Left/right position
-   [ ] Circular relationship prevention
-   [ ] Duplicate parent-position prevention
-   [ ] Level calculation
-   [ ] Sponsor lookup
-   [ ] Parent lookup
-   [ ] Child lookup
-   [ ] Downline lookup
-   [ ] Referral tree API
-   [ ] Binary tree API
-   [ ] Permissions
-   [ ] Extensive tests

### APIs

``` text
GET /api/network/my-sponsor/
GET /api/network/my-team/
GET /api/network/referral-tree/
GET /api/network/binary-tree/
GET /api/network/<member_id>/
```

> Final automatic-placement rules must be approved by Sir before
> implementation.

------------------------------------------------------------------------

# 8. Income App --- `income`

## Model: IncomeTransaction

Possible fields:

``` text
member
income_type
amount
source_member
reference
status
created_at
```

Possible income types:

``` text
REFERRAL
BINARY
PAIR
SALES
OTHER
```

### Tasks

-   [ ] Income transaction model
-   [ ] Income service layer
-   [ ] Referral income
-   [ ] Binary income
-   [ ] Pair calculation
-   [ ] Sales income if required
-   [ ] Duplicate-income prevention
-   [ ] Income ledger
-   [ ] Income history API
-   [ ] Income summary API
-   [ ] Tests for every calculation

### APIs

``` text
GET /api/income/
GET /api/income/summary/
GET /api/income/history/
```

### Architecture Rule

Do not put complex income calculations directly inside
views/serializers.

Prefer:

``` text
View
  ↓
Service
  ↓
Business Logic
  ↓
Model / Transaction
```

Example:

``` text
income/services/referral.py
income/services/binary.py
income/services/pair.py
```

------------------------------------------------------------------------

# 9. Wallet App --- `wallet`

## Models

### Wallet

``` text
member
balance
created_at
updated_at
```

### WalletTransaction

``` text
wallet
transaction_type
amount
balance_before
balance_after
reference
description
created_at
```

Transaction types:

``` text
CREDIT
DEBIT
```

### Tasks

-   [ ] Wallet model
-   [ ] WalletTransaction
-   [ ] Automatic wallet creation
-   [ ] Credit
-   [ ] Debit
-   [ ] Balance maintenance
-   [ ] Negative balance prevention
-   [ ] Balance-before/after records
-   [ ] Transaction references
-   [ ] Wallet history API
-   [ ] Wallet summary API
-   [ ] `transaction.atomic` where appropriate
-   [ ] Tests

### APIs

``` text
GET /api/wallet/
GET /api/wallet/transactions/
```

------------------------------------------------------------------------

# 10. Withdrawals App --- `withdrawals`

## Model: Withdrawal

Possible fields:

``` text
member
amount
status
payment_method
payment_details
requested_at
processed_at
processed_by
remarks
```

Statuses:

``` text
PENDING
APPROVED
REJECTED
PROCESSING
COMPLETED
```

### Tasks

-   [ ] Withdrawal model
-   [ ] Request API
-   [ ] Available-balance validation
-   [ ] Minimum withdrawal validation
-   [ ] Duplicate/invalid request prevention
-   [ ] Safe balance handling
-   [ ] Admin approve API
-   [ ] Admin reject API
-   [ ] Withdrawal history
-   [ ] Permissions
-   [ ] Tests

### APIs

``` text
POST /api/withdrawals/
GET  /api/withdrawals/
GET  /api/withdrawals/<id>/
```

------------------------------------------------------------------------

# 11. Common Backend Architecture

### API structure

``` text
/api/
    auth/
    members/
    plans/
    epins/
    network/
    income/
    wallet/
    withdrawals/
```

### Responsibilities

-   [ ] API structure/versioning if required
-   [ ] Authentication
-   [ ] Permissions
-   [ ] Serializer validation
-   [ ] Consistent error responses
-   [ ] Pagination
-   [ ] Filtering
-   [ ] Searching
-   [ ] Ordering
-   [ ] Logging
-   [ ] Environment configuration
-   [ ] CORS
-   [ ] Security settings

------------------------------------------------------------------------

# 12. Database Responsibility

Main relationship:

``` text
User
 │
 └── MemberProfile
       ├── Sponsor / Referral
       ├── Network / Binary Node
       ├── MemberPlan
       ├── EPIN Usage
       ├── Income
       ├── Wallet
       └── Withdrawal
```

### Database checklist

-   [ ] Foreign keys
-   [ ] Unique constraints
-   [ ] Database indexes
-   [ ] Correct `related_name`
-   [ ] Correct `on_delete`
-   [ ] Validation
-   [ ] Timestamps
-   [ ] Migration testing
-   [ ] Data integrity

------------------------------------------------------------------------

# 13. API Documentation

For every API document:

``` text
Endpoint
Method
Authentication
Request Body
Response
Possible Errors
Permissions
```

Example:

``` text
POST /api/auth/login/

Authentication:
Not required

Request:
{
    "email": "...",
    "password": "..."
}

Response:
{
    "access": "...",
    "refresh": "..."
}
```

Keep Swagger/OpenAPI documentation updated if used.

------------------------------------------------------------------------

# 14. Testing

Critical backend tests:

-   [ ] Registration
-   [ ] Login
-   [ ] JWT authentication
-   [ ] Permissions
-   [ ] Member creation
-   [ ] EPIN validation
-   [ ] EPIN duplicate prevention
-   [ ] Plan activation
-   [ ] Sponsor relationship
-   [ ] Binary tree placement
-   [ ] Referral income
-   [ ] Binary income
-   [ ] Wallet credit
-   [ ] Wallet debit
-   [ ] Negative balance prevention
-   [ ] Withdrawal validation
-   [ ] Withdrawal approval/rejection

------------------------------------------------------------------------

# 15. GitHub Branches

## Main branches

``` text
main
develop
```

Recommended flow:

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

## My feature branches

### Foundation

``` text
feature/backend-foundation
```

For: - DRF - SimpleJWT - Environment configuration - API structure -
Common backend configuration

### Accounts

``` text
feature/accounts
```

For: - Custom User - UserManager - Register - Login - JWT - Profile -
Password change - Permissions

### Members

``` text
feature/members
```

For: - MemberProfile - Member ID - Member APIs - Member status -
Validation

### Plans

``` text
feature/plans
```

For: - Plan - MemberPlan - Plan activation - Plan APIs

### EPIN

``` text
feature/epins
```

For: - EPIN model - Generation - Validation - Usage - EPIN APIs

### Network

``` text
feature/network
```

For: - Sponsor - Referral - Parent - Left/right - Binary tree - Referral
tree - Network APIs

### Income

``` text
feature/income
```

For: - IncomeTransaction - Referral income - Binary income - Pair
income - Income services - Income APIs

### Wallet

``` text
feature/wallet
```

For: - Wallet - WalletTransaction - Credit/debit - Ledger - Wallet APIs

### Withdrawals

``` text
feature/withdrawals
```

For: - Withdrawal - Request - Approval - Rejection - Withdrawal APIs

------------------------------------------------------------------------

# 16. Commit Convention

### Good

``` text
feat: create custom user model
feat: implement JWT authentication
feat: add member profile model
feat: implement member registration API
feat: create plan activation service
feat: add EPIN validation
feat: implement sponsor relationship
feat: create binary tree service
feat: add wallet ledger
feat: implement withdrawal request API
test: add EPIN validation tests
test: add wallet transaction tests
fix: prevent duplicate EPIN usage
fix: prevent negative wallet balance
refactor: move income calculation to services
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

# 17. Pull Request Format

Every PR should contain:

``` text
## What was done?

## Why?

## Models changed

## APIs added/changed

## Tests

## Screenshots (if applicable)

## Notes / Breaking Changes
```

Example title:

``` text
feat: implement member registration API
```

------------------------------------------------------------------------

# 18. Rahul Integration Workflow

Rahul owns React + API integration.

``` text
Naresh
  ↓
DRF API
  ↓
API Documentation
  ↓
Rahul
  ↓
React Integration
```

For every completed API:

-   [ ] Endpoint finalized
-   [ ] Request documented
-   [ ] Response documented
-   [ ] Error responses documented
-   [ ] Authentication requirement documented
-   [ ] Rahul informed
-   [ ] API tested

------------------------------------------------------------------------

# 19. Prabhakar Integration Workflow

Prabhakar owns Admin + Django/DRF CRUD modules.

``` text
Requirements
      ↓
Database Design
      ↓
Prabhakar implements CRUD/API
      ↓
PR
      ↓
Code Review
      ↓
develop
```

He should implement his assigned modules himself; I provide architecture
guidance/review when needed.

------------------------------------------------------------------------

# 20. First Sprint --- My Immediate Tasks

## Step 1 --- Backend Foundation

-   [x] Create project folder
-   [x] Django setup
-   [x] DRF setup
-   [x] SimpleJWT setup
-   [ ] PostgreSQL configuration
-   [ ] `.env` configuration
-   [ ] API root structure
-   [ ] Git initialization
-   [ ] `.gitignore`
-   [ ] requirements.txt

## Step 2 --- Accounts

-   [ ] Custom User model
-   [ ] UserManager
-   [ ] Register API
-   [ ] Login API
-   [ ] JWT refresh
-   [ ] Profile API
-   [ ] Password change
-   [ ] Permissions
-   [ ] Tests

## Step 3 --- Members

-   [ ] MemberProfile
-   [ ] Member ID generation
-   [ ] Member APIs
-   [ ] Validation
-   [ ] Tests

------------------------------------------------------------------------

# 21. Second Sprint

-   [ ] Plans
-   [ ] EPIN
-   [ ] Plan activation
-   [ ] EPIN validation
-   [ ] EPIN usage tracking
-   [ ] Admin support APIs

------------------------------------------------------------------------

# 22. Third Sprint

-   [ ] Sponsor system
-   [ ] Referral relationship
-   [ ] Binary tree structure
-   [ ] Parent/child relationship
-   [ ] Left/right placement
-   [ ] Referral tree API
-   [ ] Binary tree API
-   [ ] Network tests

------------------------------------------------------------------------

# 23. Fourth Sprint

-   [ ] Income architecture
-   [ ] Referral income
-   [ ] Binary income
-   [ ] Pair income
-   [ ] Income ledger
-   [ ] Wallet
-   [ ] Wallet ledger
-   [ ] Withdrawal
-   [ ] Withdrawal validation
-   [ ] Withdrawal workflow

------------------------------------------------------------------------

# 24. Definition of Done

A task is DONE only when:

``` text
Code written
    ↓
Validation added
    ↓
Tests added
    ↓
API tested
    ↓
Documentation updated
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

# 25. Important Rules

1.  Do not directly push feature code to `main`.
2.  Do not hard-code unapproved business rules.
3.  Keep complex business logic outside views where practical.
4.  Use database transactions for financial operations.
5.  Never store passwords manually.
6.  Never commit secrets or `.env`.
7.  Never commit virtual environments or `__pycache__`.
8.  Write tests for critical financial/network logic.
9.  Keep APIs documented for Rahul.
10. Every feature should have meaningful commits and a Pull Request.
11. Do not create fake commits to increase GitHub contribution.
12. Review major business logic with Sir before merging.

------------------------------------------------------------------------

# 26. Final Ownership Summary

  Area                         Owner
  ---------------------------- ---------------
  Backend Architecture         **Naresh**
  Django + DRF Configuration   **Naresh**
  SimpleJWT Authentication     **Naresh**
  Accounts                     **Naresh**
  Members                      **Naresh**
  Plans                        **Naresh**
  EPIN                         **Naresh**
  Network / Binary Tree        **Naresh**
  Income Engine                **Naresh**
  Wallet                       **Naresh**
  Withdrawals Backend          **Naresh**
  Core Database Design         **Naresh**
  Backend Security             **Naresh**
  Backend Testing              **Naresh**
  API Documentation            **Naresh**
  React Frontend               **Rahul**
  Admin / CRUD Backend         **Prabhakar**

------------------------------------------------------------------------

# 27. Current Status

``` text
Django Project        ✅
DRF                   ✅
SimpleJWT             ✅
Custom User           ⬜
Authentication APIs   ⬜
Member Model          ⬜
Plan Model            ⬜
EPIN Model            ⬜
Network Model         ⬜
Income Engine         ⬜
Wallet                ⬜
Withdrawal            ⬜
```

## Immediate Next Task

``` text
feature/backend-foundation
        ↓
feature/accounts
        ↓
feature/members
        ↓
feature/plans
        ↓
feature/epins
        ↓
feature/network
        ↓
feature/income
        ↓
feature/wallet
        ↓
feature/withdrawals
```

**My first milestone:** Complete the authentication + member foundation
and provide stable, documented APIs for the frontend team.
