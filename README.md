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
	
###导入数据静态页面

	/ocp/static/import_data.html
-	【权限】U
-	【说明】
		
	>点击导入按钮，选择需要导入的数据即可  
	>文件名写死了匹配关系，不能修改  
	>时间比较长，不要关闭，可以查看浏览器debug console

-	【参数】


###用户中心接口列表

####1.获取用户信息
	/app1/get_user
-	【权限】U
-	【说明】
-	【参数】

		{
		  "pid": "5704a81b39b0570053979274"
		}



####2.获取单条活动信息
	/app1/get_activity
-	【权限】U
-	【说明】
-	【参数】

		{
		  "objectId": "584a1bb48e450a006ab377e5"
		}

####3.获取多个活动信息列表
	/app1/get_activities
-	【权限】U
-	【说明】

		isDelete	  	删除
		isShow        	展示
		limit			单页数量
		skip			offset偏移

		数据中的admin__name 为外键中的数据，需要关注

-	【参数】

		{"isDelete":"1",
		 "isShow":"0",
		 "limit":10,
		 "skip":20
		}