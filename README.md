# ocp
使用django 构建的基础一卡通web项目

>使用说明：

	 执行 pip install -r requirement.txt 安装依赖包		  
	 执行run.sh,本地接口地址换成 127.0.0.1:3390

## 1.接口说明	
-	1.host:139.196.243.147:3390
-	2.返回结果格式如下，code＝0表示接口正常返回，msg附带接口返回说明，data为接口返回数据
		get_activities_by_join
		{political
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
		
-	3.权限，cookie等其他功能后续开启，目前服务启动采用python自带的socket和wsgiref，比较脆弱
-	4.部分字段有isShow的，传入isShow='-1'则查询匹配的，不传则查询isShow != '-1'的


## 2.返回状态说明
	状态码									含义
	200 OK								GET请求成功
	202 ACCEPTED						POST请求成功
	401 FORBIDDEN						token无效,被禁止访问
	400 BAD REQUEST						POST请求失败或GET请求参数有误
	403 FORBIDDEN						token无效,被禁止访问
	404 NOT FOUND						请求的资源不存在，路由出差
	500 INTERNAL SERVER ERROR			内部错误
	
### 导入数据静态页面

	/ocp/static/import_data.html
-	【权限】U
-	【说明】
		
	>点击导入按钮，选择需要导入的数据即可  
	>文件名写死了匹配关系，不能修改  
	>时间比较长，不要关闭，可以查看浏览器debug console

-	【参数】


### 用户中心接口列表

#### 1.获取用户信息
	/app1/get_user
-	【权限】U
-	【说明】
-	【参数】

		{
		  "pid": "5704a81b39b0570053979274"
		}

#### 2.获取admin信息
	/app1/get_admins
-	【权限】U
-	【说明】
	> type  group  loaction
	> username和name 支持模糊查询
	> parentId 无该参数时，不为限制条件
	> group_type 无参数时，不为限制条件

-	【参数】

		{"isDelete":"0",
		 "isShow":"1",
		 "limit":10,
		 "page_index":1,
		"isShow": "1",
		"type": "group",
		"username": "",
		"name": "",
		"parentId": "",
		"group_type": 1
		}

#### 3.登录接口
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


#### 5.获取单个管理员详情
	/app1/get_admin
-	【权限】U
-	【说明】

	>
		

-	【参数】

		{
		  "pid": "57054a7bc4c971005149399a"
		}

#### 6.修改用户信息
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

#### 7.修改单位组织信息
	/app1/update_admin
-	【权限】U
-	【说明】

	>和pid不能修改，其他的都可以修改，所以不修改的情况下，原封不动传回去	  
	>group_type :
	>
		0		默认值   
	    1  		乡镇单位
		2		乡镇下属单位

-	【参数】

		{
		  "pid": "57071b601ea49300559f8ec4",
		  "address": "\u5d07\u660e\u65b0\u5d07\u5357\u8def298-3-403",
		  "person": "",
		  "name": "\u502a\u777f\u6587",
		  "username": "nrw1500",
		  "tel": "111"
		  "isShow": "1",
		  "mobile": "18019161988",
		  "flagNumber": "16056011",
		  "group_type": 0,
		  "parentId": "98998888"
		}

#### 8.查看报名信息
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
		  "group": "5704024971cfe4005dc06f9d",
		  "isShow": "1"
		}

#### 9.获取user列表
	/app1/get_users
-	【权限】U
-	【说明】

	>
		下面参数都支持模糊查询
		order_by 支持user的所有参数，包括createdAt 等，支持前面加负号倒序
		checkin 无该参数则不作为条件，false or true

-	【参数】
		
		{
		  "limit": 10,
		  "page_index": 1,
		  "political": "dang",
		  "group": "5704024971cfe4005dc06f9d",
		  "location": "5704024971cfe4005dc06f9d",
		  "flagNumber": "11",
		  "mobile": "",
		  "idcard": "",
		  "realname": "",
		  "username": "",
		  "order_by": "-flagNumber",
	   	  "isShow": "1",
		  "group__name": "ss",
		  "location__name": "ss",
		  "checkin": false,
		  "group_type": "admin" // "admin"和原来一样  "all"的时候，一起查出下属的，默认admin
		}


#### 10.签到
	/app1/update_user_checkin
-	【权限】U
-	【说明】

	>

-	【参数】
		
		{
		  "user": "5729c1362e958a0069492879",
          "checkin": ["true","2016","05","12","16:02:27"]
		}


#### 11.创建用户
	/app1/create_user_admin
-	【权限】U
-	【说明】

	>group_type 查看其他接口定义

