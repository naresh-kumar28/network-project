# Prompt for Antigravity — MLM/Network Admin Panel UI (Django)

Copy-paste the block below into Antigravity.

---

## PROMPT START

I have an existing Django 6.1 project called **network-project**. I need you to build the **complete Admin Panel UI/UX** (frontend only, static/dummy data is fine for now — no backend logic, no models, no views wiring beyond simple render() calls) inside the existing `apps/admin` Django app, using **Django template inheritance**. Match the visual design shown in the two reference screenshots I'm providing (a SaaS-style MLM/Network Marketing admin dashboard called "NETWORK PRO ADMIN PANEL").

### Project context (already exists — do not recreate)
- Django 6.1 project, apps live under `apps/` (`apps/accounts`, `apps/admin`, `apps/core`)
- Styling is **Tailwind CSS v4** via `@tailwindcss/cli`, compiled from `config/static/css/input.css` → `config/static/css/main.css` (npm script: `npm run dev`)
- Root template is `templates/base.html`, which does `{% load static %}`, links `main.css`, and includes `templates/includes/header.html` and `templates/includes/footer.html` — these are currently empty and NOT meant for the admin panel (they're for the public site)
- `config/urls.py` already includes `apps.admin.urls`

### What to build
Build a **separate, self-contained admin panel layout** that does NOT reuse the public `templates/base.html`. Instead:

1. **Templates location**: Create ALL admin panel templates inside `apps/admin/templates/admin/` (app-namespaced templates folder, standard Django convention: `apps/admin/templates/<app_label>/*.html`).
2. **Template inheritance structure**:
   - `apps/admin/templates/admin/layout/base.html` — master layout with `<html>`, `<head>`, Tailwind CSS link, and the overall page shell (sidebar + topbar + `{% block content %}`)
   - `apps/admin/templates/admin/layout/_sidebar.html` — left sidebar nav (included via `{% include %}`)
   - `apps/admin/templates/admin/layout/_topbar.html` — top header bar (hamburger, notification bell, admin profile dropdown)
   - Every page template (e.g. `dashboard.html`, `members.html`, `plans.html`, etc.) should `{% extends "admin/layout/base.html" %}` and only override `{% block content %}` (and `{% block title %}` / `{% block page_actions %}` if needed)
3. **Sidebar navigation items** (build a working page — even if mostly placeholder content — for each):
   - Dashboard
   - Members
   - Binary Tree
   - Referral Tree
   - Plans
   - EPIN Management (badge: "New")
   - Income Management
   - Wallets
   - Withdrawals
   - Transactions
   - Sales & Packages
   - Reports
   - KYC Verification
   - Support Tickets
   - Notifications
   - Settings
   - Admins
   - System Settings
   - Each sidebar link should have its own icon (use `lucide` icon set via CDN or inline SVGs — match icon style from the screenshots), a hover/active state, and the active page should be highlighted with the purple background shown in the screenshots.
   - Sidebar footer shows an "Admin — Super Admin" profile chip with dropdown.

### Design system (extract from screenshots — match closely)
- **Brand**: "NETWORK PRO" logo (hexagon/badge icon in gold/amber `#F5B301`-ish color) + "ADMIN PANEL" subtitle, top-left of sidebar, on a near-black (`#0F0F10` / `#111827`-ish) sidebar background
- **Primary accent color**: Purple/Indigo (`#6D4AFF` / `#7C3AED`-ish) — used for active nav item, primary buttons, links, chart accents
- **Layout**: Fixed dark sidebar (~240px) on left, light gray (`#F5F6FA`-ish) main content area on right, with a white sticky topbar
- **Topbar**: hamburger/menu icon (left), page breadcrumb area, notification bell with red badge count, admin avatar + name + role + chevron dropdown (right)
- **Stat cards**: white rounded-xl cards with soft shadow, colored icon-in-circle on the left, big bold number, label above it, small green "↑ X% from last 7 days" trend line below
- **Data table**: white rounded-xl card, search input with icon, several filter dropdowns (Select Plan / Select Status / Select KYC Status / Select Date Range), "Filter" and "Reset" buttons, columns with avatar-initial badges (colored circles with 2-letter initials), status pills, action column with "View" + dropdown chevron, pagination footer ("Showing X to Y of Z", numbered pagination with prev/next)
- **Modal**: centered overlay modal (e.g. "Generate Plan EPIN") with a form on the left/center (select dropdowns, text inputs, date picker) and an info/preview panel on the right (light purple/lavender background `#F5F3FF`-ish, bullet list "How It Works", "Benefits" with green checkmarks, a highlighted "Note" callout box), Cancel + primary action buttons at the bottom
- **Bottom info strip**: 3-column row of small info cards with icon + heading + short description at the bottom of content pages (like "About Plan EPIN", "EPIN Types", "Manage EPINs" in image 1)
- **Charts** (dashboard only): use **Chart.js** (via CDN) for the "Member Growth Overview" area/line chart and the "Plan Wise Members" donut chart — match colors and layout from the screenshot
- **Buttons**: primary = solid purple, rounded-lg; secondary/outline = white bg, gray border, gray text
- Use **rounded-xl / rounded-2xl** corners throughout, soft `shadow-sm`, consistent `p-6` card padding, and a consistent 8px-based spacing scale (Tailwind defaults)

### Pages to build in detail (match screenshots exactly)
1. **Dashboard** (`dashboard.html`) — replicate Image 2 exactly:
   - 5 stat cards row (Total Members, New Members Today, Total Team Size, Total Wallet Balance, Total Earnings)
   - Date range picker top-right
   - "Member Growth Overview" line/area chart card (with "Last 7 Days" dropdown)
   - "Plan Wise Members" donut chart card with legend
   - "Income Summary" card (list of income types with amounts + Total Income row)
   - "Pair Summary (Today)" card (Pairs Completed / Pending Pairs counts + Total Pairs banner)
   - "Recent Registrations" table card (with "View All" link)
   - "Recent Withdrawals" table card (with status pills: Pending/Approved/Rejected) + "View All" link
   - "Income Overview (This Month)" — 4 small cards
   - "System Overview" — 4 small stat cards
2. **Members** (`members.html`) — replicate Image 1's base page (table, not modal) exactly:
   - 5 stat cards (Total/Active/Inactive/KYC Verified/New Members Today)
   - Toolbar: search + 4 filter dropdowns + Filter/Reset buttons, and top-right "Export Members" / "Generate EPIN" / "+ Add Member" buttons
   - Members table with columns: #, Member ID, Name (avatar+name), Joining Date, Action (View + dropdown)
   - Pagination footer
   - Bottom 3-column info strip
3. **Generate EPIN modal** — build as a reusable modal partial (`apps/admin/templates/admin/members/_generate_epin_modal.html` or similar) matching Image 1's modal exactly: Select Plan dropdown, EPIN Prefix input, Number of EPINs + Expiry Date inputs, Usage Limit dropdown, Description textarea/input, right-side "Generated EPINs Preview" panel with copyable EPIN code chips + "Copy All"/"Download CSV" buttons, right info panel "What is EPIN?" with numbered "How EPIN Works" list, green-check "Benefits" list, and amber "Note" callout. Wire it with a small vanilla JS toggle (no framework) to open/close on the "Generate EPIN" button click.
4. **All other sidebar pages** (Binary Tree, Referral Tree, Plans, EPIN Management, Income Management, Wallets, Withdrawals, Transactions, Sales & Packages, Reports, KYC Verification, Support Tickets, Notifications, Settings, Admins, System Settings): build each with the same base layout (sidebar+topbar) and a sensible placeholder content structure appropriate to its name (e.g., Binary Tree = a card with a placeholder tree visualization area; Withdrawals = a table similar to Members' table with relevant dummy columns; Settings = a form card with sections). Use realistic **dummy/static data** (hardcode sample rows directly in the templates or pass simple Python lists/dicts from the views) so every page looks fully designed, not empty.

### Django wiring requirements
- Add a `urls.py` entry per page inside `apps/admin/urls.py` (e.g. `path('admin-panel/', views.dashboard, name='admin_dashboard')`, `path('admin-panel/members/', views.members, name='admin_members')`, etc. — pick a sensible URL prefix so it doesn't collide with Django's own `/admin/` at `config/urls.py`)
- Add corresponding simple view functions in `apps/admin/views.py` that just do `return render(request, 'admin/<page>.html', {context if needed})`
- Update `apps/admin/apps.py` config name if needed, ensure `apps.admin` app has `'DIRS'`-less app-template discovery working (Django auto-discovers `apps/admin/templates/` because `APP_DIRS: True` is already set in `config/settings.py` — confirm this works with the app label `admin` not colliding with Django's built-in `django.contrib.admin` template namespace; if there's a namespace collision, use a distinct folder name like `apps/admin/templates/panel/` instead and note this clearly in your response)
- Do NOT touch `django.contrib.admin`'s own admin site — this is a **custom-built admin panel**, fully separate from `/admin/` (Django admin).

### Assets
- Use **lucide icons** (CDN: `https://unpkg.com/lucide@latest`) or inline SVG for all sidebar/topbar/card icons to match the screenshot icon style
- Use **Chart.js** via CDN for the two dashboard charts
- Keep all custom CSS minimal — prefer Tailwind utility classes; only add small custom CSS in `config/static/css/input.css` if something isn't achievable with utilities alone (e.g. custom scrollbar styling)

### Deliverable checklist
- [ ] `apps/admin/templates/admin/layout/base.html` + `_sidebar.html` + `_topbar.html`
- [ ] One template per sidebar item (18 pages total) extending the base layout
- [ ] Generate EPIN modal partial, wired to the Members page
- [ ] `apps/admin/urls.py` + `apps/admin/views.py` updated with all routes
- [ ] Sidebar active-state highlighting works correctly per page (use a `{% block active_nav %}` or context variable like `active='members'` checked in `_sidebar.html`)
- [ ] Fully responsive-safe markup (doesn't need to be perfect on mobile, but shouldn't visibly break)
- [ ] All dummy data clearly commented as placeholder for future backend integration

## PROMPT END
