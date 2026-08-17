from django.shortcuts import render

def dashboard(request):
    return render(request, 'panel/dashboard.html', {'active_page': 'dashboard'})

def members(request):
    return render(request, 'panel/members.html', {'active_page': 'members'})

def binary_tree(request):
    return render(request, 'panel/binary_tree.html', {'active_page': 'binary_tree'})

def referral_tree(request):
    return render(request, 'panel/referral_tree.html', {'active_page': 'referral_tree'})

def plans(request):
    return render(request, 'panel/plans.html', {'active_page': 'plans'})

def epin(request):
    return render(request, 'panel/epin.html', {'active_page': 'epin'})

def income(request):
    return render(request, 'panel/income.html', {'active_page': 'income'})

def wallets(request):
    return render(request, 'panel/wallets.html', {'active_page': 'wallets'})

def withdrawals(request):
    return render(request, 'panel/withdrawals.html', {'active_page': 'withdrawals'})

def transactions(request):
    return render(request, 'panel/transactions.html', {'active_page': 'transactions'})

def sales(request):
    return render(request, 'panel/sales.html', {'active_page': 'sales'})

def reports(request):
    return render(request, 'panel/reports.html', {'active_page': 'reports'})

def kyc(request):
    return render(request, 'panel/kyc.html', {'active_page': 'kyc'})

def tickets(request):
    return render(request, 'panel/tickets.html', {'active_page': 'tickets'})

def notifications(request):
    return render(request, 'panel/notifications.html', {'active_page': 'notifications'})

def settings(request):
    return render(request, 'panel/settings.html', {'active_page': 'settings'})

def admins(request):
    return render(request, 'panel/admins.html', {'active_page': 'admins'})

def system_settings(request):
    return render(request, 'panel/system_settings.html', {'active_page': 'system_settings'})
