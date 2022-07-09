# pochub

## 简介
`pochub` 用来记录互联网上已公开的漏洞检测poc，提供一个快速查找漏洞对应检测poc的平台

漏洞检测poc在`/app/database/pochub.db`文件中，为了方便部署使用`sqlite`数据库
## 演示demo
http://1.14.93.41:8080/

后续看情况会添加域名访问

![](./img/run.png)

## 使用方法
主页中的搜索类型有四种(见名知意):
+ text     -- poc正文内容
+ name     -- poc名
+ system   -- poc所对应的系统
+ category -- poc类别

选择你想要搜索的类型，在搜索框中输入关键字进行搜索即可

poc库的充实是另一个需要完善的方面，poc的上传分两步：多文件上传到临时poc表中 -> 整合临时poc表中的数据到正式poc表中

为什么要这么做，主要就是为了方便快速上传poc并进行分类，懒~ 具体的操作可以点击`upload`按钮进行尝试

## 自行搭建

```
git clone https://github.com/Cl0udG0d/pochub
cd pochub
docker-compose up -d 
```

## 已整理poc

## TODO
+ 存储POC
  + https://github.com/Cl0udG0d/edusrc_POC
  + https://github.com/luck-ying/Library-POC
  + https://github.com/helloexp/0day
  + https://github.com/cckuailong/reapoc
  + https://github.com/ybdt/poc-hub
  + https://github.com/coffeehb/Some-PoC-oR-ExP
  + https://github.com/mcw0/PoC
  + https://github.com/Lucifer1993/AngelSword
  + https://github.com/DawnFlame/POChouse
  + https://github.com/HacTF/poc--exp
  + https://github.com/mntn0x/POC
  + https://github.com/nomi-sec/PoC-in-GitHub
+ 整理
+ 搭建查找网站
+ 扩充支持上传的poc格式
+ ...

## 贡献
欢迎PR或者直接联系我微信来维护这个项目

## END 
 
建了一个微信的安全交流群，欢迎添加我微信备注`进群`，一起来聊天吹水哇，以及一个会发布安全相关内容的公众号，欢迎关注 :)
 
<div>
    <img  alt="GIF" src="https://springbird.oss-cn-beijing.aliyuncs.com/img/mmqrcode1632325540724.png"  width="280px" />
    <img  alt="GIF" src="https://springbird.oss-cn-beijing.aliyuncs.com/img/qrcode_for_gh_cead8e1080d6_344.jpg"  width="280px" />
</div>
