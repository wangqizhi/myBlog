/**
* 
* By wqz
* Licensed None
* 
*/

(function(){

    console.log("Welcome to My Blog! by wqz...");
    psShowA = document.getElementById('psShowA');
    psShowA.addEventListener('click',function(){
        alert('Nothing Now!')
    });

    // // set root skill
    // var rootArea = document.getElementById('root');
    // rootArea.style['width'] = "100%";

    // var pythonPart = document.createElement('span');
    // pythonPart.id = "pythonPart"
    // pythonPart.innerHTML = "python";
    // pythonPart.style['margin-right'] = "10px";
    // pythonPart.style['border-color'] = "#73560D";
    // pythonPart.style['border-style'] = "dotted";
    // pythonPart.style['border-width'] = "2px";
    // pythonPart.style['cursor'] = "pointer";

    // rootArea.appendChild(pythonPart);


    // function addAboutSkill(span){
    //     var baseKnow = document.createElement('span');
    //     baseKnow.innerHTML = "BaseSyntax";
    //     span.appendChild(baseKnow);
    //     baseKnow.style['padding-right'] = "10px";

    // }

    // function delAboutSkill(span){
    //     tmp = span.firstChild;
    //     while(span.hasChildNodes()){
    //         span.removeChild(span.firstChild)
    //     }
    //     span.appendChild(tmp);
    // }

    // // mouse event
    // pythonPart.addEventListener('mouseover', function(e) {
    //     if (rootArea.childElementCount == 1) {
    //         addAboutSkill(rootArea);
    //     }
    // });

    // rootArea.addEventListener('mouseleave', function(e) {
    //     delAboutSkill(rootArea);
    //     rootArea.appendChild(pythonPart);
    // });

    // // setInterval(function(){
    // //     console.log("1");
    // // },1000);

}());