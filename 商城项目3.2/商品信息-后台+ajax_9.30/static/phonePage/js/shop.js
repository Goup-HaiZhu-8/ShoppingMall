
    
// function addCar(){
//       this.style.boxShadow = '1px 0.1px 5px grey';
//    }
$(document).ready(function(){
   var $buttons = $('.addcar');
   // for(i=0;i<$buttons.length;i++){
   $buttons.bind('click',function(event){
    	$(event.target).css('boxShadow','1px 0.1px 5px  grey');
    	//发送商品信息
        var data = {};
    	var $img = $(event.target).parent().children('img').attr('src');
    	var $description = $(event.target).parent().children('p').text();
    	// $money = $(event.target).parent().children('span.place').text();
    	data['img_url'] = $img;
     	data['description'] = $description;
    	// data['money'] = $money;
    	console.log(data);
    	$.ajax(
       {
        url:'/',     //url会拼接到当前url的后面，后端需要解析url
        type:'POST',
        dataType:'json',
        contentType:'application/json;charset=utf-8',
        // data:{'data':data},
        data:JSON.stringify(data),
        async:'true',
	    success:function(data,status,xhr){
	   		var $div = $("<div style='height:30px;\
          			width:120px;position:absolute;\
          			top:50%;left:50%;\
          			background-color:rgba(0,0,0,0.08);\
          			text-align:center;border-radius:5px;'>\
          			<p style='font-size:14px;color:red;'>\
          			已经添加到购物车</p></div>");


	      $div.appendTo($('#head'));
	   	  setTimeout(function(){
	    			$div.remove();
	   		   },1000);
	     },

        error:function(xhr,status,error){

		}
    	});
        
        

    })
    .bind('mouseout',function(event){
    	$(event.target).css('boxShadow','none');
    })

   // .bind('click',function(event){
   //  	$(event.target+'span').text('ok');
   //  })






})