-	【参数】
	> user
		
		 {
		  "password": "123456",
		  "username": "suyuan",
		  "userRole": "Users",
		  "isShow": "1",
		  "username": "suyuan",
		  "realname": "suyuan",
		  "sex": "",
		  "idcard": "",
		  "mobile": "",
		  "birth": "2016-04-06T06:09:31.065Z",
		  "flagNumber": "1",
		  "political": "1"
		  "group": "12334",
		  "location": "111111"
		}
	
	>admin
			
		 {
		  "password": "123456",
		  "username": "suyuan",
		  "userRole": "Admins",
		  "isShow": '1',
          "pwd": "123456",
          "username": "sy",
          "name": "sy",
          "type": "11",
          "person": "11",
          "address": "12",
          "mobile": "11",
          "tel": "1",
		  "group_type": 0,
		  "parentId": "98998888" //自己的admin_pid
        }



### 活动接口列表

#### 1.获取单条活动信息
	/app1/get_activity
-	【权限】U
-	【说明】
-	【参数】

		{
		  "objectId": "584a1bb48e450a006ab377e5"
		}

#### 2.获取多个活动信息列表
	/app1/get_activities
-	【权限】U
-	【说明】

		isDelete	  	删除
		isShow        	展示
		limit			单页数量
		skip			offset偏移
		admin			支持模糊查询
		group_type			查询方式，all为查出自己包括子组织；admin为查询指定admin的，不传的时候，默认值为admin
        status          all 全部数据，pass 通过的数据
        
		数据中的admin__name 为外键中的数据，需要关注

-	【参数】

		{
		"isDelete":"0",
		"isShow":"1",
		"limit":10,
		"page_index":2,
		"admin":"57071cdda34131004cfea8fe",
	    "isShow": "-1",
		"group_type": "all", // all  admin
		"status": "all" // all pass fail wait
		}



#### 3.获取参加指定活动的人数，该接口还可以用来 查询自己是否参加该活动
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

#### 4.获取参加指定活动的人
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



#### 5.参加活动
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

#### 6.评价星级
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

#### 7.创建活动
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
		  "isShow": "1",
		  "joinnum": 3,
		  "tag_ids": [1, 2, 3]
		}

#### 8.更新活动
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
		  "isShow": "1",
		  "place": "",
		  "limit": "",
          "tag_ids": [1,2,3]
		}



#### 9.获取参加、未参加的活动
	/app1/get_activities_by_join
-	【权限】U
-	【说明】

	>isShow "-1" 所有值，"0" 只有"0"的值，"1"只有"1"的值
	>isDelete "0" 或者"1" 
		
-	【参数】

		{
		  "user": "5729c1362e958a0069492879", //pid
		  "admin":"57071d2ed342d300542437ea", //pid
		  "page_index": 1,
		  "limit": 10,
          "join": false,
		  "isShow": "1",
		  "isDelete": "0",
		}


#### 10.获取评星数据
	/app1/get_act_join_log
-	【权限】U
-	【说明】

	> admin 支持模糊查询
	> user  支持模糊查询
	> activity 支持模糊查询		

-	【参数】

		{
		  "user": "5728a16f49830c00536952a2",
		  "admin":"5707269b2e958a0057b3e3b0",
		  "activity": "",
		  "page_index": 1,
		  "limit": 10
		}

#### 11.更新附加分
	/app1/update_act_join_log_extra
-	【权限】U
-	【说明】
	

-	【参数】

		{
		  "objectId": "3e58917cf6ae11e6aff70016",
		  "extra":10
		}


### Tag接口列表

#### 1.添加更新Tag
	/app1/add_update_tag
-	【权限】U
-	【说明】

	>id=0的时候为添加，否则为更新

-	【参数】

		{
		  "id": 1,
		  "txt": "111nihao苏"
		}


#### 2.添加更新Tag和activity对应
	/app1/add_update_activity2tag
-	【权限】U
-	【说明】

	>id=0的时候为添加，否则为更新

-	【参数】

		{
		  "id": 1,
		  "tag_id": 1,
		  "activity_id": "11111111111111"
		}

#### 3.删除Tag和activity对应
	/app1/delete_activity2tag
-	【权限】U
-	【说明】

-	【参数】

		{
		  "id": 1
		}


#### 4.获取tags
	/app1/get_tags
-	【权限】U
-	【说明】
	> txt支持模糊查询
	> isDelete 不传递时，默认为0

-	【参数】

		{
		"txt": "n",
		"page_index": 1,
		"limit": 10,
		"isDelete": 0
		}

#### 5.删除tags
	/app1/delete_tags
-	【权限】U
-	【说明】

-	【参数】

		{
		"tag_ids": [1, 2, 3]
		}


### 新增接口列表

#### 1.删除admin
	/app1/delete_admin
-	【权限】U
-	【说明】

-	【参数】

		{
		"pid": "1111111111111"
		}

#### 2.删除user
	/app1/delete_user
-	【权限】U
-	【说明】

-	【参数】

		{
		"pid": "1111111111111"
		}

#### 3.更新活动状态
	/app1/update_activity_status
-	【权限】U
-	【说明】

-	【参数】

		{
		"objectId": "1111111111111"，
		"status": "pass" // "fail",""pass","wait"
		}
