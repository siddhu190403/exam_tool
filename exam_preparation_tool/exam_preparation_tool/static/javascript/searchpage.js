function reload(){
    console.log(window.location.href == 'http://127.0.0.1:8000/search/result/');

    if(window.location.href == 'http://127.0.0.1:8000/search/result/')
        location.replace('http://127.0.0.1:8000/search/')
}

function focus(){
    document.getElementById('search').focus();
    var dropdown = document.getElementById('mark');
    
    if(dropdown == null){
        document.getElementById("form").action = 'question';
    }
}

function redirect(link){
    location.replace('http://127.0.0.1:8000/'+link)
}

function showquestion(){
    var questiondiv = document.getElementById("question");
    var qbutton = document.getElementById('button');
    console.log(questiondiv.getAttribute("hidden"));
    
    if(questiondiv.getAttribute("hidden") == 'hidden'){
        questiondiv.removeAttribute("hidden");
        qbutton.innerHTML = 'Hide question';
    }
    else{
        questiondiv.setAttribute('hidden','hidden');
        qbutton.innerHTML = 'Generate question';
    }
}