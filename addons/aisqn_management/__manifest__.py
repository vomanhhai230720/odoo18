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
        #'security/ir.model.access.csv',  # phân quyền
        'views/views.xml',               # view cơ bản
        'views/menu.xml',                # menu app
        'views/templates.xml',        
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
