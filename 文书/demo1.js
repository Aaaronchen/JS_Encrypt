const app1 = require('./http')
const res1 = require('./data')
const e = require('./baidu')
const wenshu = require('./wenshu')
var url = require('url');
const des = require('./des')
const querystring = require("querystring");

console.log(app1)
app1.get('/getTest1', (req, res) => {
  res.status(200)
  res.json(res1)
})


app1.get('/getdata', (req, res) => {
  console.log('req.url:'+req.url)
  var parse = url.parse(req.url, true).query;
  var key = parse.key
  var sign = e(key)
  res.status(200)
  res.json(sign)
})


app1.post('/decrypt/',function (req, res) {
  var post='';
  req.on('data',function(chunk){
    post +=chunk;
  });
  
  req.on('end',function(){
    post=querystring.parse(post);
    console.log('word:'+post['word']);
    console.log('key:'+post['key']); 
    console.log('iv:'+post['iv']);
    var sign = des.TripleDES_Decrypt(post['word'],post['key'],post['iv'])
    res.status(200)
    res.json(sign)
  });
});


app1.get('/get_random/', (req, res) => {
  var parse = url.parse(req.url, true).query;
  var size = parse.size
  var sign = wenshu.get_random(size)
  res.status(200)
  res.json(sign)
})

app1.get('/get_cipher/', (req, res) => {
  var sign = wenshu.cipher()
  res.status(200)
  res.json(sign)
})

app1.get('/get_uuid/', (req, res) => {
  var sign = wenshu.get_uuid()
  res.status(200)
  res.json(sign)
})


const server = app1.listen(3000, () => {
  const host = server.address().address
  const port = server.address().port
  console.log('Listen at http://%s:%s', host, port)
})