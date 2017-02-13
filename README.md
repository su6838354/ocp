# ocp
使用django 构建的基础一卡通web项目

##1.接口说明	
-	1.host:139.196.243.147:3390
-	2.返回结果格式如下，code＝0表示接口正常返回，msg附带接口返回说明，data为接口返回数据
		
		{
		"code": 112,
		"data":{}
		}
-	3.权限，cookie等其他功能后续开启，目前服务启动采用python自带的socket和wsgiref，比较脆弱，


##2.返回状态说明
	状态码									含义
	200 OK								GET请求成功
	202 ACCEPTED						POST请求成功
	401 FORBIDDEN						token无效,被禁止访问
	400 BAD REQUEST						POST请求失败或GET请求参数有误
	403 FORBIDDEN						token无效,被禁止访问
	404 NOT FOUND						请求的资源不存在，路由出差
	500 INTERNAL SERVER ERROR			内部错误
	



###用户中心接口列表

####1.获取用户信息
	/app1/get_user
-	【权限】U
-	【说明】
-	【参数】

		{
		  "pid": "5704a81b39b0570053979274"
		}