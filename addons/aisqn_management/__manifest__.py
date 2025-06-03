# -*- coding: utf-8 -*-
{
    'name': "AISQN Management",

    'summary': "Centralized management module for AISQN system",

    'description': """
AISQN Management
================
Quản lý dữ liệu và nghiệp vụ liên quan đến hệ thống AISQN.
Bao gồm các chức năng như người dùng, quy trình nội bộ, báo cáo,...
    """,

    'author': "HaiManh",
    'website': "https://client.aisqn.com",

    'category': 'Management',
    'version': '0.1',

    'depends': ['base'],

    # Luôn được nạp
    'data': [
        'security/ir.model.access.csv',  # phân quyền
        'views/user_view.xml',               # view cơ bản       # menu app
        'views/templates.xml',
        'views/account_balance.xml',
        'views/customer_document_views.xml',
        'views/history_deposit_bank_views.xml', 
        'views/broker_views.xml',
        'views/trading_account_views.xml',
        'views/trading_strategy_views.xml',
        'views/customer_view.xml',           # view customer
        'views/notification_view.xml',       # view notification
        'views/wallet_view.xml',              # view wallet
        'views/wallet_transaction_view.xml',
         'views/payment_transaction_views.xml',
        'views/payment_transaction_crypto_views.xml',
        'views/payment_method_views.xml',
         'views/menu.xml',        
        # 'views/user_view.xml',
    ],

    # Dữ liệu demo (tùy chọn)
    'demo': [
        'demo/demo.xml',
    ],

    'installable': True,
    'application': True, 
    'auto_install': False,
}
