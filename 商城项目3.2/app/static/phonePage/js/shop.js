
    
// function addCar(){
//       this.style.boxShadow = '1px 0.1px 5px grey';
//    }
$(document).ready(function(){
   var $buttons = $('.addcar');
   // for(i=0;i<$buttons.length;i++){
   $buttons.bind('click',function(event){
    	$(event.target).css('boxShadow','1px 0.1px 5px  grey');
    	var data = {};
    	img = $(event.target).parent().children('img').attr('src');
    	description = $(event.target).parent().children('p').text();
    	money = $(event.target).parent().children('span.place').text();
    	data['img_url'] = img;
     	data['description'] = description;
    	data['money'] = money;
    	console.log(data);
    	$.ajax({
        type:'POST',
        // dataType:'json'
        contentType:'application/json;charse=utf-8',
        data:JSON.stringify(data),
        url:'',
	    success:function(msg){
	   		var $div = $("<div style='height:50px;\
			width:120px;position:fixed;z-index: 100;\
			top:0;left:0;right:0;bottom:0;margin:auto;\
			background-color:rgba(255,0,0,0.8);\
			text-align:center;border-radius:5px;'>\
			<p style='font-size:14px;color:white;text-align: center'>\
			已经添加到购物车</p></div>");



	        $div.appendTo($('#head'))
	   	    setTimeout(function(){
	    			$div.remove();
	   		   },1000);
	   }


    	})
    })
    .bind('mouseout',function(event){
    	$(event.target).css('boxShadow','none');
    })

   // .bind('click',function(event){
   //  	$(event.target+'span').text('ok');
   //  })






})