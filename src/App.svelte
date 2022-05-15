<svelte:head>
	<title>Virtuagnosis</title>
</svelte:head>


<script>
import Container from "./components/Container.svelte"
import Title from "./components/Title.svelte"
import PredictionCard from "./components/PredictionCard.svelte"
import { predictions,showResults } from "./stores"
import {onMount} from "svelte"
import {counterUp} from 'counterup2'




window.onbeforeunload = function () {
    window.scrollTo(0,0);
};

// Show mobile icon and display menu
let showMobileMenu = false;

// Mobile menu click event handler
const handleMobileIconClick = () => (showMobileMenu = !showMobileMenu);

// Media match query handler
const mediaQueryHandler = e => {
  // Reset mobile state
  if (!e.matches) {
    showMobileMenu = false;
  }
};

let numSymptoms;
let numDiseases;
async function getSymptoms() {
        const response = await fetch("/symptoms")
        const data = await response.json();
		numSymptoms = data.data.length;
}

async function getDiseases() {
    const response = await fetch("/diseaseinfo")
    const data = await response.json();
	numDiseases = Object.keys(data).length;
}


onMount(async () => {
	await getSymptoms();
	await getDiseases();
	
	const counterSymptoms = document.createElement("h1");
	counterSymptoms.classList.add("counter")
	counterSymptoms.innerHTML = numSymptoms + " symptoms";
	counterSymptoms.style.textAlign = "center";
	counterSymptoms.style.fontFamily ="'Rampart One', cursive"
	counterSymptoms.style.color = "white";

	const counterDiseases = document.createElement("h1");
	counterDiseases.classList.add("counter")
	counterDiseases.innerHTML = numDiseases + " diseases supported";
	counterDiseases.style.textAlign = "center";
	counterDiseases.style.fontFamily ="'Rampart One', cursive";
	counterDiseases.style.color = "white";


	document.body.insertBefore(counterSymptoms,document.body.firstChild);
	document.body.insertBefore(counterDiseases,document.body.firstChild);
	counterUp(counterSymptoms, {
    duration: 5000,
    delay: 16,
} )
	counterUp(counterDiseases, {
		duration: 5000,
		delay: 16,
	} )
})

</script>


<head>
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<style>
	body {font-family: Arial, Helvetica, sans-serif;}
	* {box-sizing: border-box;}
	
	input[type=text], select, textarea {
	  width: 100%;
	  padding: 12px;
	  border: 1px solid #ccc;
	  border-radius: 4px;
	  box-sizing: border-box;
	  margin-top: 6px;
	  margin-bottom: 16px;
	  resize: vertical;
	}
	
	input[type=submit] {
	  background-color: #04AA6D;
	  color: white;
	  padding: 12px 20px;
	  border: none;
	  border-radius: 4px;
	  cursor: pointer;
	}
	
	input[type=submit]:hover {
	  background-color: #45a049;
	}
	
	.container {
		margin-top : 25	px;
	}
	</style>
	
	</head>
	<body>
	

	<div><Title/></div>
	<div class="container">
	<Container></Container>
	
	
	</div>
	
	<h1 id="pred-heading"> YOUR DISEASE PREDICTIONS: </h1>
			{#if $showResults}
			<div id="card-row">
				{#each Object.entries($predictions) as [name, innerData]}
					<PredictionCard diseaseName={name} diseaseDesc={innerData.desc} symptoms={innerData.symptoms} animationName="animate__animated animate__backInUp"></PredictionCard>
				{/each}
			</div>
			{/if}
		
	</body>

<style>
	@import url('https://fonts.googleapis.com/css2?family=Rampart+One&display=swap');
	
	#pred-heading {
		color : white;
		margin-top : 20px;
		text-align: center;
	}

	#card-row {
		display : flex;
		margin-top : 20px;
	}

	
</style>

