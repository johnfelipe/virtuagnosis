<svelte:head>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/animate.css/4.1.1/animate.min.css" />
</svelte:head>

<script>
    import Typed from "typed.js"
    import anime from "animejs/lib/anime.es.js";
    
    window.onload = () => {
        
        let expressions = ["Pick your symptoms with a simple click!","Predict your disease in real-time!"]
        var options = {
        strings: expressions,
        typeSpeed: 30,
        backSpeed : 30,
        smartBackspace : true,
        loop : true,
        cursorChar : null
      };


      var typed = new Typed('#typed-word', options);

    }
    

</script>

<h1 class="app-title"> Virtuagnosis: <span id="typed-word"> </span></h1>
<img class="app-icon animate__animated animate__bounceInUp" src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/8e/Font_Awesome_5_solid_medkit.svg/1200px-Font_Awesome_5_solid_medkit.svg.png">
<style>
    @import url('https://fonts.googleapis.com/css2?family=Roboto+Mono:wght@100;200;400&family=VT323&display=swap');

    .app-title {
        margin-top : 20px;
        text-align : center;
        font-family: 'VT323', monospace;
        font-style: italic;
        font-size : 35px;
        color : white;
    }
    
    .app-icon {
        display : block;
        margin-left : auto;
        margin-right : auto;
        border-radius : 50%;
        width : 10%;
        height : 10%;
    }
    

    
</style>