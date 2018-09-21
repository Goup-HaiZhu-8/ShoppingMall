 window.onload = function () {
            var container = document.getElementById('container');
            var list = document.getElementById('list');
            var buttons = document.getElementById('buttons').getElementsByTagName('span');
            var prev = document.getElementById('prev');
            var next = document.getElementById('next');
            var index = 1;
            var len = 3;
            var animated = false;
            var interval = 3000;
            var timer;

            function animate (offset) { /*offset为初始*/
                if (offset == 0) {
                    return;
                }
                animated = true;
                var time = 300;      /*轮换时间*/
                var inteval = 10;
                var speed = offset/(time/inteval);    /*实现平滑切换图片*/
                var left = parseInt(list.style.left) + offset;

                var go = function (){
                    if ( (speed > 0 && parseInt(list.style.left) < left) || 
                        (speed < 0 && parseInt(list.style.left) > left)) 
                    {
                        list.style.left = parseInt(list.style.left) + speed + 'px';
                        setTimeout(go, inteval);
                    }
                    else {
                        list.style.left = left + 'px';
                        if(left>-200){
                            list.style.left = -1342 * len + 'px';
                        }
                        if(left<(-1342 * len)) {
                            list.style.left = '-1342px';
                        }
                        animated = false;
                    }
                }
                go();
            }

            function showButton() {
                for (var i = 0; i < buttons.length ; i++) {
                    if( buttons[i].className == 'on'){
                        buttons[i].className = '';
                        break;
                    }
                }
                buttons[index - 1].className = 'on';
            }
            			
			/*自动播放*/
            function play() {
                timer = setTimeout(function () {
                    next.onclick();
                    play();
                }, interval);
            }
            function stop() {
                clearTimeout(timer);
            }

            next.onclick = function () {
                if (animated) {
                    return;
                }
                if (index == 3) {
                    index = 1;
                }
                else {
                    index += 1;
                }
                animate(-1342);
                showButton();
            }
            prev.onclick = function () {
                if (animated) {
                    return;
                }
                if (index == 1) {
                    index = 3;
                }
                else {
                    index -= 1;
                }
                animate(1342);
                showButton();
            }

            for (var i = 0; i < buttons.length; i++) {
                buttons[i].onclick = function () {
                    if (animated) {
                        return;
                    }
                    if(this.className == 'on') {
                        return;
                    }
                    var myIndex = parseInt(this.getAttribute('index'));
                    var offset = -1342* (myIndex - index);

                    animate(offset);
                    index = myIndex;
                    showButton();
                }
            }

            container.onmouseover = stop;
            container.onmouseout = play;


            /*点击登录按钮重定向到登录界面*/
            var login = document.getElementById('login')
            login.onclick = function(){
                location.href = '###';     /*登录页面*/        
            }  

            /*信息卡片模块*/
            function waterfall(parent,pin){
                var  oParent = document.getElementById('main');
                var  oChild = oParent.getElementsByClassName('pin');
                var  cPinW = oChild[0].offsetWidth;
                var num = Math.floor((window.screen.width-200)/cPinW);
                oParent.style.cssText = 'width:'+(cPinW*num-200)+'px;';
                
                }

            /*商品展示列表栏-显示隐藏功能*/
            function  on_show(){
                var show_box = document.getElementById('showBox');
                var show_List1 = document.getElementById('showList').getElementsByTagName('li')[0];
                show_List1.onmouseover = function(){
                    show_box.style.display = 'block';
                }
            }

            function  on_hide(){
                var show_box = document.getElementById('showBox');
                var show_List1 = document.getElementById('showList').getElementsByTagName('li')[0];   
                show_List1.onmouseout = function(){
                        show_box.onmouseover = function(){
                            show_box.style.display = 'block';
                        };
                        show_box.onmouseout = function(){
                            show_box.style.display = 'none';
                        };

                    show_box.style.display = 'none';

                    }
            }



            waterfall();   
            play();
            on_show();
            on_hide();
        
        };

