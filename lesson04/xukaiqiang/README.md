## userdemo

此项目是python构建的管理员演示系统,具有一下功能:

 - 管理员登陆验证
 - 添加用户信息
 - 修改用户信息
 - 删除用户信息
 - 保存用户信息
 - 退出登陆

## 用户数据类型 

### 管理员账号密码:

user:admin

password:123456

### 数据实例:

```
users = [
    {'name' : 'monkey1', 'age':20, 'tel':'132xxx', 'address':'beijing', 'id':1},
    {'name' : 'monkey2', 'age':20, 'tel':'132xxx', 'address':'beijing', 'id':2},
    {'name' : 'monkey3', 'age':20, 'tel':'132xxx', 'address':'beijing', 'id':3},
]

```

## 项目运行

```
git clone https://github.com/xxxxx/usersysdemo.git

python usersysdemo.py

```

## 效果演示

- 管理员登陆

	![login](https://raw.githubusercontent.com/iteemo/images/master/lesson04/login.png)

- 添加用户

	![adduser](https://raw.githubusercontent.com/iteemo/images/master/lesson04/adduser.png)

- 查询用户

	![queryuser](https://raw.githubusercontent.com/iteemo/images/master/lesson04/query.png)

- 删除用户

	![adduser](https://raw.githubusercontent.com/iteemo/images/master/lesson04/del.png)

- 保存用户

	![adduser](https://raw.githubusercontent.com/iteemo/images/master/lesson04/save.png)

- 锁定用户

	![adduser](https://raw.githubusercontent.com/iteemo/images/master/lesson04/lock.png)