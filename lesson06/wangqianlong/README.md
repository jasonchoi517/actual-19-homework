﻿###作业6 用户管理系统说明：

界面修改为：

-----------------------------------
认证成功！欢迎使用本用户管理系统！
您可以执行以下操作：
    1. 添加用户(add)
    2. 删除用户(delete)
    3. 更新用户(update)
    4. 搜索用户(query)
    5. 查询用户并导出xls (export)
    6. 退出登录（exit）
-----------------------------------

①修改为token认证：0075844e71051dd19138ecf0e54179e1ad38601c
  
  3次失败锁定，锁定时间30s。

②修改数据存储方式为mysql数据库；连接数据库的配置文件conf2.ini，本系统在数据库'python19'，

表'USERINFO'存在的情况下执行。


③锁文件/xls文件/记录log文件路径都在conf.ini中。实现数据库文件导出到excel文件。


④hash加密算法函数未使用，不知道在哪里使用？？？？


⑤运行main.py，（相关包文件有DB.py、useradmin.py、utils.py）具体自测结果见test文档.....

