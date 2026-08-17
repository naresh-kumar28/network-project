from django.urls import path
from . import views

urlpatterns = [
    path('admin-panel/', views.dashboard, name='admin_dashboard'),
    path('admin-panel/members/', views.members, name='admin_members'),
    path('admin-panel/binary-tree/', views.binary_tree, name='admin_binary_tree'),
    path('admin-panel/referral-tree/', views.referral_tree, name='admin_referral_tree'),
    path('admin-panel/plans/', views.plans, name='admin_plans'),
    path('admin-panel/epin/', views.epin, name='admin_epin'),
    path('admin-panel/income/', views.income, name='admin_income'),
    path('admin-panel/wallets/', views.wallets, name='admin_wallets'),
    path('admin-panel/withdrawals/', views.withdrawals, name='admin_withdrawals'),
    path('admin-panel/transactions/', views.transactions, name='admin_transactions'),
    path('admin-panel/sales/', views.sales, name='admin_sales'),
    path('admin-panel/reports/', views.reports, name='admin_reports'),
    path('admin-panel/kyc/', views.kyc, name='admin_kyc'),
    path('admin-panel/tickets/', views.tickets, name='admin_tickets'),
    path('admin-panel/notifications/', views.notifications, name='admin_notifications'),
    path('admin-panel/settings/', views.settings, name='admin_settings'),
    path('admin-panel/admins/', views.admins, name='admin_admins'),
    path('admin-panel/system-settings/', views.system_settings, name='admin_system_settings'),
]