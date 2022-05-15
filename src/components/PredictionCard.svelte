<script>
    export let diseaseName;
    export let diseaseDesc;
    export let symptoms;
    export let animationName;

    let titleBgColor;

    

    if (symptoms.length <= 5) {
        titleBgColor = "background-color:green;";
    }
    else if (symptoms.length > 5 && symptoms.length <= 10) {
        titleBgColor = "background-color:yellow;";
    }
    else {
        titleBgColor = "background-color:red;";
    }

</script>

<div class="card {animationName}">
    <div class="text-container">    
        <h1> Disease Name </h1>
        <h1 class="name" style={titleBgColor}>{diseaseName}</h1>
        <h1> Symptoms </h1>
        <p class="info-p">{symptoms.join(", ")}</p>
        <h1> Description </h1>
        <p class="info-p">{diseaseDesc}</p>
    </div>
</div>

<style>

.card {
    background-color: white;
    margin : 20px;
    border-radius : 10px;
}

.card:hover {
    transform : scale(1.05);
    animation-fill-mode: none;
    transition : scale 200ms ease-in-out
}

.name {
    font-size : 20px;
    padding : 10px;
}

.info-p {
    font-size : 15px;
    text-align : center;
    padding : 10px;
}

h1 {
    text-align : center;
    margin-top : 10px;
}

</style>