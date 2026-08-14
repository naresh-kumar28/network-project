# Network Management System

A web-based Network Management System built with Django and Django Templates.

The platform is designed to manage a structured member network, membership plans, EPIN-based onboarding, binary placement, referral relationships, income tracking, wallets, KYC verification, withdrawals, and administrative operations.

---

## Project Overview

The Network Management System provides a centralized platform for managing a membership-based network.

The system consists of three major areas:

1. Public Website
2. Admin Panel
3. Member Panel

The platform does not support open/public member registration.

A new member can only enter the network through the authorized onboarding process using a valid EPIN and the required sponsor and placement information.

---

## Technology Stack

### Backend
- Python
- Django

### Frontend
- Django Templates
- HTML5
- CSS3
- JavaScript

### Database
- PostgreSQL

### Development
- Git
- GitHub

---

# User Roles

## 1. Super Admins

The development company consists of:

- Rahul
- Naresh
- Prabhakar

The three developers are responsible for developing, maintaining, reviewing, and managing the application at the technical level.

They are not part of the business member hierarchy.

---

## 2. Website Owner / Admin

The actual owner of the website operates the business through the Admin Panel.

The Admin has complete business-level control over the platform.

### Admin Responsibilities

- Manage members
- Create and manage plans
- Generate EPINs
- Monitor EPIN usage
- Verify KYC
- Monitor wallets
- Review withdrawal requests
- Approve or reject withdrawals
- View binary tree
- View referral tree
- Manage member placement
- Monitor income
- Monitor sales
- View reports
- Manage notifications
- Manage support requests
- Manage system settings

---

## 3. Members

Members are users who have successfully entered the network through the authorized onboarding process.

A member can:

- View their profile
- View their membership plan
- Add/invite new members
- View their direct members
- View their team
- View their binary tree
- View their referral tree
- View income
- View wallet
- Request withdrawals
- Submit KYC
- View notifications
- Contact support

Members cannot:

- Create plans
- Generate EPINs
- Approve KYC
- Approve withdrawals
- Modify another member's wallet
- Modify income manually
- Modify the binary tree manually

---

# Member Onboarding

The platform does not provide open registration.

A user cannot simply create an account using only an email and password.

A valid onboarding process requires the necessary membership information.

### Basic Flow

    Admin
      ↓
    Create Plan
      ↓
    Generate EPIN
      ↓
    EPIN provided to new member
      ↓
    Member Onboarding
      ↓
    EPIN Validation
      ↓
    Sponsor Validation
      ↓
    Placement Validation
      ↓
    Member Account Creation
      ↓
    Member ID Generation
      ↓
    Plan Activation
      ↓
    Network Placement

---

# EPIN System

EPINs are generated and managed by the Admin.

Each EPIN is associated with a membership plan and has a lifecycle.

Example lifecycle:

    Generated
        ↓
    Available
        ↓
    Used
        ↓
    Assigned to Member

Invalid or already-used EPINs cannot be used for onboarding.

The system must prevent:

- Invalid EPIN usage
- Duplicate EPIN usage
- Unauthorized EPIN usage
- EPIN reuse

---

# Sponsor Relationship

A sponsor represents the member who introduced or referred another member into the network.

Example:

    M00001
       ↓
    M00002

In this case:

    M00002 Sponsor = M00001

Sponsor relationships are used for referral-related operations and income calculations.

---

# Binary Network

The system maintains a binary placement structure.

Each member can have:

- Left position
- Right position

Example:

                    M00001
                   /      \
                M00002    M00003
                /   \
             M00004 M00005

The binary tree represents the member's placement structure.

---

# Sponsor vs Parent

Sponsor and Parent are separate concepts.

### Sponsor

The member who referred the new member.

### Parent

The member under whom the new member is placed in the binary tree.

### Position

The position of the member under the parent:

- LEFT
- RIGHT

Therefore, the system must maintain these relationships separately.

---

# Referral Tree

The referral tree is based on sponsor relationships.

Example:

    M00001
    ├── M00002
    │   └── M00004
    │       └── M00008
    │
    └── M00003

The referral tree shows the direct and indirect referral structure.

---

# Binary Tree

The binary tree is based on placement relationships.

Example:

                    M00001
                   /      \
                M00002    M00003
                /   \
             M00004 M00005

The referral tree and binary tree are separate structures and must not be treated as the same relationship.

---

# Income System

The system may contain multiple income types based on the final business rules.

### Referral Income

Generated according to eligible referral activity.

### Binary Income

Calculated according to the left/right binary structure and qualifying pairs.

### Slab Income

Generated when a member reaches the required performance or qualification level.

### Sales Income

Generated according to applicable sales and commission rules.

All income calculations must follow centralized business rules.

Income must not be manually calculated inside individual page views.

---

# Pair Calculation

Binary income may depend on qualifying members on the left and right sides.

Conceptually:

    Left Team
        +
    Right Team
        ↓
    Qualifying Pair
        ↓
    Business Rule
        ↓
    Binary Income

The exact pair rules, limits, amounts, and eligibility conditions are determined by the approved business requirements.

---

# Wallet

Each member has a wallet for tracking eligible financial transactions.

Wallet activity may include:

- Income credits
- Adjustments, if authorized
- Withdrawal debits
- Other approved transactions

The system should maintain a transaction history rather than relying only on a manually editable balance.

