
import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from src.models import School,Classes
# AttributeError: Can't get attribute 'School' on <module '__main__' from 'admin.py'>
# https://www.cnblogs.com/zuoan104/p/11422483.html
# https://www.cnblogs.com/wuliwawa/p/9655672.html

from src.admin_service import main

if __name__ == '__main__':
    main()