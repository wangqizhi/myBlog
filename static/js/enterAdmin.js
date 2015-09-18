// Copyright 2015 wangqizhi
// 
// Licensed None

(function(){
    document.addEventListener('keydown', function(e) {
        hiddenPwd = document.getElementById('hiddenId');
        if ( e.keyCode == 65 ) {
            hiddenPwd.value = "a";
        } 

        if ( e.keyCode == 83 ) {
            tmp = hiddenPwd.value;
            hiddenPwd.value = tmp + "s";
            if (hiddenPwd.value) {
                location.href = "/admin" ;
            };

        } 
        
    });
    document.addEventListener('keyup', function(e) {
        hiddenPwd = document.getElementById('hiddenId');

        if ( e.keyCode == 65 ) {
            hiddenPwd.value = "";
        } 
        
    });




})();