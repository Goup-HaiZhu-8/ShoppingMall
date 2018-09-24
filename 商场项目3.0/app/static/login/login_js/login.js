$(document).ready(function(){
       $.getJSON('/customer/login',function(json){
       	   alter(json);
           if (json['msg'] == 'no_register'){
           	  var $div = $('<div></div>');
           	  $div.css({'width':'120px','height':'35px','border-radius':'5px','border':'1px grey solid','position':'absolute','top':'200px','left':'50%','color':'blue','font-size':'16px','font-weight':'900','background-color':'white','vetical-align':'center'});
           	  $p = $('<p></p>');
           	  $p.text('您还没有注册!');
           	  $div.html($p);
           	  $('.denglu').after($div);

           }
       })

	});
