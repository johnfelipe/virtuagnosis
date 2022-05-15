<svelte:head>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/animate.css/4.1.1/animate.min.css" />
</svelte:head>


<script>
    
    import { predictions,showResults } from "../stores"
    import PredictionCard from "./PredictionCard.svelte"
    
    let visible = false;

function reverse(node, { targets, duration }) {
return {
  css: t => {
    return anime({
      targets,
      duration,
      easing: "easeInOutCirc",
      opacity: [1, 0],
      translateX: [0, -500],
      scale: [1, 0],
      delay: anime.stagger(200),
    });
  }
};

}
function forward(node, { targets, duration }) {
return {
  css: t => {
    anime({
      targets,
      duration,
      easing: "easeInOutCirc",
      opacity: [0, 1],
      translateX: [-500, 0],
      scale: [0, 1],
      delay: anime.stagger(200)
    });
  }
};
}
    let bodypart = 'none';
    let currentSymptoms = [];
    let headSymptoms = [];
    let faceSymptoms = [];
    let armSymptoms = [];
    let ubSymptoms = [];
    let lbSymptoms = [];
    let legSymptoms = [];
    let allSymptoms = [];


    async function getPredictions() {
        
        showResults.set(false);


        const body = {
            symptoms : currentSymptoms
        }
        const headers =  {
            "Content-Type": "application/json"
        }
        const reqData = {
            method : "POST",
            headers : headers,
            body : JSON.stringify(body)
        }

        
        const response = await fetch("/predict",reqData);
        const predData = await response.json();
        predictions.set(predData);
        showResults.set(true);
        
    }


    async function getSymptoms() {
        const response = await fetch("/symptoms")
        const data = await response.json();
        
        for (let i = 0; i < data.data.length; i++) {
            allSymptoms.push(data.data[i]);
        }
    }

    async function getbodyParts() {
        const response = await fetch("/bodyparts")
        const data1 = await response.json();
        for (let i = 0; i < data1.head.length; i++) {
            headSymptoms = [...headSymptoms,data1.head[i]];
        }
        for (let i = 0; i < data1.face.length; i++) {
            faceSymptoms = [...faceSymptoms, data1.face[i]];
        }
        for (let i = 0; i < data1.arms.length; i++) {
            armSymptoms = [...armSymptoms, data1.arms[i]];
        }
        for (let i = 0; i < data1.upper_body.length; i++) {
            ubSymptoms = [...ubSymptoms, data1.upper_body[i]];
        }
        for (let i = 0; i < data1.lower_body.length; i++) {
            lbSymptoms = [...lbSymptoms, data1.lower_body[i]];
        }
        for (let i = 0; i < data1.legs.length; i++) {
            legSymptoms = [...legSymptoms, data1.legs[i]];
        }
    }

    getSymptoms();  
    getbodyParts();

   

</script>



