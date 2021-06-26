flask-priceapi
用Python的flask框架写的一个蔬果价格查询api
利用定时任务每天爬取北京市是蔬果价格存到MongoDB中
接口格式/vegetable?name= &date=
/fruit?kind= &date=
利用get方法，查询字符串传参
日期非必须参数如果不传默认今天，name或kind不传默认查询今天全部数据
蔬菜商品名与俗称大多类似采用商品名作为查询参数
水果一般不习惯称呼商品名，所以使用kind参数（类别）来筛选，匹配中还用到了正则规则，例如传入芒果将会查找出所有芒果类的价格，大台农小台农青芒等。
