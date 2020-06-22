
<!--Author:2508334228 -->
<html>
<head>
<base href="http://192.168.123.90/douyin/">
<title>抖音无水印解析</title>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1,shrink-to-fit=no,user-scalable=0" />
<meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1" />
<meta name="renderer" content="webkit" />
<meta name="referrer" content="never">
<link rel="shortcut icon" href="favicon.ico" type="image/x-icon" />
<meta name="copyright" content="Wlan" />
<link href="bootstrap.min.css" rel="stylesheet"/>
<style>
html,body{
    font-family:微软雅黑;
}
::-webkit-scrollbar {
    width: 6px;
    background-color: transparent;
}
::-webkit-scrollbar-thumb {
    -webkit-border-radius: 8px;
    background-color: rgba(0,0,0,.16);
}
::-webkit-scrollbar-thumb:hover {
    background-color: rgba(0,0,0,.2);
}
.panel{border-radius:0px;border-color:#cfdbe2}
.panel-title {
color:#fff;
font-size:15px;
}
.addclass{
    border:3px solid #5ccdde;
}
.desc a{    
    display: inline-block;
    overflow: hidden;
    width: 200px;
    word-break: keep-all;
    white-space: nowrap;
    text-overflow: ellipsis;
    line-height: 28px;
} 
@charset "UTF-8";@font-face{font-family:toast;src:url(/public/Index/toast/fonts/toast.eot?76tjxy);src:url(/public/Index/toast/fonts/toast.eot?76tjxy#iefix) format("embedded-opentype"),url(/public/Index/toast/fonts/toast.ttf?76tjxy) format("truetype"),url(/public/Index/toast/fonts/toast.woff?76tjxy) format("woff"),url(/public/Index/toast/fonts/toast.svg?76tjxy#toast) format("svg");font-weight:400;font-style:normal}i.toast-icon{font-family:toast!important;speak:none;font-style:normal;font-weight:400;font-variant:normal;text-transform:none;line-height:1;-webkit-font-smoothing:antialiased;-moz-osx-font-smoothing:grayscale}.toast-icon-error:before{content:""}.toast-icon-info:before{content:""}.toast-icon-notice:before{content:""}.toast-icon-success:before{content:""}.toast-icon-warning:before{content:""}.toast-item-wrapper{min-width:250px;padding:10px;box-sizing:border-box;color:#fff;overflow:hidden;-webkit-user-select:none;-moz-user-select:none;-ms-user-select:none;user-select:none}.toast-item-wrapper i.toast-icon{position:absolute;top:12px;left:0;width:50px;text-align:center;vertical-align:middle;font-size:2rem}.toast-item-wrapper .toast-close{font-size:1.2rem;position:absolute;top:0;right:0;width:20px;text-align:center;cursor:pointer}.toast-item-wrapper.success{background-color:#29ab9f;border:1px solid #1a9581}.toast-item-wrapper.error{background-color:#ff7946;border:1px solid #f35818}.toast-item-wrapper.warning{background-color:#fff1c0;border:1px solid #f0c948;color:#333}.toast-item-wrapper.notice{background-color:#48a9f8;border:1px solid #208ce4}.toast-item-wrapper.info{background-color:#7f97a3;border:1px solid #6b8699}.toast-item-wrapper.toast-top-left{left:20px;top:20px}.toast-item-wrapper.toast-top-right{right:20px;top:20px}.toast-item-wrapper.toast-top-center{margin:0 auto;top:20px}.toast-item-wrapper.toast-bottom-left{left:20px;bottom:20px}.toast-item-wrapper.toast-bottom-right{right:20px;bottom:20px}.toast-item-wrapper.toast-bottom-center{margin:0 auto;bottom:20px}.toast-item-wrapper.fullscreen{left:20px;right:20px;width:calc(100% - 40px)}.toast-item-wrapper p{margin:0}.toast-item-wrapper .toast-message{font-size:.87rem}.toast-item-wrapper .toast-progress{width:0;height:3px;background-color:rgba(0,0,0,.5);position:absolute;bottom:0;right:0}.toast-item-wrapper.rtl{direction:rtl;text-align:right}.toast-item-wrapper.rtl i.toast-icon{left:auto;right:0}.toast-item-wrapper.rtl .toast-close{right:auto;left:0}.toast-item-wrapper.rtl p{text-align:right}.toast-item-wrapper.rtl .toast-progress{left:auto;right:0}
</style>

</head>
<body style="background:url(bj.png) fixed">
<script src="jquery-2.1.0.js"></script>
<div class="container" style="margin-top: 5px;"> 
<div class="col-sm-10 center-block" style="float: none;">
<div class="panel">
<div class="panel-heading">
<h3 class="panel-title">抖音无水印解析视频</h3>
</div>
<div class="panel-body">
<div class="form-group">
<div class="input-group">
<span class="input-group-addon">抖音分享链接</span>
<input type="text" id="url" class="form-control" placeholder="请粘贴抖音分享链接在此处">
<input type="text" id="page" class="form-control" placeholder="页数 (默认为1，页数越大，解析所需时间越长，请耐心等待...)">
</div>
</div>
<button class="btn btn-info btn-block" id="submit" >立即解析</button>
<button class="btn btn-info btn-block" id="submit1" onclick="download_all()">一键下载</button>
<!--<button class="btn btn-info btn-block" id="submit2" onclick="xl_download()">迅雷批量下载（推荐）</button>-->
<font color="red" id="return"></font>
<div class="row" id="list" style="display:none">
</div>
</div>
</div>
</div>
</div>
<script src="layui.all.js"></script>
<script src="http://danml.com/js/download2.js"></script>
<script>

/*
    * 使用download.js 强制浏览器下载图片、视频等文件
    * @param {any} url url链接地址
    * @param {any} strFileName 文件名
    * @param {any} strMimeType 文件类型
    * dzl
    * 2020年5月8日
     */
    function downloadfile(url, strFileName, strMimeType) {
      var xmlHttp = null;
      if (window.ActiveXObject) {
        // IE6, IE5 浏览器执行代码
        xmlHttp = new ActiveXObject("Microsoft.XMLHTTP");
      } else if (window.XMLHttpRequest) {
        // IE7+, Firefox, Chrome, Opera, Safari 浏览器执行代码
        xmlHttp = new XMLHttpRequest();
      }
      //2.如果实例化成功，就调用open（）方法：
      if (xmlHttp != null) {
        xmlHttp.open("get", url, true);
        xmlHttp.responseType = 'blob';//关键
        xmlHttp.send();
        xmlHttp.onreadystatechange = doResult; //设置回调函数
      }
      function doResult() {
        if (xmlHttp.readyState == 4) { //4表示执行完成
          if (xmlHttp.status == 200) { //200表示执行成功
            download(xmlHttp.response, strFileName, strMimeType);
          }
        }
      }
    }
/*
 * 根据文件名的尾缀 返回文件类型
 * @param {any} fileName 文件名
 * dzl
 * 2020年5月9日
 */
function getFileType(fileName) {
  // 后缀获取
  let suffix = '';
  // 获取类型结果
  let result = '';
  try {
    const flieArr = fileName.split('.');
    suffix = flieArr[flieArr.length - 1];
  } catch (err) {
    suffix = '';
  }
  // fileName无后缀返回 false
  if (!suffix) { return false; }
  suffix = suffix.toLocaleLowerCase();
  // 图片格式
  const imglist = ['png', 'jpg', 'jpeg', 'bmp', 'gif'];
  // 进行图片匹配
  result = imglist.find(item => item === suffix);
  if (result) {
    return 'image';
  }
  // 匹配txt
  const txtlist = ['txt'];
  result = txtlist.find(item => item === suffix);
  if (result) {
    return 'txt';
  }
  // 匹配 excel
  const excelist = ['xls', 'xlsx'];
  result = excelist.find(item => item === suffix);
  if (result) {
    return 'excel';
  }
  // 匹配 word
  const wordlist = ['doc', 'docx'];
  result = wordlist.find(item => item === suffix);
  if (result) {
    return 'word';
  }
  // 匹配 pdf
  const pdflist = ['pdf'];
  result = pdflist.find(item => item === suffix);
  if (result) {
    return 'pdf';
  }
  // 匹配 ppt
  const pptlist = ['ppt', 'pptx'];
  result = pptlist.find(item => item === suffix);
  if (result) {
    return 'ppt';
  }
  // 匹配 视频
  const videolist = ['mp4', 'm2v', 'mkv', 'rmvb', 'wmv', 'avi', 'flv', 'mov', 'm4v'];
  result = videolist.find(item => item === suffix);
  if (result) {
    return 'video';
  }
  // 匹配 音频
  const radiolist = ['mp3', 'wav', 'wmv'];
  result = radiolist.find(item => item === suffix);
  if (result) {
    return 'radio';
  }
  // 其他 文件类型
  return 'other';
}


$("#submit").click(function(){
    playaddress_Array=new Array();
    cover_Array=new Array();
    desc_Array=new Array();
    max_cursor = 0;
    has_more = true;
    page = 1;

    if(!$("#url").val() || $("#url").val().indexOf("http")==-1){
        return alert('请先输入抖音分享链接');
    }
    if(!$("#page").val()){
        page = 1;
    }else{page = $("#page").val() * 1;}
    

    $("#list").show().empty().html('<hr>');
    $.ajax({
        type:"post",
        url:"get_douyin.php?action=getjs",
        data:{
            userid:$("#url").val()
        },
        dataType:"script",
        success:function(){
            page = page - 1;
            $.ajax({
                type:"post",
                url:"get_douyin.php?action=getlist",
                data:{
                    uid:getuid(),dytk:getdytk(),signature:generateSignature(getuid())
                },
                dataType:"json",
                success:function(data){
                    //$("#return").html(data.url);
                    max_cursor = data.max_cursor;
                    has_more = data.has_more;
                    $.each(data.data,function(index,res){
                        //$("#list").append('<div class="col-xs-6 col-sm-3 col-md-3 "><a href="javascript:download(\''+res.aweme_id+'\')"><div class="thumbnail" style="height:300px;"><center><img src="'+res.video.cover.url_list[0]+'" width="100%" height="100%" style="border-radius: 10px;display: table-cell;vertical-align: middle;text-align: center;"></center></div></a></div>');
                        cover_Array.push(res.video.cover.url_list[0]);
                        desc_Array.push(res.desc);
                        $.ajax({
                            type:"post",
                            url:"get_douyin.php?action=get_palyaddress",
                            async: false,
                            data:{
                                url:res.video.play_addr.url_list[0],
                            },
                            dataType:"json",
                            success:function(data){
                                playaddress_Array.push(data.result);
                            },
                            error:function(msg){
                                console.log(msg);
                                playaddress_Array.push(res.video.play_addr.url_list[0]);
                            }
                        });
                    });
                    ////第二页
                    while (has_more && page > 0){
                        page = page - 1;
                        $.ajax({
                            type:"post",
                            url:"get_douyin.php?action=getlist2",
                            async: false,
                            data:{
                                uid:getuid(),dytk:getdytk(),signature:generateSignature(getuid()),max_cursor:max_cursor
                            },
                            dataType:"json",
                            success:function(data){
                                
                                max_cursor = data.max_cursor;
                                has_more = data.has_more;
                                $.each(data.data,function(index,res){
                                    cover_Array.push(res.video.cover.url_list[0]);
                                    desc_Array.push(res.desc);
                                    $.ajax({
                                        type:"post",
                                        url:"get_douyin.php?action=get_palyaddress",
                                        async: false,
                                        data:{
                                            url:res.video.play_addr.url_list[0],
                                        },
                                        dataType:"json",
                                        success:function(data){
                                            playaddress_Array.push(data.result);
                                        },
                                        error:function(msg){
                                            console.log(msg);
                                            playaddress_Array.push(res.video.play_addr.url_list[0]);
                                        }
                                    });
                                });
                            }
                        });
                    }


                    for (x in playaddress_Array){
                        $("#list").append('<div class="col-xs-6 col-sm-3 col-md-3 "> <div class="" style="height:300px;"> <a href= "'+playaddress_Array[x]+'"  target="_black"><center><img src="'+cover_Array[x]+'" width="100%" height="100%" style="border-radius: 10px;display: table-cell;vertical-align: middle;text-align: center;"></center></a> </div><div class="desc"><a> '+desc_Array[x]+' </a></div> <div style="margin-bottom:30px;margin-top:8px;" class="col-xs-6 col-sm-6 col-md-6 "><a href= "'+playaddress_Array[x]+'"  target="_black" class="btn btn-info btn-block" id="submit1">播放</a></div><div style="margin-bottom:30px;margin-top:8px;" class="col-xs-6 col-sm-6 col-md-6 name="button"><a class="btn btn-info btn-block" id="submit2"  url= "'+playaddress_Array[x]+'" name="'+desc_Array[x]+'">下载</a></div> </div>');
                    };
                    
                }
            });
        },
        error:function(msg){
            console.log(msg);
            layer.alert('Status：'+msg.status+'，StatusText：'+msg.statusText);
        }
    });
});



$("#list").on('click','#submit2',function(){
    var name = $(this).attr('name');
    var url = $(this).attr('url');
    name = name.replace(/[~"!?\|/^*%$@<>+-=:]/g,"")+".mp4";
    //console.log(name,url);
    downloadfile(url,name,getFileType(name));
});


function download_all() {
    if(playaddress_Array.length < 1){
       return alert('请先输入抖音分享链接进行解析');
    }
    for (x in playaddress_Array){
        var name = desc_Array[x];
        var url = playaddress_Array[x];
        name = name.replace(/[~"!?\|/^*%$@<>+-=:]/g,"")+".mp4";
        //console.log(name,url);
        downloadfile(url,name,getFileType(name));
    }
}

function xl_download() {
    if(playaddress_Array.length < 1){
       return alert('请先输入抖音分享链接进行解析');
    }
    var name = getuid() + ".txt";
    for (x in playaddress_Array){
        var url = playaddress_Array[x];
        //downloadfile(url,name,getFileType(name));
    }
}

</script>
</body>
</html>