<div class="container animate__animated animate__backInUp animate__delay-1s	">
    <h1>SYMPTOM CHECKER</h1> 
          
    <div class="flex">
    <div class="symptom-info">
        <div class="header">
            <img src="https://static.thenounproject.com/png/353760-200.png" alt=gay/ width=30px height=30px>
            <h3 class="yo">Head & Brain</h3>
        </div>
        <div class="symptom-info1">
            <ul class="ks-cboxtags">
            {#each headSymptoms as sympts}
              <li><input type="checkbox" id={sympts} value={sympts} name={sympts} bind:group={currentSymptoms}><label for={sympts}>{sympts}</label></li>
            {/each}
            </ul>
        </div>
    </div>
    <div class="symptom-info">
        <div class="header">
            <img src="https://static.thenounproject.com/png/967517-200.png" alt=gay/ width=30px height=30px>
            <h3 class="yo">Face, Eyes, Ears, Nose, Mouth & Neck</h3>
        </div>
        <div class="symptom-info1">
            <ul class="ks-cboxtags">
            {#each faceSymptoms as sympts}
                <li><input type="checkbox" id={sympts} value={sympts} name={sympts} bind:group={currentSymptoms}><label for={sympts}>{sympts}</label></li>
            {/each}
            </ul>
        </div>
    </div>
    <div class="symptom-info">
        <div class="header">
            <img src="https://cdn-icons-png.flaticon.com/128/105/105362.png" alt=gay/ width=30px height=30px>
            <h3 class="yo">Arms, Shoulders & Hands</h3>
        </div>
        <div class="symptom-info1">
            <ul class="ks-cboxtags">
            {#each armSymptoms as sympts}
                <li><input type="checkbox" id={sympts} value={sympts} name={sympts} bind:group={currentSymptoms}><label for={sympts}>{sympts}</label></li>
                {/each}
                </ul>
        </div>
    </div>
</div>
<div class="flex">
    <div class="symptom-info">
        <div class="header">
            <img src="https://static.thenounproject.com/png/1861015-200.png" alt=gay/ width=30px height=30px>
            <h3 class="yo">Upper Body, Back & Chest</h3>
        </div>
        <div class="symptom-info1">
            <ul class="ks-cboxtags">
            {#each ubSymptoms as sympts}
                <li><input type="checkbox" id={sympts} value={sympts} name={sympts} bind:group={currentSymptoms}><label for={sympts}>{sympts}</label></li>
                {/each}
                </ul>
        </div>
    </div>
    <div class="symptom-info">
        <div class="header">
            <img src="https://static.thenounproject.com/png/2619827-200.png" alt=gay/ width=30px height=30px>
            <h3 class="yo">Lower Body, Back, Waist & Abdomen </h3>
        </div>
        <div class="symptom-info1">
            <ul class="ks-cboxtags">
            {#each lbSymptoms as sympts}
                <li><input type="checkbox" id={sympts} value={sympts} name={sympts} bind:group={currentSymptoms}><label for={sympts}>{sympts}</label></li>
                {/each}
                </ul>
        </div>
    </div>
    <div class="symptom-info">
        <div class="header">
            <img src="https://static.thenounproject.com/png/1861016-200.png" alt=gay/ width=30px height=30px>
            <h3 class="yo">Legs & Feet </h3>
        </div>
        <div class="symptom-info1">
            <ul class="ks-cboxtags">
            {#each legSymptoms as sympts}
                <li><input type="checkbox" id={sympts} value={sympts} name={sympts} bind:group={currentSymptoms}><label for={sympts}>{sympts}</label></li>
                {/each}
                </ul>
        </div>
    </div>
</div>

<a href="#card-row">
<button on:click={getPredictions} class="predict-btn">
    Predict Disease
</button></a>


</div>

<style>
    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@300&family=Ubuntu:wght@300;400&display=swap');


/* CSS */
.predict-btn {
  align-items: center;
  background-color: #FFFFFF;
  border: 1px solid rgba(0, 0, 0, 0.1);
  border-radius: .25rem;
  box-shadow: rgba(0, 0, 0, 0.02) 0 1px 3px 0;
  box-sizing: border-box;
  color: rgba(0, 0, 0, 0.85);
  cursor: pointer;
  display: inline-flex;
  font-family: system-ui,-apple-system,system-ui,"Helvetica Neue",Helvetica,Arial,sans-serif;
  font-size: 16px;
  font-weight: 600;
  justify-content: center;
  line-height: 1.25;
  margin-top : 10px;
  min-height: 3rem;
  padding: calc(.875rem - 1px) calc(1.5rem - 1px);
  position: relative;
  text-decoration: none;
  transition: all 250ms;
  user-select: none;
  -webkit-user-select: none;
  touch-action: manipulation;
  vertical-align: baseline;
  width: auto;
}

.header{
    display:flex;
    justify-content:center;
}

.yo {
    margin-left: 10px;
}

.predict-btn:hover,
.predict-btn:focus {
  border-color: rgba(0, 0, 0, 0.15);
  box-shadow: rgba(0, 0, 0, 0.1) 0 4px 12px;
  color: rgba(0, 0, 0, 0.65);
}

.predict-btn:hover {
  transform: translateY(-1px);
}

.predict-btn:active {
  background-color: #F0F0F1;
  border-color: rgba(0, 0, 0, 0.15);
  box-shadow: rgba(0, 0, 0, 0.06) 0 2px 4px;
  color: rgba(0, 0, 0, 0.65);
  transform: translateY(0);
}

    .symptom-info{
        width: 33%;
    }

    .symptom-info1 {
        height: 80%;
        overflow:scroll;
    }

    .flex {
        margin-top: 20px;
        padding: 20px 5px;
        display: flex;
        justify-content:space-between;
        height: 30vh;
    }

    .container {
        box-shadow: 0 15px 30px 1px grey;
        width:90%;
        height:85vh;
	    background: rgba(255, 255, 255, 0.90);
	    text-align: center;
	    border-radius: 5px;
        font-family: "Ubuntu", sans-serif;
        margin-top: 30px;
        margin-left:5%;
        margin-right: 5%;
        overflow-y:scroll;
        overflow-x:scroll;
    }

    ul.ks-cboxtags {
    list-style: none;
    padding: 20px;
}
ul.ks-cboxtags li{
  display: inline;
}
ul.ks-cboxtags li label{
    display: inline-block;
    background-color: rgba(255, 255, 255, .9);
    border: 2px solid rgba(139, 139, 139, .3);
    color: #adadad;
    border-radius: 25px;
    white-space: nowrap;
    margin: 3px 0px;
    -webkit-touch-callout: none;
    -webkit-user-select: none;
    -moz-user-select: none;
    -ms-user-select: none;
    user-select: none;
    -webkit-tap-highlight-color: transparent;
    transition: all .2s;
}

ul.ks-cboxtags li label {
    padding: 8px 12px;
    cursor: pointer;
}

ul.ks-cboxtags li label::before {
    display: inline-block;
    font-style: normal;
    font-variant: normal;
    text-rendering: auto;
    -webkit-font-smoothing: antialiased;
    font-family: "Font Awesome 5 Free";
    font-weight: 900;
    font-size: 12px;
    padding: 2px 6px 2px 2px;
    content: "\f067";
    transition: transform .3s ease-in-out; 
}

ul.ks-cboxtags li input[type="checkbox"]:checked + label::before {
    content: "\f00c";
    transform: rotate(-360deg);
    transition: transform .3s ease-in-out;
}

ul.ks-cboxtags li input[type="checkbox"]:checked + label {
    border: 2px solid #004F2D;
    background-color: #004F2D;
    color: #fff;
    /* transition: all .2s; */
}

ul.ks-cboxtags li input[type="checkbox"] {
  /* position: absolute; */
  opacity: 0;
}
ul.ks-cboxtags li input[type="checkbox"]:focus + label {
  border: 2px solid #004F2D;
}
</style>