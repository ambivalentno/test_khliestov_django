
function somef(inputa,outputa){
    var $textarea = $("#"+inputa);
    var $chars = $("#"+outputa);

    $textarea.keyup(function(){
        $chars.html((parseInt($textarea.val().length)));
    });
    $textarea.keydown(function(){
        $chars.html((parseInt($textarea.val().length)));
    });
}