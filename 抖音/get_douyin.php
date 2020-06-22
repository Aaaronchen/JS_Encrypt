<?php

function get_curl($url,$post=0,$referer=0,$cookie=0,$header=0,$ua=0,$nobaody=0,$timeout=5,$location=0){
	$ch = curl_init();
	curl_setopt($ch, CURLOPT_URL,$url);
	curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, false);
	curl_setopt($ch, CURLOPT_SSL_VERIFYHOST, false);
	$httpheader[] = "Accept: */*";
	$httpheader[] = "Accept-Encoding: gzip,deflate,sdch";
	$httpheader[] = "Accept-Language: zh-CN,zh;q=0.8";
	$httpheader[] = "Connection: close";
	$httpheader[] = "x-requested-with: XMLHttpRequest";
	curl_setopt($ch, CURLOPT_TIMEOUT, $timeout);
	if($post){
		curl_setopt($ch, CURLOPT_POST, 1);
		curl_setopt($ch, CURLOPT_POSTFIELDS, $post);
		$httpheader[] = "Content-Type: application/x-www-form-urlencoded; charset=UTF-8";
	}
	curl_setopt($ch, CURLOPT_HTTPHEADER, $httpheader);
	if($header){
		curl_setopt($ch, CURLOPT_HEADER, TRUE);
	}
	if($cookie){
		curl_setopt($ch, CURLOPT_COOKIE, $cookie);
	}
	if($referer){
		if($referer==1){
			curl_setopt($ch, CURLOPT_REFERER, 'http://m.qzone.com/infocenter?g_f=');
		}else{
			curl_setopt($ch, CURLOPT_REFERER, $referer);
		}
	}
	if($ua){
		curl_setopt($ch, CURLOPT_USERAGENT,$ua);
	}else{
		curl_setopt($ch, CURLOPT_USERAGENT,'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.4355.400 QQBrowser/9.7.12672.400');
	}
	if($nobaody){
		curl_setopt($ch, CURLOPT_NOBODY,1);
	}
	curl_setopt($ch, CURLOPT_ENCODING, "gzip");
	curl_setopt($ch, CURLOPT_RETURNTRANSFER,1);
	if($location)curl_setopt($ch, CURLOPT_FOLLOWLOCATION, 2);
	$ret = curl_exec($ch);

	if($nobaody){
		$headerSize = curl_getinfo($ch, CURLINFO_HEADER_SIZE);
		// 根据头大小去获取头信息内容
		$header = substr($ret, 0, $headerSize);
		curl_close($ch);
		return $header;
	}
	curl_close($ch);
	return $ret;
}
function getSubstr($str, $leftStr, $rightStr){
	$left = strpos($str, $leftStr);
	$right = strpos($str, $rightStr,$left);
	if($left < 0 or $right < $left) return '';
	return substr($str, $left + strlen($leftStr), $right-$left-strlen($leftStr));
}
if($_GET['action']=='getjs'){
	@header('Content-Type: application/javascript; charset=UTF-8');
	$userid=str_replace('/ 复制此链接，打开【抖音短视频】，直接观看视频！','',$_POST['userid']);
	if(strpos($userid,'//')!==false){
		$data=get_curl($userid,0,0,0,0,'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1',0,0,1);
		$json=getSubstr($data,"/index').init(",");");
		$json=str_replace('  "  "  "  "','',str_replace("'",'"',str_replace('  "  "  "  "  "  ','',str_replace(':','":',str_replace('  ','  "',$json)))));
		$arr=json_decode($json,true);
		$uid=(string)$arr['uid'];
	}else{
		$uid='70359904504';
	}
	$data=get_curl('https://www.douyin.com/share/user/'.$uid,0,0,0,0,$_SERVER['HTTP_USER_AGENT'],0,0,1);
	$tac=getSubstr($data,"tac='","'</sc");
	$data=str_replace(array("\n","\r\n","  "),'',$data);
	$dytk=getSubstr($data,"dytk: '","'}");
	$file=str_replace('{$UA}',$_SERVER['HTTP_USER_AGENT'],file_get_contents('douyin_fuck.js'));
	$file=str_replace('{$uid}',$uid,$file);
	$file=str_replace('{$tac}',$tac,$file);
	$file=str_replace('{$dytk}',$dytk,$file);
	exit($file);
}elseif($_GET['action']=='getlist'){
	$uid=$_POST['uid'];
	$dytk=$_POST['dytk'];
	$signature=$_POST['signature'];
	$ua=$_SERVER['HTTP_USER_AGENT'];
	$data=get_curl('https://www.iesdouyin.com/web/api/v2/aweme/post/?user_id='.$uid.'&count=21&max_cursor=0&aid=1128&_signature='.$signature.'&dytk='.$dytk,0,0,0,0,$ua);
	//echo $data;

	$arr=json_decode($data,true);
	if($arr['aweme_list']){
		$code=0;
		$msg='获取成功';
	}else{
		$code=1;
		$msg='获取失败，请重新复制抖音链接';
	}
	$result=array('code'=>$code,'data'=>$arr['aweme_list'],'msg'=>$msg,'url'=>'https://www.iesdouyin.com/web/api/v2/aweme/post/?user_id='.$uid.'&count=21&max_cursor=0&aid=1128&_signature='.$signature.'&dytk='.$dytk,'uid'=>$uid,'max_cursor'=>$arr['max_cursor'],'has_more'=>$arr['has_more']);
	exit(json_encode($result));
}elseif($_GET['action']=='getlist2'){
	$uid=$_POST['uid'];
	$dytk=$_POST['dytk'];
	$signature=$_POST['signature'];
	$max_cursor=$_POST['max_cursor'];
	$ua=$_SERVER['HTTP_USER_AGENT'];
	$data=get_curl('https://www.iesdouyin.com/web/api/v2/aweme/post/?user_id='.$uid.'&count=21&max_cursor='.$max_cursor.'&aid=1128&_signature='.$signature.'&dytk='.$dytk,0,0,0,0,$ua);
	//echo $data;

	$arr=json_decode($data,true);
	if($arr['aweme_list']){
		$code=0;
		$msg='获取成功';
	}else{
		$code=1;
		$msg='获取失败，请重新复制抖音链接';
	}
	$result=array('code'=>$code,'data'=>$arr['aweme_list'],'msg'=>$msg,'url'=>'https://www.iesdouyin.com/web/api/v2/aweme/post/?user_id='.$uid.'&count=21&max_cursor='.$max_cursor.'&aid=1128&_signature='.$signature.'&dytk='.$dytk,'uid'=>$uid,'max_cursor'=>$arr['max_cursor'],'has_more'=>$arr['has_more']);
	exit(json_encode($result));
}elseif($_GET['action']=='get_palyaddress'){
	$url=$_POST['url'];
	$ua="Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Mobile Safari/537.36";//$_SERVER['HTTP_USER_AGENT'];
	$data=get_curl($url,0,0,0,1,$ua,1);
	$headArr = explode("\r\n", $data);
	foreach ($headArr as $loop) {
		if(strpos($loop, "location") !== false){
			$edengUrl = trim(substr($loop, 10));
			//print_r($edengUrl);
			$result=array('result'=>$edengUrl);
			exit(json_encode($result));
		}
	}
}