

/* 
//Ô­JS½á¹û
<script>var x="@T@substr@toLowerCase@0xEDB88320@__jsl_clearance@href@@charCodeAt@Array@@reverse@@toString@@callP@F@1500@var@@0@GMT@pathname@139@@attachEvent@chars@1584324912@match@X@1@replace@@RegExp@firstChild@@catch@eval@length@@@join@D@@false@5@if@__p@e@hantom@g@else@@0xFF@location@CU@@fromCharCode@Expires@as@try@@function@@Mon@@DOMContentLoaded@12@@split@@return@@03@document@@@@Path@https@@d@@@rOm9XFMtA3QKV7nYsPGT4lifyWwkq5vcjH2IdxUoCbhERLaz81DNB6@SKhY@16@15@createElement@@@setTimeout@E@f@@4@Q@20@@36@3@charAt@8@div@window@Wg@@2@@innerHTML@parseInt@search@onreadystatechange@String@a@challenge@captcha@addEventListener@@@while@@6@Mar@cookie@for@new@JgSe0upZ".replace(/@*$/,"").split("@"),y="j 23=1h(){20('19.7=19.n+19.2k.w(/[\\?|&]2p-2o/,\\'\\')',i);1t.2x='6=s.o|l|'+(1h(){j 23=[[2v],[~~[]],[-~{}]+[-~[-~[10]]],[-~(-~{}-~-~{}-~((-~[]<<-~-~{})))],[-~{}]+[-~((-~[]<<-~-~{}))],[-~{}],[-~{}]+((-~[]<<-~-~{})+[]),[-~{}]+[2g],((-~[]<<-~-~{})+[]),[-~[-~[10]]],[-~{}]+[2v],[-~{}]+[~~[]],[2g],[(-~~~[]+[-~-~{}]>>-~-~{})],[-~{}]+[-~{}],[-~{}]+[(-~~~[]+[-~-~{}]>>-~-~{})],[2b],[-~((-~[]<<-~-~{}))]];2y(j 27=l;27<23.D;27++){23[27]=['2','2e',[{}+[[]][l]][l].2a(29)+[{}+[[]][l]][l].2a([-~{}]+[2g]),'1a',[2g],'H',[!!2d['12'+'14'+'1e']+[]][l].2a(-~{}-~{})+[!{}+[]][l].2a(-~{}-~{}-~-~{}),'h',[(-~~~[]+[-~-~{}]>>-~-~{})],'u','1E',[!{}+[]][l].2a(-~{}-~{}-~-~{})+[!!2d['12'+'14'+'1e']+[]][l].2a(-~{}-~{})+[2d['g'+'14']+[]+[[]][l]][l].2a(24),'21%','25%',[{}+[]+[[]][l]][l].2a(-~![]+[~~{}]-(-~![])),[{}+[]+[[]][l]][l].2a(-~![]+[~~{}]-(-~![]))+[!{}+[]][l].2a(-~{}-~{}-~-~{})+([(-~[]<<-~[])]/~~''+[]+[]).2a((+[])),[[][[]]+[]+[]][l].2a((+[]))+[{}+[]][l].2a(-~[-~[]+2v]),[!{}+[]][l].2a(-~{}-~{}-~-~{})][23[27]]};1q 23.G('')})()+';1d=1j, 1F-2w-26 1s:1G:1m m;1x=/;'};11((1h(){1f{1q !!2d.2q;}B(13){1q J;}})()){1t.2q('1l',23,J)}16{1t.q('2l',23)}",f=function(x,y){var a=0,b=0,c=0;x=x.split("");y=y||99;while((a=x.shift())&&(b=a.charCodeAt(0)-77.5))c=(Math.abs(b)<13?(b+48.5):parseInt(a,36))+y*c;return c},z=f(y.match(/\w/g).sort(function(x,y){return f(x)-f(y)}).pop());while(z++)try{eval(y.replace(/\b\w+\b/g, function(y){return x[f(y,z)-1]||("_"+y)}));break}catch(_){}</script>
*/


function getjs(x,y){
    var f = function(x, y) {
        /** @type {number} */
        var a = 0;
        /** @type {number} */
        var d = 0;
        /** @type {number} */
        var c = 0;
        x = x.split("");
        y = y || 99;
        for (; (a = x.shift()) && (d = a.charCodeAt(0) - 77.5);) {
          /** @type {number} */
          c = (Math.abs(d) < 13 ? d + 48.5 : parseInt(a, 36)) + y * c;
        }
        return c;
    };
    x = x.replace(/@*$/,"").split("@");

    var z = f(y.match(/\w/g).sort(function(r, x) {
        return f(r) - f(x);
    }).pop());

    for (; z++;) {
        try {
            res = y.replace(/\b\w+\b/g, function(y) {
              return x[f(y, z) - 1] || "_" + y;
            });
            return res
        } catch (_) {
        }
    };
}