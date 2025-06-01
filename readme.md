# B1: Tải docker tại: docker.com

# B2: clone git này : 

# B3: Chạy command lênh: 
docker compose up -d (Chạy ở chế độ nền không bị dừng khi docker vẫn đang chạy)

# B4: server start tại : localhost:8068  admin/admin

# B5: Active module mới



# Tài liệu thêm:
# hướng dẫn cài đặt: https://opensourcehustle.com/blog/odoo-erp-1/odoo-windows-docker-compose-7

# các lệnh command thêm: 

# start lần đầu: 
# odoo -d odoo_db -i base --db_user=odoo --db_password=odoo --db_host=db

# update module
#  odoo -d odoo_db -u aisqn_management --db_user=odoo --db_password=odoo --db_host=db 

# update xml khi thay đổi
#  odoo -d odoo_db -u aisqn_management --dev=xml --db_user=odoo  --db_password=odoo --db_host=db 

# Tạo module mới:  docker compose exec odoo18 odoo scaffold aisqn_management /mnt/extra-addons 

