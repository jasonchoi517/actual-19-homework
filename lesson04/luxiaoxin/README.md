## 管理员账号密码
 - 账号：admin
 - 密码：51@reboot

-------------------------------------
## 本周作业完成内容
- 重新做了一版新的，不基于上一版

- 使用模块time,getpass和json

- 将各功能模块使用函数实现

- 将管理员用户锁定、登录、操作（显示、添加、更改、查询、删除、保存和退出）功能分别编写为函数

-------------------------------------
## 基本功能:
- 系统基本功能：管理员用户锁定、登录、操作（显示、添加、更改、查询、删除、保存和退出）

- 使用列表分页方式进行用户信息打印，在用户列表显示、用户添加、修改和查询均调用打印函数格式化打印用户信息

- 管理员账户三次锁定，解锁时间为24小时

---------------------------------------
## 系统特色:
- 不需要用户建立用户信息文件和锁定信息文件，第一次使用系统可自动检查是否有信息文件，如果没有自动建立

- 能复用的功能，例如打印、保存均抽象出来单独编写函数