Example:

    Referral Income       +₹500
    Binary Income        +₹1000
    Slab Income          +₹2000
    Withdrawal           -₹1000
    ----------------------------
    Current Balance       ₹2500

---

# Withdrawal System

Members can request withdrawals from their eligible wallet balance.

### Flow

    Member
      ↓
    Withdrawal Request
      ↓
    Balance Validation
      ↓
    KYC / Eligibility Check
      ↓
    Admin Review
      ↓
    Approve / Reject
      ↓
    Transaction Processing

The Admin is responsible for reviewing and approving or rejecting withdrawal requests.

---

# KYC System

Members can submit their required KYC information and documents.

### KYC Lifecycle

    Not Submitted
          ↓
       Pending
          ↓
    Admin Review
       ↙     ↘
   Verified   Rejected

KYC status can affect eligibility for certain operations such as withdrawals according to the final business rules.

---

# Admin Panel

The Admin Panel provides centralized business management.

### Main Sections

- Dashboard
- Members
- Network
- Plans
- EPIN
- Income
- Wallet
- Withdrawals
- KYC
- Sales
- Reports
- Notifications
- Support
- Settings

---

# Member Panel

The Member Panel provides members with access to their own network and account information.

### Main Sections

- Dashboard
- Profile
- My Plan
- My Team
- Add Member
- Binary Tree
- Referral Tree
- Income
- Wallet
- Withdrawals
- KYC
- Notifications
- Support

---

# Public Website

The public website contains general information about the platform.

Typical sections include:

- Home
- About
- Plans
- How It Works
- FAQ
- Contact
- Terms & Conditions
- Privacy Policy
- Login

The public website does not provide unrestricted member registration.

---

# Application Architecture

The project follows a modular Django application architecture.

Major application responsibilities include:

### Core

Handles common/public website functionality.

### Admin Panel

Handles the website owner's dashboard and admin-facing operations.

### Accounts

Handles authentication, user identity, roles, and access control.

### Members

Handles member profiles and member identity.

### Plans

Handles membership plans.

### EPIN

Handles EPIN generation, validation, usage, and tracking.

### Network

Handles sponsor relationships, parent relationships, binary placement, and network trees.

### Income

Handles referral, binary, slab, and other income calculations.

### Wallet

Handles wallet balances and financial transactions.

### Sales

Handles sales-related records and operations.

### Withdrawals

Handles member withdrawal requests and administrative processing.

### KYC

Handles member KYC submission and verification.

### Notifications

Handles system and member notifications.

### Support

Handles member support requests and tickets.

### Reports

Handles administrative reports and analytics.

---

# Development Principles

The project follows these principles:

### 1. Modular Architecture

Each business domain should remain inside its responsible Django app.

### 2. Separation of Responsibilities

Views should handle HTTP requests and responses.

Business logic should be placed in appropriate service/rule layers.

### 3. Centralized Business Rules

Income, pair calculations, eligibility, wallet operations, and other important business rules should not be duplicated across views.

### 4. Security First

Sensitive operations must always be validated on the server side.

Client-side validation alone must never be trusted.

### 5. No Open Registration

Member creation must always follow the authorized onboarding process.

### 6. Auditability

Important financial and administrative actions should be traceable.

### 7. Database Integrity

Sponsor, parent, position, EPIN, plan, wallet, income, and transaction relationships must remain consistent.

---

# Git & Collaboration Rules

The development team follows a feature-branch workflow.

### Main branches

    main
    develop

### Feature branches

    feature/rahul-<feature>
    feature/naresh-<feature>
    feature/prabhakar-<feature>

Developers should not directly push to `main`.

Recommended workflow:

    Create Task
        ↓
    Create Feature Branch
        ↓
    Develop
        ↓
    Test
        ↓
    Commit
        ↓
    Push
        ↓
    Pull Request
        ↓
    Code Review
        ↓
    Changes (if required)
        ↓
    Merge
        ↓
    Integration Testing

---

# Code Ownership

## Rahul

Primary ownership:

- Accounts
- Members
- Network
- Income
- Wallet
- Project architecture
- Code review
- Integration
- Team coordination

## Naresh

Primary ownership:

- Plans
- EPIN
- Sales
- Withdrawals

## Prabhakar

Primary ownership:

- KYC
- Notifications
- Support
- Reports
- Shared UI components

All developers are responsible for writing clean, tested, maintainable code within their assigned modules.

---

# Development Workflow

The project will be developed incrementally.

The team will first establish the complete user interface and user flows so that the business process is clearly understood.

After the UI and user flows are finalized, the corresponding backend models, relationships, services, validations, and business rules will be implemented.

The final stages will include:

- Backend integration
- Business logic implementation
- Testing
- Security review
- Bug fixing
- Performance improvements
- Deployment
- Documentation

---

# Project Goal

The goal is to build a reliable, maintainable, and secure network management platform that allows the website owner to manage the complete business ecosystem while allowing members to manage their own profiles, teams, network positions, income, wallet, KYC, and withdrawal activities.

The system should be designed so that business rules can evolve without requiring major changes to the overall architecture.

---

## Status

**Project Status:** In Development

**Architecture:** Django + Django Templates

**Database:** PostgreSQL

**Version Control:** Git + GitHub

**Development Team:**
- Rahul
- Naresh
- Prabhakar