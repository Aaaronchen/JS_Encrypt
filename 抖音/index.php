

<html>
<head>
<base href="http://localhost/douyin/">
<title>蔚蓝抖音无水印解析</title>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1,shrink-to-fit=no,user-scalable=0" />
<meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1" />
<meta name="renderer" content="webkit" />
<link rel="shortcut icon" href="favicon.ico" type="image/x-icon" />
<meta name="copyright" content="Wlan" />
<link href="https://douyincdn.wlansq.cn/public/Index/bootstrap/css/bootstrap.min.css?date=20190705" rel="stylesheet"/>
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
@charset "UTF-8";@font-face{font-family:toast;src:url(/public/Index/toast/fonts/toast.eot?76tjxy);src:url(/public/Index/toast/fonts/toast.eot?76tjxy#iefix) format("embedded-opentype"),url(/public/Index/toast/fonts/toast.ttf?76tjxy) format("truetype"),url(/public/Index/toast/fonts/toast.woff?76tjxy) format("woff"),url(/public/Index/toast/fonts/toast.svg?76tjxy#toast) format("svg");font-weight:400;font-style:normal}i.toast-icon{font-family:toast!important;speak:none;font-style:normal;font-weight:400;font-variant:normal;text-transform:none;line-height:1;-webkit-font-smoothing:antialiased;-moz-osx-font-smoothing:grayscale}.toast-icon-error:before{content:""}.toast-icon-info:before{content:""}.toast-icon-notice:before{content:""}.toast-icon-success:before{content:""}.toast-icon-warning:before{content:""}.toast-item-wrapper{min-width:250px;padding:10px;box-sizing:border-box;color:#fff;overflow:hidden;-webkit-user-select:none;-moz-user-select:none;-ms-user-select:none;user-select:none}.toast-item-wrapper i.toast-icon{position:absolute;top:12px;left:0;width:50px;text-align:center;vertical-align:middle;font-size:2rem}.toast-item-wrapper .toast-close{font-size:1.2rem;position:absolute;top:0;right:0;width:20px;text-align:center;cursor:pointer}.toast-item-wrapper.success{background-color:#29ab9f;border:1px solid #1a9581}.toast-item-wrapper.error{background-color:#ff7946;border:1px solid #f35818}.toast-item-wrapper.warning{background-color:#fff1c0;border:1px solid #f0c948;color:#333}.toast-item-wrapper.notice{background-color:#48a9f8;border:1px solid #208ce4}.toast-item-wrapper.info{background-color:#7f97a3;border:1px solid #6b8699}.toast-item-wrapper.toast-top-left{left:20px;top:20px}.toast-item-wrapper.toast-top-right{right:20px;top:20px}.toast-item-wrapper.toast-top-center{margin:0 auto;top:20px}.toast-item-wrapper.toast-bottom-left{left:20px;bottom:20px}.toast-item-wrapper.toast-bottom-right{right:20px;bottom:20px}.toast-item-wrapper.toast-bottom-center{margin:0 auto;bottom:20px}.toast-item-wrapper.fullscreen{left:20px;right:20px;width:calc(100% - 40px)}.toast-item-wrapper p{margin:0}.toast-item-wrapper .toast-message{font-size:.87rem}.toast-item-wrapper .toast-progress{width:0;height:3px;background-color:rgba(0,0,0,.5);position:absolute;bottom:0;right:0}.toast-item-wrapper.rtl{direction:rtl;text-align:right}.toast-item-wrapper.rtl i.toast-icon{left:auto;right:0}.toast-item-wrapper.rtl .toast-close{right:auto;left:0}.toast-item-wrapper.rtl p{text-align:right}.toast-item-wrapper.rtl .toast-progress{left:auto;right:0}
</style>

</head>
<body style="background:url(https://douyincdn.wlansq.cn/public/Index/images/bj.png) fixed">
<script src="https://douyincdn.wlansq.cn/public/Index/js/jquery.min.js"></script>
<div class="container" style="margin-top: 5px;"> 
<div class="col-sm-10 center-block" style="float: none;">
<div class="panel">
<div class="panel-heading">
<h3 class="panel-title">蔚蓝抖音无水印解析视频</h3>
</div>
<div class="panel-body">
<div class="form-group">
<div class="input-group">
<span class="input-group-addon">抖音分享链接</span>
<input type="text" id="url" class="form-control" placeholder="请粘贴抖音分享链接在此处">
</div>
</div>
<a class="btn btn-info btn-block" id="submit">立即解析</a>
<font color="red" id="return"></font>
<div class="row" id="list" style="display:none">
</div>
</div>
</div>
</div>
</div>
<script src="https://douyincdn.wlansq.cn/public/Index/layui/layui.all.js"></script>
<script>
function download(uri){
    $.ajax({
        type:"post",
        url:"//douyin.wlansq.cn/get_douyin.php?action=getvideo",
        data:{
            uri:uri
        },
        dataType:"json",
        success:function(data){
            if(data.code==0){
                window.location.href=data.video_url;
            }
        }
    });
}
$("#submit").click(function(){
    if(!$("#url").val() || $("#url").val().indexOf("http")==-1){
        return layer.alert('请先输入抖音分享链接');
    }

    $("#list").show().empty().html('<hr>');
    $.ajax({
        type:"post",
        url:"get_douyin.php?action=getjs",
        data:{
            userid:$("#url").val()
        },
        dataType:"script",
        success:function(){
            $.ajax({
                type:"post",
                url:"get_douyin.php?action=getlist",
                data:{
                    uid:getuid(),dytk:getdytk(),signature:generateSignature(getuid())
                },
                dataType:"json",
                success:function(data){
                    $("#return").html(data.url);
                    $.each(data.data,function(index,res){
                        $("#list").append('<div class="col-xs-6 col-sm-3 col-md-3 "><a href="javascript:download(\''+res.aweme_id+'\')"><div class="thumbnail" style="height:300px;"><center><img src="'+res.video.cover.url_list[0]+'" width="100%" height="100%" style="border-radius: 10px;display: table-cell;vertical-align: middle;text-align: center;"></center></div></a></div>');
                    });
                }
            });
        },
        error:function(msg){
            console.log(msg);
            layer.alert('Status：'+msg.status+'，StatusText：'+msg.statusText);
        }
    });
});
</script>
</body>
</html>