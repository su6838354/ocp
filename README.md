# ocp
使用django 构建的基础一卡通web项目

##1.接口说明	
-	1.host:139.196.243.147:3390
-	2.返回结果格式如下，code＝0表示接口正常返回，msg附带接口返回说明，data为接口返回数据
		
		{
		"code": 112,
		"data":{}
		}
			
>若data是列表数据,参数一般需要page_index(当前页码) 和 limit(每页数量)  
	
>返回值中带有

>	
			pagination":
			{
				"count": 13, // 总数update_activity
				"page_index": 2, // 当前页码
				"page_count": 2, // 页码总数
				"limit": 10 // 每页数量
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

####2.获取admin信息
	/app1/get_admins
-	【权限】U
-	【说明】
-	【参数】

		{"isDelete":"0",
		 "isShow":"1",
		 "limit":10,
		 "page_index":1
		}

####3.登录接口
	/app1/login
-	【权限】U
-	【说明】

	> 
		userRole		"Admins", "Users" 	
		cookie 中存放了 user_name, user_pid, user_role
	 
	 

-	【参数】

		{
		 "userRole": "Users",
		  "userName": "ly0522",
		  "userPwd": "123456"
		}

		or

		{
		 "userRole": "Admins",
		  "userName": "shcm_mz",
		  "userPwd": "479985"
		}

####4.获取评星数据
	/app1/get_act_join_log
-	【权限】U
-	【说明】

	> admin 支持模糊查询
		

-	【参数】

		{
		  "user": "5728a16f49830c00536952a2",
		  "admin":"5707269b2e958a0057b3e3b0",
		  "page_index": 1,
		  "limit": 10
		}


####5.获取单个管理员详情
	/app1/get_admin
-	【权限】U
-	【说明】

	>
		

-	【参数】

		{
		  "pid": "57054a7bc4c971005149399a"
		}

####6.修改用户信息
	/app1/update_user
-	【权限】U
-	【说明】

	>
		objectId 和pid不能修改，其他的都可以修改，所以不修改的情况下，原封不动传回去	

-	【参数】

		{
		  "username": "nrw1500",
		  "group":  "5704024971cfe4005dc06f9d",
		  "realname": "\u502a\u777f\u6587",
		  "objectId": "57071b61128fe10052698894",
		  "mobile": "18019161988",
		  "political": "\u56e2\u5458",
		  "checkin": [
		    "true",
		    "2016",
		    "06",
		    "06",
		    "15:39:35"
		  ],
		  "idcard": "310230200111161500",
		  "pid": "57071b601ea49300559f8ec4",
		  "isShow": "1",
		  "sex": "\u5973",
		  "job": "\u5b66\u751f",
		  "location": "5706319f8ac247004c07af53",
		  "birth": "2001-11-15T16:00:00Z",
		  "address": "\u5d07\u660e\u65b0\u5d07\u5357\u8def298-3-403",
		  "updatedAt": "2016-06-06T07:39:35Z",
		  "createdAt": "2016-04-08T02:45:53Z",
		  "flagNumber": "16056011"
		}

####7.修改管理员信息
	/app1/update_admin
-	【权限】U
-	【说明】

	>
		objectId 和pid不能修改，其他的都可以修改，所以不修改的情况下，原封不动传回去	

-	【参数】

		{
		  "username": "nrw1500",
		  "group":  "5704024971cfe4005dc06f9d",
		  "realname": "\u502a\u777f\u6587",
		  "objectId": "57071b61128fe10052698894",
		  "mobile": "18019161988",
		  "political": "\u56e2\u5458",
		  "checkin": [
		    "true",
		    "2016",
		    "06",
		    "06",
		    "15:39:35"
		  ],
		  "idcard": "310230200111161500",
		  "pid": "57071b601ea49300559f8ec4",
		  "isShow": "1",
		  "sex": "\u5973",
		  "job": "\u5b66\u751f",
		  "location": "5706319f8ac247004c07af53",
		  "birth": "2001-11-15T16:00:00Z",
		  "address": "\u5d07\u660e\u65b0\u5d07\u5357\u8def298-3-403",
		  "updatedAt": "2016-06-06T07:39:35Z",
		  "createdAt": "2016-04-08T02:45:53Z",
		  "flagNumber": "16056011"
		}

####8.查看报名信息
	/app1/get_user_checkin
-	【权限】U
-	【说明】

	>
		group 支持模糊查询，传空""的时候表示查找出所有的	

-	【参数】
		
		{
		  "checkin": true, //true 表示签到的
		  "limit": 10,
		  "page_index": 1,
		  "group": "5704024971cfe4005dc06f9d" 
		}

####9.获取user列表
	/app1/get_users
-	【权限】U
-	【说明】

	>
		下面参数都支持模糊查询
		order_by 支持user的所有参数，包括createdAt 等，支持前面加负号倒序

-	【参数】
		
		{
		  "limit": 10,
		  "page_index": 1,
		  "group": "5704024971cfe4005dc06f9d",
		  "flagNumber": "11",
		  "mobile": "",
		  "idcard": "",
		  "realname": "",
		  "username": "",
		  "order_by": "-flagNumber"
		}


####10.签到
	/app1/update_user_checkin
-	【权限】U
-	【说明】

	>

-	【参数】
		
		{
		  "user": "5729c1362e958a0069492879",
          "checkin": ["true","2016","05","12","16:02:27"]
		}



###活动接口列表

####1.获取单条活动信息
	/app1/get_activity
-	【权限】U
-	【说明】
-	【参数】

		{
		  "objectId": "584a1bb48e450a006ab377e5"
		}

####2.获取多个活动信息列表
	/app1/get_activities
-	【权限】U
-	【说明】

		isDelete	  	删除
		isShow        	展示
		limit			单页数量
		skip			offset偏移
		admin			支持模糊查询

		数据中的admin__name 为外键中的数据，需要关注

-	【参数】

		{
		"isDelete":"0",
		"isShow":"1",
 		"limit":10,
		"page_index":2,
		"admin":"57071cdda34131004cfea8fe"
		}



####3.获取参加指定活动的人数，该接口还可以用来 查询自己是否参加该活动
	/app1/get_act_registration_count
-	【权限】U
-	【说明】

	>
		查询自己是否参加过活动，指定user的pid

-	【参数】
		
		{
		 "activity": "57397f922e958a0069d68de2",
		  "user": ""
		}

####3.获取参加指定活动的人数，该接口还可以用来 查询自己是否参加该活动
	/app1/get_act_registration
-	【权限】U
-	【说明】

	>
		查询自己是否参加过活动，指定user的pid

-	【参数】
		
		{
		 "activity": "57397f922e958a0069d68de2",
		"page_index": 1,
		"limit": 10
		}



####4.参加活动
	/app1/create_act_registration
-	【权限】U
-	【说明】

	>
		

-	【参数】
		
		{
		 "admin":"57071d2ed342d300542437ea",
		 "userLocationArr":"570539afa34131004ceeb5a3",
		 "activity":"57397fbc79df5400601c42c0",
		 "userGroupArr": "57074e1e5bbb500051f10d3a",
		 "user": "570c5e0639b057006b82e0ef",
		 "isInner": false
		}

####5.评价星级
	/app1/create_act_join_log
-	【权限】U
-	【说明】

	>支持自动更新activity 的joinjum
	

-	【参数】
		
		{
		  "admin": "5707269b2e958a0057b3e3b0",
		  "userLocationArr": "",
		  "createdAt": "2016-05-16T07:04:22.430Z",
		  "star": 5,
		  "activity": "57396fc11ea4930060f40d93",
		  "isInner": true,
		  "userGroupArr": "5707269b2e958a0057b3e3b0",
		  "user":"5728a7c771cfe4006b88c9f3"
		}

####6.创建活动
	/app1/create_activity
-	【权限】U
-	【说明】

	>
		

-	【参数】
		
		{
		  "limit": "3",
		  "admin": "5704bfd371cfe4005418a086",
		  "place": "城西社区",
		  "content": "2月15日参与环境洁净日活动，清扫道路、绿化带，整理自行车棚。",
		  "title": "环境洁净日",
		  "isDelete": "0",
		  "isShow": "1",gt
		  "joinnum": 3
		}

####7.更新活动
	/app1/update_activity
-	【权限】U
-	【说明】

	>
		createdAt 和objectId 保持原来的，其他数据随便改

-	【参数】
		
		{
  		  "objectId": "57396fc11ea4930060f40d93",
		  "content": "2月15日参与环境洁净日活动，清扫道路、绿化带，整理自行车棚。",
		  "title": "环境洁净日",
		  "isDelete": "0",
		  "isShow": "1"
		}



####8.获取参加、未参加的活动
	/app1/get_activities_by_join
-	【权限】U
-	【说明】

	>
		
-	【参数】

		{
		  "user": "5729c1362e958a0069492879", //pid
		  "admin":"57071d2ed342d300542437ea", //pid
		  "page_index": 1,
		  "limit": 10,
          "join": false
		}


