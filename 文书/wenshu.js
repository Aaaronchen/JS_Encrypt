const des = require('./des')



function cipher() {
	var date = new Date();
	var timestamp = date.getTime().toString();
	var salt = get_random(24);
	var year = date.getFullYear().toString();
	var month = (date.getMonth() + 1 < 10 ? "0" + (date.getMonth() + 1) : date
			.getMonth()).toString();
	var day = (date.getDate() < 10 ? "0" + date.getDate() : date.getDate())
			.toString();
	var iv = year + month + day;
	var enc = des.TripleDES_Encrypt(timestamp, salt, iv).toString();
	var str = salt + iv + enc;
	var ciphertext = strTobinary(str);
	return ciphertext;
}

function strTobinary(str) {
	var result = [];
	var list = str.split("");
	for (var i = 0; i < list.length; i++) {
		if (i != 0) {
			result.push(" ");
		}
		var item = list[i];
		var binaryStr = item.charCodeAt().toString(2);
		result.push(binaryStr);
	};
	return result.join("");
}

function get_random(size){
        	var str = "",
        	arr = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'];
        	for(var i=0; i<size; i++){
        		str += arr[Math.round(Math.random() * (arr.length-1))];
        	}
        	return str;
}
function get_uuid(){
        	var guid = "";
            for (var i = 1; i <= 32; i++) {
                var n = Math.floor(Math.random() * 16.0).toString(16);
                guid += n;
                // if ((i == 8) || (i == 12) || (i == 16) || (i == 20)) guid +=
				// "-";
            }
            return guid;
        }

module.exports = {
  cipher:cipher,
  get_random:get_random,
  get_uuid:get_uuid
}
